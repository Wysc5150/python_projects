# Cam W
# 11/14/22
# Evidence Functions & Arguments

# Define the Alien

# Create Dictionary

def alien(fname, height, **characteristics):
    """Describe alien"""
    print('In 1947, the Air Force captured an alien in Roswell, New Mexico.')
    characteristics['first_name']=fname
    characteristics['height']=height
    return characteristics

the_literal_sense=alien(fname='Jaquaviontavius Bartholomuewl D\'markus James III', height='7ft', eyes='2', skin='tan', apparel='beret', weapon='baguette')

print(the_literal_sense)