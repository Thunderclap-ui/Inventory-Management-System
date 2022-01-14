from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("                                                                                                                             Inventory Management System | Developed By Gaayana And Jayanth")
        self.root.config(bg="ghost white")
        self.root.focus_force()
        #---------------------------------------------------
        #-------all variable-------------------
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_salary=StringVar()
        #--------------------search frame--------------------------------
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("rockwell",12,"bold"),bd=2,relief=RIDGE,bg="ghost white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #----------------------option---------------
        cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("rockwell",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("rockwell",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="Search",font=("rockwell",15),bg="#4caf50",fg="ghost white",cursor="hand2").place(x=410,y=9,width=150,height=30)   

        #---------------title----------------
        title=Label(self.root,text="Employee Details",font=("rockwell",15),bg="#0f4d7d",fg="ghost white").place(x=40,y=100,width=1200) 

        #--------------------content----------------
        #--------------------row1------------------------
        lbl_empid=Label(self.root,text="Emp ID",font=("rockwell",15),bg="ghost white").place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("rockwell",15),bg="ghost white").place(x=400,y=150) 
        lbl_contact=Label(self.root,text="Contact",font=("rockwell",15),bg="ghost white").place(x=750,y=150)
        
        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("rockwell",15),bg="lightyellow").place(x=150,y=150,width=180)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female"),state='readonly',justify=CENTER,font=("rockwell",15))
        cmb_gender.place(x=500,y=150,width=180)
        cmb_gender.current(0) 
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("rockwell",15),bg="lightyellow").place(x=850,y=150,width=180)

        #----------------------------row2--------------------------
        lbl_name=Label(self.root,text="Name",font=("rockwell",15),bg="ghost white").place(x=50,y=190)
        lbl_dob=Label(self.root,text="D.O.B",font=("rockwell",15),bg="ghost white").place(x=400,y=190) 
        lbl_doj=Label(self.root,text="D.O.J",font=("rockwell",15),bg="ghost white").place(x=750,y=190)
        
        txt_name=Entry(self.root,textvariable=self.var_name,font=("rockwell",15),bg="lightyellow").place(x=150,y=190,width=180)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=("rockwell",15),bg="lightyellow").place(x=500,y=190,width=180)
        txt_doj=Entry(self.root,textvariable=self.var_doj,font=("rockwell",15),bg="lightyellow").place(x=850,y=190,width=180)
        
        #--------------------------row3----------------------------
        lbl_email=Label(self.root,text="Email",font=("rockwell",15),bg="ghost white").place(x=50,y=230)
        lbl_password=Label(self.root,text="Password",font=("rockwell",15),bg="ghost white").place(x=400,y=230) 
        lbl_usertype=Label(self.root,text="User-type",font=("rockwell",15),bg="ghost white").place(x=750,y=230)

        txt_email=Entry(self.root,textvariable=self.var_email,font=("rockwell",15),bg="lightyellow").place(x=150,y=230,width=180)
        txt_password=Entry(self.root,textvariable=self.var_pass,font=("rockwell",15),bg="lightyellow").place(x=500,y=230,width=180)
        cmb_usertype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Select","Admin","Employee"),state='readonly',justify=CENTER,font=("rockwell",15))
        cmb_usertype.place(x=850,y=230,width=180)
        cmb_usertype.current(0) 

        #--------------------------row4----------------------------
        lbl_address=Label(self.root,text="Address",font=("rockwell",15),bg="ghost white").place(x=50,y=270)
        lbl_salary=Label(self.root,text="Salary",font=("rockwell",15),bg="ghost white").place(x=500,y=270) 
        

        self.txt_address=Text(self.root,font=("rockwell",15),bg="lightyellow")
        self.txt_address.place(x=150,y=270,width=300,height=60)
        txt_salary=Entry(self.root,textvariable=self.var_salary,font=("rockwell",15),bg="lightyellow").place(x=600,y=270,width=180)
        #-------------------------button---------------------------------
        btn_add=Button(self.root,text="ADD",font=("rockwell",15),bg="#2196f3",fg="ghost white",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,text="UPDATE",font=("rockwell",15),bg="#4caf50",fg="ghost white",cursor="hand2").place(x=620,y=305,width=110,height=28)
        btn_delete=Button(self.root,text="DELETE",font=("rockwell",15),bg="#f44336",fg="ghost white",cursor="hand2").place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root,text="CLEAR",font=("rockwell",15),bg="#607d8b",fg="ghost white",cursor="hand2").place(x=860,y=305,width=110,height=28)
        


        #----------Employee details--------------------
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)


        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.heading("eid",text="Emp ID")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("email",text="Email")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("dob",text="D.O.B")
        self.EmployeeTable.heading("doj",text="D.O.J")
        self.EmployeeTable.heading("pass",text="Password")
        self.EmployeeTable.heading("utype",text="User-type")
        self.EmployeeTable.heading("address",text="Address")
        self.EmployeeTable.heading("salary",text="Salary")
        self.EmployeeTable["show"]="headings"
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.column("eid",width=90)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("email",width=100)
        self.EmployeeTable.column("gender",width=100)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("dob",width=100)
        self.EmployeeTable.column("doj",width=100)
        self.EmployeeTable.column("pass",width=100)
        self.EmployeeTable.column("utype",width=100)
        self.EmployeeTable.column("address",width=100)
        self.EmployeeTable.column("salary",width=100)

if __name__=="__main__":
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()

