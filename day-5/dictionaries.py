

capitals = {
    'USA': 'Washington DC',
    'India': 'New Delhi',
    'China': 'Beijing',
    'Russia': 'Moscow'
}

#print(capitals['Germany'])
#print(capitals.get('Germany'))
# capitals.clear()
capitals.update({'Germany': 'Berlin'})
capitals.update({'India': 'Old Delhi'})
capitals.pop('China')


for i, key in enumerate(capitals.keys()):
    print(str(i + 1) + ': ' + capitals.get(key))

for key, values in capitals.items():
    print(key + ': ' + values)


