# Cam W
# 10/24/22
# Zombie Project



from time import sleep


print('It was a cloudy night, and you find yourself at a "Dick\'s Sporting Goods" and just as you are about to start looking for weapons, a zombie appears!')
sleep(3)

print('You run from the zombie, which is approaching at a snail\'s pace, and you really have all the time in the world.')
sleep(3)

print('You make it to the weapons counter and see a wide variety of weapons.')
sleep(3)

weapons=['rifle', 'axe', 'football', 'baseball', 'tent', 'holy spear', 'whip', 'baseball bat', 'katana', 'golf club', 'boxing gloves', 'bare hands', 'walking stick', 'do nothing']

print(f'Your weapon choices are {weapons}')
sleep(10)
print('You can also choose your own')
sleep(2)
choice=input('Enter 1 for one of my options or enter 2 for your own. ')
sleep(3)

if choice=='1':
    print('Yeah, that\'s right. Enjoy trying to find the right option.')
    sleep(3)
    weapon=input('Now choose from my lovely collection (by name (ex. axe)). ')

    if weapon=='rifle':
        print('You grab the rifle, aim it at the zombie, and shoot.')
        sleep(3)
        print('Except you don\'t.')
        sleep(2)
        print('Why would a gun in a store be pre-loaded?')
        sleep(2)
        print('Anyway, you kept trying to shoot but the zombie takes a nice big chunk out of you.')
        sleep(3)
        print('Ending 1/15: "Trigger Trouble"')
    elif weapon=='axe':
        print('You swiftly grab the axe and take a swing.')
        sleep(3)
        print('For some reason, the axe is made of plastic and for some reason you did\'t notice.')
        sleep(4)
        print('You got bit.')
        sleep(2)
        print('Ending 2/15: "The Real Fake"')
    elif weapon=='football':
        print('Instead of grabbing the many weapons, you grab a football.')
        sleep(3)
        print('You literally only have one shot. You miss, because of course you did.')
        sleep(3)
        print('You get snacked on.')
        sleep(2)
        print('Ending 3/15: "Field Goal"')
    elif weapon=='baseball':
        print('While you COULD have gone for the much bigger football, you did not.')
        sleep(3)
        print('You miss. Nice one.')
        sleep(2)
        print('The zombie gives you a little nibble for your attempt.')
        sleep(3)
        print('Ending 4/15: "Run Home"')
    elif weapon=='tent':
        print('You set up the tent for protection, when running would have been a much better option than any I gave you.')
        sleep(5)
        print('The zombie respectfully enters and gives you a welcome chomp.')
        sleep(3)
        print('Ending 5/15: "You Can Run..."')
    elif weapon=='holy spear':
        print('You pick up the light-infused spear, and throw it at the zombie.')
        sleep(3)
        print('As it turns out, God got turned into the zombie, so when the spear hit the zombie, he becam powered up.')
        sleep(5)
        print('Luckily, you did not get bit. You got absolutely destroyed.')
        sleep(3)
        print('Ending 6/15: "A Certain Bloodline of Vampire Slayers..."')
    elif weapon=='whip':
        print('You choose the whip because whenever you see it used, it\'s used well.')
        sleep(3)
        print('You do not know how to use it well, and in your attempts, hurt yourself.')
        sleep(4)
        print('The zombie, of course, takes advantage of this and bites you.')
        sleep(3)
        print('Ending 7/15: "Why Would You Pick the Helicopter if You Didn\'t Know How To Fly It?!"')
    elif weapon=='baseball bat':
        print('You grab the bat and take a swing at the zombie, and slam its head off!')
        sleep(3)
        print('However, the head ricochets off the wall and its teeth sink into your arm.')
        sleep(4)
        print('Ending 8/15: "Home Run!"')
    elif weapon=='katana':
        print('You grab the katana and slash at the zombie.')
        sleep(3)
        print('You raise your arms in victory.')
        sleep(2)
        print('You only cut the torso from the legs. The zombie crawls over and knaws on your leg.')
        sleep(4)
        print('Ending 9/15: "Salt the Wound"')
    elif weapon=='golf club':
        print('You grab the club and go for a swing.')
        sleep(2)
        print('However, you forget to square your shoulders, straighten your back, and bend your knees.')
        sleep(4)
        print('Your golf swing sucks, and the zombie tears at you.')
        sleep(3)
        print('Ending 10/15: "What About Your Short Game?"')
    elif weapon=='boxing gloves':
        print('You put on the gloves and take a swing.')
        sleep(2)
        print('You miss.')
        sleep(2)
        print('You swing, and swing again.')
        sleep(2)
        print('You miss, you miss both times.')
        sleep(2)
        print('The zombie takes a swing with its head, and does not miss.')
        sleep(3)
        print('Ending 11/15: "This Went on for Several Hours..."')
    elif weapon=='bare hands':
        print('Out of all weapons, you choose the ones you already have.')
        sleep(3)
        print('The zombie catches your hand with its mouth.')
        sleep(3)
        print('Ending 12/15: "Knuckle Sandwich"')
    elif weapon=='walking stick':
        print('You pick up the walking stick and approach the zombie menacingly.')
        sleep(3)
        print('The zombie grabs the stick and knocks you unconcious. Probably bit you too.')
        sleep(3)
        print('Ending 13/15: "I Had to Beat an Old Lady With a Stick to Get This"')
    elif weapon=='do nothing':
        print('Doing nothing went about as well as you expected it to.')
        sleep(3)
        print('Ending 14/15: "What Did You Think Would Happen?"')
elif choice=='2':
    print('Sorry my weapons weren\'t good enough. Type your choice below.')
    sleep(3)
    user_weapon=input('')
    sleep(1)
    print(f'I can\'t predict what you pick, so let\'s assume your {user_weapon} worked. Make your own story.')
    sleep(5)
    print('Ending 15/15: "I Already Did 14 Other Endings, It\'s Your Turn."')
