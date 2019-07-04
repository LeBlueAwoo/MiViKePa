ver=("Ver. 1.1.0") # <- The version number

#External scripts used by the program and its subprograms are loaded here
try:
    module=("time")
    import time
    module=("sys")
    import sys
    module=("traceback")
    import traceback
    module=("os")
    import os
    module=("tkinter")
    import tkinter
    module=("tkinter as an internal asset")
    from tkinter import *
except:
    print("[FATAL] Failed to load module:", module)
    while True:
        input("Please close this window.")

print("Virtual Mini Keypad\nBy Max Nicholson\n\n##############################################\n\n")
time.sleep(1)
os.system("cls")

#Variables and functions are defined here
code_file="null"
open(r"var.txt","w").close
num=("")

def NumAppend1():
    code_file=open(r"var.txt","a+")
    code_file.write("1")
    print("1")
    code_file.close()

def NumAppend2():
    code_file=open(r"var.txt","a+")
    code_file.write("2")
    print("2")
    code_file.close()

def NumAppend3():
    code_file=open(r"var.txt","a+")
    code_file.write("3")
    print("3")
    code_file.close()

def NumAppend4():
    code_file=open(r"var.txt","a+")
    code_file.write("4")
    print("4")
    code_file.close()

def NumAppend5():
    code_file=open(r"var.txt","a+")
    code_file.write("5")
    print("5")
    code_file.close()

def NumAppend6():
    code_file=open(r"var.txt","a+")
    code_file.write("6")
    print("6")
    code_file.close()

def NumAppend7():
    code_file=open(r"var.txt","a+")
    code_file.write("7")
    print("7")
    code_file.close()

def NumAppend8():
    code_file=open(r"var.txt","a+")
    code_file.write("8")
    print("8")
    code_file.close()

def NumAppend9():
    code_file=open(r"var.txt","a+")
    code_file.write("9")
    print("9")
    code_file.close()

def NumAppend0():
    code_file=open(r"var.txt","a+")
    code_file.write("0")
    print("0")
    code_file.close()

def fCancel():
    os.system("cls")
    open(r"var.txt","w").close

def fEnter():
    code=open(r"code.txt", "r")
    var=open(r"var.txt","r")
    codeContents=code.read()
    varContents=var.read()
    os.system("cls")
    print(varContents)
    if varContents == codeContents:
        print("\nACCESS GRANTED!")
        os.system("color 20")
        time.sleep(0.2)
        os.system("color 02")
        time.sleep(0.2)
        os.system("color 20")
        time.sleep(0.2)
        os.system("color 07")
        time.sleep(0.2)
    else:
        print("\nACCESS DENIED!\nTry again!")
        os.system("color 40")
        time.sleep(0.2)
        os.system("color 04")
        time.sleep(0.2)
        os.system("color 40")
        time.sleep(0.2)
        os.system("color 07")
        time.sleep(0.2)
    var.close()
    code.close()

try:
    #Draw the main menu GUI
    Top=tkinter.Tk()
    title=("Virtual Mini KeyPad")
    Top.title(title)
    C=tkinter.Canvas(Top, bd=1, bg="black", width=700, height=90)
    C.pack()
    C.create_text(330,30,fill="green",font="consolas 25 bold",text="Please enter the 10 digit code:")
    label = Label(Top, text= ver)

    # create the main sections of the layout, 
    # and lay them out
    top = tkinter.Frame(Top)
    bottom = tkinter.Frame(Top)
    top.pack(side="top")
    bottom.pack(expand=True)

    #Make the buttons... (The above programs are only run when these buttons are pressed)
    bA=tkinter.Button(top, text="1", command=NumAppend1,width=5, height=2 )
    bB=tkinter.Button(top, text="2", command=NumAppend2,width=5, height=2 )
    bC=tkinter.Button(top, text="3", command=NumAppend3,width=5, height=2 )
    bD=tkinter.Button(top, text="4", command=NumAppend4,width=5, height=2 )
    bE=tkinter.Button(top, text="5", command=NumAppend5,width=5, height=2 )
    bF=tkinter.Button(top, text="6", command=NumAppend6,width=5, height=2 )
    bG=tkinter.Button(top, text="7", command=NumAppend7,width=5, height=2 )
    bH=tkinter.Button(top, text="8", command=NumAppend8,width=5, height=2 )
    bI=tkinter.Button(top, text="9", command=NumAppend9,width=5, height=2 )
    bJ=tkinter.Button(top, text="0", command=NumAppend0,width=5, height=2 )
    bK=tkinter.Button(top, text="CLEAR", command=fCancel,width=10, height=2 )
    bL=tkinter.Button(top, text="ENTER", command=fEnter,width=10, height=2 )

    #...and place them all at the bottom of the window
    label.pack(side=("left")) 
    bA.pack(in_=top, side="left")
    bB.pack(in_=top, side="left")
    bC.pack(in_=top, side="left")
    bD.pack(in_=top, side="left")
    bE.pack(in_=top, side="left")
    bF.pack(in_=top, side="left")
    bG.pack(in_=top, side="left") 
    bH.pack(in_=top, side="left")
    bI.pack(in_=top, side="left")
    bJ.pack(in_=top, side="left")
    bK.pack(in_=top, side="left")
    bL.pack(in_=top, side="left")
    top.mainloop()
    
except:
    print("[FATAL] Failed to start the graphical interface!")
    print("        Here's what failed:\n")
    traceback.print_exc()
    input("        Press ENTER to quit...")
