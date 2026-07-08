# create a library management system with also issue and return options


import tkinter as tk

window = tk.Tk()

window.title("expense tracker")

window.geometry("900x600")



label = tk.Label(window,text="BOOK NAME",font=("arial",15),width=30,height=4)

label.grid(row=0,column=0)

entry = tk.Entry(window)

entry.grid(row=0,column=1)

label = tk.Label(window,text="AUTHOR",font=("arial",15),width=30,height=4)

label.grid(row=1,column=0)

entry1 = tk.Entry(window)

entry1.grid(row=1,column=1)

label = tk.Label(window,text="BOOK ID",font=("arial",15),width=30,height=4)

label.grid(row=2,column=0)

entry2 = tk.Entry(window)

entry2.grid(row=2,column=1)



# def click(value):
#     entry.insert(tk.END,value)

# no need for this as we are not using lambda = click

def delete():

    entry.delete(0,tk.END)

    entry1.delete(0,tk.END)

    entry2.delete(0,tk.END)




def store():

    f = open("lib.txt","a")

    f.write(entry.get() + "," + entry1.get() + ","  + entry2.get() + "\n")



def read():
    
    f = open("lib.txt","r")

    line = f.readline()

# remember its readline not lines if you want readlines then add data = line[0].split","

    f.close()

    data = line.split(",")

    entry.delete(0,tk.END)

    entry1.delete(0,tk.END)

    entry2.delete(0,tk.END)


    
    entry.insert(0,data[0].strip())

    entry1.insert(0,data[1].strip())

    entry2.insert(0,data[2].strip())



def iss():

    f = open("lib.txt","w")

    f.write(entry.get() + "," + entry1.get() + ","  + entry2.get() + "," + "ISSUED")
    


def ret():

    f = open("lib.txt","w")

    f.write(entry.get() + "," + entry1.get() + ","  + entry2.get() + "," + "AVAILABLE")




button = tk.Button(window,text="save",command=store)

button.grid(row=3,column=0)

button1 = tk.Button(window,text="clear",command=delete)

button1.grid(row=4,column=0)

button2 = tk.Button(window,text="load",command=read)

button2.grid(row=5,column=0)


button3 = tk.Button(window,text="issue",command=iss)

button3.grid(row=6,column=0)


button4 = tk.Button(window,text="return",command=ret)

button4.grid(row=7,column=0)


window.mainloop()