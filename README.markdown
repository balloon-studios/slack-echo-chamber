slack-echo-chamber
==================

A little [Flask][flask] webapp to pass messages from one channel to  another.
We use this to replicate the content of some internal discussion channels with
our guest-accessible "friends of Balloon" channel.

[flask]: http://flask.pocoo.org


Setup
-----

Create an incoming webhook for the target channel.

    # on some webservery-like unix box
    pip install -r requirements.txt
    export SLACK_WEBHOOK='YOUR_INCOMING_WEBHOOK_URL'
    python echo.py

This will start the webserver listening on port 3246.

Configure an outgoing webhook in your Slack integrations from the channel you
want replicated that points to `http://your-webserver.example.com:3246`.

Now, when something is said in the replicated channel, you should see it
echoed back in the target channel.

Deploying this properly is left as an exercise for the reader.
