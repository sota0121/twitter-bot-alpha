import os
import random
from random import shuffle
from typing import Callable, Final

import tweepy
import yaml
from dotenv import load_dotenv, dotenv_values
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


def init_envvars(environment: str) -> None:
    """
        - environment: "development" or "production"
        - if development, load .env
        - if production, already loaded .env by cloud function
    """
    if environment == "development":
        load_dotenv(dotenv_path=ENV_FILE_PATH)
    elif environment == "production":
        pass
    else:
        raise ValueError(f"environment must be 'development' or 'production'")


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


def shuffle_str(src_str: str) -> str:
    """
        ### Args
        - src_str: str
            - source string should be shuffled

        ### Returns
        - tweet: str
    """
    shuffled_str = "".join(random.sample(src_str, len(src_str)))
    return shuffled_str


def post_shuffle_tweet(init_var_func: Callable, environment: str, src_str: str) -> str:
    """
        ### Args
        - init_var_func: Callable
            - environment variable initialization function
        - environment: str
            - "development" or "production"
        - src_str: str
            - source string should be shuffled

        ### Returns
        - tweet: str
    """
    init_var_func(environment)

    api = init_tweepy()

    # Generate shuffled tweet string
    tweet_str = shuffle_str(src_str)

    # Post tweet
    ret = api.update_status(status=tweet_str)

    # Print result
    # print(f"result: {ret}")
    print(f"tweeted: {tweet_str}")

    return tweet_str


def post_rnd_tweet(init_var_func: Callable, environment: str) -> str:
    """
        ### Returns
        - tweet: str
    """
    init_var_func(environment)

    api = init_tweepy()

    # Generate random tweet string
    tweet_str = generate_rnd_tweet(nb_words=10)
    tweet_str = "（新刊）" + tweet_str

    # Post tweet
    ret = api.update_status(status=tweet_str)

    # Print result
    # print(f"result: {ret}")
    print(f"tweeted: {tweet_str}")

    return tweet_str


def post_tweet_local(src_str: str="なかやまきんにくん") -> str:
    init_var_func = init_envvars
    environment = "development"
    tweet = post_shuffle_tweet(init_var_func, environment, src_str=src_str)
    # tweet = post_rnd_tweet(init_var_func, environment)
    return tweet


def post_tweet_cloud(src_str: str = "なかやまきんにくん") -> str:
    init_var_func = init_envvars
    environment = "production"
    tweet = post_shuffle_tweet(init_var_func, environment, src_str=src_str)
    return tweet
