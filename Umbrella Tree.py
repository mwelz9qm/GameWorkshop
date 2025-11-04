import time
import random

 

# Create functions for code:
# Type function so its more interactive
def typing(string):
    for char in string:
        print(char, end="")
        time.sleep(0.025)

 

# Function to convert all words in input into their first letters.
def the_rule(guess):
    guess2 = guess.lower().split()
    filtered_list = [word for word in guess2 if len(word) > 2]
    first_letters = [word[0] for word in filtered_list]
    return first_letters

 

# Defined variables
idx = 0
defining_phrase = "umbrellatree"
defining_list = list(defining_phrase)
    
# Introduction
typing("Let's take a trip to the 'Umbrella Tree' shall we? ")
print()
time.sleep(0.5)
typing("Your goal is to find the rule that dictates what you can bring! ")
time.sleep(0.75)

 

# Start of the game code
while idx < 12:
    response = random.randint(1,5)
    suggestion = random.randint(1,3)
    if idx == 0:
        trip = "first"
    elif idx == 1:
        trip = "second"
    elif idx == 2:
        trip = "third"
    elif idx == 3:
        trip = "fourth"
    elif idx == 4:
        trip = "fifth"
    elif idx == 5:
        trip = "sixth"
    else:
        trip = "next"
    print()
    
    if suggestion == 1:
        typing(f"What is the {trip} item you would like to take on this trip to the Umbrella Tree? ")
    elif suggestion == 2:
        typing(f"What do you suppose the {trip} item would be? ")
    else:
        typing(f"Well how about our {trip} trip to the Umbrella Tree, what are you gonna bring? ")
        
    user_input = input()
    the_call = the_rule(user_input)
    
    if defining_list[idx] in the_call:
        
        idx += 1
        if response == 1:
            typing("Yes!! let's take that on this trip! ")
        elif response == 2:
            typing("We can take that on this trip, ")
            time.sleep(0.5)
        elif response == 3:
            typing("You are absolutely right! Lets take that!")
        elif response == 4:
            typing("I suppose we could take that on this trip.")
        else:
            typing("What a fine idea, ")
            time.sleep(0.75)
        time.sleep(0.75)
        
    else:
        example = ""
        number = random.randint(1,6)
        if idx == 0:
            if number == 1:
                example = "a unicorn"
            elif number == 2:
                example = "an Uno card deck"
            elif number == 3:
                example = "an under rated movie"
            elif number == 4:
                example = "an urban worker"
            elif number == 5:
                example = "a uranium Isotope"
            else:
                example = "an undercover cop"
        elif idx == 1:
            if number == 1:
                example = "a music book"
            elif number == 2:
                example = "a millenial"
            elif number == 3:
                example = "a Mac Book Pro"
            elif number == 4:
                example = "a moose"
            elif number == 5:
                example = "a musical chair"
            else:
                example = "minestrone pasta"
        elif idx == 2:
            if number == 1:
                example = "Barnes and Noble"
            elif number == 2:
                example = "a bike"
            elif number == 3:
                example = "a brown bear"
            elif number == 4:
                example = "a bassoon"
            elif number == 5:
                example = "a basketball"
            else:
                example = "a bloated oaf"
        elif idx == 3:
            if number == 1:
                example = "a reptile"
            elif number == 2:
                example = "a red rover"
            elif number == 3:
                example = "a renamed child"
            elif number == 4:
                example = "a roman dictator"
            elif number == 5:
                example = "real pasta"
            else:
                example = "an 'R' rated movie"
        elif idx == 4:
            if number == 1:
                example = "an elephant"
            elif number == 2:
                example = "an eggplant"
            elif number == 3:
                example = "an extravagant doctor"
            elif number == 4:
                example = "an egotistic swine"
            elif number == 5:
                example = "an eel"
            else:
                example = "an egg"
        elif idx == 5:
            if number == 1:
                example = "a llama"
            elif number == 2:
                example = "a list of complaints with this game"
            elif number == 3:
                example = "a limbo bar"
            elif number == 4:
                example = "a lamborghini"
            elif number == 5:
                example = "a limo"
            else:
                example = "last Friday"
        elif idx == 6:
            if number == 1:
                example = "a laxative"
            elif number == 2:
                example = "a lonely bird"
            elif number == 3:
                example = "a loaf of bread"
            elif number == 4:
                example = "a literal reference"
            elif number == 5:
                example = "a lost person"
            else:
                example = "a lobster"
        elif idx == 7:
            if number == 1:
                example = "an apple"
            elif number == 2:
                example = "an after thought"
            elif number == 3:
                example = "an apprentice"
            elif number == 4:
                example = "allowance"
            elif number == 5:
                example = "anchovies"
            else:
                example = "an astroid"
        elif idx == 8:
            if number == 1:
                example = "a triceratops"
            elif number == 2:
                example = "a tree"
            elif number == 3:
                example = "a tall person"
            elif number == 4:
                example = "tense music"
            elif number == 5:
                example = "a talking donkey"
            else:
                example = "a troll"
        elif idx == 9:
            if number == 1:
                example = "a random bloke"
            elif number == 2:
                example = "risky ideas"
            elif number == 3:
                example = "rancid milk"
            elif number == 4:
                example = "a rastafarian"
            elif number == 5:
                example = "risky actions"
            else:
                example = "rolling die"
        elif idx == 10:
            if number == 1:
                example = "an elastic band"
            elif number == 2:
                example = "an evergreen"
            elif number == 3:
                example = "earth"
            elif number == 4:
                example = "an endangered species"
            elif number == 5:
                example = "an equatoral dwelling"
            else:
                example = "an estate"
        elif idx == 11:
            if number == 1:
                example = "an eloped princess"
            elif number == 2:
                example = "the ending of a story"
            elif number == 3:
                example = "an eatery"
            elif number == 4:
                example = "an eventual downfall"
            elif number == 5:
                example = "an emu"
            else:
                example = "an ear lobe"
                
        if response == 1:
            typing("We can not take that on this trip to the Umbrella Tree. ")
            time.sleep(0.5)
            typing(f"Instead, lets take {example} on this trip. ")
        elif response == 2:
            typing("Oh heavens no, we can't bring that. ")
            time.sleep(0.5)
            typing(f"Let's take {example} instead. ")
        elif response == 3:
            typing("Nope, ")
            time.sleep(0.5)
            typing("we can't bring that right now. ")
            time.sleep(0.25)
            typing(f"But we could bring {example}. ")
        elif response == 4:
            typing("We could not bring that on this trip to the Umbrella Tree... ")
            time.sleep(0.5)
            typing(f"How about we bring {example} instead. ")
        else:
            typing("I don't believe we could bring that. ")
            time.sleep(0.75)
            typing(f"But we totally could bring {example}. ")
        idx += 1        
        time.sleep(0.5)        
typing("Now it seems like that is all we can bring on this trip. We can totally take another trip to the Umbrella Tree if you aren't quite sure yet!")