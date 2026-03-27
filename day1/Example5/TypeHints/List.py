from typing import List

def get_post_titles() -> List[str]:
    return ["Post 1", "Post 2", "Post 3"]

print(get_post_titles())
# ['Post 1', 'Post 2', 'Post 3']


class Post:
    def __init__(self, title: str):
        self.title = title

def get_posts() -> List[Post]:
    return [Post("A"), Post("B")]

print(get_posts())
# [
# <__main__.Post object at 0x7f79ba23d520>, 
# <__main__.Post object at 0x7f79ba23a8e0>
#]

