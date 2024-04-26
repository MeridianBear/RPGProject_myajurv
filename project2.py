'''
Author:         MUDRA YAJURVEDI
Date:           4/25/24
Assignment:     PROJECT 2
Course:         CPSC1050
Lab Section:    001

CODE DESCRIPTION: A text-based RPG, see README for more information

At least one working link to GitHub, I hope:
https://github.com/MeridianBear/RPGProject_myajurv
https://github.com/MeridianBear/RPGProject_myajurv.git
'''
# import time functions
import time

''' functions '''
# check if player has all 3 portal items
def check(inventory):
    # initialize checked count and all_3 bool
    checked = 0
    all_3 = False
    # if player has all 3 needed portal items, return True
    for item in inventory:
        checked += 1
    if checked == 3:
        all_3 = True
    return all_3
        
# The Portal Hub
def portal_hub(inventory, timep, fuel, space, player, game_log):
    # check if player can end game,
    x = check(inventory)
    # if they can, begin end game procedures
    if x == True:
        return_home(note, timep, fuel, space, player)
    
    # otherwise, run the items for this section
    print()
    print('Ozzi: "You\'re back already? Do you have all of the parts I need yet?"')
    time.sleep(2)
    print(f'{player}: "Not yet, what am I missing?"')
    time.sleep(1)
    if timep not in inventory:
        print('Ozzi: "You\'re missing a Timepiece. Try looking for it in Sifter\'s Stack."')
        time.sleep(2)
    if fuel not in inventory:
        print('Ozzi: "You\'re missing a Fuel Crystal. Try looking for it in the Crater Vale Asteroid Mines."')
        time.sleep(2)
    if space not in inventory:
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
        crater_vale(inventory, timep, fuel, space, player, game_log)
    elif inp == 2:
        sifters(inventory, timep, fuel, space, player, game_log)
    elif inp == 3:
        dock_deck(inventory, timep, fuel, space, player, game_log)

# The Portal Hub, ending
def return_home(note, timep, fuel, space, player, game_log):
    # add collecting all three items to log
    game_log.add(f"{player} obtained all 3 portal items, and went back to the Portal Hub to see Ozzi.")
    print('Ozzi: "You\'re back? Do you have all 3 items already?"')
    time.sleep(2)
    print(f'{player}: "Yup! I have all three of the items you asked for."')
    time.sleep(2)
    print('Ozzi takes the items from you and begins to work. You watch as Ozzi uses tools you have never seen before to miraculously put together rubble and the items you\'ve brought.')
    time.sleep(4)
    print('Ozzi: "It\'s all good to go now."')
    time.sleep(2)
    print('Ozzi: "Ah, before you go, I\'ve written you a note. Read it once you get home."')
    time.sleep(2)
    print('Ozzi hands you a folded-over, hand-written note, lovingly signed in a language that you can\'t read.')
    time.sleep(3)
    print('This marks you as a bit strange, but you are not one to question local customs.')
    time.sleep(2)
    # get note from Ozzi
    game_log.add(f"You recieve a handwritten {note.get_name}: {note.get_description}")
    inventory.append(note)

    print(f'Ozzi: "Step in whenever you\'re ready, {player}. Try *not* to conk your head during the landing this time."')
    time.sleep(3)
    print('You step through the portal, note in hand, waving goodbye to Ozzi.')
    time.sleep(2)
    print(f'{player}: "Bye, Zeron."')
    time.sleep(2)
    print('You see a flash of light, before being hit with the smell of dinner. You\'ve finally returned home.')
    time.sleep(2)
    
    # put log into new file
    f = open("adventurer_log.txt", "w")
    f.write(game_log.have_log())
    f.close()

# The Crater Vale Asteroid Mines
def crater_vale(inventory, timep, fuel, space, player, game_log):
    if fuel not in inventory:
        '''
        # exposition for this area if you have not obtained fuel crystal
        print('You walk into a bustling mining town, with all sorts of lifts and machinery moving around, and see Zeronians that look like buff Ozzis, each with fur of a different hue.')
        time.sleep(4)
        print('As you think to yourself that this must be where Ozzi is from, you hear a gruff snort come from right behind you.')
        time.sleep(3)
        print('You turn around and face a blue Zeronian that is about twice your height, and with muscles large enough to scare a boulder into spliting in half.')
        time.sleep(3)
        print('He leans down to make eye contact before speaking.')
        time.sleep(2)
        print('???: "How good are you at... arithmetic?"')
        time.sleep(2)
        print(f'{player}: "Huh? I mean... I\'m alright at it."')
        time.sleep(2)
        print('???: "Ah, I\'m sorry, I was getting ahead of myself. My name is Gerack, and I do not know arithmetic."')
        time.sleep(2)

        # add meeting Gerack to log before continuing dialogue
        game_log.add(f"{player} met Gerack in the Crater Vale Asteroid Mines.")

        print('Gerack: "However, my sweet little girl, Mais, is struggling with her homework. I\'m looking for someone who can help me understand what she is learning."')
        time.sleep(3)
        print('Gerack pauses before sputtering out another sentence.')
        time.sleep(3)
        print('Gerack: "O-Of course, I can compensate you for it, if needed."')
        time.sleep(3)
        print('Despite his somewhat scary appearance, he seems rather sweet. So you explain your situation to him, and ask if he would be able to procure an item for you.')
        time.sleep(3)
        print('Gerack: "Oh, you need a fuel crystal? Hmm... We should have a few left from our last expedition. I believe that one should be enough for a portal to Earth."')
        time.sleep(3)
        print(f'{player}: "Sounds good! Do you have any example problems we can work through?"')
        time.sleep(3)
        print('He pulls out a stack of about 30 sheets from the bag slung on his shoulder.')
        time.sleep(2)
        print('Gerack: "I believe this is more than enough?"')
        time.sleep(2)
        print('You two go to a nearby picnic table and take a seat.')
        time.sleep(2)
        print('You begin explaining how to add and subtract by counting on your fingers, and his eyes light up as he begins to make progress.')
        time.sleep(3)

        # user answers basic arithmetic questions, and the input is validated
        print()
        print('>>> Answer the following questions correctly to help Gerack understand the material, and you will obtain a Fuel Crystal from him.')
        time.sleep(2)
        print()
        print('What is 36 + 41?')
        answer = int(input().strip())
        while answer != 77:
            print()
            print('That doesn\'t seem quite right. Try again.')
            time.sleep(1)
            print('What is 36 + 41?')
            answer = int(input().strip())

        print()
        print('What is 97 - 52?')
        answer = int(input().strip())
        while answer != 45:
            print()
            print('That doesn\'t seem quite right. Try again.')
            time.sleep(1)
            print('What is 97 - 52?')
            answer = int(input().strip())

        print()
        print('What is 12 x 9?')
        answer = int(input().strip())
        while answer != 108:
            print()
            print('That doesn\'t seem quite right. Try again.')
            time.sleep(1)
            print('What is 12 x 9?')
            answer = int(input().strip())

        print()
        print('What is 100 / 5?')
        answer = int(input().strip())
        while answer != 20:
            print()
            print('That doesn\'t seem quite right. Try again.')
            time.sleep(1)
            print('What is 100 / 5?')
            answer = int(input().strip())

        print()
        print('What is 2 + 2?')
        answer = int(input().strip())
        while answer != 4:
            print()
            print('That doesn\'t seem quite right. Try again.')
            time.sleep(1)
            print('What is 2 + 2?')
            answer = int(input().strip())
        
        # once the math is done, you talk to Gerack and obtain a fuel crystal
        print()
        print('After working through many, many problems, it seems that he finally has a grasp on how to complete them.')
        time.sleep(3)
        print('Gerack: "I think I understand how to solve it now... Once my daughter returns from school, I\'ll be able to help her with her homework."')
        time.sleep(3)
        print('You see Gerack get a little misty-eyed at the thought, and politely avert your eyes.')
        time.sleep(2)
        print('He shakes off his thoughts and goes to a nearby minecart. He picks up what looks to be a stone from it and returns to you.')
        time.sleep(3)
        print('Gerack: "As promised for your help, here is a Fuel Crystal."')
        time.sleep(2)
        # fuel crystal is added to your inventory
        print('>>> Gerack hands you a large, obsidian-like stone, and you place it in your bag.')
        '''
        fuel.pick_up(inventory)
        
        # add helping Gerack and obtaining a fuel crystal to log
        game_log.add(f"{player} helped Gerack learn arithmetic for his daughter.")
        game_log.add(f"{player} obtained a {fuel.get_name}: {fuel.get_description}")

        time.sleep(2)
        print('Gerack: "Thank you for your help, Adventurer."')
        time.sleep(2)
        print(f'{player}: "Of course, thank you for the fuel crystal, Gerack."')
        time.sleep(2)
        print('You bid each other goodbye, and you head to your next destination.')
        time.sleep(2)

    # if player has already received a fuel crystal from Gerack,
    else:
    # find somewhere else to go
        print('You see Gerack guiding his daughter, Mais, through a math problem, and smile to yourself.')
        time.sleep(2)
        print('There isn\'t much else for you to do here, so you decide to head somewhere else.')
        time.sleep(2)
        # add revisiting Gerack to log
        game_log.add(f"{player} went back to the Crater Vale Asteroid Mines and saw Gerack helping his daughter with homework.")

    # check if player can end game
    x = check(inventory)
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
        portal_hub(inventory, timep, fuel, space, player, game_log)
    elif inp == 2:
        sifters(inventory, timep, fuel, space, player, game_log)
    elif inp == 3:
        dock_deck(inventory, timep, fuel, space, player, game_log)

# Sifter's Stack
def sifters(inventory, timep, fuel, space, player, game_log):
    if time not in inventory:
    # exposition for this area if you have not obtained timepiece
        print('')
        time.sleep(2)

        # add meeting Ani to log before continuing dialogue
        game_log.add(f"{player} met Ani in Sifter's Stack.")

        print('')
        time.sleep(2)

        # user answers basic questions from a letter for Ani to obtain a Timepiece
        print()
        print('text from a letter')
        print()
        print('>>> Answer the following questions correctly to help Ani understand the text, and you will obtain a Timepiece from her.')
        time.sleep(2)
        print()
        print('Question')
        print('1: Answer choice')
        print('2: Answer choice')
        print('3: Answer choice')
        print('4: Answer choice')
        answer = int(input().strip())
        while answer != 1:
            print()
            print('That doesn\'t seem quite right. Try again.')
            time.sleep(1)
            print('Question')
            answer = int(input().strip())
        
        print()
        print('Question')
        print('1: Answer choice')
        print('2: Answer choice')
        print('3: Answer choice')
        print('4: Answer choice')
        answer = int(input().strip())
        while answer != 1:
            print()
            print('That doesn\'t seem quite right. Try again.')
            time.sleep(1)
            print('Question')
            answer = int(input().strip())

        print()
        print('Question')
        print('1: Answer choice')
        print('2: Answer choice')
        print('3: Answer choice')
        print('4: Answer choice')
        answer = int(input().strip())
        while answer != 1:
            print()
            print('That doesn\'t seem quite right. Try again.')
            time.sleep(1)
            print('Question')
            answer = int(input().strip())

        print()
        print('Question')
        print('1: Answer choice')
        print('2: Answer choice')
        print('3: Answer choice')
        print('4: Answer choice')
        answer = int(input().strip())
        while answer != 1:
            print()
            print('That doesn\'t seem quite right. Try again.')
            time.sleep(1)
            print('Question')
            answer = int(input().strip())

        print()
        print('Question')
        print('1: Answer choice')
        print('2: Answer choice')
        print('3: Answer choice')
        print('4: Answer choice')
        answer = int(input().strip())
        while answer != 1:
            print()
            print('That doesn\'t seem quite right. Try again.')
            time.sleep(1)
            print('Question')
            answer = int(input().strip())

        
        # once the reading is done, you talk to Ani and obtain a timepiece
        print()
        print('')
        time.sleep(2)
        # timepiece is added to your inventory
        print('>>> Ani carefully places a glowing, translucent hourglass into your bag.')
        timep.pick_up(inventory)

        # add helping Gerack and obtaining a fuel crystal to log
        game_log.add(f"{player} helped Ani read a letter from her friend.")
        game_log.add(f"{player} obtained a {timep.get_name}: {timep.get_description}")

        time.sleep(2)
        print('')
        time.sleep(2)

    # if player has already received a fuel crystal from Gerack,
    else:
    # find somewhere else to go
        print('You see Ani happily rereading the letter out loud, by herself this time.')
        time.sleep(2)
        print('There isn\'t much else for you to do here, so you decide to head somewhere else.')
        time.sleep(2)
        # add revisiting Gerack to log
        game_log.add(f"{player} went back to Sifter's Stack and saw Ani reading her letter again.")

    # check if player can end game
    x = check(inventory)
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
        crater_vale(inventory, timep, fuel, space, player, game_log)
    elif inp == 2:
        portal_hub(inventory, timep, fuel, space, player, game_log)
    elif inp == 3:
        dock_deck(inventory, timep, fuel, space, player, game_log)

# Sid's Shuttle 'n Spacecraft Dockin' Deck
def dock_deck(inventory, timep, fuel, space, player, game_log):
    if space not in inventory:
    # exposition for this area if you have not obtained space skipper
        print('You walk into a large, sleek, white interior with windows larger than some houses. You pause to take in the sheer magnitude of the space and the strangely calming effect it has.')
        time.sleep(4)
        print('All of a sudden, you hear the whoosh of different vehicles and spacecraft rushing in and out of the deck, and you rush to clutch your bag so as to prevent it from flying off of you.')
        time.sleep(4)
        print('???: "First time?"')
        time.sleep(2)
        print('You turn towards the voice to come face to face with a woman dressed in a circuit-covered jumpsuit and covered in tool-filled tool belts.')
        time.sleep(3)
        print('Her hair must\'ve been put up neatly at some point, but it seems the gusts from the spacecraft and shuttles have made it go wayward since she put it up.')
        time.sleep(4)
        print('She laughs heartily and goes to pull a wrench from the belt slung around her waist before pointing it at you.')
        time.sleep(2)
        print('???: "It never gets old, watching newcomers get shocked by the \'crafts."')
        time.sleep(2)
        print('???: "The name\'s Sid, it\'d do ya good to remember that while you\'re here, seein\' as I run this place."')

        # add meeting Sid to log
        game_log.add(f"{player} met Sid in Sid's Shuttle 'n Spacecraft Dockin' Dec.")

        # Player talks to Sid and obtains space skipper
        time.sleep(3)
        print(f'{player}: "I\'ll be sure to keep it in mind, Sid. My name is {player}."')
        time.sleep(2)
        print(f'Sid: "{player}, y\'say? What an Earth-y name! Y\'must also be from Earth."')
        time.sleep(2)
        print('Sid: "Are y\'here on business or what? We don\'t get a lotta Earthlin\'s here if ya haven\'t noticed."')
        time.sleep(3)
        print(f'{player}: "I kind of flew in through a portal somehow, and I am trying to head back home. Unfortunately, the portal needs to be fixed, so I\'m collecting parts for it."')
        time.sleep(4)
        print('Sid: "Oh, why didn\'t ya say so? I happen to have a few Space Skippers in the \'shop somewhere if ya need one!"')
        time.sleep(3)
        print(f'{player}: "I don\'t think I have one of those yet. If you could spare one, I\'d be really grateful!"')
        time.sleep(3)
        print('Sid: "Say less, dear! I\'ll getcha one, just wait here a moment, yeah?"')
        time.sleep(2)
        print('Sid scampers off in about 5 different directions before settling on the first one, and sprints out of your view.')
        time.sleep(3)
        print('Within moments, you hear clunking noises as she comes back into view, metallic cylinder in hand.')
        time.sleep(2)
        print('Sid: "Heads up!"')
        time.sleep(2)

        # space skipper is added to your inventory
        print('>>> Sid haphazardly tosses a cylidrical object at you. You manage to catch it before tucking it away in your bag.')
        space.pick_up(inventory)

        # add talking to Sid and obtaining a space skipper to log
        game_log.add(f"{player} managed to survive a conversation with Sid.")
        game_log.add(f"{player} obtained a {space.get_name}: {space.get_description}")

        # wish Sid farewell
        time.sleep(2)
        print('Sid: "Come back \'ere if that one doesn\'t work ya, otherwise I hope ya get home safe!"')
        time.sleep(2)
        print('You give Sid your thanks just before she shoos you off in the direction of the exit.')
        time.sleep(2)

    # if player has already received a space skipper from Sid,
    else:
    # find somewhere else to go
        print('Sid waves at you before going back to fixing something on a smoking shuttle.')
        time.sleep(2)
        print('There isn\'t much else for you to do here, so you decide to head somewhere else.')
        time.sleep(2)
        # add revisiting Gerack to log
        game_log.add(f"{player} went back to Sid's Shuttle 'n Spacecraft Dockin' Deck and saw Sid fixing a part of a shuttle.")

    # check if player can end game
    x = check(inventory)
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
        crater_vale(inventory, timep, fuel, space, player, game_log)
    elif inp == 2:
        sifters(inventory, timep, fuel, space, player, game_log)
    elif inp == 3:
        portal_hub(inventory, timep, fuel, space, player, game_log)

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

    def get_name(self):
        super().get_name

    def get_description(self):
        super().get_description

    def pick_up(self, inventory):
        super().pick_up(inventory)

# output_log
class output_log:
    def create_log(self, log):
        self.log = log
    
    def add(self, text):
        self.log.append(text)

    def have_log(self):
        return self.log

# define main program
def main():
    # initialize game variables
    inventory = []
    log = []
    game_log = output_log()
    game_log.create_log(log)

    # initialize game object
    note = objects('Note from Ozzi', "A note that Ozzi handwrote to remind you that you will always be welcomed if you ever return to Zeron.")
    timep = portal_object('Timepiece',"An old-fashioned, hourglass-type timepiece. The sand within it glows a golden hue within the gaudy, crystal frame. It seems to glitch in and out of existence, perhaps this odd object might help you get home.")
    space = portal_object('Space Skipper', "It's pretty obvious that this was named by someone who thinks the concept of teleportation is lame.")
    fuel = portal_object('Fuel Crystal', "A pretty drab looking stone that was just mined out of the ground, and a major source of energy on Zeron. The miners in Crater Vale hold a lot of pride for these dark rocks, so maybe that's why they're called 'fuel crystals' and not 'fuel rocks.'")
    
    # pre-game: obtain and confirm player username
    # ask player for username and take input

    print()
    print()
    print('Welcome Space Cadet!')

    # all instances of time.sleep(seconds to pause) in this program are used to make the terminal experience better for the player
    time.sleep(1)
    print('What is your name? Please keep in mind that this will be stored in your Adventurer\'s Log and will be how you are referred to throughout the game.')
    player = input().strip()
    print()
    '''
    # confirm with player using player feedback and user validation
    print(f'Are you certain that "{player}" is the name you would like to go by? ("Yes" or "No")')
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
    game_log.add(f'{player} met Ozzi and discovered that they have mistakenly arrived on the planet Zeron.')

    # continue text
    print(f'{player}: "So, I\'m on Zeron and your name is Ozzi?"')
    time.sleep(2)
    print('Ozzi: "Correct."')
    time.sleep(2)
    print(f'{player}: "How do I get home, then?"')
    time.sleep(2)
    print('Ozzi: "Well, a portal would probably be the easiest and fastest way home."')
    time.sleep(2)
    print('Ozzi: "Unless you\'d like to be cryogenically frozen for about 1,764 years... but no one really does that anymore."')
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
        game_log.add(f'{player} talked to Ozzi and learned that human are *not* the center of the universe.')

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
    game_log.add(f'{player} learned how to get home to Earth.')
    
    # ask player where they want to go from the start location
    print()
    print()
    '''
    print('>>> It\'s time to find your way home, Space Cadet, where do you want to begin?')
    time.sleep(1)
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
        crater_vale(inventory, timep, fuel, space, player, game_log)
        game_log.add(f'{player} decided to go to the Crater Vale Asteroid Mines first.')
    elif inp == 2:
        sifters(inventory, timep, fuel, space, player, game_log)
        game_log.add(f'{player} decided to go to Sifter\'s Stack first.')
    elif inp == 3:
        dock_deck(inventory, timep, fuel, space, player, game_log)
        game_log.add(f"{player} decided to go to Sid's Shuttle 'n Spacecraft Dockin' Deck first.")

if __name__ == "__main__":
    main()