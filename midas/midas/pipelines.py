from django.contrib.auth.models import User

from django_slack_oauth.models import SlackUser
from django.contrib.auth import authenticate, login
from django.conf import settings



def register_user(request, api_data):
    if api_data['ok']:
        user, created = User.objects.get_or_create(
            username=api_data['team_id']+':'+api_data['user_id']
        )

        if user.is_active:
            slacker, _ = SlackUser.objects.get_or_create(slacker=user)
            slacker.access_token = api_data.pop('access_token')
            slacker.extras = api_data
            slacker.save()

        if created:
            request.created_user = user
        login(request, user, backend=settings.AUTHENTICATION_BACKENDS[0])
    return request, api_data

def debug_oauth_request(request, api_data):
    print(api_data)
    return request, api_data