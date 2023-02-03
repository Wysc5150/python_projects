# Cam W
# 11/14/22
# Evidence Functions & Arguments

# Create keyword arguments

# Set default price

def trip(city, country, days, price='1700'):
    """Plan a trip somewhere"""
    print(f'Your trip to {city}, {country} for {days} days will cost ${price}.00')

trip(city='Bordeaux', country='France', days='7', price='1000')

trip(city='Verona', country='Italy', days='10')