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
    while flag:
        for i in password:
            if i == tempArray[tempIndex % byMod]:
                tempIndex = tempIndex + 1
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
    # setting the password field blank for every instance of password generation
    var.set("")
    password = ''
    digit = var1.get()
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
    entry.insert(0, password)


def Reset():
    var.set("")
    var1.set("")


def Copy():
    value = var.get()
    root.clipboard_clear()
    root.clipboard_append(value)


# adding GUI
root = Tk()
var = StringVar()
var1 = IntVar()

# Title of your GUI window
root.title("Random Password Generator")

# create labels
# Label 1
Random_password = Label(root, text='Password')
Random_password.grid(row=0)
entry = Entry(root, textvariable = var)
entry.grid(row=0, column=1)

# label 2
Random_length = Label(root, text='Length')
Random_length.grid(row=1)
entry_length = Entry(root, text=var1)
var1.set("")
entry_length.grid(row=1, column=1)

# make Buttons
# sample button for further use
# generate_button = Button(root, text="Generate", command=main).grid(row=0, column=2)
Button(root, text="Generate", command=main).grid(row=0, column=2)
Button(root, text="Copy", command=Copy).grid(row=0, column=3)
Button(root, text="Reset", command=Reset).grid(row=1, column=2)

root.mainloop()
