import numpy as np
import datetime
from tkinter import *
from tkinter.ttk import *
import pyperclip

Capital = "ABCDEFGIJKLMNOPQRSTUVWXYZ"
small = 'abcdefgijklmnopqrstuvwxyz'
number = '0123456789'
specialCharacters = '!@#$%^&*()'


# digit = int(input())
# print("digit ", digit)

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


def checkForDuplicates(currentSum, flag, password):
    byMod = 0
    if flag == 0:
        tempArray = Capital
        byMod = len(Capital)
    elif flag == 1:
        tempArray = small
        byMod = len(small)
    elif flag == 2:
        tempArray = number
        byMod = len(number)
    elif flag == 3:
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


def choiceCapital(currentSum, password):
    # index = currentSum % 26
    index = checkForDuplicates(currentSum, 0, password)
    print("value of index for Capital", index)
    print("Capital index ", Capital[index])
    return Capital[index]


def choiceSmall(currentSum, password):
    # index = currentSum % 26
    index = checkForDuplicates(currentSum, 1, password)
    print("value of index for Small", index)
    print("small index", small[index])
    return small[index]


def choiceNumber(currentSum, password):
    # index = currentSum % 10
    index_number = checkForDuplicates(currentSum, 2, password)
    print("value of index for number", index_number)
    print("number index", number[index_number])
    return number[index_number]


def choiceCharacters(currentSum, password):
    # index = currentSum % 10
    index_character = checkForDuplicates(currentSum, 3, password)
    print("value of index for characters", index_character)
    print("character index", specialCharacters[index_character])
    return specialCharacters[index_character]


def main():
    password = ''
    digit = var.get()
    for index in range(0, digit):
        currentSum = choice1()
        if currentSum % 4 == 0:
            character = choiceCapital(currentSum, password)
            password = password + character
        elif currentSum % 4 == 1:
            character = choiceSmall(currentSum, password)
            password = password + character
        elif currentSum % 4 == 2:
            character = choiceNumber(currentSum, password)
            password = password + character
        elif currentSum % 4 == 3:
            character = choiceCharacters(currentSum, password)
            password = password + character
        else:
            print("Error 404")
            break
    print("Generated Password", password)
    entry.insert(10, password)


# adding GUI
root = Tk()
var = IntVar()
var1 = IntVar()

# Title of your GUI window
root.title("Random Password Generator")

# create labels
Random_password = Label(root, text='Password')
Random_password.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)

Random_length = Label(root, text='Length')
Random_length.grid(row=1)
# entry_length = Entry(root,textvariable = var)
# entry_length.grid(row=0, column=1)

# make Generate Button
generate_button = Button(root, text="Generate", command=main)
generate_button.grid(row=0, column=2)

combo = Combobox(root, textvariable=var)

# Combo Box for length of your password
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                   17, 18, 19, 20, 21, 22, 23, 24, 25,
                   26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)

root.mainloop()
