from tkinter import *
from tkinter import ttk

root = Tk()


root.title("Welcome - Window")
root.config(bg="black")
root.geometry("800x600")

lbl_1=Label(root, text="Welcome To My Programe", bg="black",fg="orange",font= ('Helvetica 25 bold'))
lbl_1.place(x=180, y=80)

pic_logo=PhotoImage(file="Untitled__1_-removebg-preview.png")
lbl_2=Label(root,image=pic_logo, bg="black",fg="orange",font= ('Helvetica 25 bold'))
lbl_2.place(x=80, y=120)


progress = ttk.Progressbar(root, orient="horizontal", length=800, mode="determinate")
progress.place(x=1,y=570)


progress["value"] = 0


lbl_3=Label(root, text="Please Wait ", bg="black",fg="orange",font= ('Helvetica 15 bold'))
lbl_3.place(x=330, y=420)

root.overrideredirect(2)
def update_progress():
    progress["value"] += 10
    if progress["value"] < 110:
        progress.after(1000, update_progress)
    else:
        
        root.destroy()
        import Lock_Screen 
        
    Label(root, text=progress["value"] ,bg="black",fg="orange",font= ('Helvetica 15 bold')).place(x=370, y=450)



update_progress()
# root.attributes("-topmost", False)
root.mainloop()