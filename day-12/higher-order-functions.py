def loud(word):
    return word.upper()

def quiet(word):
    return word.lower()

def hello(func):
    text = func('Hi')
    print(text)


hello(loud)
hello(quiet)

def devisor(x):
    def divident(y):
        return y / x
    return divident

divide = devisor(5)

print(divide(2))