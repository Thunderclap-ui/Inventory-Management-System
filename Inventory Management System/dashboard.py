from tkinter import*
from PIL import Image,ImageTk
from employee import employeeClass
from supplier import supplierClass
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("                                                                                                                             Inventory Management System | Developed By Gaayana And Jayanth")
        self.root.config(bg="ghost white")
        #----title----
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("rockwell",40,"bold"),bg="forestgreen",fg="ghost white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #----btn_logout----
        btn_logout=Button(self.root,text="Logout",font=("rockwell",15,"bold"),bg="orangered2",cursor="hand2").place(x=1100,y=10,height=50,width=150)

        #----clock----
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("rockwell",15,"italic"),bg="dodgerblue4",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #----Left Menu----
        self.MenuLogo=Image.open("images/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((120,120),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="thistle4")
        LeftMenu.place(x=0,y=102,width=200,height=800)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        self.icon_side=PhotoImage(file="images/side.png")
        lbl_menu=Label(LeftMenu,text="Menu",font=("rockwell",20),bg="midnight blue").pack(side=TOP,fill=X)

        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("rockwell",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("rockwell",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="Category",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("rockwell",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Products",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("rockwell",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("rockwell",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("rockwell",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        #----content----
        self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="deepskyblue4",fg="snow",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=250,y=120,height=200,width=300)

        self.lbl_supplier=Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="gold2",fg="snow",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=600,y=120,height=200,width=300)

        self.lbl_category=Label(self.root,text="Total Categories\n[ 0 ]",bd=5,relief=RIDGE,bg="orangered",fg="snow",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=950,y=120,height=200,width=300)

        self.lbl_product=Label(self.root,text="Total Products\n[ 0 ]",bd=5,relief=RIDGE,bg="limegreen",fg="snow",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=250,y=400,height=200,width=300)

        self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="red4",fg="snow",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=600,y=400,height=200,width=300)



        #----footer----
        lbl_footer=Label(self.root,text="IMS - Inventory Management System | Developed By Gaayana KR & Jayanth RG\nFor any technical issue contact: +91 809xxxxxx7,+91 861xxxxxx5",font=("rockwell",15,"italic"),bg="dodgerblue4",fg="white").pack(side=BOTTOM,fill=X)
#---------------------------------------------------------------------------------------------------------------------------------------------
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()


