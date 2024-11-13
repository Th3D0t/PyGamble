import random
from time import sleep
import os

def clear():
    print("\033c")

rand_Ask = ["almost all people quit before hitting it big!", "Bet big, win big!", "Felling lucky?", "Bet you can't match our freak!" "Place your bet.", "Welcome!", "Broke ahh.", "Throw your money at us for a preposterously low chance of getting some of it back!", "What's your lucky number?", "Another round?", "Keep on gambling!"]
att_Msg = {
    1: "Try again!",
    2: "Give me a number.",
    3: "Do you know how to count?",
    4: "Bro, you aint this dumb",
    5: "Aint no fucking way",
    6: "I'll only let you try once more cuz i know you fuckin with me",
    7: "Yeah no I aint doing this shit, fuck you."}

def start_func(max_attempts = 7):
    clear()
    attempt = 1
    while attempt <= 7:
        choice_Intro = random.choice(rand_Ask)
        print(choice_Intro)
        try:
            Bet = int(input("Bet: "))
            if ValueError:
                print("Idk what the fuck you just typed, but it is NOT a valid number, try a whole number bimbo.")
                print(att_Msg[attempt])
                clear()
                start_func(max_attempts = 7)
            attempt += 1
            if attempt in att_Msg > 7: 
                break
        except:
            if Bet > 0 and isinstance(Bet, int) == True:
                clear()
                print("bets placed! Good luck :>")
            else:
                clear()
                attempt += 1
                start_func(max_attempts = 7)
                
start_func()