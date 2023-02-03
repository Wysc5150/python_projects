# Cam Wysocki
# 10/6/22
# Modified Fable

import random
import time

random.randint
random.randrange

actions=['flying', 'sprinting', 'sneaking', 'walking']

random_number=random.randint(0, 3)

print(f'Your random number is {random_number}.')

print('The Heron')
time.sleep(3)
if random_number==0:
    print('A Heron was flying along the bank of a stream, his long neck and pointed bill ready to snap up a likely morsel for his breakfast. Master Heron was hard to please that morning.')
elif random_number==1:
    print('A Heron was sprinting along the bank of a pond, his eyes on the semi-clear water, and his long neck and pointed bill ready to snap up a likely morsel for his lunch. The semi-clear water swarmed with fish, but Master Heron was hard to please that afternoon.')
elif random_number==2:
    print('A Heron was sneaking quietly along the side of an oasis, his eyes on the sandy water, and his long neck and pointed bill ready to snap up a likely morsel for his dinner. The sandy water swarmed with fish.')
elif random_number==3:
    print('A Heron was walking sedately along the bank of a stream, his eyes on the clear water, and his long neck and pointed bill ready to snap up a likely morsel for his breakfast. The clear water swarmed with fish, but Master Heron was hard to please that morning.')
time.sleep(4)
if random_number!=2:
    print('"No small fry for me," he said. "Such scanty fare is not fit for a Heron."')
elif random_number==2:
    print('"A meal is a meal," he said.')
time.sleep(3)
print('Now a fine young Perch swam near.')
time.sleep(2)
if random_number==0:
    print('"Yes please!" exclaimed the Heron. "Don\'t mind if i do!"')
elif random_number==1:
    print('"No indeed," said the Heron. "I couldn\'t bring myself to harm this creature!"')
elif random_number==2:
    print('"Now look at that," said the Heron. "A double meal for me tonight!"')
elif random_number==3:
    print('"No indeed," said the Heron. "I wouldn\'t even trouble to open my beak for anything like that!"')
time.sleep(4)
if random_number!=2:
    print('As the sun rose, the fish left the shallow water near the shore and swam below into the cool depths toward the middle. The Heron saw no more fish, and very glad was he at last to on a tiny Snail.')
elif random_number==2:
    print('"What a good meal," said the Heron as he makes his way home.')
time.sleep(4)
if random_number!=2:
    print('Do not be too hard to suit or you may have to be content with the worst or with nothing at all.')