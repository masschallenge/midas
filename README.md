# midas - handraiser for slack

Midas makes it easy to raise your hand in the #handraising channel on slack.


quickstart:

- clone the repo and build 
```
git clone https://github.com/masschallenge/midas.git
cd midas
touch .env # fill in .env with SLACK_CLIENT_ID and SLACK_CLIENT_SECRET values
docker-compose build 
docker-compose up
```

- visit http://localhost:9000 in browser

- authenticate with slack

- once the model loads, pressing \<spacebar\> sends a hand to the handraising channel

## automatic mode (expirimental)

clicking the "Automatic Mode" enables automatic hand-raise detection via your webcam. this is considered experimental and may cause false detections in bad lighting conditions.
