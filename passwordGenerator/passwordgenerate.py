import numpy as np
import datetime

Capital = 'ABCDEFGIJKLMNOPQRSTUVWXYZ'
small = 'abcdefgijklmnopqrstuvwxyz'
number = '0123456789'
specialCharacters = '!@#$%^&*()'

digit = int(input())
print("digit ", digit)

password = ''

index = 0

# defining probabilities for all the sets
p_Capital = 0
p_small = 0
p_number = 0
p_character = 0


# calculating the currentSum on the basis of current Time
def choice1():
    currentTimeStamp = datetime.datetime.now()
    currentMonth = currentTimeStamp.month
    currentYear = currentTimeStamp.year
    currentDay = currentTimeStamp.day
    currentMinute = currentTimeStamp.minute
    currentHour = currentTimeStamp.hour
    currentSecond = currentTimeStamp.second
    currentMicroSecond = currentTimeStamp.microsecond
    currentSum = currentYear + currentMonth + currentDay + currentHour + currentMinute + currentSecond + currentMicroSecond
    print("currentSum ", currentSum)
    return currentSum


def choiceCapital(currentSum):
    index = currentSum % 26
    print("Capital index ", Capital[index])
    return Capital[index]


def choiceSmall(currentSum):
    index = currentSum % 26
    print("value of index", index)
    print("small index", small[index])
    return small[index]


def choicenumber(currentSum):
    index = currentSum % 10
    print("number index", number[index])
    return number[index]


def choiceCharacters(currentSum):
    index = currentSum % 10
    print("character index", specialCharacters[index])
    return specialCharacters[index]


for index in range(0, digit):
    currentSum = choice1()
    if currentSum % 4 == 0:
        character = choiceCapital(currentSum)
        password = password + character
    elif currentSum % 4 == 1:
        character = choiceSmall(currentSum)
        password = password + character
    elif currentSum % 4 == 2:
        character = choicenumber(currentSum)
        password = password + character
    elif currentSum % 4 == 3:
        character = choiceCharacters(currentSum)
        password = password + character
    else:
        print("Error 404")
        break

print("Generated Password", password)
