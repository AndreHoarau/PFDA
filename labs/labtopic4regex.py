# This is the lab for the topic 4 regular expressions
# Author Andre Hoarau
import re
filename = "access.log"
regex = ".*"
with open(filename) as quizfile:
    for line in quizfile:
        searchresult= re.search(regex, line)
        if(searchresult): 
            matchingline=line
            print(matchingline, end= "")

#Answers to the quiz
# A Line 1
# B Line 2,3,5
# C Line 2,3
# D line 2 ,3 ,4 ,6
# E line 2 ,3 ,6
# F Line 2,3,4
# G No lines have a capital after 
# H Line 3
# I line 7
# J Line 8
# K Errorgi
# l Line 10
