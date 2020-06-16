from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import sqlite3
import tkinter.messagebox
import csv
import os
from babel.numbers import format_currency
import datetime


def main():
    root = Tk()
    app = Window1(root)
    root.mainloop()

b = []
author = []
super_list = []
mukadam_list = []

date = datetime.datetime.now().date()

dbr = ('labour_managment.db')
labour = sqlite3.connect(dbr)
la = labour.cursor()
labour.commit()

db = ('tender_list.db')
mom = sqlite3.connect(db)
m = mom.cursor()
m.execute("CREATE TABLE IF NOT EXISTS new_tender (id INTEGER PRIMARY KEY ,authorized TEXT, ward_no TEXT,"
          "tender_no TEXT,tender_brief TEXT,final TEXT)")
mom.commit()

author_table = ('author_table.db')
conn = sqlite3.connect(author_table)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS author (id INTEGER PRIMARY KEY , authorized TEXT)")
conn.commit()

super = ('supervisor.db')
super = sqlite3.connect(super)
su = super.cursor()
su.execute("CREATE TABLE IF NOT EXISTS super_table (id INTEGER PRIMARY KEY, s_list)")
super.commit()

dam = ('mukadam.db')
mukadam = sqlite3.connect(dam)
mu = mukadam.cursor()
mu.execute("CREATE TABLE IF NOT EXISTS mukadam_table (id INTEGER PRIMARY KEY,m_list TEXT)")
mukadam.commit()


previous_table = ('pre_tender.db')
call = sqlite3.connect(previous_table)
ca = call.cursor()
ca.execute("CREATE TABLE IF NOT EXISTS pre (id INTEGER PRIMARY KEY , list TEXT)")
call.commit()

labr = ('labour_quantity.db')
za = sqlite3.connect(labr)
z = za.cursor()
z.execute("CREATE TABLE IF NOT EXISTS quantity (id INTEGER PRIMARY KEY , list INT )")
za.commit()

class Window1:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1400x750+0+0")
        self.master.title("Contractor Login")
        self.mainfram = Frame(master)
        self.mainfram.pack()

        # ========================================Label==========================================#
        self.heading_l = Label(self.master, text="C O N T R O", font=("Montserrat Subrayada", 70))
        self.heading_l.place(x=450, y=50)

        self.user = Label(self.master, text="Username : ", font=("Century Gothic", 15), fg="black")
        self.user.place(x=500, y=250)

        self.password = Label(self.master, text="Password : ", font=("Century Gothic", 15), fg="black")
        self.password.place(x=500, y=300)

        # ========================================Entry==========================================#

        self.user_e = Entry(self.master, font=("Century Gothic", 12, "bold"))
        self.user_e.place(x=680, y=250)

        self.password_e = Entry(self.master, font=("Century Gothic", 12, "bold"))
        self.password_e.place(x=680, y=300)

        # ========================================Button==========================================#

        self.submit = Button(self.master, text="Submit !", font=("Century Gothic", 12), fg="black",command = self.login)
        self.submit.place(x=720, y=360)


    def login(self):
        '''user_name = self.user_e.get()
        password = self.password_e.get()
        if user_name == "Shubham" and password == "quality":

            tkinter.messagebox.showinfo("Good","Its working")'''
        self.new_window = Toplevel(self.master)
        self.app = Window2(self.new_window)


    def Registration_window(self):
        self.new_window = Toplevel(self.master)
        self.app = Window2(self.new_window)

    def Hospital_window(self):
        self.new_window1 = Toplevel(self.master)
        self.app = Window3(self.new_window1)


class Window2:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1350x750+0+0")
        self.master.title("Contractor Login Window")



        self.tab_control = ttk.Notebook(master, style="lefttab.TNotebook")
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab3 = ttk.Frame(self.tab_control)
        self.tab4 = ttk.Frame(self.tab_control)
        self.tab5 = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab1, text=F'{"New Tender Registration " :^20s}')
        self.tab_control.add(self.tab2, text=F'{"Labour Expences Managment " :^20s}')
        self.tab_control.add(self.tab3, text=F'{"Search ": ^20s}')
        self.tab_control.add(self.tab4, text=F'{"Export " :^20s}')
        self.tab_control.add(self.tab5, text=F'{"about " :^20s}')
        self.tab_control.pack(expand=1, fill="both")
        self.view()
        self.tab2_fuc()
        # =================New registration window=====================#
        self.heading = Label(self.tab1, text="New Tender Registration.", font=("Corbel Light", 35))
        self.heading.place(x=450, y=20)

        #==========================tab1 label ===============================#

        self.authorized = Label(self.tab1, text="Authorized by ", font=("Corbel Light", 15)).place(x=20, y=100)
        self.ward = Label(self.tab1,text = "Ward no." ,font=("Corbel Light", 15)).place(x = 20, y = 160)
        self.tender_no = Label(self.tab1, text="Tender no.", font=("Corbel Light", 15)).place(x=20, y= 220)
        self.tender_brief = Label(self.tab1, text="Tender brief ", font=("Corbel Light", 15)).place(x=20, y=280)
        self.total_costing = Label(self.tab1, text="Total costing", font=("Corbel Light", 15)).place(x=20, y=420)
        self.below_percentage = Label(self.tab1, text="Below percentage ", font=("Corbel Light", 15)).place(x=20, y=480)

        self.get_bill_l = Label(self.tab1, text="", font=("Century Gothic", 35))
        self.get_bill_l.place(x=50, y=600)

        #self.authorized_e = Entry(self.tab1, font=("Corbel Light", 12))
        #self.authorized_e.place(x=200, y=150)
        self.author_com = ttk.Combobox(self.tab1, font=("Corbel Light", 12), state='readonly')
        self.author_com['values'] = author
        self.author_com.place(x=200, y=100)


        self.ward_e = Entry(self.tab1, font=("Century Gothic", 12))
        self.ward_e.place(x=200, y=160)


        self.tender_no_e = Entry(self.tab1, font=("Century Gothic", 12))
        self.tender_no_e.place(x=200, y=220)

        self.tender_brief_e = Text(self.tab1,width = 20,height = 5, font=("Century Gothic", 12))
        self.tender_brief_e.place(x=200, y=280)

        self.total_costing_e = Entry(self.tab1, font=("Century Gothic", 12))
        self.total_costing_e.place(x=200, y=420)

        self.below_percentage_e = Entry(self.tab1, font=("Century Gothic", 12))
        self.below_percentage_e.place(x=200, y=480)

        self.dis_b = Button(self.tab1, text="new", height=1, font=("Century Gothic", 10), command=self.dis_authorized)
        self.dis_b.place(x=450, y=100)

        self.below_b = Button(self.tab1, text="calculate", height=1, font=("Century Gothic", 10), command=self.below_calculations)
        self.below_b.place(x=450, y=300)

        self.add_in_tender_list_b = Button(self.tab1, text="Add in tender list", height=1, font=("Century Gothic", 10),
                              command=self.add_in_tender_list)
        self.add_in_tender_list_b.place(x=450, y=400)

        self.view_authorized()
        self.author_com = ttk.Combobox(self.tab1, font=("Corbel Light", 12), state='readonly')
        self.author_com['values'] = author
        self.author_com.place(x=200, y=100)

    def add_authorized(self):
        if self.enter.get() == "":
            author.clear()
            self.view_authorized()
            self.author_com = ttk.Combobox(self.tab1, font=("Corbel Light", 12), state='readonly')
            self.author_com['values'] = author
            self.author_com.place(x=200, y=100)
            self.add.place_forget()
            self.clr.place_forget()
            self.enter.place_forget()
            self.dis_b = Button(self.tab1, text="new", height=1, font=("Corbel Light", 10), command=self.dis_authorized)
            self.dis_b.place(x=450, y=100)


        else:
            author.clear()
            x = self.enter.get()
            cur.execute("INSERT INTO author(authorized) VALUES (?) ", (x,))
            conn.commit()
            self.view_authorized()
            self.author_com = ttk.Combobox(self.tab1, font=("Corbel Light", 12), state='readonly')
            self.author_com['values'] = author
            self.author_com.place(x=200, y=100)
            self.enter.delete(0, END)
            self.add.place_forget()
            self.clr.place_forget()
            self.enter.place_forget()
            self.dis_b = Button(self.tab1, text="new", height=1, font=("Corbel Light", 10), command=self.dis_authorized)
            self.dis_b.place(x=450, y=100)


    def view_authorized(self):
        cur.execute("SELECT authorized from author ")
        s = cur.fetchall()
        for i in s:
            x = i[0]
            author.append(x)

    def remove_authorized(self):
        if self.author_com.get() == "":
            c = self.enter.get()
            cur.execute("DELETE FROM author WHERE authorized = ?", (c,))
            conn.commit()
            author.clear()
            self.view_authorized()
            self.author_com = ttk.Combobox(self.tab1, font=("Corbel Light", 12), state='readonly')
            self.author_com['values'] = author
            self.author_com.place(x=200, y=100)
            self.enter.delete(0, END)
            self.add.place_forget()
            self.clr.place_forget()
            self.enter.place_forget()
            self.dis_b = Button(self.tab1, text="new", height=1, font=("Corbel Light", 10), command=self.dis_authorized)
            self.dis_b.place(x=450, y=100)
        else:
            c = self.author_com.get()
            cur.execute("DELETE FROM author WHERE authorized = ?", (c,))
            conn.commit()
            author.clear()
            self.view_authorized()
            self.author_com = ttk.Combobox(self.tab1, font=("Corbel Light", 12), state='readonly')
            self.author_com['values'] = author
            self.author_com.place(x=200, y=100)
            self.enter.delete(0, END)
            self.add.place_forget()
            self.clr.place_forget()
            self.enter.place_forget()
            self.dis_b = Button(self.tab1, text="new", height=1, font=("Corbel Light", 10), command=self.dis_authorized)
            self.dis_b.place(x=450, y=100)

    def dis_authorized(self):
        self.dis_b.place_forget()
        self.add = Button(self.tab1, text=" Add ", font=("Bookman Old Style", 10, "bold"), bg="steel blue", fg="white",
                          command=self.add_authorized)
        self.add.place(x=700, y=100)

        self.clr = Button(self.tab1, text=" Clear ", font=("Bookman Old Style", 10, "bold"), bg="steel blue", fg="white",
                          command=self.remove_authorized)
        self.clr.place(x=800, y=100)

        self.enter = Entry(self.tab1, font=("Corbel Light", 12))
        self.enter.place(x=500, y=100)

    def below_calculations(self):
        self.temp = (float(self.below_percentage_e.get()) / 100)
        self.below = self.temp * int(self.total_costing_e.get())
        self.amount = int(self.total_costing_e.get()) - self.below
        self.get_bill = format_currency(self.amount, 'INR', locale='en_IN')
        self.get_bill_l.configure(text = str(self.get_bill))

    def  add_in_tender_list(self):
        if self.ward_e.get() =="" and self.author_com.get() =="" and self.tender_brief_e.get() == "" and self.tender_no_e.get() =="":
            tkinter.messagebox.showerror("Error","Fill all details")

        else:
            self.final = "(" + str(self.ward_e.get()) + ")" + " " + "(" + str(self.tender_no_e.get()) + ")" \
                         + " " + self.tender_brief_e.get("1.0", END)
            m.execute("INSERT INTO new_tender(authorized,ward_no,tender_no,tender_brief,final) VALUES (?,?,?,?,?) ",
                      (self.author_com.get(),self.ward_e.get(),self.tender_no_e.get(),self.tender_brief_e.get("1.0",END),self.final))
            mom.commit()
            self.author_com.delete(0,END)
            self.ward_e.delete(0,END)
            self.tender_no_e.delete(0,END)
            self.tender_brief_e.delete("1.0", END)
            self.total_costing_e.delete(0, END)
            self.below_percentage_e.delete(0, END)
            self.get_bill_l.destroy()
            self.view()
            self.com = ttk.Combobox(self.tab2, font=("Corbel Light", 12), state='readonly', width=40)
            self.com['values'] = b
            self.com.place(x=130, y=120)

            self.com_1 = ttk.Combobox(self.view_details_frame, font=("Calibri", 12), state='readonly', width=40)
            self.com_1['values'] = b
            self.com_1.place(x=50, y=40)






        # =================supervisor =====================#

    def super_view(self):
        super_list.clear()
        su.execute("SELECT s_list FROM super_table")
        re = su.fetchall()
        for i in re:
            a = i[0]
            super_list.append(a)
            self.supervisor_e = ttk.Combobox(self.tab2, font=("Calibri", 12))
            self.supervisor_e['values'] = super_list
            self.supervisor_e.place(x=130, y=190)
    def add_super(self):
        if self.supervisor_e.get() == "":
            super_list.clear()
            self.add_super_b.place_forget()
            self.remove_super_b.place_forget()
            self.dis_super_b = Button(self.tab2, text="new", height=1, font=("Century Gothic", 10),
                                      command=self.new_super_button)
            self.dis_super_b.place(x=400, y=220)
            self.super_view()
        else:
            super_list.clear()
            s = self.supervisor_e.get()
            su.execute("INSERT INTO super_table(s_list) values(?)",(s,))
            super.commit()
            self.super_view()
            self.add_super_b.place_forget()
            self.remove_super_b.place_forget()
            self.dis_super_b = Button(self.tab2, text="new", height=1, font=("Century Gothic", 10),
                                      command=self.new_super_button)
            self.dis_super_b.place(x=400, y=220)
    def new_super_button(self):
        self.dis_super_b.place_forget()
        self.add_super_b = Button(self.tab2, text="Add", height=1, font=("Century Gothic", 10),command = self.add_super)
        self.add_super_b.place(x=400, y=220)

        self.remove_super_b = Button(self.tab2, text="remove", height=1, font=("Century Gothic", 10),command = self.super_remove)
        self.remove_super_b.place(x=470, y=220)

    def super_remove(self):
        n = self.supervisor_e.get()
        su.execute("DELETE FROM super_table WHERE s_list = ?",(n,))
        super.commit()
        self.add_super_b.place_forget()
        self.remove_super_b.place_forget()
        self.dis_super_b = Button(self.tab2, text="new", height=1, font=("Century Gothic", 10),
                                  command=self.new_super_button)
        self.dis_super_b.place(x=400, y=220)
        self.super_view()

    def tab2_fuc(self):


        self.regular = []
        self.mestri = []
        self.other = []
        self.la = []
        self.super_view()
        self.mukadam_view()
        #======================View details===========================================#
        self.view_details_frame = Frame(self.tab2,width = 1250,height = 200,bg = "gray")
        self.view_details_frame.place(x = 40 , y = 450)

                                          #=========lables=========#

        self.heading_2 = Label(self.tab2, text="View Labour Details", font=("Corbel Light", 15))
        self.heading_2.place(x=550, y=430)

        self.to = Label(self.view_details_frame, text="To", font=("Century Gothic", 12),bg = "gray",fg ="white").place(x=250, y=100)

        self.Enter_the_site_0 = Label(self.view_details_frame, text="Select the Site : ", font=("Century Gothic", 10),
                                 bg="gray", fg="white")
        self.Enter_the_site_0.place(x=100, y=20)

        self.date__label_0 = Label(self.view_details_frame, text=" Date : ", font=("Century Gothic", 10),
                                    bg="gray", fg="white")
        self.date__label_0.place(x=500, y=20)

                                 # =========Entry=========#
        self.view()
        self.com_1 = ttk.Combobox(self.view_details_frame, font=("Calibri", 12), state='readonly', width=40)
        self.com_1['values'] = b
        self.com_1.place(x=50, y=40)

        self.date_0 = Entry(self.view_details_frame, font=("Century Gothic", 12))
        self.date_0.place(x=450, y=40)

        self.date_1 = Entry(self.view_details_frame, font=("Century Gothic", 12))
        self.date_1.place(x=50, y=100)

        self.date_2 = Entry(self.view_details_frame, font=("Century Gothic", 12))
        self.date_2.place(x=300, y=100)

        self.details_new_window_b_0 = Button(self.view_details_frame, text="Show details", height=1,
                                           font=("Century Gothic", 8),
                                           command=self.validation_2)
        self.details_new_window_b_0.place(x=660, y=37)

        self.details_new_window_b_1 = Button(self.view_details_frame, text="Show details", height=1,
                                           font=("Century Gothic", 8),command=self.details_new_window_1)
        self.details_new_window_b_1.place(x=520, y=97)

        #====================================main frame==============================#



        self.dis_super_b = Button(self.tab2, text="new", height=1, font=("Century Gothic", 10),command = self.new_super_button)
        self.dis_super_b.place(x=400, y=190)

        self.dis_mukadam_b = Button(self.tab2, text="new", height=1, font=("Century Gothic", 10),
                                  command=self.new_mukadam_button)
        self.dis_mukadam_b.place(x=400, y=260)



        self.labour_quality_b = Button(self.tab2, text="labour count", height=1, font=("Century Gothic", 10),
                                  command=self.validation,bg = "steel blue",fg = 'white')
        self.labour_quality_b.place(x=170, y=380)

        self.heading_2 = Label(self.tab2,text = "Labour Expences Managment", font=("Corbel Light", 35))
        self.heading_2.place(x=420, y=20)

        self.date = Label(self.tab2,text="Date : " + str(date), font=("Century Gothic", 20), fg="white", bg="Royal blue")
        self.date.place(x=1100, y=40)

        self.date_top_lable = Label(self.tab2, text="Date", font=("Corbel Light", 15)).place(x=20, y=70)
        self.new_site_l = Label(self.tab2, text="Select site", font=("Corbel Light", 15)).place(x=20, y=120)
        self.supervisor = Label(self.tab2, text="Supervisor", font=("Corbel Light", 15)).place(x=20, y=190)
        self.mukadam = Label(self.tab2, text="Mukadam", font=("Corbel Light", 15)).place(x=20, y=260)
        self.labour_type = Label(self.tab2, text="Labour", font=("Corbel Light", 15)).place(x=20, y=330)


        self.date_top = Entry(self.tab2, font=("Century Gothic", 12))
        self.date_top.place(x=130, y=70)
        self.date_top.insert(END,date)

        self.save_b = Button(self.tab2, text=" save ", height=1, font=("Century Gothic", 10),bg = 'sea green',fg ='white',
                             command=self.save_labour)
        self.save_b.place(x=400, y=330)

        self.supervisor_e = ttk.Combobox(self.tab2, font=("Calibri", 12))
        self.supervisor_e['values'] = super_list
        self.supervisor_e.place(x=130, y=190)

        self.mukadam_e = ttk.Combobox(self.tab2, font=("Calibri", 12))
        self.mukadam_e['values'] = mukadam_list
        self.mukadam_e.place(x=130, y=260)

        self.labour_type = ttk.Combobox(self.tab2, font=("Calibri", 12))
        self.labour_type['values'] = ['Regular','Mestri','Other']
        self.labour_type.place(x=130, y=330)

        self.view()
        self.com = ttk.Combobox(self.tab2, font=("Calibri", 12), state='readonly',width = 40)
        self.com['values'] = b
        self.com.place(x=130, y=120)



    def validation(self):
            self.labour_quanity_fuc()

    def validation_2(self):

            self.details_new_window()


    def labour_quanity_fuc(self):
        self.labour_quality_b.place_forget()
        self.name = self.com.get()

        m.execute(F"SELECT * FROM new_tender WHERE final = '{self.name}'")
        self.x = m.fetchall()
        self.ge = self.x[0]

        a = self.ge[4].split()
        self.b = ('_'.join(a))

        self.labour_quality_l = Label(self.tab2, text="Labour quantity", font=("Corbel Light", 15))
        self.labour_quality_l.place(x=20, y=390)

        self.labour_quality_e = Entry(self.tab2, font=("Calibri", 12))
        self.labour_quality_e.place(x=200, y=390)
        self.labour_quality_e.focus()

        self.add_labour_b = Button(self.tab2, text="Add", height=1, font=("Century Gothic", 10),command = self.add_datewise_labour_record)
        self.add_labour_b.place(x=400, y=390)

        la.execute(
            F"CREATE TABLE IF NOT EXISTS {self.b} (id INTEGER PRIMARY KEY , Date DATE,Supervisor TEXT,Mukadam TEXT,Labour_type TEXT,Labour_quantity INTEGER,Amount INTEGER)")

        self.today_date = self.date_top.get()
        supervisor_name = str(self.supervisor_e.get())
        mukadam_name = str(self.mukadam_e.get())
        labour_name = str(self.labour_type.get())
        la.execute(F"INSERT INTO {self.b} (Date,Supervisor,Mukadam,Labour_type) values(?,?,?,?)",
                        (self.today_date, supervisor_name, mukadam_name, labour_name))
        labour.commit()

    def add_datewise_labour_record(self):

        if self.labour_type.get() == "Regular":
            self.regular.append(self.labour_quality_e.get())
        elif self.labour_type.get() == "Mestri":
            self.mestri.append(self.labour_quality_e.get())
        else:
            self.other.append(self.labour_quality_e.get())

        self.labour_quality_e.place_forget()
        self.labour_quality_l.place_forget()
        self.add_labour_b.place_forget()
        self.labour_quality_b = Button(self.tab2, text="labour count", height=1, font=("Century Gothic", 10),
                                       command=self.labour_quanity_fuc,bg = "steel blue",fg = 'white')
        self.labour_quality_b.place(x=170, y=380)

    def save_labour(self):

        for i in self.regular:
            la.execute(F"UPDATE {self.b}  SET Labour_quantity = {i}  WHERE Labour_type = 'Regular'")
            labour.commit()

        for j in self.mestri:
            la.execute(F"UPDATE {self.b}  SET Labour_quantity = {j}  WHERE Labour_type = 'Mestri'")
            labour.commit()

        for k in self.other:
            la.execute(F"UPDATE {self.b}  SET Labour_quantity = {k}  WHERE Labour_type = 'Other'")
            labour.commit()

        #self.la.execute(F"SELECT Labour_quantity FROM {self.b}   WHERE Labour_type = 'Mestri' AND Date = '{self.today_date}'")
        #re = self.la.fetchall()
        #for d in re:
            #print(d)
        a = (' , '.join(self.regular))
        mes = (' , '.join(self.mestri))
        self.show_l = ScrolledText(self.tab2, width=30, height=15, font=("Courier New", 12), bg="black",
                                   fg="lime green")
        self.show_l.place(x=750, y=150)

        final = ("Date :  " + str(date) + "\n\n" + "Site Name :  " + self.ge[4] + "\n\n" + "Tender number :  " + str(
            self.ge[3]) + "\n" + "Supervisor Name :  " + str(self.supervisor_e.get()) + "\n" + "Mukadam Name :  " + str(self.mukadam_e.get()) + "\n" + "Regular Labours :  " + str(a) + "\n" + "Mestri :  " + str(mes))
        self.show_l.insert(END, final)
        self.regular.clear()
        self.mestri.clear()
        self.com.delete(0,END)
        self.supervisor_e.delete(0, END)
        self.mukadam_e.delete(0, END)
        self.labour_type.delete(0, END)

    def details_new_window(self):
        self.de_window = Toplevel(self.master)
        self.app = details_window(self.de_window,self.com_1.get(),self.date_0.get())

    def details_new_window_1(self):
        self.de_window = Toplevel(self.master)
        self.app = details_window_1(self.de_window, self.com_1.get(), self.date_1.get(),self.date_2.get())


        #=================site on tab2 ======================#

    def view(self):
        b.clear()
        m.execute("SELECT final from new_tender")
        s = m.fetchall()
        for i in s:
            x = i[0]
            b.append(x)

    def remove(self):
        if self.com.get() == "":
            c = self.enter.get()
            m.execute("DELETE FROM new_tender WHERE final = ?", (c,))
            mom.commit()
            b.clear()
            self.view()
            self.com = ttk.Combobox(self.tab2, font=("Calibri", 12), state='readonly',width = 40)
            self.com['values'] = b
            self.com.place(x=100, y=120)

            self.com_1 = ttk.Combobox(self.view_details_frame, font=("Calibri", 12), state='readonly', width=40)
            self.com_1['values'] = b
            self.com_1.place(x=200, y=120)

            self.enter.delete(0, END)

        else:
            c = self.com.get()
            m.execute("DELETE FROM new_tender WHERE final = ?", (c,))
            mom.commit()
            b.clear()
            self.view()
            self.com = ttk.Combobox(self.tab2, font=("Calibri", 12),width = 40, state='readonly')
            self.com['values'] = b
            self.com.place(x=100, y=120)

            self.com_1 = ttk.Combobox(self.view_details_frame, font=("Calibri", 12), state='readonly', width=40)
            self.com_1['values'] = b
            self.com_1.place(x=200, y=120)

        # ================= mukadam =====================#

    def mukadam_view(self):
        mukadam_list.clear()
        mu.execute("SELECT m_list FROM mukadam_table")
        re = mu.fetchall()
        for i in re:
            a = i[0]
            mukadam_list.append(a)
            self.mukadam_e = ttk.Combobox(self.tab2, font=("Calibri", 12))
            self.mukadam_e['values'] = mukadam_list
            self.mukadam_e.place(x=130, y=260)

    def add_mukadam(self):
        if self.mukadam_e.get() == "":
            mukadam_list.clear()
            self.add_mukadam_b.place_forget()
            self.remove_mukadam_b.place_forget()
            self.dis_mukadam_b = Button(self.tab2, text="new", height=1, font=("Century Gothic", 10),
                                      command=self.new_mukadam_button)
            self.dis_mukadam_b.place(x=400, y=290)
            self.mukadam_view()
        else:
            mukadam_list.clear()
            s = self.mukadam_e.get()
            mu.execute("INSERT INTO mukadam_table(m_list) values(?)", (s,))
            mukadam.commit()
            self.mukadam_view()
            self.add_mukadam_b.place_forget()
            self.remove_mukadam_b.place_forget()
            self.dis_mukadam_b = Button(self.tab2, text="new", height=1, font=("Century Gothic", 10),
                                        command=self.new_mukadam_button)
            self.dis_mukadam_b.place(x=400, y=290)

    def new_mukadam_button(self):
        self.dis_mukadam_b.place_forget()
        self.add_mukadam_b = Button(self.tab2, text="Add", height=1, font=("Century Gothic", 10), command=self.add_mukadam)
        self.add_mukadam_b.place(x=400, y=290)

        self.remove_mukadam_b = Button(self.tab2, text="remove", height=1, font=("Century Gothic", 10),
                                     command=self.mukadam_remove)
        self.remove_mukadam_b.place(x=470, y=290)

    def mukadam_remove(self):
        mukadam_list.clear()
        n = self.mukadam_e.get()
        mu.execute("DELETE FROM mukadam_table WHERE m_list = ?", (n,))
        mukadam.commit()
        self.add_mukadam_b.place_forget()
        self.remove_mukadam_b.place_forget()
        self.dis_mukadam_b = Button(self.tab2, text="new", height=1, font=("Century Gothic", 10),
                                    command=self.new_mukadam_button)
        self.dis_mukadam_b.place(x=400, y=290)
        self.mukadam_view()



class details_window(Window2):
    def __init__(self,root,ne,date_u):


        self.root = root
        self.root.geometry("1350x750+0+0")
        self.root.title("Site details window")
        self.ne = ne
        self.date_u = date_u
        self.table_view()
    def table_view(self):

        if self.ne == "":
            heading = Label(self.root, text="  Please Enter the Site Name 😐... !", font=("Corbel Light", 50),bg = "LavenderBlush3")
            heading.place(x=220, y=150)
        else:
            self.amount_b = Button(self.root, text="Calculate Amount", height=1, font=("Century Gothic", 10),
                                   command=self.amount_func, bg="green", fg='white')
            self.amount_b.place(x=1000, y=50)
            m.execute(F"SELECT * FROM new_tender WHERE final = '{self.ne}' ")
            x = m.fetchall()
            ge = x[0]

            a = ge[4].split()
            b = ('_'.join(a))
            self.tree_view = ttk.Treeview(self.root,
                                         column=("column1", "column2", "column3", "column4", "column5", "column6", "column7"),
                                         show="headings")
            self.tree_view.heading("#1", text="ID")
            self.tree_view.heading("#2", text="Date")
            self.tree_view.heading("#3", text="Supervisor")
            self.tree_view.heading("#4", text="Mukadam")
            self.tree_view.heading("#5", text="Labour Type")
            self.tree_view.heading("#6", text="Labour Count")
            self.tree_view.heading("#7", text="Amount")
            self.tree_view.place(x=10, y=150)


            if self.date_u == "" :
                heading_1 = Label(self.root, text="Tender Number : " + str(ge[3]), font=("Century Gothic", 15))
                heading_1.place(x=100, y=50)

                heading_2 = Label(self.root, text="Ward Number : " + str(ge[2]), font=("Century Gothic", 15))
                heading_2.place(x=500, y=50)

                heading_3 = Label(self.root, text="Tender Name : " + str(ge[4]), font=("Century Gothic", 15))
                heading_3.place(x=100, y=90)
                la.execute(f"SELECT * from {b} ")
                data = la.fetchall()
                for i in data:
                    self.tree_view.insert("", END, values=i)
                self.tree_view.bind("<Double-1>", self.OnDoubleClick)
                self.sit_name_new = b

            else:
                get = []
                a = self.date_u
                for i in a:
                    if i == "/":
                        get.append('-')
                    else:
                        get.append(i)
                date_me = ("".join(get))
                heading_1 = Label(self.root, text="Tender Number : " + str(ge[3]), font=("Century Gothic", 15))
                heading_1.place(x=100, y=50)

                heading_2 = Label(self.root, text="Ward Number : " + str(ge[2]), font=("Century Gothic", 15))
                heading_2.place(x=500, y=50)

                heading_3 = Label(self.root, text="Tender Name : " + str(ge[4]), font=("Century Gothic", 15))
                heading_3.place(x=100, y=90)

                la.execute(f"SELECT * from {b} WHERE Date = '{date_me}'")
                data = la.fetchall()
                for i in data:
                    self.tree_view.insert("", END, values=i)
                self.tree_view.bind("<Double-1>", self.OnDoubleClick)

                self.sit_name_new = b
    def amount_func(self):

        if self.date_u == "" :
            amo = la.execute(f"SELECT SUM(Amount) FROM {self.sit_name_new}")
            for i in amo:
                i = i
            self.Total_charge = i[0]
            self.Total_charge = format_currency( self.Total_charge, 'INR', locale='en_IN')
            print(self.Total_charge)
            self.Total_amount_l = Label(self.root, text=" Total Labour Charge : " + str(self.Total_charge),
                                        font=("Century Gothic", 20, "bold"), bg="Green", fg="white")
            self.Total_amount_l.place(x=450, y=400)
        else:
            amo = la.execute(f"SELECT SUM(Amount) FROM {self.sit_name_new} WHERE Date = '{self.date_u}'")
            for i in amo:
                i = i
            self.Total_charge = i[0]
            print(self.Total_charge)
            self.Total_amount_l = Label(self.root, text=" Total Labour Charge : " + str(self.Total_charge),
                                        font=("Century Gothic", 20, "bold"), bg="Green", fg="white")
            self.Total_amount_l.place(x=450, y=400)


    def OnDoubleClick(self, event):
        try:
            self.update_b.place_forget()
        except:
            pass
        row = self.tree_view.focus()
        get = self.tree_view.item(row)
        self.show = get['values']

        self.update_b = Button(self.root, text="Update", height=1, font=("Century Gothic", 10),
                                       command=self.update_fun, bg="steel blue", fg='white')
        self.update_b.place(x=600, y=400)

    def update_fun(self):
        self.update_b.place_forget()
        self.date_update_l = Label(self.root, text="Date", font=("Corbel Light", 13))
        self.date_update_l.place(x=20, y=420)

        self.super_update_l = Label(self.root, text="Supervisor", font=("Corbel Light", 13))
        self.super_update_l.place(x=20, y=480)

        self.mukadam_update_l = Label(self.root, text="Mukadam", font=("Corbel Light", 13))
        self.mukadam_update_l.place(x=20, y=540)

        self.labour_type_update_l = Label(self.root, text="Labour Type", font=("Corbel Light", 13))
        self.labour_type_update_l.place(x=600, y=420)

        self.labour_count_update_l = Label(self.root, text="Labour Count", font=("Corbel Light", 13))
        self.labour_count_update_l.place(x=600, y=480)

        self.amount_update_l = Label(self.root, text="Amount", font=("Corbel Light", 13))
        self.amount_update_l.place(x=600, y=540)

        self.date_update_e = Entry(self.root, font=("Century Gothic", 15))
        self.date_update_e.place(x=130, y=420)
        self.date_update_e.insert(END, self.show[1])

        self.super_update_e = Entry(self.root, font=("Century Gothic", 15))
        self.super_update_e.place(x=130, y=480)
        self.super_update_e.insert(END, self.show[2])

        self.mukadam_update_e = Entry(self.root, font=("Century Gothic", 15))
        self.mukadam_update_e.place(x=130, y=540)
        self.mukadam_update_e.insert(END, self.show[3])

        self.labour_type_update_e = Entry(self.root, font=("Century Gothic", 15))
        self.labour_type_update_e.place(x=710, y=420)
        self.labour_type_update_e.insert(END, self.show[4])

        self.labour_count_update_e = Entry(self.root, font=("Century Gothic", 15))
        self.labour_count_update_e.place(x=710, y=480)
        self.labour_count_update_e.insert(END, self.show[5])

        self.amount_update_e = Entry(self.root, font=("Century Gothic", 15))
        self.amount_update_e.place(x=710, y=540)
        self.amount_update_e.insert(END, self.show[6])

        self.update_all_b = Button(self.root, text="Update All ", height=1, font=("Century Gothic", 10),
                                           command=self.update_all_func, bg="steel blue", fg='white')
        self.update_all_b.place(x=1000, y=480)

    def update_all_func(self):

        add = F" UPDATE {self.sit_name_new} SET Date = ?, Supervisor = ? ,Mukadam = ? ,Labour_type = ?, Labour_quantity = ?, Amount = ? WHERE  ID = ?"
        la.execute(add, (self.date_update_e.get(), self.super_update_e.get(), self.mukadam_update_e.get(),
                                 self.labour_type_update_e.get(), self.labour_count_update_e.get(),
                                 self.amount_update_e.get(), self.show[0]))
        labour.commit()
        self.table_view()
        self.date_update_e.place_forget()
        self.date_update_l.place_forget()
        self.mukadam_update_l.place_forget()
        self.mukadam_update_e.place_forget()
        self.super_update_e.place_forget()
        self.super_update_l.place_forget()
        self.labour_type_update_l.place_forget()
        self.labour_type_update_e.place_forget()
        self.labour_count_update_e.place_forget()
        self.labour_count_update_l.place_forget()
        self.amount_update_l.place_forget()
        self.amount_update_e.place_forget()
        self.update_all_b.place_forget()

class details_window_1(Window2):

    def __init__(self,bot,sit_name,date_1,date_2):

        self.bot = bot
        self.bot.geometry("1350x750+0+0")
        self.bot.title("details window")
        self.sit_name = sit_name
        self.date_1_new = date_1
        self.date_2_new = date_2

        self.table_view()

    def table_view(self):
        self.cal = []
        if self.date_2_new == "" and self.date_1_new == "":
            heading = Label(self.bot, text="Please Enter the dates", font=("Corbel Light", 50),bg = "LavenderBlush3")
            heading.place(x=420, y=50)
        if self.sit_name == "":
            heading = Label(self.bot, text="  Please Enter the Site Name 😐... !", font=("Corbel Light", 50),bg = "LavenderBlush3")
            heading.place(x=220, y=150)
        else:
            self.amount_b = Button(self.bot, text="Calculate Amount", height=1, font=("Century Gothic", 10),
                                   command=self.amount_func_2_dates, bg="green", fg='white')
            self.amount_b.place(x=1000, y=50)
            m.execute(F"SELECT * FROM new_tender WHERE final = '{self.sit_name}' ")
            x = m.fetchall()
            ge = x[0]

            a = ge[4].split()
            b = ('_'.join(a))
            self.tree_view = ttk.Treeview(self.bot,
                                         column=("column1", "column2", "column3", "column4", "column5", "column6", "column7"),
                                         show="headings")
            self.tree_view.heading("#1", text="ID")
            self.tree_view.heading("#2", text="Date")
            self.tree_view.heading("#3", text="Supervisor")
            self.tree_view.heading("#4", text="Mukadam")
            self.tree_view.heading("#5", text="Labour Type")
            self.tree_view.heading("#6", text="Labour Count")
            self.tree_view.heading("#7", text="Amount")
            self.tree_view.place(x=10, y=150)



            if b == "":
                heading = Label(self.bot, text="Please  the Site Name", font=("Corbel Light", 50))
                heading.place(x=420, y=50)

            else:
                heading_1 = Label(self.bot, text="Tender Number : " + str(ge[3]), font=("Century Gothic", 15),bg = "steel blue")
                heading_1.place(x=100, y=50)

                heading_2 = Label(self.bot, text="Ward Number : " + str(ge[2]), font=("Century Gothic", 15))
                heading_2.place(x=500, y=50)

                heading_3 = Label(self.bot, text="Tender Name : " + str(ge[4]), font=("Century Gothic", 15))
                heading_3.place(x=100, y=90)

                la.execute(f"SELECT * from {b} WHERE Date BETWEEN '{self.date_1_new}' and '{self.date_2_new}'")
                data = la.fetchall()
                for i in data:
                    self.tree_view.insert("", END, values=i)
                    num= i[6]


                    if type(num) == int:
                        self.cal.append(num)


                self.tree_view.bind("<Double-1>", self.OnDoubleClick)

                self.sit_name_new = b



    def amount_func_2_dates(self):
        a = sum(self.cal)
        self.go = format_currency(a, 'INR', locale='en_IN')
        self.Total_amount_l = Label(self.bot, text=" Total Labour Charge : " + str(self.go),
                                    font=("Century Gothic", 20, "bold"), bg="Green", fg="white")
        self.Total_amount_l.place(x=450, y=400)
        self.cal.clear()

    def OnDoubleClick(self, event):
        row = self.tree_view.focus()
        get = self.tree_view.item(row)
        self.show = get['values']
        print(self.show[0],self.sit_name)
        self.update_b = Button(self.bot, text="Update", height=1, font=("Century Gothic", 10),
                                  command = self.update_fun,bg = "steel blue",fg = 'white')
        self.update_b.place(x=600, y=400)


    def update_fun(self):
        self.update_b.place_forget()
        self.date_update_l = Label(self.bot, text="Date", font=("Corbel Light", 13))
        self.date_update_l.place(x=20, y=420)

        self.super_update_l = Label(self.bot, text="Supervisor", font=("Corbel Light", 13))
        self.super_update_l.place(x=20, y=480)

        self.mukadam_update_l = Label(self.bot, text="Mukadam", font=("Corbel Light", 13))
        self.mukadam_update_l.place(x=20, y=540)

        self.labour_type_update_l = Label(self.bot, text="Labour Type", font=("Corbel Light", 13))
        self.labour_type_update_l.place(x=600, y=420)

        self.labour_count_update_l = Label(self.bot, text="Labour Count", font=("Corbel Light", 13))
        self.labour_count_update_l.place(x=600, y=480)

        self.amount_update_l = Label(self.bot, text="Amount", font=("Corbel Light", 13))
        self.amount_update_l.place(x=600, y=540)

        self.date_update_e = Entry(self.bot, font=("Century Gothic", 15))
        self.date_update_e.place(x=130, y=420)
        self.date_update_e.insert(END,self.show[1])

        self.super_update_e = Entry(self.bot, font=("Century Gothic", 15))
        self.super_update_e.place(x=130, y=480)
        self.super_update_e.insert(END,self.show[2])

        self.mukadam_update_e = Entry(self.bot,  font=("Century Gothic", 15))
        self.mukadam_update_e.place(x=130, y=540)
        self.mukadam_update_e.insert(END,self.show[3])

        self.labour_type_update_e = Entry(self.bot, font=("Century Gothic", 15))
        self.labour_type_update_e.place(x=710, y=420)
        self.labour_type_update_e.insert(END,self.show[4])

        self.labour_count_update_e = Entry(self.bot,font=("Century Gothic", 15))
        self.labour_count_update_e.place(x=710, y=480)
        self.labour_count_update_e.insert(END,self.show[5])

        self.amount_update_e = Entry(self.bot, font=("Century Gothic", 15))
        self.amount_update_e.place(x=710, y=540)
        self.amount_update_e.insert(END,self.show[6])

        self.update_all_b = Button(self.bot, text="Update All ", height=1, font=("Century Gothic", 10),
                                command = self.update_all_func,bg="steel blue", fg='white')
        self.update_all_b.place(x=1000, y=480)

    def update_all_func(self):


        add = F" UPDATE {self.sit_name_new} SET Date = ?, Supervisor = ? ,Mukadam = ? ,Labour_type = ?, Labour_quantity = ?, Amount = ? WHERE  ID = ?"
        la.execute(add,(self.date_update_e.get(),self.super_update_e.get(),self.mukadam_update_e.get(),self.labour_type_update_e.get(),self.labour_count_update_e.get(),self.amount_update_e.get(),self.show[0]))
        labour.commit()
        self.table_view()
        self.date_update_e.place_forget()
        self.date_update_l.place_forget()
        self.mukadam_update_l.place_forget()
        self.mukadam_update_e.place_forget()
        self.super_update_e.place_forget()
        self.super_update_l.place_forget()
        self.labour_type_update_l.place_forget()
        self.labour_type_update_e.place_forget()
        self.labour_count_update_e.place_forget()
        self.labour_count_update_l.place_forget()
        self.amount_update_l.place_forget()
        self.amount_update_e.place_forget()
        self.update_all_b.place_forget()



if __name__ == '__main__':
    main()
