from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height = 300)


#Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New text")
my_label.pack()




#Button
button = Button(text="Click Me", command=button_clicked)
button.pack()


#Entry
input = Entry(width = 10)
print(input.get())
input.pack()



window.mainloop()