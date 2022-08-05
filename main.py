import webbrowser
import random
import time
from datetime import datetime
import subprocess

def browser():
    while True:
        list = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ", "https://www.youtube.com/watch?v=UE5AHE2Ypr8","https://www.youtube.com/watch?v=GOvEAHakjVQ"]
        rhino = ["There are 5 species of rhino in the world.","Rhinos can weigh over 3 tonnes.","Rhinos have poor vision."]
        print("Hello welcome to the PyOS browser! What would you like to do?")
        print("1: Watch a video")
        print("2: Rhino facts")
        print("3: News")
        print("4: Exit")
        a = input()
        if a == "1":
            webbrowser.open(random.choice(list))
        if a == "2":
            print("Did you know? " + random.choice(rhino))
            time.sleep(2)
        if a == "3":
            webbrowser.open('https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en')
        if a == "4":
            break



time.sleep(0.5)

print("Booting up...")

time.sleep(1)

print("PyOS version 1.0")
print("Developed by ADev")

time.sleep(1)

print("Welcome to PyOS!")

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
time.sleep(1)

print("The current time in your area is " + current_time)
time.sleep(1)
while True:
    print("What would you like to do?")
    print("1: Internet")
    print("2: Game")
    print("3: Type")
    print("4. Exit")
    activity = input()
    if activity == "1":
        browser()
    if activity == "2":
        webbrowser.open('https://www.linerider.com/')
    if activity == "3":
        subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
    if activity == "4":
        break


