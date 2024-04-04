#!/bin/bash

# script to keep track of:
# date, number of hours, workout type, boulder, roped, workouts, cardio
# writes to a .txt file in the logs folder

# in ~/.bashrc add
# alias update_workout="(cd Documents/Github/scripts/habit_tracker/; ./workout.sh)"

currentDate=$(date +"%Y-%m-%d")
while true; do
    printf "Did you exercise today (y/n): "
    read answer
    if [[ "$answer" == "n" ]]; then
        echo 'No exercise'
        echo "$currentDate,$hours,$type,$bp,$rc,$workouts,$cardio" >> ../../logs/workout.txt
        break
    elif [[ "$answer" == "y" ]];then
        printf 'How long was the session (minutes): '
        read hours
        printf 'What type of exercise (tuple of climbing/gym/cardio): '
        read type
        if [[ $type =~ "climbing" ]]; then
            printf 'Boulder problems (number, hardest grade): '
            read bp
            printf 'Roped climbs (number, hardest grade): '
            read rc
        fi
        if [[ $type =~ "gym" ]]; then
            printf 'Workouts (workout, reps): '
            read workouts
        fi
        if [[ $type =~ "cardio" ]]; then
            printf 'Cardio (workout, duration): '
            read cardio
        fi
        echo "$currentDate,$hours,$type,$bp,$rc,$workouts,$cardio" >> ../../logs/workout.txt
        echo "Finished recording! "
        break
    else
        printf "Invalid input. \n"
    fi
done
