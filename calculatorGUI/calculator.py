import tkinter
from tkinter import *
root = Tk()
root.title("Calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)

root.config(bg="#17161b")
root.iconbitmap("./calc_icon.ico")
label = Label(root, text="", width=25, height=2, font=("arial", 30))
label.pack()

input_eq = ""
output_eq = ""

flag = False


def display(val):
    global input_eq
    global flag
    if flag == True:
        input_eq = ""
        flag = False
    if val=='x':
        val='*'
    input_eq += val
    label.config(text=input_eq)


def clear():
    global input_eq
    input_eq = ""
    label.config(text=input_eq)


def calculate():
    global input_eq
    global output_eq
    global flag
    if input_eq != "":
        try:
            output_eq = eval(input_eq)
        except:
            output_eq = "Please enter valid expression"
            input_eq = ""
    flag = True
    label.config(text=output_eq)


btnc = Button(root, text="C", width=5, height=1, bd=1, font=(
    "arial", 30, "bold"), bg="#3697f5", fg="#fff", command=lambda: clear())
btnc.place(x=10, y=100)

btn_div = Button(root, text="/", width=5, height=1, font=("arial", 30,
                 "bold"), bd=1, bg="#2a2d36", fg="#fff", command=lambda: display("/"))
btn_div.place(x=150, y=100)

btn_mod = Button(root, text="%", width=5, height=1, font=(
    "arial", 30, "bold"), bd=1, bg="#2a2d36", fg="#fff", command=lambda: display("%"))
btn_mod.place(x=290, y=100)

btn_mul = Button(root, text="x", width=5, height=1, font=(
    "arial", 30, "bold"), bd=1, bg="#2a2d36", fg="#fff", command=lambda: display("x"))
btn_mul.place(x=430, y=100)

btn_seven = Button(root, text="7", bg="#2a2d36", fg="#fff", bd=1, width=5,
                   height=1, font=("arial", 30, "bold"), command=lambda: display("7"))
btn_seven.place(x=10, y=200)

btn_eight = Button(root, text="8", bg="#2a2d36", fg="#fff", bd=1, width=5,
                   height=1, font=("arial", 30, "bold"), command=lambda: display("8"))
btn_eight.place(x=150, y=200)

btn_nine = Button(root, text="9", bg="#2a2d36", fg="#fff", bd=1, width=5,
                  height=1, font=("arial", 30, "bold"), command=lambda: display("9"))
btn_nine.place(x=290, y=200)

btn_sub = Button(root, text="-", bg="#2a2d36", fg="#fff", bd=1, width=5,
                 height=1, font=("arial", 30, "bold"), command=lambda: display("-"))
btn_sub.place(x=430, y=200)

btn_four = Button(root, text="4", bg="#2a2d36", fg="#fff", width=5, height=1,
                  bd=1, font=("arial", 30, "bold"), command=lambda: display("4"))
btn_four.place(x=10, y=300)

btn_five = Button(root, text="5", bg="#2a2d36", fg="#fff", width=5, height=1,
                  bd=1, font=("arial", 30, "bold"), command=lambda: display("5"))
btn_five.place(x=150, y=300)

btn_six = Button(root, text="6", bg="#2a2d36", fg="#fff", width=5, height=1,
                 bd=1, font=("arial", 30, "bold"), command=lambda: display("6"))
btn_six.place(x=290, y=300)

btn_add = Button(root, text="+", bg="#2a2d36", fg="#fff", width=5, height=1,
                 bd=1, font=("arial", 30, "bold"), command=lambda: display("+"))
btn_add.place(x=430, y=300)

btn_one = Button(root, text="1", width=5, height=1, bd=1, bg="#2a2d36",
                 fg="#fff", font=("arial", 30, "bold"), command=lambda: display("+"))
btn_one.place(x=10, y=400)

btn_two = Button(root, text="2", width=5, height=1, bd=1, bg="#2a2d36",
                 fg="#fff", font=("arial", 30, "bold"), command=lambda: display("2"))
btn_two.place(x=150, y=400)

btn_three = Button(root, text="3", width=5, height=1, bd=1, bg="#2a2d36",
                   fg="#fff", font=("arial", 30, "bold"), command=lambda: display("3"))
btn_three.place(x=290, y=400)

btn_zero = Button(root, text="0", width=11, height=1, bd=1, bg="#2a2d36",
                  fg="#fff", font=("arial", 30, "bold"), command=lambda: display("0"))
btn_zero.place(x=10, y=500)

btn_dec = Button(root, text=".", width=5, height=1, bd=1, font=(
    "arial", 30, "bold"), bg="#2a2d36", fg="#fff", command=lambda: display("."))
btn_dec.place(x=290, y=500)

btn_equal = Button(root, text="=", font=("arial", 30, "bold"), bd=1,
                   width=5, height=3, bg="#fe9037", fg="#fff", command=lambda: calculate())
btn_equal.place(x=430, y=400)


root.mainloop()
