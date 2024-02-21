

def greetings(**args):
    #print("Hello" + kwargs['first'] + ' ' + kwargs['last'] + kwargs['middle'])
    print('Hello', end=' ')
    for i, v in args.items():
            print(v, end=' ')

greetings(first = 'a', second = 'b', third = 'c', four = 'd', fives = 'e')