import random

# Set your random roll range
random_number = random.randint(1, 50)
print("Your random number is " + str(random_number))

# Create dictionary for items and values
gear = {'Arcanum of Wizardry': 10, 'Rib Cage of King Ragmussen': 20,
        'Helm of Helia': 30, 'Flametooth Dagger': 40, 'Wand of Zeek': 50}

# Check random_number against items in dictionary.


def rng():
    for key, value in gear.items():
        if random_number == value:
            print("You won the " + key + "!")
            break
    else:
        print("Sorry, you're a noob and win nothing!")


rng()
