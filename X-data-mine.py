from atproto import Client

client = Client()
# By default, it uses the server of bsky.app. To change this behavior, pass the base api URL to constructor
# Client('https://example.com')

def getFeed(feedName, postAmount, sorting):
    