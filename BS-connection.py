from atproto import Client
from credentials import BLUESKY_USERNAME, BLUESKY_PASSWORD

client = Client()
client.login(BLUESKY_USERNAME, BLUESKY_PASSWORD)

bluesky_did = client.get_profile(actor="bsky.app")["did"]

data = client.app.bsky.feed.get_feed({
    'feed': 'at://' + bluesky_did + '/app.bsky.feed.generator/whats-hot',
    'limit': 5,
})

print(data["feed"][0]["post"]["like_count"])
print(data["feed"][1]["post"]["like_count"])
print(data["feed"][2]["post"]["like_count"])
print(data["feed"][3]["post"]["like_count"])
print(data["feed"][4]["post"]["like_count"])


def getFeed(feedURL, limit):
    

