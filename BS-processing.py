from atproto import Client
from credentials import BLUESKY_USERNAME, BLUESKY_PASSWORD
from playwright.sync_api import sync_playwright

client = Client()
client.login(BLUESKY_USERNAME, BLUESKY_PASSWORD)

bluesky_did = client.get_profile(actor="bsky.app")["did"]

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
    content = client.app.bsky.feed.get_feed({
        'feed': uri,
        'limit': limit
    })

    return content

def getFeedPosts(feed):
    posts = []
    for post in feed["feed"]:
        posts.append(post["post"])

    return posts




uri = transformFeedURL("https://bsky.app/profile/bossett.social/feed/for-science")

feed = getFeed(uri, 2)

posts = getFeedPosts(feed)

displayPost(posts[0])
displayPost(posts[1])