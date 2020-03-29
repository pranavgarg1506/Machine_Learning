import numpy as np
import datetime

Capital = "ABCDEFGIJKLMNOPQRSTUVWXYZ"
small = 'abcdefgijklmnopqrstuvwxyz'
number = '0123456789'
specialCharacters = '!@#$%^&*()'

digit = int(input())
print("digit ", digit)

password = ''

index = 0


# defining probabilities for all the sets
# p_Capital = 0
# p_small = 0
# p_number = 0
# p_character = 0


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


def checkForDuplicates(currentSum, flag):
    byMod = 0
    if (flag == 0):
        tempArray = Capital
        byMod = len(Capital)
    elif (flag == 1):
        tempArray = small
        byMod = len(small)
    elif (flag == 2):
        tempArray = number
        byMod = len(number)
    elif (flag == 3):
        tempArray = specialCharacters
        byMod = len(specialCharacters)

    tempIndex = currentSum % byMod
    flag = True
    while (flag):
        for i in password:
            if i == tempArray[tempIndex % byMod]:
                tempIndex = tempIndex + 1
                flag = True
                break
        flag = False
    return tempIndex


def choiceCapital(currentSum):
    # index = currentSum % 26
    index = checkForDuplicates(currentSum, 0)
    print("value of index for Capital", index)
    print("Capital index ", Capital[index])
    return Capital[index]


def choiceSmall(currentSum):
    # index = currentSum % 26
    index = checkForDuplicates(currentSum, 1)
    print("value of index for Small", index)
    print("small index", small[index])
    return small[index]


def choicenumber(currentSum):
    # index = currentSum % 10
    index_number = checkForDuplicates(currentSum, 2)
    print("value of index for number", index_number)
    print("number index", number[index_number])
    return number[index_number]


def choiceCharacters(currentSum):
    # index = currentSum % 10
    index_character = checkForDuplicates(currentSum, 3)
    print("value of index for characters", index_character)
    print("character index", specialCharacters[index_character])
    return specialCharacters[index_character]


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
