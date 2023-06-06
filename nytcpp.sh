#!/bin/bash

########################################################
# OPTIONS MENU - UNINMPORTANT FOR RUNNING CALCULATIONS #
########################################################
# Display Help menu
Help()
{
   echo
   echo "NYTCPP"
   echo
   echo "Usage:"
   echo "$ bash nytcpp"
   echo
   echo "Options:"
   echo
   echo "-m | Method for searching questions. Takes any of {'easy', 'medium', 'hard', 'expert'}"
   echo
   echo "-w | Limits questions to specified weekday. Takes any of {'monday', 'tuesday', etc.}"
   echo
   echo "-d | Specifies difficulty of question. Takes any of {'easy', 'medium', 'hard'}"
   echo
}
# Allowing OPTIONS
while getopts ":m:d:x:" option; do
   case $option in
      h) # display Help
      # Code to execute when -h flag used >>
         Help
         ;;
      m) # choose method
         method="$OPTARG"
         ;;
      d) # Assign weekday
         day="$OPTARG"
         ;;
      x) # Assign difficulty
         difficulty="$OPTARG"
         ;;
   esac
done

########################################################################
# CODE WHICH ACTUALLY WRITES THE .arm FILE - LOOK HERE TO TROUBLESHOOT #
########################################################################
python3 main.py $method $day $difficulty
