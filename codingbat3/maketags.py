def make_tags(tag, word):
    return f"<{tag}>" + word + f"</{tag}>"

print(make_tags("i", 'hello'))