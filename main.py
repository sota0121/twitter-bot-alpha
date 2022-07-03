from bot.core import post_tweet_cloud


def tweet_from_cloud(request):
    """
        ## Args:
        - request: request object of flask
            - this is for cloud function
    """
    tweet = post_tweet_cloud()
    return f"tweeted: {tweet}"
