import random

random_number = random.randint(1, 50)
print("Your random number is " + str(random_number))

Arcanum_of_wizardry = 10
chest_gear = 20
head_piece = 30
sword = 40

gear = {'Arcanum of Wizardry': 10, 'Rib Cage of King Ragmussen': 20,
        'Helm of Helia': 30, 'Flametooth Dagger': 40, 'Wand of Zeek': 50}


def rng():
    for key, value in gear.items():
        if random_number == value:
            print("You won the " + key + "!")
            break
    else:
        print("Sorry, you're a noob and win nothing!")


rng()
