def hello(name=None):
    if name is not None:
        print('Hello ' + name)
    else:
        print('Hello')


hello()
hello('Flash')
