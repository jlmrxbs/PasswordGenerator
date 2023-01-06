import tkinter
from tkinter import Tk
from tkinter.ttk import Label, Style
import random


def mainFunc():
    numPasswords = 3
    passwordLengths = []
    for i in range(numPasswords):
        length = 20
        if length < 10:
            length = 12
        passwordLengths.append(length)
    passwort = genPasswort(passwordLengths)
    l1.insert(0, passwort[0])
    l2.insert(0, passwort[1])
    l3.insert(0, passwort[2])
    print(passwort)
    return passwort

def genPasswort(pwLength):
    abc = "abcdefghijklmnupqrstuvwxyz"
    passwoerter =[]
    for i in pwLength:
        password = ""
        for n in range(i):
            nextLetter_Index = random.randrange(len(abc))
            password = password + abc[nextLetter_Index]
        password = replaceWithNumber(password)
        password = replaceUpperCase(password)
        password = replaceWithSign(password)
        passwoerter.append(str(password))
    return passwoerter


def replaceWithNumber(pword):
    for i in range(random.randrange(1, 5)):
        replace_index = random.randrange(len(pword))
        pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index+1:]
        return pword


def replaceUpperCase(pw):
    for i in range(random.randrange(1, 9)):
        replace_index = random.randrange(len(pw))
        pw = pw[0:replace_index] + pw[replace_index].upper() + pw[replace_index+1:]
        return pw

def replaceWithSign(passw):
    signs="!()/&%$§?_-#*"
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(passw))
        pw = passw[0:replace_index] + str(signs[random.randrange(1, int(len(signs)))]) + passw[replace_index+1:]
        return pw


root = Tk()
root.title("Password Generator")
root.geometry("300x100")

btn = tkinter.Button(root, width=10, height=1, bg="green", text="Submit", command=mainFunc)
btn.pack()

l1 = tkinter.Entry(root, width=30)
l1.pack()
l2 = tkinter.Entry(root, width=30)
l2.pack()
l3 = tkinter.Entry(root, width=30)
l3.pack()


root.mainloop()
