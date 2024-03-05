usernames = ['Boruha', 'Boris', 'Boria', 'Borislau']
passwords = ('p@ssword', 'abc123', 'guest', 'pi')
last_log_in = ['1/1/2021', '1/2/2021', '1/3/2021']

users = zip(usernames, passwords, last_log_in)

print(users)

for i in users:
    print(i)