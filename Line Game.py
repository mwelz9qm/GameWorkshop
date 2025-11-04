import random

import time

 

def typing(word):

    for letter in word:

        print(letter, end="", flush = True)

        time.sleep(0.06)

       

count = 0

nonverb = ""

baad = ""

idx = 0

 

vector = list(range(1,11))

random.shuffle(vector)

avector = vector[:10]

 

hope = "Let's play the line game, I'll give you 10 tries. Think you can get it?"

typing(hope)

print()

time.sleep(1)

 

while count < 10:

    guess = ("Give me a good line: ")

    typing(guess)

    upper = input()

    answer = upper.lower()

    confuse = avector[idx]

    time.sleep(1)

   

    nah = random.randint(1,6)

    # confuse = random.randint(1,10)    First attempt

    adj = random.randint(1,5)

   

    if adj == 1:

        nonverb = "tremendous"

    elif adj == 2:

        nonverb = "pretty decent"

    elif adj == 3:

        nonverb = "fantastic"

    elif adj == 4:

        nonverb = "good"

    else:

        nonverb = "rather exceptional"

       

    if adj == 1:

        baad = "horrible"

    elif adj == 2:

        baad = "unpleasant"

    elif adj == 3:

        baad = "bad"

    elif adj == 4:

        baad = "rancid"

    else:

        baad = "rather filthy"

   

    

    if ' to ' in answer:

        if 'okay' in answer:

            count = 11

            typing(f"That is a {nonverb} line, good job!")

            break

        else:

           count = count + 1

           idx = idx + 1

           if count % nah == 0:

               typing(f"Sorry, that is a {baad} line.")

           elif count % nah == 3:

                typing(f"Absolutely {baad} line...")

           elif count % nah == 4:

                typing("There is no hope.")

           else:

                typing(f"No that is a {baad} line.")

        time.sleep(0.75)

       

        if confuse == 1:

            typing(" Okay, ")

            time.sleep(0.5)

            typing(f"A {nonverb} line is from here to there. ")

        elif confuse == 2:

            typing(f" Okay, a {nonverb} line would be China to Japan. ")

            time.sleep(0.5)

            typing(f"But another {baad} line would be from Russia to France.")

        elif confuse == 3:

            typing(" Let me think...")

            time.sleep(1)

            typing(" Okay, got it, ")

            time.sleep(0.5)

            typing(f"from my future to greatness is a {nonverb} line. ")

            time.sleep(0.5)

            typing(f" But a line from my future to misfortune would be another {baad} line.")

        elif confuse == 4:

            typing(f" Another {baad} line would be this code to a trashcan.")

            time.sleep(0.5)

            typing(" Terrible line... ")

            time.sleep(1)

            typing("Okay, but to a sushi bar? Now we're talking! ")

        elif confuse == 5:

            typing(" Let's see... ")

            time.sleep(1)

            typing("Okay, ")

            time.sleep(0.75)

            typing(f"a {nonverb} line would be from Brad Pitt to Leonardo De'Caprio.")

            time.sleep(0.5)

            typing(" Did I pronounce that right? ")

        elif confuse == 6:

            typing(f" Another {baad} line would be a cheeseburger to a healthy individual. ")

            time.sleep(0.75)

            typing(f"Okay, but a cheeseburger to my circuit board? That's a {nonverb} line. ")

        elif confuse == 7:

            typing(" Okay, ")

            time.sleep(0.5)

            typing(f"a {nonverb} line would be from applied mathmatics to a Nigerian Prince...")

            time.sleep(1)

            typing(" Let's sit on that one. ")

        elif confuse == 8:

            typing(f" My left to my right would be another {baad} line. ")

            time.sleep(0.5)

            typing("Okay... ")

            time.sleep(0.75)

            typing(f"but from your left to your right would be a {nonverb} line. ")

        elif confuse == 9:

            typing(f" A work to life balance is also a {baad} line. ")

            time.sleep(0.5)

            typing("Okay... ")

            time.sleep(0.75)

            typing(f"but from work to chasing Benjamins?")

            time.sleep(1)

            typing(f" Now that is a {nonverb} line. ")

        else:

            typing(" Okay,")

            time.sleep(0.5)

            typing(f" a {nonverb} line would be from a can of Mountain Dew to diabetes. ")

            time.sleep(0.25)

            typing(f"Alright, but a line from diabetes to a salad?")

            time.sleep(1)

            typing(" Baaaaaaaad line")

        time.sleep(0.5)

       

    elif 'rule' in answer:

        typing("Wouldn't you like to know Weather Boy? ")

        time.sleep(0.5)

    elif 'what' in answer:

        typing("Wouldn't you like to know Weather Boy? ")

        time.sleep(0.5)

    elif 'no' in answer:

        typing("Don't give me that sas!!")

        time.sleep(0.5)

    else:

        typing("You have to go from one place 'to' another, like 'here' to 'there'.")

    print()