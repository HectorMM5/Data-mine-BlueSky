from typing import List, Dic
import Posts
import scores
import re

def filterContainsWord(posts: List[Posts.PostObject], wordsFilter: str):
    wordsList: List[str] = []
    word: str = ""

    for letter in wordsFilter:

        if re.match(r'^[a-zA-Z-]$', letter):
            word += letter
        else:
            if word:
                wordsList.append(word)
                word = "" 

    if word:
        wordsList.append(word)

    filteredFeed: List = []

    for post in posts:
        if all(word in post.text for word in wordsList):
            filteredFeed.append(post)

    return filteredFeed



def sortEngagement(posts: List[Posts.PostObject]):
    sorted_posts = sorted(posts, key=scores.engagement_score, reverse=True)

    return sorted_posts



