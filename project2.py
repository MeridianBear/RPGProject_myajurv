'''

Author:         MUDRA YAJURVEDI
Date:           4/25/24
Assignment:     PROJECT 2
Course:         CPSC1050
Lab Section:    001

CODE DESCRIPTION: A text-based RPG

Links to GitHub, I hope:
https://github.com/MeridianBear/RPGProject_myajurv
https://github.com/MeridianBear/RPGProject_myajurv.git

time worked:
    7:00 hours

items to complete:
    input/output file
    location functions
    use classes and methods
        add at least one more class with methods to replace output log
    persistent states
    end game
    comments throughout all sections
    check that program works

'''

''' functions '''
# check if player has all 3 portal items
def check(inventory, timep, fuel, space):
    # initialize count variable
    checked = 0
    # go through each item in the player's inventory
    for item in inventory:
        # and if the item is a needed portal item, count variable increases by 1
        if item is timep or item is fuel or item is space:
            checked += 1
    # if player has all 3 needed portal items, return the number 3 to the program
    if checked == 3:
        return checked

# The Portal Hub
def portal_hub(inventory, timep, fuel, space):
    # check if player can end game,
    x = check(inventory, timep, fuel, space)
    # if they can, begin end game procedures
    if x == 3:
        return_home()
    
    # otherwise, run the items for this section


    # continue game and ask player where they want to go next
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
        crater_vale(inventory, timep, fuel, space)
    elif inp == 2:
        sifters(inventory, timep, fuel, space)
    elif inp == 3:
        dock_deck(inventory, timep, fuel, space)
    else:
        starguides(inventory, timep, fuel, space)

# The Portal Hub, ending
def return_home():
    print('YIPPEE!')

# The Crater Vale Asteroid Mines
def crater_vale(inventory, timep, fuel, space):
    # run the items for this section
    
    # check if player can end game
    x = check(inventory, timep, fuel, space)
    # if they can, notify them
    if x == 3:
        print('>>> You have all of the items you need to open a portal home! Head back to The Portal Hub to see Ozzi whenever you\'re done exploring.')

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
        portal_hub(inventory, timep, fuel, space)
    elif inp == 2:
        pods(inventory, timep, fuel, space)

# Sifter's Stack
def sifters(inventory, timep, fuel, space):
    # run the items for this section
    
    # check if player can end game
    x = check(inventory, timep, fuel, space)
    # if they can, notify them
    if x == 3:
        print('>>> You have all of the items you need to open a portal home! Head back to The Portal Hub to see Ozzi whenever you\'re done exploring.')

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
        portal_hub(inventory, timep, fuel, space)
    elif inp == 2:
        pods(inventory, timep, fuel, space)

# The Storage Pods
def pods(inventory, timep, fuel, space):
    # run the items for this section
    
    # check if player can end game
    x = check(inventory, timep, fuel, space)
    # if they can, notify them
    if x == 3:
        print('>>> You have all of the items you need to open a portal home! Head back to The Portal Hub to see Ozzi whenever you\'re done exploring.')

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
        crater_vale(inventory, timep, fuel, space)
    elif inp == 2:
        sifters(inventory, timep, fuel, space)
    else:
        portal_hub(inventory, timep, fuel, space)

# Sid's Shuttle 'n Spacecraft Dockin' Deck
def dock_deck(inventory, timep, fuel, space):
    # run the items for this section
    
    # check if player can end game
    x = check(inventory, timep, fuel, space)
    # if they can, notify them
    if x == 3:
        print('>>> You have all of the items you need to open a portal home! Head back to The Portal Hub to see Ozzi whenever you\'re done exploring.')

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
        portal_hub(inventory, timep, fuel, space)
    elif inp == 2:
        sifters(inventory, timep, fuel, space)
    else:
        city(inventory, timep, fuel, space)

# Xelominous City
def city(inventory, timep, fuel, space):
    # run the items for this section
    
    # check if player can end game
    x = check(inventory, timep, fuel, space)
    # if they can, notify them
    if x == 3:
        print('>>> You have all of the items you need to open a portal home! Head back to The Portal Hub to see Ozzi whenever you\'re done exploring.')

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
        portal_hub(inventory, timep, fuel, space)
    elif inp == 2:
        starguides(inventory, timep, fuel, space)
    else:
        dock_deck(inventory, timep, fuel, space)

# StarGuides HQ
def starguides(inventory, timep, fuel, space):
    # run the items for this section
    
    # check if player can end game
    x = check(inventory, timep, fuel, space)
    # if they can, notify them
    if x == 3:
        print('>>> You have all of the items you need to open a portal home! Head back to The Portal Hub to see Ozzi whenever you\'re done exploring.')

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
        portal_hub(inventory, timep, fuel, space)
    elif inp == 2:
        city(inventory, timep, fuel, space)
    else:
        crater_vale(inventory, timep, fuel, space)

''' classes '''
# object
class objects:
    def __init__(self, name, description):
        self.name = name
        self.desc = description

    def get_description(self):
        return self.desc

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
class portal_object(objects):
    def __init__(self, name, description):
        super().__init__(name, description)

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
    # initialize game variables
    import time
    game_over = False
    inventory = []
    # log = []
    # game_log = output_log()

    # initialize game objects
    carburetor = objects('Rusty Carburetor', "An old, rusty carburetor from Earth. Not sure how it found its way here, but it's kind of useless scrap metal now.")
    snackies = objects('Space Snacks', "Delicious snacks for space travel that were once in the Storage Pods, and are now in your stomach. :P")
    sweets = objects('StarGuide Sweets', "A somewhat pricey box of round, Zeronian sweets, sold to support the local StarGuide Sector.")
    
    timep = portal_object('Timepiece',"An old-fashioned, hourglass-type timepiece. The sand within it glows a golden hue within the gaudy, crystal frame. It seems to glitch in and out of existence, perhaps this odd object might help you get home.")
    fuel = portal_object('Fuel Crystal', "A pretty drab looking stone that was just mined out of the ground, and a major source of energy on Zeron. The miners in Crater Vale hold a lot of pride for these dark rocks, so maybe that's why they're called 'fuel crystals' and not 'fuel rocks.'")
    space = portal_object('Space Skipper', "It's pretty obvious that this was named by someone who thinks the concept of teleportation is lame. I can't believe they allow children to have these.")
    

    # intro to game - Portal Hub - only runs once
    # A character introduces you to your objective via dialogue and user response (with basic data validation)

    print('You slowly blink your eyes open and wince at the sudden throbbing in the back of your skull.')
    time.sleep(1)
    print('As blinding darkness gives way to blinding light, you hear the sound of someone speaking becoming clearer and clearer over the pulsing in your head.')
    time.sleep(1)
    print("You can't quite make out the language, but it seems that whoever is speaking is desperately trying to get your attention.")
    time.sleep(1)
    print('>>> What do you want to say?')
    time.sleep(1)
    print('1: "Hello?"')
    time.sleep(1)
    print('2: "Hey, what\'s going on?"')
    time.sleep(1)
    print('3: "OUCH!"')
    time.sleep(1)
    inp = int(input().strip())
    try:
        while inp != 1 and inp != 2 and inp != 3:
            print(">>> Hey! You can't say that! Try Option 1 or 2 or 3 next time.")
            inp = int(input().strip())
    except ValueError:
        print(">>> Hey! You can't say that! Try Option 1 or 2 or 3 next time.")
        inp = int(input().strip())

    print('Your vision clears a bit more, and you can make out the shape of a fur-covered, light pink, humanoid figure. They pause as they make eye contact with you. Their jet black eyes slowly blink at you before the figure speaks again.')
    time.sleep(1)
    print("???: \"Oh, you are an explorer from Copernican Sol III! Perhaps you're more familiar with the term 'Earth'?\"")
    time.sleep(1)
    print('>>> What do you want to say?')
    time.sleep(1)
    print('1: "You can speak English?"')
    time.sleep(1)
    inp = int(input().strip())
    try:
        while inp != 1:
            print(">>> Hey! You can't say that! Try Option 1 next time.")
            inp = int(input().strip())
    except ValueError:
        print(">>> Hey! You can't say that! Try Option 1 next time.")
        inp = int(input().strip())

    print('???: "...Sort of? But, that doesn\'t really matter."')
    time.sleep(1)
    print('???: "Are you okay? You look like you hit your head pretty hard. Do you even know where you are?"')
    time.sleep(1)
    print('>>> What do you want to say?')
    time.sleep(1)
    print('1: "What\'s your name?"')
    time.sleep(1)
    print('2: "Toto, I\'ve a feeling we\'re not in Kansas anymore..."')
    time.sleep(1)
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
        print('???: "Oh, pardon me for not introducing myself sooner! I am called Ozzi. It\'s a pleasure to make your acquaintance!."')
        time.sleep(1)
        print('Ozzi: "I take it, though, that you don\'t know where you are? Humans have named this planet "Exoplanet Noctifer-42d," but we call it Zeron."')
        time.sleep(1)
    elif inp == 2:
        print('???: "...I\'m afraid I don\'t know what you mean. Perhaps you hit your head harder than I thought...?"')
        time.sleep(1)
        print('???: "Anyways, I am known as Ozzi, and you are on the planet Zeron."')
        time.sleep(1)
    else:
        print('???: "This is Zeron, though you may know it as "Exoplanet Noctifer-42d." My name is Ozzi."')
        time.sleep(1)

    print("So, I'm on Zeron and your name is Ozzi?")
    time.sleep(1)
    print('Ozzi: "Correct."')
    time.sleep(1)
    print('>>> What do you want to say?')
    time.sleep(1)
    print('1: "How do I get home then?"')
    time.sleep(1)
    inp = int(input().strip())
    try:
        while inp != 1:
            print(">>> Hey! You can't say that! Try Option 1 next time.")
            inp = int(input().strip())
    except ValueError:
        print(">>> Hey! You can't say that! Try Option 1 next time.")
        inp = int(input().strip())

    print('Ozzi: "Well, a portal would probably be the easiest and fastest way home."')
    time.sleep(1)
    print('Ozzi: "Unless, you\'d like to be cryogenically frozen for about 1,764 years... but no one really does that anymore"')
    time.sleep(1)
    print('Ozzi: "Anyways, you\'re in luck! I am one of the Portal Hub\'s resident Portal Mechanics. If you collect a few little parts for me, I can open a portal for you back to Earth!"')
    time.sleep(1)
    print('>>> What do you want to say?')
    time.sleep(1)
    print('1: "Why isn\'t there already a portal to Earth here?"')
    time.sleep(1)
    print('2: "What do I need to collect?"')
    time.sleep(1)
    print('3: "Where can I get something to eat before I start collecting items?"')
    time.sleep(1)
    inp = int(input().strip())
    try:
        while inp != 1 and inp != 2 and inp != 3:
            print(">>> Hey! You can't say that! Try Option 1 or 2 or 3 next time.")
            inp = int(input().strip())
    except ValueError:
        print(">>> Hey! You can't say that! Try Option 1 or 2 or 3 next time.")
        inp = int(input().strip())
    if inp == 1:
        print('Ozzi: "Silly humans, assuming the universe revolves around you! No one here has much interest in Earth besides those far and few who come from that little planet."')
        time.sleep(1)
        print('Ozzi: "Because of that, any portal we have opened to Earth has fallen to disrepair because nobody ever uses it, so we only open one when a human asks to go home."')
        time.sleep(1)
    elif inp == 3:
        print('Ozzi: "The Storage Pods are your best bet, but they are a bit far from here."')
        time.sleep(1)
        print('Ozzi: "Here, I can lend you a snack or two for the journey there."')
        time.sleep(1)
        print('>>> Ozzi gives you a few Space Snacks for your journey.')
        time.sleep(1)
        snackies.pick_up(inventory)
    else:
        pass
    
    print('Ozzi: "In order for me to open a portal to Earth, I need three items: a Timepiece, a Space Skipper, and a Fuel Crystal."')
    time.sleep(1)
    print('Ozzi: "We Zeronians are not fond of currency, so most creatures here will either give the item to you if you ask, or will offer a trade."')
    time.sleep(1)

    print('Ozzi: "Here, I happen to have a... carburetor that I have no use for. Maybe it\'ll be useful to you."')
    time.sleep(1)
    print('>>> Ozzi offers you a Rusty Carburetor. Would you like to accept it?')
    time.sleep(1)
    print('>>> Respond either "Yes" or "No"')
    inp = input().strip().lower()
    while inp not in ['yes', 'no']:
        print('>>> Hey! You can\'t say that! Try saying "Yes" or "No" next time.')
        inp = input().strip().lower()
    if inp == 'yes':
        carburetor.pick_up(inventory)
        print()
        print('>>> Carburetor has been added to your inventory')
        time.sleep(1)
        print('Carburetor: ' + carburetor.get_description())
        time.sleep(1)
        print('You give Ozzi your thanks.')
        time.sleep(1)
    else:
        print('"...it\'s a carburetor...thaaanks..."')
        time.sleep(1)
        print('You gently refuse the rusty metal... thing...')
        time.sleep(1)
    
    # continue dialogue until you are offered the ability to go somewhere else


    # ask player where they want to go next
    print()
    print('>>> Now that you know what you\'re doing, Space Cadet, where do you want to go?')
    time.sleep(1)
    print('1: The Crater Vale Asteroid Mines')
    time.sleep(1)
    print('2: Sifter\'s Stack')
    time.sleep(1)
    print("3: Sid's Shuttle 'n Spacecraft Dockin' Deck")
    time.sleep(1)
    print('4: StarGuides HQ')
    time.sleep(1)
    inp = int(input().strip())
    try:
        while inp != 1 and inp != 2 and inp != 3 and inp != 4:
            print(">>> Hey! You can't say that! Try Option 1, 2, 3, or 4 next time.")
            inp = int(input().strip())
    except ValueError:
        print(">>> Hey! You can't say that! Try Option 1, 2, 3, or 4 next time.")
        inp = int(input().strip())

    timep.pick_up(inventory)
    space.pick_up(inventory)
    fuel.pick_up(inventory)
    # run selected location function, game continues from here within the functions defined above
    if inp == 1:
        crater_vale(inventory, timep, fuel, space)
    elif inp == 2:
        sifters(inventory, timep, fuel, space)
    elif inp == 3:
        dock_deck(inventory, timep, fuel, space)
    else:
        starguides(inventory, timep, fuel, space)

    # return to portal hub once all 3 parts are found
    
    # if user is at portal hub AND has all three portal items AND wants to open portal:
        # open portal home
        # run end game dialogue

if __name__ == "__main__":
    main()