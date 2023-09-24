import tkinter as tk
from tkinter import *
var = 0


# images 



# root setup
root = tk.Tk()
root.title("hello world")
root.geometry("250x250")
cookie = PhotoImage(file=r"C:\Users\accompagnant\Desktop\code that work's\ver\test\\cookie.png")
# funtions 
def count():
    global var
    var += 1
    name_title.config(text=f"you have now {var}")



# root and his button and labele 
name_title = tk.Label(root,text=f"you have now {var} ",font= 12,fg= "brown")
name_title.config(text=f"you have now {var}")
name_title.pack()

buttion = tk.Button(root,text="+1",image= cookie, command= count)
buttion.pack(pady= 80)




# main loop 
root.mainloop()


