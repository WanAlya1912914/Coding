from tkinter import*

# PRACTICE 1
def click():
    label2 = Label(window, text = "I am fine, yalls ~", font=50)
    label2.place(x=10,y=80)


window = Tk()
window.geometry("500x500")
window.title("My 1st GUI Window!")

label = Label(window,text = "How are you?",font=50)
label.place(x=10,y=5)

button = Button(window, text = "Check", command=click)
button.place(x=20,y=40)

window.mainloop()       # must be at the last line


# PRACTICE 2
def click():
    label2 = Label(window, text = "Sorry, the ticket is SOLD OUT!", font=50)
    label2.place(x=20,y=200)

window = Tk()
window.geometry("500x500")
window.title("My Practice")

label = Label(window,text = "Hello and Welcome!",font=50)
label.place(x=10,y=10)

label3 = Label(window,text = "INFINTE Ticket concert on 10 November 2024",font=10)
label3.place(x=10,y=50)

label4 = Label(window,text = "Interested? Click button below")
label4.place(x=10,y=80)

button = Button(window, text = "Buy", command=click)
button.place(x=20,y=120)

window.mainloop()       # must be at the last line
