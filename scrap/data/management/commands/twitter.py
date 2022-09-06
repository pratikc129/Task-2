from django.core.management.base import BaseCommand
from selenium.common import NoSuchElementException
from tweepy import NotFound
from ...models import *
import tweepy


class Command(BaseCommand):
    help = "A commands to add data from an Excel file to the database"

    def handle(self, *args, **options):
        """twitter keys and token """
        auth = tweepy.OAuth1UserHandler(
            "qHp6xKMysYc8Rfbn7nhGfSqwK", "ABzCbRHodYZchLqP81jp0sxET5bPSyDXvgfW4dgeFg6lJDZlLn",
            "1565636677967945729-OICOLDG7cAH5vFY88A03eWdnAfduuu", "WFmwqdGJFpKSmaU4vur5YBixmM6CndwWYSOx8Zk7mR2q0"
        )
        api = tweepy.API(auth)
        twitter = TwitterInfo.objects.all()
        val = twitter.values('username', 'follower_count', 'following_count', 'twitter_count',
                             'retweet_count', 'last_tweet',
                             'location', 'profile_name', 'player_id')
        for i in val.values('username', 'follower_count', 'following_count', 'twitter_count',
                            'retweet_count', 'last_tweet',
                            'location', 'profile_name', 'player_id'):
            try:
                for i in range(1625, 1626):
                    names = TwitterInfo.objects.get(id=i)
                    handlename = names.username
                    print(handlename)
                    cursor = tweepy.Cursor(api.user_timeline, id=twitter, tweet_mode="extended").items(1)
                    for j in cursor:
                        """for loop for retweet count"""
                        retweet_count = j.retweet_count
                    twitters = handlename

                    c = api.get_user(screen_name=twitters)
                    """follower count"""
                    follower_count = c.followers_count

                    """following count"""
                    following_count = c.friends_count

                    """twitter count"""
                    twitter_count = c.statuses_count

                    """last tweet count """
                    ltweet = api.user_timeline(screen_name=twitters)
                    last_tweet = str(ltweet[0].text).encode('unicode_escape')

                    """adding twitter data into database"""
                    TwitterInfo.objects.filter(id=i).update(follower_count=follower_count,
                                                            following_count=following_count,
                                                            twitter_count=twitter_count, retweet_count=retweet_count,
                                                            location=c.location, last_tweet=last_tweet)
            except (NoSuchElementException, NotFound):
                pass
            break
