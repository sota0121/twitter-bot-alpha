import sys
from .core import post_tweet_local


if __name__ == "__main__":
    args = sys.argv
    src_str = "なかやまきんにくん" if len(args) == 1 else args[1]
    post_tweet_local(src_str=src_str)
