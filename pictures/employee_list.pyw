from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import hashlib
import mysql.connector
from PIL import ImageTk, Image
def employees_list_page():
    employee_list=Toplevel()
    def hashing(text):
        text=text.encode('utf-8')
        result = hashlib.md5(text).hexdigest()
        return result
    fnt= ('Helvetica 15 bold')
    sv7=StringVar()
    sv8=StringVar()
    sv9=StringVar()
    sv10=StringVar()
    sv11=StringVar()
    w = 1920
    h = 1080
    sw = employee_list.winfo_screenwidth()
    sh = employee_list.winfo_screenheight()
    x = (sw-w)/2+180
    y = (sh-h)/2+105
    employee_list.geometry(('%dx%d+%d+%d') % (w, h, x, y))
    employee_list.config(bg='#83A3AD')
    employee_list.title('Employees List')
    employee_list.resizable(True,False)
    employee_list.iconbitmap('pictures\\supermarket.ico')
    lbl0=Label(employee_list,text='Employees List',bg='#83A3AD',font=('Helvetica 35 bold')).place(relx=.35,rely=.001)
    frame0=LabelFrame(employee_list,text='Employees',bg='#eeeeee',width=720,border=3,height=600,font=fnt).place(x=20,y=110)
    lbl1=Label(frame0,text="ID",font=fnt,bg="#EEEEEE").place(x=80,y=170)
    en1=Entry(frame0,fg='navy',textvariable=sv7,width=37,font=5)
    en1.place(x=250,y=170)
    en1.focus()
    lbl2=Label(frame0,text="Name",font=fnt,bg="#EEEEEE").place(x=80,y=270)
    en2=Entry(frame0,fg='navy',textvariable=sv8,width=37,font=5)
    en2.place(x=250,y=270)
    lbl3=Label(frame0,text="Password",font=fnt,bg="#EEEEEE").place(x=80,y=370)
    lbl4=Label(frame0,text="phone",font=fnt,bg="#EEEEEE").place(x=80,y=470)
    en3=Entry(frame0,fg='navy',textvariable=sv9,width=37,font=5)
    en3.place(x=250,y=370)
    en4=Entry(frame0,fg='navy',textvariable=sv10,width=37,font=5)
    en4.place(x=250,y=470)
    lbl5=Label(frame0,text="Address",font=fnt,bg="#EEEEEE").place(x=80,y=570)
    en5=Entry(frame0,fg='navy',textvariable=sv11,width=37,font=5)
    en5.place(x=250,y=570)
    img=Image.open('pictures//roundedbutton.png')
    img1=img.resize((200,60))
    image=ImageTk.PhotoImage(img1)
    img2=img.resize((270,60))
    image2=ImageTk.PhotoImage(img2)
    connecet=mysql.connector.connect(host='localhost',user='usr',password='123456789',database='supermarket')
    my_cursor=connecet.cursor()
    style=ttk.Style()
    style.theme_use("alt")
    style.configure("Treeview",font="Verdana 11",background="FFFFFF",foreground="navy",rowheight=50,rowwdith=20)
    mytree=ttk.Treeview(employee_list,style='Treeview', columns = ('ID','Name','Password','phone','Address'), show = 'headings', selectmode ='browse',height="300")
    mytree['columns']=("ID","Name","Password","Phone","Address")
    mytree.column("#0",width=0,minwidth=0,anchor='w')
    mytree.column("#1",width=50,minwidth=25,anchor='w')
    mytree.column("#2",width=155,minwidth=25,anchor='w')
    mytree.column("#3",width=320,minwidth=25,anchor='w')
    mytree.column("#4",width=130,minwidth=25,anchor='w')
    mytree.column("#5",width=120,minwidth=25,anchor='w')
    mytree.heading("#0",text='',anchor='center')
    mytree.heading("#1",text='ID',anchor='center')
    mytree.heading("#2",text='Name',anchor='center')
    mytree.heading("#3",text='Password',anchor='center')
    mytree.heading("#4",text='Phone',anchor='center')
    mytree.heading("#5",text='Address',anchor='center')
    my_cursor.execute('select * from employees;')
    data=my_cursor.fetchall()
    for i in data:
        mytree.insert('','end',values=(i))
    scroll=Scrollbar(employee_list,orient='vertical',width=20,bg='green')
    scroll.config(command=mytree.yview)
    scroll.place(x=1513,y=110,height=650)
    scroll2=Scrollbar(employee_list,orient='horizontal')
    scroll2.config(command=mytree.xview)
    scroll2.place(x=754,y=740,height=20,width=750)
    mytree.place(x=750,y=90,height=670)
    def clear_all():
        for item in mytree.get_children():
            mytree.delete(item)
    def search():
        global my_cursor
        global mytree
        global data
        global clear_all
        clear_all()
        if sv7.get()=='':
            messagebox.showerror('error','enter ID')
            en1.focus()
        else:
            clear_all()
            my_cursor.execute("select * from employees where employee_id='%s' ;"%(sv7.get()))
            data=my_cursor.fetchall()
        for i in data:
            mytree.insert('','end',values=(i))
    def add_item():
        if sv7.get()=='':
            messagebox.showerror('error','enter ID')
            en1.focus()
        elif sv8.get()=='':
            messagebox.showerror('error','enter Name')
            en2.focus()
        elif sv9.get()=='':
            messagebox.showerror('error','enter Password')
            en3.focus()
        elif sv10.get()=='':
            messagebox.showerror('error','enter Phone')
            en4.focus()
        elif sv11.get()=='':
            messagebox.showerror('error','enter Address')
            en5.focus()
        else:
            global connecet
            global hashing
            global mytree
            global data
            global clear_all
            clear_all()
            connecet2=mysql.connector.connect(host='localhost',user='usr',password='123456789',database='supermarket')
            my_cursor2=connecet2.cursor()
            my_cursor2.execute("insert into employees values ('%s','%s','%s','%s','%s')"%(sv7.get(),sv8.get(),hashing(sv9.get()),sv10.get(),sv11.get()))
            connecet2.commit()
            my_cursor2.execute("select * from employees")
            data2=my_cursor2.fetchall()
            for x in data2:
                mytree.insert('','end',values=(x))
            messagebox.showinfo('','New employee has been added')
            sv7.set('')
            sv8.set('')
            sv9.set('')
            sv10.set('')
            sv11.set('')
            en1.focus()
    def remove_item():
        global mytree
        global clear_all
        clear_all()
        connecet3=mysql.connector.connect(host='localhost',user='usr',password='123456789',database='supermarket')
        my_cursor3=connecet3.cursor()
        if sv7.get()=='':
            messagebox.showerror('Error','Enter ID')
        else:
            my_cursor3.execute("DELETE FROM EMPLOYEES WHERE employee_id ='%s'"%(sv7.get()))
            connecet3.commit()
            my_cursor3.execute("SELECT * FROM EMPLOYEES ")
            data3=my_cursor3.fetchall()
            for a in data3:
                mytree.insert('','end',values=(a))
            messagebox.showinfo('','Employee has been removed')
    def edit_item():
        connecet4=mysql.connector.connect(host='localhost',user='usr',password='123456789',database='supermarket')
        my_cursor4=connecet4.cursor()
        if sv7.get()=='':
            messagebox.showerror('error','enter ID')
            en1.focus()
        else:
            global mytree
            global clear_all
            clear_all()
            my_cursor4.execute("UPDATE EMPLOYEES SET employee_name ='%s' WHERE employee_id='%s'"%(sv8.get(),sv7.get()))
            my_cursor4.execute("UPDATE EMPLOYEES SET employee_password ='%s' WHERE employee_id='%s'"%(hashing(sv9.get()),sv7.get()))
            my_cursor4.execute("UPDATE EMPLOYEES SET employee_phone ='%s' WHERE employee_id='%s'"%(sv10.get(),sv7.get()))
            my_cursor4.execute("UPDATE EMPLOYEES SET address ='%s' WHERE employee_id='%s'"%(sv11.get(),sv7.get()))
            connecet4.commit()
            my_cursor4.execute("SELECT * FROM EMPLOYEES ")
            data3=my_cursor4.fetchall()
            for a in data3:
                mytree.insert('','end',values=(a))
            messagebox.showinfo('','Data has been changed')
            sv7.set('')
            sv8.set('')
            sv9.set('')
            sv10.set('')
            sv11.set('')
            en1.focus()
    def exit():
        employee_list.destroy()
    btn=Button(employee_list,text='Search',image=image,width=120,height=60,border=0,font=fnt,fg='white',cursor='hand2',compound='center',command=search).place(x=30,y=630)
    btn=Button(employee_list,text='Add',image=image,width=120,height=60,border=0,font=fnt,fg='white',cursor='hand2',compound='center',command=add_item).place(x=160,y=630)
    btn=Button(employee_list,text='Remove',image=image2,width=180,height=60,border=0,font=fnt,fg='white',cursor='hand2',compound='center',command=remove_item).place(x=280,y=630)
    btn=Button(employee_list,text='Edit',image=image,width=150,height=60,border=0,font=fnt,fg='white',cursor='hand2',compound='center',command=edit_item).place(x=450,y=630)
    btn=Button(employee_list,text='Exit',image=image,width=120,height=60,border=0,font=fnt,fg='white',cursor='hand2',compound='center',command=exit).place(x=600,y=630)
    employee_list.mainloop()