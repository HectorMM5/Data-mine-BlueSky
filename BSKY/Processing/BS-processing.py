from atproto import Client
from BSKY.Processing.credentials import BLUESKY_USERNAME, BLUESKY_PASSWORD
from playwright.sync_api import sync_playwright
import BSKY.Functionality.Posts as Posts

client = Client()
client.login(BLUESKY_USERNAME, BLUESKY_PASSWORD)

def transformFeedURL(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        page = browser.new_page()
        page.goto(url)
        page.wait_for_selector('xpath=//div[contains(text(), "@")]', timeout=10000)

        element = page.locator('xpath=//div[contains(text(), "@")]')

        owner_username = element.text_content().strip()[2:-1]
        owner_did = client.get_profile(actor=(owner_username))["did"]
        feed_id = url.split("/")[-1]

        uri = 'at://' + owner_did + '/app.bsky.feed.generator/' + feed_id

        return uri

def getFeed(uri, limit):
    try:
        content = client.app.bsky.feed.get_feed({
            'feed': uri,
            'limit': limit
        })

        return content
      
    except Exception as e:  
        print(f"Error: The URI was invalid.")

        return None 


def bskyGetPosts(url, limit=50):
    uri = transformFeedURL(url)
    feed = getFeed(uri, limit)

    posts = []    
    for post in feed["feed"]:

        post = post["post"]

        
        posts.append(Posts.PostObject(post["author"], post["record"]["text"], post["embed"], post["like_count"], post["repost_count"], post["reply_count"]))

    return posts



for post in bskyGetPosts("https://bsky.app/profile/bossett.social/feed/for-science"):
    print(post.text)
