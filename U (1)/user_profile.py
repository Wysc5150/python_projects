# Cam W
# 11/8/22
# Try it yourself, 8-13, 8-14

def build_profile(first, last, **user_info):
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info

user_profile=build_profile('Cam', 'Wysocki', fav_food='pierogies', fav_game='Persona 5 Royal', occupation='student')

print(user_profile)
print()
print('/////////////////////////////////////////////////////////////////////////////////////////////')
print()
def make_car(brand, type, **extra_info):
    """make a car, dude"""
    extra_info['car_brand']=brand
    extra_info['car_type']=type
    return extra_info

car=make_car('subaru', 'outback', color='black')

print(car)