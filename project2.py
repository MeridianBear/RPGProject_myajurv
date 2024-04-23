'''
- filled out readme
- needs 3+ if statement branches
- needs 3+ while/for loops
- needs 4+ functioning classes
    - at least one class must inherit from another
    - needs 10+ functioning methods
- needs at least one input/output file -> output log (summary of game events)
- game title, navigable map (or similar), items/characters to interact with
- persistent states (e.g. if you pick up an item it's not there later)
'''
# FIX LIST:
# make it so that user HAS to input a correct value before moving on

# time worked:
# 5:45 hours

''' functions '''
# The Portal Hub
def portal_hub():
    # run the items for this section

    # ask player where they want to go next
    print('>>> Where do you want to go next, Space Cadet?')
    print('1: The Crater Vale Asteroid Mines')
    print('2: Sifter\'s Stack')
    print("3: Sid's Shuttle 'n Spacecraft Dockin' Deck")
    print('4: StarGuides HQ')
    inp = int(input().strip())
    try:
        while inp != 1 and inp != 2 and inp != 3 and inp != 4:
            print("Hey! You can't say that! Try Option 1, 2, 3, or 4 next time.")
            inp = int(input().strip())
    except ValueError:
        print("Hey! You can't say that! Try Option 1, 2, 3, or 4 next time.")
        inp = int(input().strip())
    # run location functions as user picks where they want to go next
    if inp == 1:
        crater_vale()
    elif inp == 2:
        sifters()
    elif inp == 3:
        dock_deck()
    else:
        starguides()

# The Crater Vale Asteroid Mines
def crater_vale():
    # run the items for this section

    # ask player where they want to go next
    print('>>> Where do you want to go next, Space Cadet?')
    print('1: The Portal Hub')
    print('2: The Storage Pods')
    inp = int(input().strip())
    try:
        while inp != 1 and inp != 2:
            print("Hey! You can't say that! Try Option 1 or 2 next time.")
            inp = int(input().strip())
    except ValueError:
        print("Hey! You can't say that! Try Option 1 or 2 next time.")
        inp = int(input().strip())
    # run location functions as user picks where they want to go next
    if inp == 1:
        portal_hub()
    elif inp == 2:
        pods()

# Sifter's Stack
def sifters():
    # run the items for this section

    # ask player where they want to go next
    print('>>> Where do you want to go next, Space Cadet?')
    print('1: The Portal Hub')
    print('2: The Storage Pods')
    inp = int(input().strip())
    try:
        while inp != 1 and inp != 2:
            print("Hey! You can't say that! Try Option 1 or 2 next time.")
            inp = int(input().strip())
    except ValueError:
        print("Hey! You can't say that! Try Option 1 or 2 next time.")
        inp = int(input().strip())
    # run location functions as user picks where they want to go next
    if inp == 1:
        portal_hub()
    elif inp == 2:
        pods()

# The Storage Pods
def pods():
    # run the items for this section

    # ask player where they want to go next
    print('>>> Where do you want to go next, Space Cadet?')
    print('1: The Crater Vale Asteroid Mines')
    print('2: Sifter\'s Stack')
    print("3: The Portal Hub")
    inp = int(input().strip())
    try:
        while inp != 1 and inp != 2 and inp != 3 and inp != 4:
            print("Hey! You can't say that! Try Option 1, 2, or 3 next time.")
            inp = int(input().strip())
    except ValueError:
        print("Hey! You can't say that! Try Option 1, 2, or 3 next time.")
        inp = int(input().strip())
    # run location functions as user picks where they want to go next
    if inp == 1:
        crater_vale()
    elif inp == 2:
        sifters()
    else:
        portal_hub()

# Sid's Shuttle 'n Spacecraft Dockin' Deck
def dock_deck():
    # run the items for this section

    # ask player where they want to go next
    print('>>> Where do you want to go next, Space Cadet?')
    print('1: The Portal Hub')
    print('2: Sifter\'s Stack')
    print("3: Xelominous City")
    inp = int(input().strip())
    try:
        while inp != 1 and inp != 2 and inp != 3:
            print("Hey! You can't say that! Try Option 1, 2, or 3 next time.")
            inp = int(input().strip())
    except ValueError:
        print("Hey! You can't say that! Try Option 1, 2, or 3 next time.")
        inp = int(input().strip())
    # run location functions as user picks where they want to go next
    if inp == 1:
        portal_hub()
    elif inp == 2:
        sifters()
    else:
        city()

# Xelominous City
def city():
    # run the items for this section

    # ask player where they want to go next
    print('>>> Where do you want to go next, Space Cadet?')
    print('1: The Portal Hub')
    print('2: StarGuides HQ')
    print("3: Sid's Shuttle 'n Spacecraft Dockin' Deck")
    inp = int(input().strip())
    try:
        while inp != 1 and inp != 2 and inp != 3:
            print("Hey! You can't say that! Try Option 1, 2, or 3 next time.")
            inp = int(input().strip())
    except ValueError:
        print("Hey! You can't say that! Try Option 1, 2, or 3 next time.")
        inp = int(input().strip())
    # run location functions as user picks where they want to go next
    if inp == 1:
        portal_hub()
    elif inp == 2:
        starguides()
    else:
        dock_deck()

# StarGuides HQ
def starguides():
    # run the items for this section

    # ask player where they want to go next
    print('>>> Where do you want to go next, Space Cadet?')
    print('1: The Portal Hub')
    print('2: Xelominous City')
    print("3: The Crater Vale Asteroid Mines")
    inp = int(input().strip())
    try:
        while inp != 1 and inp != 2 and inp != 3:
            print("Hey! You can't say that! Try Option 1, 2, or 3 next time.")
            inp = int(input().strip())
    except ValueError:
        print("Hey! You can't say that! Try Option 1, 2, or 3 next time.")
        inp = int(input().strip())
    # run location functions as user picks where they want to go next
    if inp == 1:
        portal_hub()
    elif inp == 2:
        city()
    else:
        crater_vale()

# all 3 portal items?
def all_three():
    pass

''' classes '''
# object
class reg_object:
    def __init__(self, name, description):
        self.name = name
        self.desc = description

    def pick_up(self, inventory):
        inventory.append(self.name)
        return inventory

    def give(self, inventory, character_inventory):
        character_inventory.append(self.name)
        inventory.remove(self.name)
        # returns tuple
        # in main program, separate values
        return inventory, character_inventory

    def discard(self, inventory):
        inventory.remove(self.name)
        return inventory

# portal_object
class portal_object:
    def __init__(self, name, description):
        self.name = name
        self.desc = description

    def pick_up(self, inventory):
        inventory.append(self.name)
        return inventory

# portal
class portal:
    def __init__(self, portal_objects: list):
        self.objects = portal_objects

    def check_items(self, inventory):
        count = 0
        for item in inventory:
            if item in self.objects:
                count += 1
        return count

# output_log
class output_log:
    def add(self, log):
        log.append()
        return log
    
    def output(self, log):
        pass
        # print out log in adventure_log.txt file

# define main program
def main():
    # initialize game variables and log
    game_over = False
    inventory = []
    log = []
    game_log = output_log()

    # initialize game objects
    carburetor = reg_object('Rusty Carburetor', "An old, rusty carburetor from Earth. Not sure how it found its way here, but it's kind of useless scrap metal now.")
    snackies = reg_object('Space Snacks', "Delicious snacks for space travel that were once in the Storage Pods, and are now in your stomach. :P")
    sweets = reg_object('StarGuide Sweets', "A somewhat expensive box of round, Zeronian sweets, sold to support the local StarGuide Sector.")
    
    time = portal_object('Timepiece',"An old-fashioned, hourglass-type timepiece. The sand within it glows a golden hue within the gaudy, crystal frame. It seems to glitch in and out of existence, perhaps this odd object might help you get home.")
    fuel = portal_object('Fuel Crystal', "A pretty drab looking stone that was just mined out of the ground, and a major source of energy on Zeron. The miners in Crater Vale hold a lot of pride for these dark rocks, so maybe that's why they're called 'fuel crystals' and not 'fuel rocks.'")
    space = portal_object('Space Skipper', "It's pretty obvious that this was named by someone who thinks the concept of teleportation is lame. I can't believe they allow children to have these.")
    
    # intro to game - Portal Hub - only runs once
    print('You slowly blink your eyes open and wince at the sudden throbbing in the back of your skull.')
    print('As blinding darkness gives way to blinding light, you hear the sound of someone speaking become clearer and clearer over the pulsing in your head.')
    print("You can't quite make out the language, but it seems that whoever is speaking is desperately trying to get your attention.")
    print('>>> What do you want to say?')
    print('1: "Hello?"')
    print('2: "Hey, what\'s going on?"')
    print('3: "OUCH!"')
    inp = int(input().strip())
    try:
        while inp != 1 and inp != 2 and inp != 3:
            print("Hey! You can't say that! Try Option 1 or 2 or 3 next time.")
            inp = int(input().strip())
    except ValueError:
        print("Hey! You can't say that! Try Option 1 or 2 or 3 next time.")
        inp = int(input().strip())

    print()
    print('Your vision clears a bit more, you can make out the shape of a fur-covered, light pink, humanoid figure. They pause as they make eye contact with you. Their jet black eyes slowly blink at you before the figure speaks again.')
    print("???: \"Oh, you are an explorer from Copernican Sol III! Perhaps you're more familiar with the term 'Earth'?\"")
    print('>>> What do you want to say?')
    print('1: "You can speak English?"')
    inp = int(input().strip())
    try:
        while inp != 1:
            print("Hey! You can't say that! Try Option 1 next time.")
            inp = int(input().strip())
    except ValueError:
        print("Hey! You can't say that! Try Option 1 next time.")
        inp = int(input().strip())

    print()
    print('???: "...Sort of? But, that doesn\'t really matter."')
    print('"Are you okay? You look like you hit your head pretty hard. Do you even know where you are?"')
    print('>>> What do you want to say?')
    print('1: "What\'s your name?"')
    print('2: "Toto, I\'ve a feeling we\'re not in Kansas anymore..."')
    print('3: "Where am I?"')
    inp = int(input().strip())
    try:
        while inp != 1 and inp != 2 and inp != 3:
            print("Hey! You can't say that! Try Option 1 or 2 or 3 next time.")
            inp = int(input().strip())
    except ValueError:
        print("Hey! You can't say that! Try Option 1 or 2 or 3 next time.")
        inp = int(input().strip())
    if inp == 1:
        print('???: Oh, pardon me for not introducing myself sooner! I am called Ozzi. It\'s a pleasure to make your acquaintance!.')
        print('Ozzi: I take it, though, that you don\'t know where you are? Humans have named this planet "Exoplanet Noctifer-42d," but we call it Zeron.')
    elif inp == 2:
        print('???: ...I\'m afraid I don\'t know what you mean. Perhaps you hit your head harder than I thought...?')
        print('???: Anyways, I am known as Ozzi, and you are on the planet Zeron.')
    else:
        print('???: This is Zeron, though you may know it as "Exoplanet Noctifer-42d." My name is Ozzi.')

    # Ozzi blabs about how to get home
    print()
    print("So, I'm on Zeron and your name is Ozzi?")
    print('Ozzi: "Correct."')
    print('"How do I get home then?"')
    print('Ozzi: ""')
    print('Ozzi: ""')
    print('Ozzi: ""')
    print('Ozzi: ""')

    # Ozzi gifts a carburetor... sweet...
    print()
    print('>>> Ozzi offers you a Rusty Carburetor. Would you like to accept it?')
    print('"Yes" or "No"')
    inp = input().strip().lower()
    while inp not in ['yes', 'no']:
        print('Hey! You can\'t say that! Try saying "Yes" or "No" next time.')
        inp = input().strip().lower()
    if inp == 'yes':
        print()
        print('"Thanks, Ozzi!"')
        carburetor.pick_up(inventory)
        print('>>> Carburetor has been added to your inventory')
    else:
        print()
        print('"...it\'s a carburetor...thaaanks..."')
        print('>>> You gently refuse the rusty metal... blob.')
    
    # continue dialogue until you are offered the ability to go somewhere else


    # ask player where they want to go next
    print()
    print('>>> Now that you know what you\'re doing, Space Cadet, where do you want to go?')
    print('1: The Crater Vale Asteroid Mines')
    print('2: Sifter\'s Stack')
    print("3: Sid's Shuttle 'n Spacecraft Dockin' Deck")
    print('4: StarGuides HQ')
    inp = int(input().strip())
    try:
        while inp != 1 and inp != 2 and inp != 3 and inp != 4:
            print("Hey! You can't say that! Try Option 1, 2, 3, or 4 next time.")
            inp = int(input().strip())
    except ValueError:
        print("Hey! You can't say that! Try Option 1, 2, 3, or 4 next time.")
        inp = int(input().strip())
    # run location functions as user picks where they want to go next
    if inp == 1:
        crater_vale()
    elif inp == 2:
        sifters()
    elif inp == 3:
        dock_deck()
    else:
        starguides()

    # return to portal hub once all 3 parts are found
    
    # if user is at portal hub AND has all three portal items AND wants to open portal:
        # open portal home
        # run end game dialogue

if __name__ == "__main__":
    main()