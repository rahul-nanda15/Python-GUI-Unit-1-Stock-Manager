from tkinter import*

# function to calculate projected price
def calculate():
    print("running")

    # Wrapping my code with error checking (if statements) to make sure the user can't break my program
    if ecalc2.get().isdigit() == False:
        error1.config(text= 'Error: Enter a Whole Number for the Stock Price (e.g. 45)', bg='red', fg='white')
    else:
        error1.config(text=' ', bg='grey', fg='white')
    
    if ecalc1.get() == '' or ecalc1.get().isdigit():
        error2.config(text= 'Error: Please Enter a Stock Name (e.g. NKE)', bg='red', fg='white')
    else:
        error2.config(text=' ', bg='grey', fg='white')

    if ecalc3.get().isdigit() == False:
        error3.config(text = 'Error: Enter a Whole Number for the % Change (e.g. 40)', bg='red', fg='white')
        return
    else:
        error3.config(text= ' ', bg='grey', fg='white')

    try:
        float(ecalc3.get())
    except ValueError:
            print('A Number Needs to be entered in the Percentage Change')

    # setting each user inputted entry box to a variable and manipulating the varibale to do a calculation
    stockname = str(ecalc1.get())
    num1 = float(ecalc2.get()) 
    num2 = float(ecalc3.get())/100
    num3 = num2 * num1
    psum = round(num1 + num3, 2)
    projected = str(psum)
   
    # printing the projected price under the group of entry bars
    projectedprice.config(text='The projected price of ' + stockname + ' is $' + projected,bg='grey',fg='white')

    # deleting text inside entry bars after the button is clicked
    ecalc1.delete(0,END)
    ecalc2.delete(0,END)
    ecalc3.delete(0,END)

    # inserting the projected price into the history or listbox
    listbox.insert(END, '  The projected price of ' + stockname + ' is $' + projected)

# function to delete history
def clear():
    listbox.delete(0, END)

# function to add a stock to the favorites section
def add():

    favname = entryrtop.get()
    favprice = entryrtop2.get()

    # wrapping my code with error checking (if statements) for the add a favorite button
    if entryrtop.get() == '' or entryrtop.get().isdigit() or entryrtop2.get().isdigit() == False:
        ferror1.config(text= 'Error: Stock Ticker and Price', bg='red', fg='white')
    else:
        ferror1.config(text=' ', bg='#a8a5a5', fg='white')
        blbox.insert(END, '                        ' + favname)
        blbox2.insert(END, '             ' + favprice)

    # clearing text in the entry boxes when the button is clicked
    entryrtop.delete(0,END)
    entryrtop2.delete(0,END)

   
    
   
     
# function to clear list of favorites
def clear2():
    blbox.delete(0, END)
    blbox2.delete(0, END)

# creating a window and setting its title and size
Sm = Tk()
Sm.title("Stock Manager and Calculator")
Sm.geometry("800x1000")



# calculate title frame
title1 = Frame(Sm,width=800,height= 40,bg="#1c1f1d") 
title1.pack(fill=X)
title1.pack_propagate(0)


# calculate title text
title1text = Label(title1,text="Calculate",fg="white",bg="#1c1f1d")
title1text.config(font=("Bold", 16))
title1text.pack(pady=5)

# main body frame for calculate section
calculatebody = Frame(Sm, height=250)
calculatebody.pack(fill=X)

# left body frame for calculate section
leftcalc = Frame(calculatebody, borderwidth=2.0, relief=RAISED, width=400, height=400, bg="grey")
leftcalc.grid(row=0,column=0)
leftcalc.pack_propagate(0)

#invisible frame for spacing and text for left body

invisibleframe = Frame(leftcalc, borderwidth=0.0, width=400, height=60, bg="grey")
invisibleframe.pack(pady=5)
invisibleframe.pack_propagate(0)

#instructions inside invisible frame for how to use program

invislabel = Label(invisibleframe, text='By entering the stock ticker, price (rounded to nearest \n one, e.g. 34), and percentage change (nearest one),  by clicking \n the button, you will get the projected stock price.',font='italic',fg="white", bg="grey")
invislabel.pack()

# left body frame text and entry boxes
lcalc1 = Label(leftcalc,text="Enter Stock Ticker:", fg="white", bg="grey")
lcalc1.pack()

ecalc1 = Entry(leftcalc)
ecalc1.pack(pady=5)

lcalc2 = Label(leftcalc, text="Enter Stock Price:", fg="white",bg='grey')
lcalc2.pack()

ecalc2 = Entry(leftcalc)
ecalc2.pack(pady=5)

lcalc3 = Label(leftcalc, text='Enter Percentage Change:', fg='white',bg='grey')
lcalc3.pack()

ecalc3 = Entry(leftcalc)
ecalc3.pack(pady=5)

# left body frame button
bcalc1 = Button(leftcalc,text='Project',command=calculate)
bcalc1.pack(pady=8)

# setting an invisible label that can be configured when the price is calculated
projectedprice = Label(leftcalc,text="",bg='grey', fg='white')
projectedprice.pack()

# setting an invisible label that can be configured when there is an error in the program
error1 = Label(leftcalc, text = '', bg='grey', fg='white')
error1.pack()

error2 = Label(leftcalc, text = '', bg='grey', fg='white')
error2.pack()

error3 = Label(leftcalc, text = '', bg='grey', fg='white')
error3.pack()

# right body frame for calculate section
rightcalc = Frame(calculatebody, borderwidth=2.0, relief=RAISED, width=400, height = 400, bg="#a8a5a5")
rightcalc.grid(row=0,column=2)
rightcalc.pack_propagate(0)

# the actual title for the right body frame
righttitle = Label(rightcalc, text='History \n \n Here you can browse your previously calculated stocks', fg='white',bg='#a8a5a5')
righttitle.pack(pady=35)
righttitle.config(font=('Bold', 14))

#placing an invisible frame for the listbox to go into
rinvisframe = Frame(rightcalc, borderwidth=0.0, width=400, height=390, bg='#a8a5a5')
rinvisframe.pack()
rinvisframe.pack_propagate(0)

# setting the title of the listbox
listtitle = Frame(rinvisframe, borderwidth=0.0, width = 380,height=40, bg='#a8a5a5')
listtitle.grid(row=0,column=0)
listtitle.pack_propagate(0)

titleframel = Frame(listtitle, width = 150, height=10, bg='#a8a5a5')
titleframel.grid(row=0,column=0)

titleframer = Frame(listtitle, width = 150, height=10, bg='#a8a5a5')
titleframer.grid(row=0,column=1)


# the frames for the listbox
listframe1 = Frame(rinvisframe, width=380, height=200, bg="#a8a5a5")
listframe1.grid(row=1,column=0)
listframe1.pack_propagate(0)

# creating the listbox with scroll bar
scrollbar = Scrollbar(listframe1, bg= 'white')
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(listframe1, yscrollcommand=scrollbar.set, height=200)

listbox.pack(fill=X, padx=(10,1))
scrollbar.config(command=listbox.yview, bg='#a8a5a5')

# creating the clear button for the listbox
buttonframe = Frame(rinvisframe, bg='#a8a5a5', width=380, height=100)
buttonframe.grid(row=2, column=0)

clearbutton = Button(buttonframe, text='Clear', command=clear, width = 10, fg='red')
clearbutton.pack(pady =5)

# manage title frame
title2 = Frame(Sm,width=800,height= 40,bg="#1c1f1d") 
title2.pack(fill=X)
title2.pack_propagate(0)

# manage title text
title2text = Label(title2,text="Manage",fg="white",bg="#1c1f1d")
title2text.config(font=("Bold", 16))
title2text.pack(pady=5)

# main body frame for manage section
managebody = Frame(Sm, height=250)
managebody.pack(fill=X)

# top body frame for manage section
topman = Frame(managebody, borderwidth=2.0, relief=RAISED, width=800, height=150, bg="#a8a5a5")
topman.grid(row=0,column=0)
topman.pack_propagate(0)

# invisible frame for the left side of the top frame
ltopman = Frame(topman, borderwidth=0.0, width=250,height=150, bg='#a8a5a5')
ltopman.grid(row=0,column=0)
ltopman.pack_propagate(0)

# text for the left side of the top frame
labelltop = Label(ltopman, text='Here, you can add\n your Favorite stocks!',fg='white',bg='#a8a5a5')
labelltop.pack(padx=15,pady=30)
labelltop.config(font=('Bold',20))

# invisible frame for the middle of the top frame
mtopman = Frame(topman, borderwidth=0.0, width=350,height=150, bg='#a8a5a5')
mtopman.grid(row=0,column=1)
mtopman.pack_propagate(0)

# entries and labels for adding favorites in the top frame
labelrtop = Label(mtopman, text='Stock Ticker:',fg='white',bg='#a8a5a5')
labelrtop.pack(pady=5)

entryrtop = Entry(mtopman)
entryrtop.pack()

labelrtop2 = Label(mtopman, text='Stock Price (nearest one, e.g. 31):',fg='white',bg='#a8a5a5')
labelrtop2.pack(pady=5)

entryrtop2 = Entry(mtopman)
entryrtop2.pack()

# frame for the right part in the top frame
rtopman = Frame(topman, borderwidth=0.0, width=200,height=150, bg='#a8a5a5')
rtopman.grid(row=0,column=2)
rtopman.pack_propagate(0)


# button in the right frame
buttonrtop = Button(rtopman, text='Add',command=add, width = 50)
buttonrtop.pack(pady=30, padx=20, anchor='w')

# setting an empty label for the error messages
ferror1 = Label(rtopman, text='', bg='#a8a5a5', fg='white')
ferror1.pack()

# bottom body frame for manage section
bottomman = Frame(managebody, borderwidth=2.0, relief=RAISED, width=800, height = 230, bg="grey")
bottomman.grid(row=1,column=0)
bottomman.pack_propagate(0)

# invisible bottom body frame for text for manage section
invisbman = Frame(bottomman, borderwidth=0.0, width=795, height = 230, bg="grey")
invisbman.pack(pady=5)

# text inside invisible frame
lbottomman = Label(invisbman, text='View Your Favorite Stocks', fg='white',bg='grey')
lbottomman.grid(row=0,column=0)
lbottomman.config(font=("Arial",16))

# 2nd invisible frame for table of "favorite stocks"
invis2bman = Frame(invisbman, borderwidth=0.0, width=795, height=120, bg='grey')
invis2bman.grid(row=1,column=0)

# Title of the listbox of "favorite stocks"
blistlabel1 = Label(invis2bman, text='\nName', fg='white', bg='grey')
blistlabel1.grid(row=0,column=0)

blistlabel2 = Label(invis2bman, text='\nPrice', fg='white', bg='grey')
blistlabel2.grid(row=0,column=1)

# frame for listbox of favorite stocks
blistframe1 = Frame(invis2bman, relief='solid', width=230, height=120, bg="grey")
blistframe1.grid(row=1,column=0)
blistframe1.pack_propagate(0)

blistframe1b = Frame(invis2bman, relief='solid', width=135, height=120, bg="grey")
blistframe1b.grid(row=1,column=1)
blistframe1b.pack_propagate(0)


# listbox for favorite stocks
blbox = Listbox(blistframe1, height=120)
blbox.pack(fill=X)
blbox2 = Listbox(blistframe1b, height=120)
blbox2.pack(fill=X)

# creating a clear button for the list of favorite stocks
buttonframe2 = Frame(invis2bman, bg='grey', width=100, height = 50)
buttonframe2.grid(row=1, column=2)

clearbutton2 = Button(buttonframe2, text='Clear', fg='red', command=clear2, width=10)
clearbutton2.pack(padx=10)



Sm.mainloop()









