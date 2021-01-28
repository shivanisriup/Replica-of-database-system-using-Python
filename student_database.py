from tkinter import*
from tkinter import filedialog
import sqlite3

class Gui:
       def __init__(self):
           global en3
           self.scr = Tk()
           self.scr.geometry("2000x3000")
           self.scr.title("VIEWING DATABASE")
           self.connection = sqlite3.connect("student_details.db")
           self.cursor = self.connection.cursor()
           self.id = StringVar()
           self.name1 = StringVar()
           self.fathername = StringVar()
           self.mothername = StringVar()
           self.cont = StringVar()
           self.email = StringVar()
           self.f1 = Frame(self.scr, bg='brown1')
           self.f1.pack(side=TOP)
           self.left_frame = Frame(self.scr, bg='red')
           self.left_frame.pack(side=LEFT, fill=Y)
           self.right_frame = Frame(self.scr, width=3000, bg='yellow')
           self.right_frame.pack(side=LEFT, fill=Y)
           l = Label(self.right_frame, text="***************SHOW TABLE RECORDS IN A DATABASE******************",
                     font=('times', 25, 'bold'), bg="black", fg="white")
           l.pack(side=TOP, fill=X)
           scrollbar = Scrollbar(self.right_frame)
           scrollbar.pack(side=RIGHT, fill=Y)
           self.list = Listbox(self.right_frame, width=61, height=12, font=('times', 25, 'bold'),
                               yscrollcommand=scrollbar.set)
           self.list.bind("student_list", self.show_records)
           self.list.pack(side=TOP, fill=Y)
           scrollbar.config(command=self.list.yview)
           self.querry_frame = Frame(self.right_frame, width=81, height=5, bg="white")
           self.querry_frame.pack(side=BOTTOM, fill=X)
           self.en3 = Entry(self.querry_frame, font=('times', 25, 'bold'))
           self.en3.pack(side=BOTTOM, fill=X)
           b = Button(self.querry_frame, text="Enter",command=self.sample, font=('times', 25, 'bold'), bg="white", fg="black")
           b.pack(side=RIGHT)
           b1 = Button(self.querry_frame, text="Save", command=self.show_data, font=('times', 25, 'bold'), bg="white",
                       fg="black")
           b1.pack(side=RIGHT)
           b = Button(self.f1, text="OPEN", command=self.file, font=('times', 25, 'bold'), bg="white", fg="black")
           b.pack(side=LEFT)
           b = Button(self.f1, text="CREATE", command=self.create_table, font=('times', 25, 'bold'), bg="white",
                      fg="black")
           b.pack(side=LEFT)
           b1 = Button(self.f1, text="INSERT", command=self.add_record, font=('times', 25, 'bold'), bg="white",
                       fg="black")
           b1.pack(side=LEFT)
           b2 = Button(self.f1, text="DELETE", command=self.del_rec, font=('times', 25, 'bold'), bg="white",
                       fg="black")
           b2.pack(side=LEFT)
           b3 = Button(self.f1, text="UPDATE", command=self.update, font=('times', 25, 'bold'), bg="white",
                       fg="black")
           b3.pack(side=RIGHT)
           b4 = Button(self.f1, text="VIEW", command=lambda: self.view_table(), font=('times', 25, 'bold'), bg="white",
                       fg="black")
           b4.pack(side=RIGHT)
           b4 = Button(self.f1, text="BROWSE", command=self.show_data, font=('times', 25, 'bold'), bg="white",
                       fg="black")
           b4.pack(side=RIGHT)
           l = Label(self.left_frame, text="View Table in Database", font=('times', 25, 'bold'), bg='blue', fg='white')
           l.pack(side=TOP, fill=X)

           self.scr.mainloop()

           try:
               self.cursor.execute("create table user(Id varchar(10),Name varchar(30),FathersName varchar(20),MothersName varchar(20),Contact varchar(10),Email varchar(30))")
               self.connection.commit()
           except:
               pass

       def insert_data(self):
           self.id = e.get()
           self.name1 = e1.get()
           self.fathername=e2.get()
           self.mothername = e3.get()
           self.cont = e4.get()
           self.email = e5.get()
           self.cursor.execute("insert into user values('{}','{}','{}','{}','{}','{}')".format(self.id,self.name1, self.fathername,self.mothername,self.cont , self.email))
           self.connection.commit()


       def show_data(self):
           self.connection = sqlite3.connect("student_details.db")
           self.cursor = self.connection.cursor()
           self.cursor.execute("Select * from user")
           rows = self.cursor.fetchall()
           for row in rows:
               l1 = self.list.insert(END, row)
           self.connection.commit()

       def update_data(self):
           self.cursor.execute("Update user set {} = '{}' where id ='{}'".format(e2.get(),e3.get(),e.get()))
           self.connection.commit()
           self.list.delete(0, END)
           self.show_data()

       def update(self):
           global e
           global e2
           global e3
           self.top1 = Toplevel(self.scr)
           self.top1.geometry("400x400")
           l1 = Label(self.top1, text="USER_ID", font=('times', 25, 'bold'), bg="green2", fg="white")
           l1.pack()
           self.Id=StringVar()
           e = Entry(self.top1, relief="sunken", textvariable=self.Id, font=('times', 25, 'bold'))
           e.pack()
           self.col_name=StringVar()
           l2 = Label(self.top1, text="col_name", font=('times', 25, 'bold'), bg="green2", fg="white")
           l2.pack()
           e2 = Entry(self.top1, relief="sunken", textvariable=self.col_name, font=('times', 25, 'bold'))
           e2.pack()
           self.value=StringVar()
           l3 = Label(self.top1, text="VALUE", font=('times', 25, 'bold'), bg="green2", fg="white")
           l3.pack()
           e3 = Entry(self.top1, relief="sunken", textvariable=self.value, font=('times', 25, 'bold'))
           e3.pack()
           b = Button(self.top1, text="UPDATE", command=self.update_data, font=('times', 25, 'bold'), bg="white",
                      fg="black")
           b.pack()

           self.top1.mainloop()

       def delete_data(self):
           self.cursor.execute("Delete from  user where id ='{}'".format(e.get()))
           self.list.delete(0,END)
           self.connection.commit()
           self.show_data()

       def del_rec(self):
           global e
           self.top2 = Toplevel(self.scr)
           self.top2.geometry("400x400")
           l1 = Label(self.top2, text="USER_ID", font=('times', 25, 'bold'), bg="green2", fg="white")
           l1.pack()
           self.Id = StringVar()
           e = Entry(self.top2, relief="sunken", textvariable=self.Id, font=('times', 25, 'bold'))
           e.pack()
           b = Button(self.top2, text="delete records", command=self.delete_data, font=('times', 25, 'bold'), bg="white",
                      fg="black")
           b.pack()
           self.top2.mainloop()

       def sample(self):
           s=('{}'.format(self.en3.get()))
           a=self.cursor.execute("{}".format(self.en3.get()))
           r=self.cursor.fetchall()
           for row in r:
               self.list.insert(0,row)
           self.connection.commit()



       def file(self):
           self.f1.filename = filedialog.askopenfilename( title="Select file")
           p=self.f1.filename
           self.list.insert(0,self.f1.filename)

       def add_record(self):
           global e
           global e1
           global e2
           global e3
           global e4
           global e5
           self.e = StringVar()
           self.e1 = StringVar()
           self.e2 = StringVar()
           self.e3 = StringVar()
           self.e4 = StringVar()
           self.e5 = StringVar()
           self.top=Toplevel(self.scr)
           self.top.geometry("400x800")
           l=Label(self.top,text="USER_ID",font=('times',25,'bold'),bg="green2",fg="white")
           l.pack()
           e=Entry(self.top,relief="sunken",textvariable=self.e,font=('times',25,'bold'))
           e.pack()
           l1 = Label(self.top, text="USERNAME", font=('times', 25, 'bold'), bg="green2", fg="white")
           l1.pack()
           e1 = Entry(self.top, relief="sunken",textvariable=self.e1, font=('times', 25, 'bold'))
           e1.pack()
           l2 = Label(self.top, text="FATHERS NAME", font=('times', 25, 'bold'), bg="green2", fg="white")
           l2.pack()
           e2 = Entry(self.top, relief="sunken",textvariable=self.e2, font=('times', 25, 'bold'))
           e2.pack()
           l3 = Label(self.top, text="MOTHERS NAME", font=('times', 25, 'bold'), bg="green2", fg="white")
           l3.pack()
           e3 = Entry(self.top, relief="sunken",textvariable=self.e3, font=('times', 25, 'bold'))
           e3.pack()
           l4 = Label(self.top, text="CONTACT NO", font=('times', 25, 'bold'), bg="green2", fg="white")
           l4.pack()
           e4 = Entry(self.top, relief="sunken",textvariable=self.e4, font=('times', 25, 'bold'))
           e4.pack()
           l5 = Label(self.top, text="E-MAIL ID", font=('times', 25, 'bold'), bg="green2", fg="white")
           l5.pack()
           e5 = Entry(self.top, relief="sunken",textvariable=self.e5, font=('times', 25, 'bold'))
           e5.pack()
           varchk=IntVar()
           b = Button(self.top, text="SUBMIT", command=self.insert_data,font=('times', 25, 'bold'), bg="white",fg="black")
           b.pack()
           self.top.mainloop()


       def view_table(self):
           global  list_box
           self.list_box = Listbox(self.left_frame, font=('times', 20, 'bold'))

           try:

            self.list_box.insert(1,"user")
            self.list_box.insert(2,self.tbl_name)
           except:
               pass
           b=Button(self.left_frame,text="Click",font=('times', 20, 'bold'),command=self.selection,bg="white",fg="black")
           b.place(x=100,y=400)
           self.list_box.place(x=10,y=50)

       def selection(self):
           lb = self.list_box.curselection()
           print(lb)
           for i in list(lb):
               self.show_data()

       def show_records(self):
           global m
           m=self.list.curselection()
           m=self.list.get(m)
           self.id.delete(0,END)
           self.id.insert(END,self.add_record())

       global table_name

       def create_table(self):
           self.top = Toplevel(self.scr)
           self.top.geometry("400x800")
           self.table_name=StringVar()
           l=Label(self.top,text="Table",font=('times', 20, 'bold'),bg="white",fg="black")
           l.pack()
           e=Entry(self.top,textvariable=self.table_name,font=('times', 20, 'bold'))
           e.pack()
           b=Button(self.top,text="Add field",command=self.fun_show ,  font=('times', 20, 'bold'),bg="white",fg="black")
           b.pack()
           b=Button(self.top,text="OK",font=('times', 20, 'bold'),command=self.show_entered_data,bg="white",fg="black")
           b.pack(side=RIGHT)


       def show_entered_data(self):
           global en1
           global en2
           global list1
           global tbl_name
           self.tbl_name=self.table_name.get()
           self.en1=self.entry1.get()
           self.en2=self.entry2.get()
           sent="Create table "+str(self.tbl_name)+"('"+str(self.en1)+  "  "+ str(self.en2)+"')"
           list1 = Text(self.top, width=41, height=8, font=('times', 25, 'bold'))
           list1.place(x=0,y=0)
           list1.insert(0.0,sent)
           print(self.tbl_name,self.en1,self.en2)
           self.cursor.execute(sent)
           self.list.insert(0,sent)
           self.connection.commit()


       def fun_show(self):
           l = Label(self.top, text="Name", font=('times', 20, 'bold'), bg="white", fg="black")
           l.pack(side=TOP)
           self.entry1 = StringVar()
           e1 = Entry(self.top, textvariable=self.entry1, font=('times', 20, 'bold'))
           e1.pack()
           l = Label(self.top, text="type", font=('times', 20, 'bold'), bg="white", fg="black")
           l.pack(side=TOP)
           self.entry2 = StringVar()
           e1 = Entry(self.top, textvariable=self.entry2, font=('times', 20, 'bold'))
           e1.pack()


Gui()