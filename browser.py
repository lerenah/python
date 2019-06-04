stack = []

def history(url):
    if len(stack) > 5:
        stack.remove(stack[0])
        stack.append(url)
    elif url in stack:
        stack.remove(url)
        stack.append(url)
    else:
        stack.append(url)

def retrieve_history():
    for idx, url in enumerate(stack[::-1]):
        print((idx + 1), url)


def clear_history():
    while len(stack):
      stack.pop()

