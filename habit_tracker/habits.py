#!/usr/bin/env python3

# simple python script to track habits with two functions
# record habits: writes to a .txt file in the logs folder
# visualise using unicode bars

# in ~/.bashrc add
# alias update_workout="(cd Documents/Github/scripts/habit_tracker/; ./workout.sh)"

from datetime import date
from collections import defaultdict

def string_align(s,n=15):
    return " "*(n-len(s)) + s + " "

todo_today = input("What do you want to do today (record/visualise): ")
if todo_today == "record":
    meditate = input("Did you meditate (0/1): ")
    workout = input("Did you workout or stretch (0/1): ")
    drink = input("Did you drink (0/1): ")
    sleeping = input("Did you sleep (0/1): ")
    readbooks = input("Did you read (0/1): ") 
    machinelearning = input("Did you do any machine learning (0/1): ")
    coding = input("Did you code (0/1): ")
    outdoor = input("Did you do anything outdoor (activity or knowledge) (0/1): ")

    to_write = str(date.today()) + ',' +meditate + workout + drink + sleeping + readbooks + machinelearning + coding + outdoor + "\n"

    f = open("../../logs/habits.txt","a+")
    f.write(to_write)
    f.close()

    print("All done!")
elif todo_today == "visualise":
    days = input("last # days: ")
    days = int(days)
    f = open("../../logs/habits.txt","r").readlines()
    
    habits = ['Meditate','Workout/stretch','Drink','Sleep','Read','ML','Code','Outdoor']
    d = defaultdict(str)
    daily_percentage = ""
    num = 0
    for line in f[-days:]:
        for i in range(8):
            num += int(line[11 + i])
            if int(line[11+i]) == 0:
                d[habits[i]] += " "
            else:
                d[habits[i]] += chr(8211)
        if num == '0':
            daily_percentage += " "
        else:
            daily_percentage += chr(9600+num)
    print(string_align("Daily progress") + daily_percentage)
    print("")
    for habit in habits:
        print(string_align(habit) + d[habit])
    print("")
    print("Today's score: ", (sum([int(x) for x in line[11:19]])/8)*100)
    
else:
    print('Invalid input')
