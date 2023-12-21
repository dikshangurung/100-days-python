# def repeated(s,n):
#     temp = ""
#     count = 0
#     for i in range(0,n):
#         temp += s
#     for i in range(0,n):
#         if temp[i] == 'a':
#             count = count + 1
#     print(count)
# repeated("aba",100000000)
import math
import os
import random
import re
import sys
# def leader(ranked,player):
#     player_score = []
#     for i in range(0,len(player)):
#         rank =1
#         for j in range(0,len(ranked)):
#             if player[i] < ranked[j] and ranked[j] != ranked[j-1]:
#                 rank = rank + 1
#         player_score.append(rank)
#
#     print(player_score)
#
# a = [100,90,90,80,80,75,60,50]
# b = [70,80,105]
# leader(a,b)

def timeInWords(h,m):
    timeWord = ""
    hourWords = ["Twelve","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve"]
    minuteWords = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven","Twelve",
                   "Thirteen","Fourteen","Fifteen","Sixteen","Seventeen", "Eighteen","Nineteen","twenty","twenty one",
                   "twenty-two","twenty-three",
                   "twenty-four","twenty-five","twenty-six","twenty-seven","twenty eight","twenty nine"]
    if(m == 0):
        timeWord = f"{hourWords[h].lower()} o' clock"
    elif(m == 15):
        timeWord = f"quater past {hourWords[h].lower()}"
    elif(m == 30):
        timeWord = f"half Past {hourWords[h].lower()}"
    elif(m==45):
        timeWord = f"quarter to {hourWords[h+1].lower()}"
    elif (m > 0 and m < 30 and m == 1):
        timeWord = f"{minuteWords[m - 1].lower()} minute past {hourWords[h].lower()}"
    elif(m > 0 and m<30):
        timeWord = f"{minuteWords[m-1].lower()} minutes past {hourWords[h].lower()}"
    elif (m > 0 and m > 30 and m == 59):
        timeWord = f"{minuteWords[60-m-1].lower()} minute to {hourWords[h+1].lower()}"
    elif (m > 0 and m > 30):
        timeWord = f"{minuteWords[60-m-1].lower()} minutes to {hourWords[h+1].lower()}"
    print(timeWord)

timeInWords(3,59)
timeInWords(3,14)
timeInWords(5,15)
timeInWords(6,45)
timeInWords(12,30)

