import ConfigParser
import os
import spotipy
import pprint
from twitter import *


class MusicBuilder:
    access_key = ''
    access_secret = ''
    consumer_key = ''
    consumer_secret = ''


    def __init__(self, access_key, access_secret, consumer_key, consumer_secret):
        self.access_key = access_key
        self.access_secret = access_secret
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret


    def get_music(self, username):
        twitter = Twitter(
            auth=OAuth(self.access_key, self.access_secret, self.consumer_key, self.consumer_secret))

        user = twitter.users.lookup(screen_name=username)
        sp = spotipy.Spotify()
        words = user[0]['description'].split()

        images = []
        for word in words:
            if len(word) > 2:
                result = sp.search(word, limit=1)
                print "word :" + str(word);
                if len(result['tracks']['items']) > 0:
                    #images.append(result['tracks']['items'][0]['album']['images'][1]['url'])
                    images.append(result['tracks'])

        return images
