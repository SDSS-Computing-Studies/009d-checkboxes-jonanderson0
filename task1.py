#! python3
""" 
Create a binary converter.
Recall that binary is a system of counting based on powers of 2.
00000001 = 1
00000010 = 2
00001110 = 14

Create a converter that will convert binary to decimal or decimal to
binary using the interface shown in task1.png.  Use the shell that
has been started in task1.py
This is an incomplete program.  You will need to add onto it, 
but you should not change any of the commands that are already 
here

Use assignment_test.py to test your functions
"""


import tkinter as tk 



def binary_to_decimal(binary):
    b = binary [0] + binary[1] + binary[2] + binary [3] + binary[4] + binary[5] + binary[6] + binary[7]
    decimal = int(b,2)
    # binary is a tuple of length 8
    # return value is an integer decimal


    return decimal

def decimal_to_binary(decimal):
    a = bin (decimal)[2:].zfill(8)
    binary = [a[0],a[1],a[2],a[3],a[4],a[5],a[6],a[7]]
    return binary 

    # decimal is an integer value
    # binary is a tuple of length 8 that contains 1's and 0's

    return binary


def get_binary():
    decimal = int(e1.get())
    
    # function should read the entry widget and generate an integer
    # this integer will be used as an input parameter for decimal to binary and the result updated
    # in the 8 checkboxes

    binary = binary_to_decimal(decimal)
    s1.set(binary[0])
    s2.set(binary[1])
    s3.set(binary[2])
    s4.set(binary[3])
    s5.set(binary[4]) 
    s6.set(binary[5])
    s7.set(binary[6])
    s8.set(binary[7])

def get_decimal():
    # function should read the checkboxes and generate a tuple called binary of length 8 that has 1's and 0's
    # this tuple will be used as an input parameter for binary_to_decimal and the result updated
    # in the entry box
    binary = []
    decimal = binary_to_decimal(binary)



win = tk.Tk()



b1 = Button(win, text="Convert to Binary", command=get_binary)
b2 = Button(win, text="Convert to Decimal", command=get_decimal)





win.mainloop()
