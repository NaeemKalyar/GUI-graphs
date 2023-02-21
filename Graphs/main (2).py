import pandas as pd
import matplotlib.pyplot as plt
from tkinter import filedialog
from tkinter import *
root =Toplevel()


root.title("Main - Window")
root.config(bg="black")
root.geometry("900x600")

lbl_1=Label(root, text="Main System Page", bg="black",fg="orange",font= ('Helvetica 25 bold'))
lbl_1.place(x=0, y=50)

home= Button(root, text="Home ", bg="orange",fg="black",font= ('Helvetica 16 bold'))
home.place(x=1, y=100) 





def browse_file():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("csv files", "*.csv"), ("all files", "*.*")))
    data = pd.read_csv(filename)
    data = pd.read_csv(filename)
    attribute_list = list(data.columns)
    x_listbox.delete(0, END)
    y_listbox.delete(0, END)
    for attribute in attribute_list:
        x_listbox.insert(END, attribute)
        y_listbox.insert(END, attribute)
    return pd.read_csv(filename)
    
# def load():
    
#     return data

def open_file():

    def show_attributes(data):
        attribute_list = list(data.columns)
        for attribute in attribute_list:
            print(attribute)

    def plot_graph(data):
        x_attribute = x_entry.get()
        y_attribute = y_entry.get()
        if x_attribute not in data.columns or y_attribute not in data.columns:
            print("Attribute not in data")
        else:
            plt.plot(data[x_attribute], data[y_attribute])
            plt.xlabel(x_attribute)
            plt.ylabel(y_attribute)
            plt.title("Line Graph")
            plt.show()



    data = browse_file()
    show_attributes(data)

    Label(root, text = "Enter X Attribute:").place(x=250,y=250)
    x_entry = Entry(root)
    x_entry.place(x=350,y=250)
    Label(root, text = "Enter Y Attribute:").place(x=250,y=350)
    y_entry = Entry(root)
    y_entry.place(x=350,y=350)

    # plot_button = Button(root, text="Plot", command=lambda : plot_graph(data))
    # plot_button.place(x=350,y=450)

    # root.mainloop()


    home= Button(root, text="Print Result", bg="orange",fg="black",font= ('Helvetica 16 bold'), command=lambda : plot_graph(data))
    home.place(x=1, y=300) 

    def plot_save():
        plt.savefig("Output.png")

    home= Button(root, text="Save results", bg="orange",fg="black",font= ('Helvetica 16 bold'),command=plot_save)
    home.place(x=1, y=250) 


x_listbox = Listbox(root ,height=250,bg="black",fg='orange',width=40)
x_listbox.place(x=550,y=0)
y_listbox = Listbox(root,height=250 ,bg="black",fg='orange',width=40)
y_listbox.place(x=730,y=0)
x_listbox.clipboard_get()
y_listbox.clipboard_get()










def exit_():
    root.destroy()


exit_login = Button(root, text="Exit", bg="red",fg="black",font= ('Helvetica 16 bold'),command=exit_)
exit_login.place(x=1, y=400)
home= Button(root, text="Open File", bg="orange",fg="black",font= ('Helvetica 16 bold'),command=open_file)
home.place(x=1, y=150) 

home= Button(root, text="Load File", bg="orange",fg="black",font= ('Helvetica 16 bold'),command=open_file)
home.place(x=1, y=200) 


def reset():
    open_file.__format__


home= Button(root, text="Reset", bg="orange",fg="black",font= ('Helvetica 16 bold'),command=reset)
home.place(x=1, y=350) 
root.mainloop()