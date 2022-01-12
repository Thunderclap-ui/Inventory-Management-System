from tkinter import*
from PIL import Image,ImageTk
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x900+50+50")
        self.root.title("                                                                                                                                                                                   Inventory Management System | Developed By Gaayana And Jayanth")
        self.root.config(bg="ghost white")
        #----title----
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("rockwell",40,"bold"),bg="turquoise4",fg="gray4",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #----btn_logout----
        btn_logout=Button(self.root,text="Logout",font=("rockwell",15,"bold"),bg="orangered2",cursor="hand2").place(x=1150,y=10,height=50,width=150)

        #----clock----
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("rockwell",15,"italic"),bg="red4",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #----Left Menu----
        self.MenuLogo=Image.open("images/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="ghost white")
        LeftMenu.place(x=0,y=102,width=250,height=700)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        lbl_menu=Label(LeftMenu,text="Menu",font=("rockwell",20),bg="midnight blue").pack(side=TOP,fill=X)


root=Tk()
obj=IMS(root)
root.mainloop()
