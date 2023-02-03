from random import randint
import random
from time import sleep
from sys import exit
import sys

hp=25
base_mp=10
mp=10
lvl=1
next_lvl=15
money=0
attack_pwr=5
potion_stock=0
potion=20
fire=10
ice=15
lightning=20
cure=potion
magic=['Fire (8)']
ailments=['Whispering Wind (4)']
enemy_status='none'
player_status='none'
boss_key=0
none=0
dagger=2
weapon=none
weapon_id="none"
crit=(attack_pwr+lvl+weapon)*2
area=1
attack=attack_pwr+lvl+weapon
enemy=''
wolf_bite=5
wolf_bite_crit=(wolf_bite+area)*2
wolf_scratch=3
wolf_scratch_crit=(wolf_scratch+area)*2
def battle():
    global hp
    if hp<=0:
        print('GAME OVER')
        print()
        print('Retry?(This will restart your progress completely)')
        retry=input('Y/N ')
        if retry=='Y':
            hp=25
            mp=10
            base_mp=10
            lvl=1
            next_lvl=15
            money=0
            attack_pwr=5
            potion_stock=0
            magic=['Fire (8)']
            ailments=['Whispering Wind (4)']
            weapon=none=0
            area=1
            print('Restarting...')
            sleep(5)
            print()
            print(menu())
        elif retry=='N':
            exit()
    elif hp>0:
        if player_status=='fear':
            print(fear())
        print('What would you like to do?')
        print()
        sleep(2)
        print('Attack')
        print()
        sleep(1)
        print('Magic')
        print()
        sleep(1)
        print('Inflict')
        print()
        sleep(1)
        print('Potion')
        print()
        sleep(1)
        print('Run')
        print()
        sleep(1)
        print('Example: Attack')
        print()
        choice=input()
        if choice.title()=='Attack':
            print(hit())
        elif choice.title()=='Magic':
            print(spellcast())
        elif choice.title()=='Inflict':
            print(inflict())
        elif choice.title()=='Potion':
            if potion_stock==0:
                sleep(2)
                print('No potions available')
                print(battle())
            else:
                potion+hp
                sleep(2)
                print(f'HP: {hp}')
                print(battle())
        elif choice.title()=='Run':
            print(run())
        else:
            print('Option not available')
            print(battle())

def inflict():
    print('What would you like to inflict?')
    print(ailments)
    print('Press "q" to go back to the battle menu')
    print()
    skill=input()
    if skill.title()=='Whispering Wind':
        if mp<4:
            print('Not enough MP!')
            print(inflict())
        else:
            randint(1,3)
            mp=mp-4
            if randint==3:
                print('Inflicted Fear!')
                enemy_status='fear'
                print(opponent())
            else:
                print('No Effect!')
                print(opponent())
    elif skill.lower=='q':
        print(battle())
    else:
        print('Skill does not exist!')
        print(inflict())


def spellcast():
    global enemy
    print()
    print('Which spell would you like to use?')
    print()
    print(magic)
    print('Ex: Fire')
    print()
    spell=input()
    if spell.title()=='Fire':
        print(flame())
    elif spell.title()=='ice':
        print(freeze())

def flame():
    global mp
    global enemy
    print('You cast fire!')
    if mp<8:
        print('Insufficient MP!')
        print(spellcast())
    else:
        randint(1,3)
        if randint==3:
            print('Inflicted Burn!')
            enemy_status='burn'
        mp=mp-8
        enemy=enemy-fire
        print(f'Enemy HP:{enemy}')
        print()
        print(opponent())

def freeze():
    global mp
    global enemy
    if 'ice' in magic:
            print('You cast ice!')
            if mp<13:
                print('Insufficient MP!')
                print(spellcast())
            else:
                randint(1,3)
                if randint==3:
                    print('Inflicted Freeze!')
                    enemy_status='frozen'
                enemy=enemy-ice
                mp=mp-13
                print(f'Enemy HP: {enemy}')
                print(opponent())
    else:
        print('You don\'t know how to use ice magic...')
        print(spellcast())

def fear():
    if enemy_status=='fear':
        randint(1,3)
        if randint==1:
            print(f'The {enemy_id} is shaken!')
            enemy_status='none'
            print(battle())
        elif randint==2:
            enemy_status='none'
            print(opponent())
        elif randint==3:
            print(f'The {enemy_id} ran away!')
            enemy_status='none'
            enemy=0
            print(opponent())
    if player_status=='fear':
        randint(1,3)
        if randint==1:
            print('You\'re shaken!')
            player_status='none'
            print(opponent())
        elif randint==2:
            player_status='none'
            print(battle())
        elif randint==3:
            print('You ran away!')
            print(run())

def burn():
    if enemy_status=='burn':
        print(f'{enemy_id} is on fire!')
        sleep(1)
        burn_damage=5+area
        enemy=enemy-burn_damage
        print(f'{enemy_id} took {burn_damage} burn damage!')
        if enemy<=0:
            print(victory())
        else:
            print(battle())


def victory():
    if enemy_id=='wolf':
        print('Victory!')
        print()
        print('5xp & 10G')
        next_lvl-5
        money+5
    elif enemy_id=='skelleton':
        print('Victory!')
        print()
        print('15xp & 25G')
        next_lvl-15
        money+25
    if next_lvl<=0:
        print('Level Up!')
        hp+10
        base_mp+5
        attack_pwr+3
        lvl+1
        if lvl==2:
            next_lvl+30
        elif lvl==3:
            next_lvl+45
        elif lvl==4:
            next_lvl+60
        elif lvl==5:
            next_lvl+75
        elif lvl==6:
            next_lvl+90
        elif lvl==7:
            next_lvl+105
        elif lvl==8:
            next_lvl+120
        elif lvl==9:
            next_lvl+135
        elif lvl==10:
            next_lvl+150
        elif lvl==11:
            next_lvl+165
        elif lvl==12:
            next_lvl+180
        elif lvl==13:
            next_lvl+195
        elif lvl==14:
            next_lvl+210
        elif lvl==15:
            next_lvl+225
        elif lvl==16:
            next_lvl+240
        elif lvl==17:
            next_lvl+255
        elif lvl==18:
            next_lvl+270
        elif lvl==19:
            next_lvl+285
        elif lvl==20:
            next_lvl+300
        mp=base_mp
        input('Press ENTER to continue')
        print(stats())
    else:
        mp=base_mp
        input('Press ENTER to continue')
        print(menu())

def run():
    if player_status=='fear':
        player_status='none'
        print(menu())
    else:
        randint(1,3)
        if randint==3:
            mp=base_mp
            print('You escaped!')
            print(menu())
        else:
            print('Couldn\'nt get away!')
            print(opponent())



            
def stats():
    print(f'Level: {lvl}')
    print()
    sleep(1)
    print(f'HP: {hp}')
    print()
    sleep(1)
    print(f'MP: {mp}')
    print()
    sleep(1)
    print(f'Attack power: {attack_pwr}')
    print()
    sleep(1)
    print(f'Money: {money}G')
    print()
    sleep(1)
    print(f'Weapon: {weapon_id} +{weapon}')
    print()
    sleep(1)
    print(f'xp to next level: {next_lvl}')
    print()
    input('Press ENTER to continue')
    print(menu())

def check_magic():
    print(f'Known spells: {magic}')
    print()
    print(f'Known Ailments: {ailments}')
    print()
    input('Press ENTER to continue')
    print(menu())

def hit():
    global enemy
    randint(1,20)
    if randint==1:
        sleep(2)
        print('You missed!')
        print()
        print(opponent())
    elif randint==20:
        sleep(2)
        print(f'Critical hit! {crit} damage')
        print()
        enemy=enemy-crit
        wolf_hp=enemy-crit
        print(f'Enemy HP:{enemy}')
        print(opponent())
    else:
        sleep(2)
        print('Hit!')
        enemy=enemy-attack
        print(f'Enemy HP:{enemy}')
        print()
        print(opponent())
    
def encounter():
    global area
    if area==1:
        encounters=['Wolf', 'Wolf', 'Wolf', 'Wolf', 'Skelleton', 'Skelleton']
    elif area==2:
        encounters=['Wolf', 'Skelleton', 'Skelleton', 'Skelleton', 'Orc', 'Orc']
    elif area==3:
        encounters=['Skelleton', 'Skelleton', 'Orc', 'Orc', 'Orc', 'Orc']
    random.choice(encounters)
    if random.choice(encounters)=='Wolf':
        global wolf_hp
        wolf_hp=15
        global enemy_id
        enemy_id='wolf'
        global enemy
        enemy=wolf_hp
        print('A wolf appears!')
        print(battle())
        #enemy ID

def opponent():
    global enemy
    global wolf_hp
    global hp
    global enemy_id
    if enemy_id=='wolf':
        w_attacks=['Bite', 'Scratch', 'Howl']
        if enemy>0:
            random.choice(w_attacks)
            if random.choice(w_attacks)=='Bite':
                randint(1,5)
                if randint==1:
                    sleep(2)
                    print('The wolf charges for a bite')
                    sleep(2)
                    print('The wolf misses!')
                    sleep(3)
                    print(battle())
                elif randint==5:
                    sleep(2)
                    print('The wolf charges for a bite')
                    sleep(2)
                    print(f'Critical hit! {wolf_bite_crit} damage')
                    hp=hp-wolf_bite_crit
                    print(f'HP:{hp}')
                    sleep(3)
                    print(battle())
                else:
                    sleep(2)
                    print('The wolf charges for a bite')
                    sleep(2)
                    print(f'Hit! {wolf_bite} damage')
                    hp=hp-wolf_bite
                    print(f'HP:{hp}')
                    sleep(3)
                    print(battle())
            elif random.choice(w_attacks)=='Scratch':
                randint(1,5)
                if randint==1:
                    sleep(2)
                    print('The wolf raises its paw to scratch')
                    sleep(2)
                    print('The wolf misses!')
                    sleep(3)
                    print(battle())
                elif randint==5:
                    sleep(2)
                    print('The wolf raises its paw to scratch')
                    sleep(2)
                    print(f'Critical hit! {wolf_scratch_crit} damage')
                    hp=hp-wolf_scratch_crit
                    print(f'HP:{hp}')
                    sleep(3)
                    print(battle())
                else:
                    sleep(2)
                    print('The wolf raises its paw to scratch')
                    sleep(2)
                    print(f'Hit! {wolf_scratch} damage')
                    hp=hp-wolf_scratch
                    print(f'HP:{hp}')
                    sleep(3)
                    print(battle())
            elif random.choice(w_attacks)=='Howl':
                randint(1,3)
                if randint==3:
                    print('Inflicted with Fear!')
                    player_status='fear'
                    print(battle())
                else:
                    print('No Effect!')
                    print(battle())
            if enemy_status=='burn':
                print(burn())
                
        elif enemy<=0:
            print(victory())
            

def menu():
    print()
    print('What would you like to do?')
    print()
    sleep(2)
    print('Hunt')
    print()
    sleep(1)
    print('Check Magic')
    print()
    sleep(1)
    print('Shop')
    print()
    sleep(1)
    print('Check Stats')
    print()
    sleep(1)
    print('Fight Boss')
    print()
    sleep(1)
    print('Press "q" to quit (Your progress will not be saved)')
    print()
    sleep(1)
    print('Example: Hunt')
    print()
    action=input()
    if action.title()=='Hunt':
        print(encounter())
    elif action.title()=='Check Magic':
        print(check_magic())
    elif action.title()=='Shop':
        'shop'
    elif action.title()=='Check Stats':
        print(stats())
    elif action.title()=='Fight Boss':
        'boss'
    elif action.lower()=='q':
        exit()
    else:
        print('Option not available')
        print(menu())

def shop():
    print('Shop purchases do not need to include the amount of Gold required to buy it when inputing your purchase')
    if area==1:
        shoplist=['Potion (30G)', 'Dagger (50G)', 'Area 1 Boss Key (75G)']
        sleep(2)
        print('Whatcha buyin\'?')
        sleep(1)
        print(shoplist)
        sleep(1)
        print('Press "q" to leave')
        purchase=input()
        if purchase.title()=='Potion':
            if money<30:
                print('Sorry, you ain\'t got enough gold')
                sleep(3)
                print(shop())
            else:
                print('Thank you for your patronage')
                money-30
                potion_stock+1
                sleep(2)
                print(shop())
        elif purchase.title()=='Dagger':
            if shoplist.count('Dagger')==True:
                if money<50:
                    print('Killing comes at a price, kid')
                    sleep(3)
                    print(shop())
                else:
                    print('Happy stabbing')
                    money-50
                    weapon_id='Dagger'
                    weapon=dagger
                    sleep(2)
                    print(shop())
            else:
                print('You got that already')
                sleep(2)
                print(shop())
        elif purchase.title()=='Area 1 Boss Key':
            if shoplist.count('Area 1 Boss Key')==True:
                if money<75:
                    print('A gutsy move for someone who doesn\'t got enough cash')
                    sleep(3)
                    print(shop())
                else:
                    print('Good luck')
                    money-75
            else:
                print('We only had one of those')
                sleep(2)
                print(shop())









print(menu())

