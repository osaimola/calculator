import tkinter

window = tkinter.Tk()
window.title("Tkinter Calculator")

#set default value of Ans to 0
answer = "0"
#create boolean to track if calculations have been computed and set to false
computed = False
print(computed)

#entry windows
compute_window = tkinter.Text(window, height=7, width=40,borderwidth=5)
compute_window.grid(row=0, column=4, rowspan=2)

result_window = tkinter.Text(window, height=7, width=40, borderwidth=5)
result_window.grid(row=3, column=4, rowspan=2)

#button functions
def zero():
	result_window.insert(tkinter.END, "0")

def one():
	result_window.insert(tkinter.END, "1")

def two():
	result_window.insert(tkinter.END, "2")

def three():
	result_window.insert(tkinter.END, "3")

def four():
	result_window.insert(tkinter.END, "4")

def five():
	result_window.insert(tkinter.END, "5")

def six():
	result_window.insert(tkinter.END, "6")

def seven():
	result_window.insert(tkinter.END, "7")

def eight():
	result_window.insert(tkinter.END, "8")

def nine():
	result_window.insert(tkinter.END, "9")

def open_bracket():
	result_window.insert(tkinter.END, "(")

def close_bracket():
	result_window.insert(tkinter.END, ")")

#begin delete from 2 characters before the end up to the end
#(Tkinter adds an extra new line character to Text widgets)
def backspace():
	result_window.delete("end-2c", tkinter.END)

#begin deleting from the first character to the end
def clear():
	compute_window.delete("1.0", tkinter.END)
	result_window.delete("1.0", tkinter.END)

def divide():
	"""adds content of result_window to the the compute_window and clears result_window"""
	#if computed is true, compute window contains answer to previous calculation so is cleared
	global computed
	if computed:
		compute_window.delete("1.0", tkinter.END)
		computed = False
	value = result_window.get("1.0", "end-1c")
	compute_window.insert(tkinter.END, value+"/")
	result_window.delete("1.0", tkinter.END)

def multiply():
	"""adds content of result_window to the the compute_window and clears result_window"""
	#if computed is true, compute window contains answer to previous calculation so is cleared
	global computed
	if computed:
		compute_window.delete("1.0", tkinter.END)
		computed = False
	value = result_window.get("1.0", "end-1c")
	compute_window.insert(tkinter.END, value+"*")
	result_window.delete("1.0", tkinter.END)

def subtract():
	"""adds content of result_window to the the compute_window and clears result_window"""
	#if computed is true, compute window contains answer to previous calculation so is cleared
	global computed
	if computed:
		compute_window.delete("1.0", tkinter.END)
		computed = False
	value = result_window.get("1.0", "end-1c")
	compute_window.insert(tkinter.END, value+"-")
	result_window.delete("1.0", tkinter.END)

def add():
	"""adds content of result_window to the the compute_window and clears result_window"""
	#if computed is true, compute window contains answer to previous calculation so is cleared
	global computed
	if computed:
		compute_window.delete("1.0", tkinter.END)
		computed = False
	value = result_window.get("1.0", "end-1c")
	compute_window.insert(tkinter.END, value+"+")
	result_window.delete("1.0", tkinter.END)

def dot():
	result_window.insert(tkinter.END, ".")

def equal():
	"""
	uses the eval() function to compute the string content of compute_window
	specifies global computed value is used and sets to true
	"""
	global computed
	global answer
	computed =True
	value = result_window.get("1.0", "end-1c")
	compute_window.insert(tkinter.END, value)
	try:
		answer = eval(compute_window.get("1.0", "end-1c"))
		compute_window.delete("1.0", tkinter.END)
		result_window.delete("1.0", tkinter.END)
		compute_window.insert(tkinter.END, answer)
	except SyntaxError:
		compute_window.insert(tkinter.END, "= SyntaxError")
	except TypeError:
		compute_window.insert(tkinter.END, "= SyntaxError. Use operands before and after brackets.")

def ans():
	global answer
	result_window.insert(tkinter.END, answer)

#buttons
b_open_bracket = tkinter.Button(window, text="(", padx=41, pady=20, command=open_bracket)
b_open_bracket.grid(row=0, column=0)

b_close_bracket = tkinter.Button(window, text=")", padx=41, pady=20, command=close_bracket)
b_close_bracket.grid(row=0, column=1)

b_backspace = tkinter.Button(window, text="<-", padx=37, pady=20, command=backspace, bg="#fff175")
b_backspace.grid(row=0, column=2)

b_clear = tkinter.Button(window, text="clear", padx=31, pady=20, command=clear, bg="#f97070")
b_clear.grid(row=0, column=3)

b_seven = tkinter.Button(window, text="7", padx=40, pady=20, command=seven)
b_seven.grid(row=1, column=0)

b_eight = tkinter.Button(window, text="8", padx=40, pady=20, command=eight)
b_eight.grid(row=1, column=1)

b_nine = tkinter.Button(window, text="9", padx=40, pady=20, command=nine)
b_nine.grid(row=1, column=2)

b_divide = tkinter.Button(window, text="/", padx=40, pady=20, command=divide, bg="#89c4ff")
b_divide.grid(row=1, column=3)

b_four = tkinter.Button(window, text="4", padx=40, pady=20, command=four)
b_four.grid(row=2, column=0)

b_five = tkinter.Button(window, text="5", padx=40, pady=20, command=five)
b_five.grid(row=2, column=1)

b_six = tkinter.Button(window, text="6", padx=40, pady=20, command=six)
b_six.grid(row=2, column=2)

b_multiply = tkinter.Button(window, text="X", padx=40, pady=20, command=multiply, bg="#89c4ff")
b_multiply.grid(row=2, column=3)

b_one = tkinter.Button(window, text="1", padx=40, pady=20, command=one)
b_one.grid(row=3, column=0)

b_two = tkinter.Button(window, text="2", padx=40, pady=20, command=two)
b_two.grid(row=3, column=1)

b_three = tkinter.Button(window, text="3", padx=40, pady=20, command=three)
b_three.grid(row=3, column=2)

b_subtract = tkinter.Button(window, text="-", padx=40, pady=20, command=subtract, bg="#89c4ff")
b_subtract.grid(row=3, column=3)

b_zero = tkinter.Button(window, text="0", padx=40, pady=20, command=zero)
b_zero.grid(row=4, column=0)

b_dot = tkinter.Button(window, text=".", padx=41, pady=20, command=dot)
b_dot.grid(row=4, column=1)

b_equal = tkinter.Button(window, text="=", padx=40, pady=20, command=equal,bg="#71db6f")
b_equal.grid(row=4, column=2)

b_add = tkinter.Button(window, text="+", padx=39, pady=20, command=add, bg="#89c4ff")
b_add.grid(row=4, column=3)

b_ans = tkinter.Button(window, text="Ans", padx =40, pady=20, command=ans)
b_ans.grid(row=2, column=4)


#launch the tkinter window
window.mainloop()