Created the following tutorial: https://www.fullstackpython.com/blog/build-first-slack-bot-python.html

Deployed to Heroku free tier: https://github.com/ianhillmedia/slackbot-for-heroku

# Test coverage
Run tests to make sure the json is valid!
- make a virtual environment
- pip install
- `make test`

# Deployment
Deploy: `git push heroku`
Also do this, on first deploy only: `heroku ps:scale worker=1`
Currently this is linked to a personal Heroku account- james.fefes@uplight.com. This was mainly done because it fits within the Heroku free tier.

If interest continues in using this, it might be a fun experiment to get it into Lambda, or something else that is cheap yet easier to access.
