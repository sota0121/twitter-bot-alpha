import os
from typing import Final

import tweepy
from dotenv import load_dotenv
from faker import Faker

# --------------------------------------------------
# constants
# --------------------------------------------------
ENV_FILE_PATH: Final[str] = ".env"
VAR_ACC_TOKEN: Final[str] = "access_token"
VAR_ACC_SECRET: Final[str] = "access_secret"
VAR_CNS_KEY: Final[str] = "consumer_key"
VAR_CNS_SECRET: Final[str] = "consumer_secret"

# --------------------------------------------------
# Main Functions
# --------------------------------------------------
load_dotenv(dotenv_path=ENV_FILE_PATH)
ja_faker = Faker("ja_JP")
en_faker = Faker("en_US")


def init_tweepy() -> tweepy.API:
    """
    Initialize tweepy API
    """
    auth = tweepy.OAuthHandler(os.getenv(VAR_CNS_KEY), os.getenv(VAR_CNS_SECRET))
    auth.set_access_token(os.getenv(VAR_ACC_TOKEN), os.getenv(VAR_ACC_SECRET))
    return tweepy.API(auth)

def generate_rnd_tweet(nb_words: int) -> str:
    """
    Generate random tweet string
    """
    result = ja_faker.sentence(nb_words=nb_words)
    result = result.replace('。', '')
    return result

def post_rnd_tweet() -> None:
    api = init_tweepy()

    # Generate random tweet string
    tweet_str = generate_rnd_tweet(nb_words=10)

    # Post tweet
    ret = api.update_status(status=tweet_str)

    # Print result
    # print(f"result: {ret}")
    print(f"tweeted: {tweet_str}")
