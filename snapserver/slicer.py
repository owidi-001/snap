from itertools import islice
from api.models import Post


def slicer():
    posts_dict = dict()
    posts = Post.objects.all()
    column_count = len(posts) // 4
    columns = [column_count, column_count, column_count, column_count]
    remainder = len(posts) % 4
    if remainder:
        i = 0
        while remainder:
            columns[i] += 1
            remainder -= 1
            i += 1
    posts = iter(posts)
    posts = [list(islice(posts, column)) for column in columns]
    labels = ['first', 'second', 'third', 'fourth']
    for i in range(len(labels)):
        posts_dict[labels[i]] = posts[i]

    return posts_dict
