from tkinter import *
root =Toplevel()


root.title("LockScreen - Window")
root.config(bg="black")
root.geometry("900x600")

pic_logo=PhotoImage(file=r"lounge-cyber-security-1.png")
lbl_2=Label(root,image=pic_logo, bg="black",fg="white",font= ('Helvetica 25 bold'))
lbl_2.place(x=80, y=120)

lbl_1=Label(root, text="Login To My Programe", bg="black",fg="orange",font= ('Helvetica 25 bold'))
lbl_1.place(x=230, y=80)



lbl_user=Label(root,text='UserName', bg="black",fg="orange",font= ('Helvetica 16 bold'))
lbl_user.place(x=380, y=220)

lbl_pass=Label(root,text='Password', bg="black",fg="orange",font= ('Helvetica 16 bold'))
lbl_pass.place(x=380, y=270)


user_1=Entry(root, bg="black",fg="orange",font= ('Helvetica 16 bold'))
user_1.place(x=500, y=220)

pass_1=Entry(root, bg="black",fg="orange",font= ('Helvetica 16 bold') ,show="*")
pass_1.place(x=500, y=270)

def main_():
    root.destroy()
    import main
    


btn_login = Button(root, text="Login ", bg="orange",fg="black",font= ('Helvetica 16 bold'),command=main_)
btn_login.place(x=300, y=400) 

def exit_():
    root.destroy()


exit_login = Button(root, text="Exit", bg="red",fg="black",font= ('Helvetica 16 bold'),command=exit_)
exit_login.place(x=500, y=400)



root.mainloop()