'''
Author:         MUDRA YAJURVEDI
Date:           4/25/24
Assignment:     PROJECT 2
Course:         CPSC1050
Lab Section:    001

CODE DESCRIPTION: A text-based RPG, see README

At least one working link to GitHub, I hope:
https://github.com/MeridianBear/RPGProject_myajurv
https://github.com/MeridianBear/RPGProject_myajurv.git

time worked:
    8:45 hours

items to complete:
    - output log
        - add items/lines to output log
        - create and write to output file
    - location functions
        - update dialogue and characters
        - use classes and methods
        - update item existence both in location and in inventory (persistent states)
        - end game function
    - comments throughout all sections
    - confirm that program works

'''
# import time functions
import time

''' functions '''
# check if player has all 3 portal items
def check(inventory, has_t, has_f, has_s):
    # initialize checked bool
    checked = False
    # if player has all 3 needed portal items, return checked as True
    if has_t == True and has_f == True and has_s == True:
        checked = True
        return checked

# The Portal Hub
def portal_hub(inventory, has_t, has_f, has_s, player):
    # check if player can end game,
    x = check(inventory, has_t, has_f, has_s)
    # if they can, begin end game procedures
    if x == True:
        return_home(note, timep, fuel, space, player)
    
    # otherwise, run the items for this section
    print()
    print('Ozzi: "You\'re back already? Do you have all of the parts I need yet?"')
    time.sleep(2)
    print(f'{player}: "Not yet, what am I missing?"')
    time.sleep(1)
    if has_t == False:
        print('Ozzi: "You\'re missing a Timepiece. Try looking for it in Sifter\'s Stack."')
        time.sleep(2)
    if has_f == False:
        print('Ozzi: "You\'re missing a Fuel Crystal. Try looking for it in the Crater Vale Asteroid Mines."')
        time.sleep(2)
    if has_s == False:
        print('Ozzi: "You\'re missing a Space Skipper. Try looking for it in Sid\'s Docking Deck."')
        time.sleep(2)
    print(f'{player}: "Thanks for the tip, Ozzi! I\'ll see you again when I have all of the parts you need, or if I need help again."')
    time.sleep(2)
    print('Ozzi: "Of course! I\'ll be right here if you need anything."')
    time.sleep(2)

    # continue game and ask player where they want to go next
    print()
    print('>>> Where do you want to go next, Space Cadet?')
    print('1: The Crater Vale Asteroid Mines')
    print('2: Sifter\'s Stack')
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
        crater_vale(inventory, has_t, has_f, has_s, player)
    elif inp == 2:
        sifters(inventory, has_t, has_f, has_s, player)
    elif inp == 3:
        dock_deck(inventory, has_t, has_f, has_s, player)

# The Portal Hub, ending
def return_home(note, timep, fuel, space, player):
    # run end game dialogue
    # get note from Ozzi (object already defined)
    # put log into new file
    pass

# The Crater Vale Asteroid Mines
def crater_vale(inventory, has_t, has_f, has_s, player):
    # run the items for this section
    
    # check if player can end game
    x = check(inventory, has_t, has_f, has_s)
    # if they can, begin end game procedures
    if x == True:
        print()
        print('>>> You have all of the items you need to open a portal home! Head back to The Portal Hub to see Ozzi whenever you\'re done exploring.')

    # continue game and ask player where they want to go next
    print()
    print('>>> Where do you want to go next, Space Cadet?')
    print('1: The Portal Hub')
    print('2: Sifter\'s Stack')
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
        portal_hub(inventory, has_t, has_f, has_s, player)
    elif inp == 2:
        sifters(inventory, has_t, has_f, has_s, player)
    elif inp == 3:
        dock_deck(inventory, has_t, has_f, has_s, player)

# Sifter's Stack
def sifters(inventory, has_t, has_f, has_s, player):
    # run the items for this section
    
    # check if player can end game
    x = check(inventory, has_t, has_f, has_s)
    # if they can, begin end game procedures
    if x == True:
        print()
        print('>>> You have all of the items you need to open a portal home! Head back to The Portal Hub to see Ozzi whenever you\'re done exploring.')

    # continue game and ask player where they want to go next
    print()
    print('>>> Where do you want to go next, Space Cadet?')
    print('1: The Crater Vale Asteroid Mines')
    print('2: The Portal Hub')
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
        crater_vale(inventory, has_t, has_f, has_s, player)
    elif inp == 2:
        portal_hub(inventory, has_t, has_f, has_s, player)
    elif inp == 3:
        dock_deck(inventory, has_t, has_f, has_s, player)

# Sid's Shuttle 'n Spacecraft Dockin' Deck
def dock_deck(inventory, has_t, has_f, has_s, player):
    # run the items for this section
    
    # check if player can end game
    x = check(inventory, has_t, has_f, has_s)
    # if they can, begin end game procedures
    if x == True:
        print()
        print('>>> You have all of the items you need to open a portal home! Head back to The Portal Hub to see Ozzi whenever you\'re done exploring.')

    # continue game and ask player where they want to go next
    print()
    print('>>> Where do you want to go next, Space Cadet?')
    print('1: The Crater Vale Asteroid Mines')
    print('2: Sifter\'s Stack')
    print("3: The Portal Hub")
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
        crater_vale(inventory, has_t, has_f, has_s, player)
    elif inp == 2:
        sifters(inventory, has_t, has_f, has_s, player)
    elif inp == 3:
        portal_hub(inventory, has_t, has_f, has_s, player)

''' classes '''
# object
class objects:
    def __init__(self, name, description):
        self.name = name
        self.desc = description
    
    def get_name(self):
        return self.name

    def get_description(self):
        return self.desc

    def pick_up(self, inventory):
        inventory.append(self.name)
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
    def create_log(self, log):
        self.log = log
    
    def add(self, text):
        self.log.append(text)

    def print_log(self):
        for item in self.log:
            print(item)



# define main program
def main():
    # initialize game variables
    has_t = False
    has_s = False
    has_f = False
    inventory = []
    log = []
    game_log = output_log()
    game_log.create_log(log)
    
    # initialize game objects
    note = objects('Note from Ozzi',"A heartfelt note from the furry, pink guy you met on Zeron. You are beyond grateful for his help to get you home.")
    timep = portal_object('Timepiece',"An old-fashioned, hourglass-type timepiece. The sand within it glows a golden hue within the gaudy, crystal frame. It seems to glitch in and out of existence, perhaps this odd object might help you get home.")
    fuel = portal_object('Fuel Crystal', "A pretty drab looking stone that was just mined out of the ground, and a major source of energy on Zeron. The miners in Crater Vale hold a lot of pride for these dark rocks, so maybe that's why they're called 'fuel crystals' and not 'fuel rocks.'")
    space = portal_object('Space Skipper', "It's pretty obvious that this was named by someone who thinks the concept of teleportation is lame. I can't believe they allow children to have these.")

    # pre-game: obtain and confirm player username
    print()
    print()

    # ask player for username and take input
    print('Welcome Space Cadet!')

    # all instances of time.sleep(seconds to pause) in this program are used to make the terminal experience better for the player
    time.sleep(1)
    print('What is your name? Please keep in mind that this will be stored in your Adventurer\'s Log and will be how you are referred to throughout the game.')
    player = input().strip()
    print()

    # confirm with player using player feedback and user validation
    print(f'Are you certain that "{player}" is the name you would like to go by?')
    y_n = input().strip().lower()
    while y_n not in ['yes','no']:
        print()
        print(">>> Hey! You can't say that! Try saying \"Yes\" or \"No\" next time.")
    if y_n == 'no':
        print('What would you like us to call you then?')
        player = input().strip()
    print()
    print(f'Perfect! You\'re all set to go Space Cadet {player}! Happy Adventuring!')
    time.sleep(2)
    
    # intro to game: Portal Hub - only runs once, is most of the actual program under "__main__"
    # A character introduces you to your objective via dialogue and player response (with very basic data validation)
    print()
    print()

    # have user begin game when they're ready
    print('>>> Type "Start" to begin game')
    start = input().strip().lower()

    # while user does not type "Start," remind player to start when they're ready
    while start != 'start':
        print()
        print('>>> Type "Start" whenever you\'re ready to play.')

    # add username to log
    game_log.add(f"Space Cadet {player}'s Adventurer's Log:")

    # once user has started, play out the opening act of the game
    print()
    time.sleep(1)
    print()
    time.sleep(1)
    print('You slowly blink your eyes open and wince at the sudden throbbing in the back of your skull.')
    time.sleep(2)
    print('As blinding darkness gives way to blinding light, you hear the sound of someone speaking becoming clearer and clearer over the pulsing in your head.')
    time.sleep(2.5)
    print("You can't quite make out the language, but it seems that whoever is speaking is desperately trying to get your attention.")
    time.sleep(2)

    # offer player response options and validate input
    print()
    print('>>> What do you want to say?')
    time.sleep(1)
    print('1: "Hello?"')
    time.sleep(1)
    print('2: "Hey, what\'s going on?"')
    time.sleep(1)
    print('3: "OUCH!"')
    time.sleep(1)
    inp = int(input().strip())

    # all instances of try/except in this program are meant to catch a user the first time they type a non-numerical value
    try:
        while inp != 1 and inp != 2 and inp != 3:
            print()
            print(">>> Hey! You can't say that! Try Option 1 or 2 or 3 next time.")
            inp = int(input().strip())
    except ValueError:
        print()
        print(">>> Hey! You can't say that! Try Option 1 or 2 or 3 next time.")
        inp = int(input().strip())

    # continue text
    print()
    print('Your vision clears a bit more, and you can make out the shape of a fur-covered, light pink, humanoid figure.')
    print('They pause as they make eye contact with you. Their jet black eyes slowly blink at you before they speak again.')
    time.sleep(3.5)
    print("???: \"Oh, you must be an explorer from Copernican Sol III! Perhaps you're more familiar with the term 'Earth'?\"")
    time.sleep(2)
    print(f'{player}: "I... think so? What happened?"')
    time.sleep(2)
    print('???: "You look like you hit your head pretty hard when you came through that portal. Are you okay? Do you even know where you are?"')
    time.sleep(2)

    # offer user response options and validate user input
    print()
    print('>>> What do you want to say?')
    time.sleep(1)
    print('1: "What\'s your name?"')
    time.sleep(1)
    print('2: "Toto, I\'ve a feeling we\'re not in Kansas anymore..."')
    time.sleep(1)
    print('3: "No, I\'m afraid I don\'t. Where am I?"')
    inp = int(input().strip())
    try:
        while inp != 1 and inp != 2 and inp != 3:
            print("Hey! You can't say that! Try Option 1 or 2 or 3 next time.")
            inp = int(input().strip())
    except ValueError:
        print("Hey! You can't say that! Try Option 1 or 2 or 3 next time.")
        inp = int(input().strip())
    print()

    # depending on what the user says, change the dialogue displayed in the terminal
    if inp == 1:
        print('???: "Oh, pardon me for not introducing myself sooner! I am called Ozzi. It\'s a pleasure to make your acquaintance!"')
        time.sleep(2)
        print('Ozzi: "I take it, though, that you don\'t know where you are? Humans have named this planet "Exoplanet Noctifer-42d," but we call it Zeron."')
        time.sleep(2)
    elif inp == 2:
        print('???: "...I\'m afraid I don\'t know what you mean. Perhaps you hit your head harder than I thought...?"')
        time.sleep(2)
        print('???: "Anyways, I am known as Ozzi, and you are on the planet Zeron."')
        time.sleep(2)
    else:
        print('???: "This is Zeron, though you may know it as "Exoplanet Noctifer-42d." My name is Ozzi."')
        time.sleep(2)

    # add meeting Ozzi to log
    game_log.add(f'{player} meets Ozzi and discovers that they have mistakenly arrived on to the planet Zeron.')

    # continue text
    print(f'{player}: "So, I\'m on Zeron and your name is Ozzi?"')
    time.sleep(2)
    print('Ozzi: "Correct."')
    time.sleep(2)
    print(f'{player}: "How do I get home, then?"')
    print('Ozzi: "Well, a portal would probably be the easiest and fastest way home."')
    time.sleep(2)
    print('Ozzi: "Unless you\'d like to be cryogenically frozen for about 1,764 years... but no one really does that anymore"')
    time.sleep(3)
    print('Ozzi: "Anyways, you\'re in luck! I am one of the Portal Hub\'s resident Portal Mechanics. If you collect a few little parts for me, I can open a portal for you back to Earth!"')
    time.sleep(3)
    print()

    # take and validate user input for dialogue
    print('>>> What do you want to say?')
    time.sleep(1)
    print('1: "Why isn\'t there already a portal to Earth here?"')
    time.sleep(1)
    print('2: "What do I need to collect?"')
    time.sleep(1)
    inp = int(input().strip())
    try:
        while inp != 1 and inp != 2:
            print()
            print(">>> Hey! You can't say that! Try Option 1 or 2 next time.")
            inp = int(input().strip())
    except ValueError:
        print()
        print(">>> Hey! You can't say that! Try Option 1 or 2 next time.")
        inp = int(input().strip())
    print()
    if inp == 1:
        print('Ozzi: "Silly humans, assuming the universe revolves around you! No one here has much interest in Earth besides those far and few who come from that little planet."')
        time.sleep(3)
        print('Ozzi: "Because of that, any portal we have opened to Earth has fallen to disrepair because nobody ever uses it, so we only open one when a human asks to go home."')
        time.sleep(3)
        # add having audacity to log
        game_log.add(f'{player} talks to Ozzi and discovers that human are *not* the center of the universe.')

    # continue dialogue until intro portion of game is over
    print('Ozzi: "In order for me to open a new portal to Earth, I will need three items: a Timepiece, a Space Skipper, and a Fuel Crystal."')
    time.sleep(2)
    print('Ozzi: "We Zeronians are not fond of currency, so if you ask around, most on this planet will either give the item to you, or will offer you a trade for it."')
    time.sleep(3)
    print('Ozzi: "Just make your way around some of the more populated areas of the planet, and I\'m sure you\'ll be able to collect all three of those items in no time!"')
    time.sleep(3)
    print('Ozzi: "Here, I\'ll mark a few spots where you should have some luck."')
    time.sleep(2)
    print('Ozzi: "Go on, now. I have much to do if I want to prepare that pile of rocks to take you home. Make sure to come back here once you\'re ready to go."')
    time.sleep(3)

    # add learning objective to log
    game_log.add(f'{player} learns how to get home to Earth.')
    
    # ask player where they want to go from the start location
    print()
    print()
    print('>>> It\'s time to find your way home, Space Cadet, where do you want to begin?')
    time.sleep(2)
    print('1: The Crater Vale Asteroid Mines')
    time.sleep(1)
    print('2: Sifter\'s Stack')
    time.sleep(1)
    print("3: Sid's Shuttle 'n Spacecraft Dockin' Deck")
    time.sleep(1)
    inp = int(input().strip())
    try:
        while inp != 1 and inp != 2 and inp != 3:
            print()
            print(">>> Hey! You can't say that! Try Option 1, 2, or 3 next time.")
            inp = int(input().strip())
    except ValueError:
        print()
        print(">>> Hey! You can't say that! Try Option 1, 2, or 3 next time.")
        inp = int(input().strip())
    print()

    # run player-selected location via location function, add first location to game log, and continue game from within the functions defined above the main program
    if inp == 1:
        crater_vale(inventory, has_t, has_f, has_s, player)
        game_log.add(f'{player} decides to go to the Crater Vale Asteroid Mines first.')
    elif inp == 2:
        sifters(inventory, has_t, has_f, has_s, player)
        game_log.add(f'{player} decides to go to Sifter\'s Stack first.')
    elif inp == 3:
        dock_deck(inventory, has_t, has_f, has_s, player)
        game_log.add(f"{player} decides to go to Sid's Shuttle 'n Spacecraft Dockin' Deck first.")

if __name__ == "__main__":
    main()