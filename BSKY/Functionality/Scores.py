

def sortEngagement(post):
    # A custom designed engagement score, based on how common these interactions are
    return (
        post['likes'] * 1 # Common interaction
        + post['reposts'] * 2 # Less common
        + post['replies'] * 5 # Least common
    )


