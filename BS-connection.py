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
        last_part = url.split("/")[-1]

        uri = 'at://' + owner_did + '/app.bsky.feed.generator/' + last_part

        return uri

def getFeed(uri, limit):
    content = client.app.bsky.feed.get_feed({
        'feed': uri,
        'limit': limit
    })
    

getFeed("https://bsky.app/profile/bsky.app/feed/whats-hot")