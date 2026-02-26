#!/usr/bin/python3

def personalized_greeting(name, quest):
    print(f"Greetings {name}! May your quest for {quest} be successful! Failure is not an option")

user_name = input("What is your name? ")
user_quest = input("What is your quest? ")
personalized_greeting(user_name, user_quest)
