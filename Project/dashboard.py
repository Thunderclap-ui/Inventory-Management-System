from distutils import command
from tkinter import*
from PIL import Image,ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
import sqlite3
from tkinter import messagebox
import os
import time
class IMS:
    def __init__(self,root):
        self.root=root
        window_width = 1350
        window_height = 700
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)
        self.root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        self.root.title("                                                                                                                             Inventory Management System | Developed By Gaayana And Jayanth")
        self.root.config(bg="white")
        #----title----
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("rockwell",40,"bold"),bg="cyan4",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #----btn_logout----
        btn_logout=Button(self.root,text="Logout",command=self.logout,font=("rockwell",15,"bold"),bg="orangered2",cursor="hand2").place(x=1100,y=10,height=50,width=150)

        #----clock----
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("rockwell",15,"italic"),bg="navy",fg="white")
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
        lbl_menu=Label(LeftMenu,text="Menu",font=("rockwell",20),bg="navy",fg="white").pack(side=TOP,fill=X)

        btn_employee=Button(LeftMenu,text="Employee",command=self.employee,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("rockwell",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text="Supplier",command=self.supplier,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("rockwell",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text="Category",command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("rockwell",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text="Products",command=self.product,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("rockwell",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text="Sales",command=self.sales,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("rockwell",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("rockwell",20,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        
        #----content----
        self.lbl_employee=Label(self.root,text="Total Employees\n[ 0 ]",bd=5,relief=RIDGE,bg="deepskyblue4",fg="ghost white",font=("rockwell",20,))
        self.lbl_employee.place(x=250,y=120,height=200,width=300)

        self.lbl_supplier=Label(self.root,text="Total Suppliers\n[ 0 ]",bd=5,relief=RIDGE,bg="gold2",fg="ghost white",font=("rockwell",20))
        self.lbl_supplier.place(x=600,y=120,height=200,width=300)

        self.lbl_category=Label(self.root,text="Total Categories\n[ 0 ]",bd=5,relief=RIDGE,bg="orangered",fg="ghost white",font=("rockwell",20))
        self.lbl_category.place(x=950,y=120,height=200,width=300)

        self.lbl_product=Label(self.root,text="Total Products\n[ 0 ]",bd=5,relief=RIDGE,bg="limegreen",fg="ghost white",font=("rockwell",20))
        self.lbl_product.place(x=250,y=400,height=200,width=300)

        self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="red4",fg="ghost white",font=("rockwell",20))
        self.lbl_sales.place(x=600,y=400,height=200,width=300)



        #----footer----
        lbl_footer=Label(self.root,text="IMS - Inventory Management System | Developed By Gaayana KR & Jayanth RG\nFor any technical issue contact: +91 809xxxxxx7,+91 861xxxxxx5",font=("times new roman",15,"italic"),bg="cyan4",fg="white").pack(side=BOTTOM,fill=X)
        self.update_content()
#---------------------------------------------------------------------------------------------------------------------------------------------
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)    

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win) 

    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f'Total Products\n[ {str(len(product))}]')

            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Total Suppliers\n[ {str(len(supplier))}]')

            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f'Total Category\n[ {str(len(category))}]')

            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Total Employees\n[ {str(len(employee))}]')

            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales\n [{str(bill)}]')

            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
            self.lbl_clock.after(200,self.update_content)

        except Exception as ex:
            messagebox.showerror("Error",f'Error due to: {str(ex)}',parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python login.py")

if __name__=="__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()


