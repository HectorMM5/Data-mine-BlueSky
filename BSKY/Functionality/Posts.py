class PostObject:
    def __init__(self, author, text, embed, likes, reposts, replies):
        self.author = author  # Store the author's name or handle
        self.text = text      # Store the post content
        self.embed = embed    # Store embedded content (if any)
        self.likes = likes    # Number of likes the post has received
        self.reposts = reposts  # Number of times the post has been reposted
        self.replies = replies  # Number of replies to the post
        
def getPostText(post):
    print(post["record"]["text"])
