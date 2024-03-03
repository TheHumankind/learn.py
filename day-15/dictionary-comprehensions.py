c_in_F =  {
    'New York': 32,
    'Boston': 75,
    'Los Angeles': 100,
    'Chicago': 50,
}
#
# c_in_C = {
#     key: ((val - 32) * (5 / 9)) for (key, val) in c_in_F.items()
# }
# print(c_in_C)

w_in_cities = {
    'Boston': 'sunny',
    'New York': 'snowing',
    'LA': 'sunny',
    'Chicago': 'cloudy'
}

# sunny_in_cities = {
#     key: val for (key, val) in w_in_cities.items() if val == 'sunny'
# }

def check_temp(val):
    if val > 70:
        return 'hot'
    else:
        return 'it\' ok'


# sunny_in_cities = {
#     key: ('sunny' if val == 'sunny' else 'BAD') for (key, val) in w_in_cities.items()
# }

sunny_in_cities = {
    key: check_temp(val) for (key, val) in c_in_F.items()
}

print(sunny_in_cities)
