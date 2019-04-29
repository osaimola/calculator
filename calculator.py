import tkinter

window = tkinter.Tk()
window.title("Tkinter Calculator")

# set default value of Ans to 0
answer = "0"
# create boolean to track if current value of compute_text_area is result of a recent calculation and set to False
computed = False

# entry windows
compute_text_area = tkinter.Text(window, height=7, width=40, borderwidth=5)
compute_text_area.grid(row=0, column=4, rowspan=2)

entry_text_area = tkinter.Text(window, height=7, width=40, borderwidth=5)
entry_text_area.grid(row=3, column=4, rowspan=2)


# button functions
def entry_button(value):
    """adds value of clicked buttons to entry_text_area"""
    entry_text_area.insert(tkinter.END, value)


def operator_button(operator):
    """adds text in entry_text_area to compute_text_area. Will clear compute text area if computed is True"""
    global computed
    if computed:
        compute_text_area.delete("1.0", tkinter.END)
        computed = False
    value = entry_text_area.get("1.0", "end-1c")
    compute_text_area.insert(tkinter.END, value + operator)
    entry_text_area.delete("1.0", tkinter.END)


# begin delete from 2 characters before the end up to the end
# (Tkinter adds an extra new line character to Text widgets)
def backspace():
    """delete most recent character in entry_text_area"""
    entry_text_area.delete("end-2c", tkinter.END)


# begin deleting from the first character to the end
def clear():
    """clear all current entries"""
    compute_text_area.delete("1.0", tkinter.END)
    entry_text_area.delete("1.0", tkinter.END)


def equal():
    """
    uses the eval() function to compute the string content of compute_text_area
    sets the global value of computed to True
    sets global value of answer to calculation result
    """
    global computed
    global answer
    computed = True
    value = entry_text_area.get("1.0", "end-1c")
    compute_text_area.insert(tkinter.END, value)
    try:
        answer = eval(compute_text_area.get("1.0", "end-1c"))
        compute_text_area.delete("1.0", tkinter.END)
        entry_text_area.delete("1.0", tkinter.END)
        compute_text_area.insert(tkinter.END, answer)
    except SyntaxError:
        compute_text_area.insert(tkinter.END, "= SyntaxError")
    except TypeError:
        compute_text_area.insert(tkinter.END, "= SyntaxError. Use operands before and after brackets.")


def ans():
    """enters the most recent calculation result to entry_text_area"""
    global answer
    entry_text_area.insert(tkinter.END, answer)


# buttons
b_open_bracket = tkinter.Button(window, text="(", padx=41, pady=20, command=lambda: entry_button("("))
b_open_bracket.grid(row=0, column=0)

b_close_bracket = tkinter.Button(window, text=")", padx=41, pady=20, command=lambda: entry_button(")"))
b_close_bracket.grid(row=0, column=1)

b_backspace = tkinter.Button(window, text="<-", padx=37, pady=20, command=backspace, bg="#fff175")
b_backspace.grid(row=0, column=2)

b_clear = tkinter.Button(window, text="clear", padx=31, pady=20, command=clear, bg="#f97070")
b_clear.grid(row=0, column=3)

b_seven = tkinter.Button(window, text="7", padx=40, pady=20, command=lambda: entry_button("7"))
b_seven.grid(row=1, column=0)

b_eight = tkinter.Button(window, text="8", padx=40, pady=20, command=lambda: entry_button("8"))
b_eight.grid(row=1, column=1)

b_nine = tkinter.Button(window, text="9", padx=40, pady=20, command=lambda: entry_button("9"))
b_nine.grid(row=1, column=2)

b_divide = tkinter.Button(window, text="/", padx=40, pady=20, command=lambda: operator_button("/"), bg="#89c4ff")
b_divide.grid(row=1, column=3)

b_four = tkinter.Button(window, text="4", padx=40, pady=20, command=lambda: entry_button("4"))
b_four.grid(row=2, column=0)

b_five = tkinter.Button(window, text="5", padx=40, pady=20, command=lambda: entry_button("5"))
b_five.grid(row=2, column=1)

b_six = tkinter.Button(window, text="6", padx=40, pady=20, command=lambda: entry_button("6"))
b_six.grid(row=2, column=2)

b_multiply = tkinter.Button(window, text="X", padx=40, pady=20, command=lambda: operator_button("*"), bg="#89c4ff")
b_multiply.grid(row=2, column=3)

b_one = tkinter.Button(window, text="1", padx=40, pady=20, command=lambda: entry_button("1"))
b_one.grid(row=3, column=0)

b_two = tkinter.Button(window, text="2", padx=40, pady=20, command=lambda: entry_button("2"))
b_two.grid(row=3, column=1)

b_three = tkinter.Button(window, text="3", padx=40, pady=20, command=lambda: entry_button("3"))
b_three.grid(row=3, column=2)

b_subtract = tkinter.Button(window, text="-", padx=40, pady=20, command=lambda: operator_button("-"), bg="#89c4ff")
b_subtract.grid(row=3, column=3)

b_zero = tkinter.Button(window, text="0", padx=40, pady=20, command=lambda: entry_button("0"))
b_zero.grid(row=4, column=0)

b_dot = tkinter.Button(window, text=".", padx=41, pady=20, command=lambda: entry_button("."))
b_dot.grid(row=4, column=1)

b_equal = tkinter.Button(window, text="=", padx=40, pady=20, command=equal, bg="#71db6f")
b_equal.grid(row=4, column=2)

b_add = tkinter.Button(window, text="+", padx=39, pady=20, command=lambda: operator_button("+"), bg="#89c4ff")
b_add.grid(row=4, column=3)

b_ans = tkinter.Button(window, text="Ans", padx=40, pady=20, command=ans)
b_ans.grid(row=2, column=4)

# launch the tkinter window
window.mainloop()
