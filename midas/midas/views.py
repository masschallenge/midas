from django.http.response import HttpResponseRedirect, HttpResponse
from django.views.generic import RedirectView, View
from django.shortcuts import render
from django_slack_oauth.models import SlackUser
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import os
import slack
import base64
import cv2
import numpy as np
import math
import urllib


def auth_view(request):
        return render(request, 'auth.html', {})


def handraising_view(request):
    SlackUser.objects.get_or_create(slacker=request.user)
    return render(request, 'handraising.html', {})


@csrf_exempt
def raise_hand_action(request):
    client = slack.WebClient(token=request.user.slack_user.access_token)
    response = client.chat_postMessage(
        channel='#handraising',
        #channel='#apitesting',
        text=":hand:")
    return HttpResponse("success")


def detector_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('slack_auth'))
    return render(request, 'detector.html', {})
