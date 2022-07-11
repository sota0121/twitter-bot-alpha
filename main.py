from bot.core import post_tweet_cloud


def tweet_from_cloud(request):
    """
        ## Args:
        - request: request object of flask
            - this is for cloud function
    """
    src_str = request.args.get("src_str", default="なかやまきんにくん", type=str)
    tweet = post_tweet_cloud(src_str=src_str)
    return f"tweeted: {tweet}"
