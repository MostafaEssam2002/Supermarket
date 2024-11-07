from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import hashlib
from time import strftime
import time
from PIL import ImageTk, Image
try:
    connect=mysql.connector.connect(host='localhost',user='usr',password='123456789',database='supermarket')
    my_cursor=connect.cursor()
    sum=0
    def clear_all():
        global mytree
        for item in mytree.get_children():
            mytree.delete(item)
    def clear_all2():
        global mytree2
        for item in mytree2.get_children():
            mytree2.delete(item)
    def hashing(text):
        text=text.encode('utf-8')
        result = hashlib.md5(text).hexdigest()
        return result
    def admin_button():
        def admin_page():
            def inventory_page():
                global mytree2
                global clear_all2
                inventory=Toplevel()
                fnt= ('Helvetica 15 bold')
                sv11=StringVar()
                sv12=StringVar()
                sv13=StringVar()
                sv14=StringVar()
                inventory.state('zoomed')
                inventory.iconbitmap('pictures//inventory.ico')
                inventory.config(bg='#5D534A')
                inventory.title('Inventory')
                lbl0=Label(inventory,text='inventory',bg='#5D534A',font=('Helvetica 35 bold')).place(relx=.45,rely=.001)
                frame0=LabelFrame(inventory,text='Items',bg='#eeeeee',width=720,border=3,height=600,font=fnt).place(x=20,y=110)
                lbl1=Label(inventory,text="ID",font=fnt,bg="#EEEEEE").place(x=80,y=200)
                en1=Entry(inventory,fg='navy',textvariable=sv11,width=37,font=5)
                en1.place(x=250,y=200)
                en1.focus()
                lbl2=Label(inventory,text="Item",font=fnt,bg="#EEEEEE").place(x=80,y=300)
                en2=Entry(inventory,fg='navy',textvariable=sv12,width=37,font=5)
                en2.place(x=250,y=300)
                lbl3=Label(inventory,text="In Stock",font=fnt,bg="#EEEEEE").place(x=80,y=400)
                lbl4=Label(inventory,text="Price",font=fnt,bg="#EEEEEE").place(x=80,y=500)
                en3=Entry(inventory,fg='navy',textvariable=sv13,width=37,font=5)
                en3.place(x=250,y=400)
                en4=Entry(inventory,fg='navy',textvariable=sv14,width=37,font=5)
                en4.place(x=250,y=500)
                img=Image.open('pictures//roundedbutton.png')
                img1=img.resize((200,60))
                image=ImageTk.PhotoImage(img1)
                img2=img.resize((270,60))
                image2=ImageTk.PhotoImage(img2)
                style=ttk.Style()
                style.theme_use("alt")
                style.configure("Treeview",font="Verdana 15",background="FFFFFF",foreground="navy",rowheight=50)
                mytree2=ttk.Treeview(inventory,style='Treeview')
                mytree2['columns']=("item_id","item","in_stock","price")
                mytree2.column("#0",width=0,minwidth=0,anchor='center')
                mytree2.column("#1",width=187,minwidth=25,anchor='center')
                mytree2.column("#2",width=187,minwidth=25,anchor='center')
                mytree2.column("#3",width=187,minwidth=25,anchor='center')
                mytree2.column("#4",width=187,minwidth=25,anchor='center')
                mytree2.heading("#0",text='',anchor='center')
                mytree2.heading("#1",text='item_id',anchor='center')
                mytree2.heading("#2",text='item',anchor='center')
                mytree2.heading("#3",text='in_stock',anchor='center')
                mytree2.heading("#4",text='price',anchor='center')
                connecet1=mysql.connector.connect(host='localhost',user='usr',password='123456789',database='supermarket')
                my_cursor1=connecet1.cursor()
                my_cursor1.execute("select * from inventory ;")
                data1=my_cursor1.fetchall()
                for s in data1:
                    mytree2.insert('','end',values=(s))
                mytree2.place(x=750,y=90,height=670)
                scroll=Scrollbar(inventory,orient='vertical',width=20,bg='green',command=mytree2.yview)
                scroll.place(x=1480,y=110,height=650)
                def search():
                    global mytree2
                    global data
                    global clear_all2
                    if sv11.get()=='':
                        messagebox.showerror('error','enter ID')
                        en1.focus()
                    else:
                        clear_all2()
                        connecet0=mysql.connector.connect(host='localhost',user='usr',password='123456789',database='supermarket')
                        my_cursor0=connecet0.cursor()
                        my_cursor0.execute("select * from inventory where id='%s' ;"%(sv11.get()))
                        data10=my_cursor0.fetchall()
                        for i in data10:
                            mytree2.insert('','end',values=(i))
                def add_item():
                    if sv11.get()=='':
                        messagebox.showerror('error','enter ID')
                        en1.focus()
                    elif sv12.get()=='':
                        messagebox.showerror('error','enter Name')
                        en2.focus()
                    elif sv13.get()=='':
                        messagebox.showerror('error','enter Password')
                        en3.focus()
                    elif sv14.get()=='':
                        messagebox.showerror('error','enter Phone')
                        en4.focus()
                    else:
                        global mytree2
                        global clear_all2
                        clear_all2()
                        connecet2=mysql.connector.connect(host='localhost',user='usr',password='123456789',database='supermarket')
                        my_cursor2=connecet2.cursor()
                        my_cursor2.execute("insert into inventory values ('%s','%s','%s','%s')"%(sv11.get(),sv12.get(),sv13.get(),sv14.get()))
                        connecet2.commit()
                        my_cursor2.execute("select * from inventory")
                        data2=my_cursor2.fetchall()
                        for x in data2:
                            mytree2.insert('','end',values=(x))
                        messagebox.showinfo('','New item has been added')
                        sv11.set('')
                        sv12.set('')
                        sv13.set('')
                        sv14.set('')
                        en1.focus()
                def remove_item():
                        connecet3=mysql.connector.connect(host='localhost',user='usr',password='123456789',database='supermarket')
                        my_cursor3=connecet3.cursor()
                        if sv11.get()=='':
                            messagebox.showerror('Error','Enter ID')
                        else:
                            global mytree2
                            global clear_all2
                            my_cursor3.execute("DELETE FROM inventory WHERE id ='%s'"%(sv11.get()))
                            connecet3.commit()
                            my_cursor3.execute("SELECT * FROM inventory ")
                            data3=my_cursor3.fetchall()
                            for b in data3:
                                mytree2.insert('','end',values=(b))
                            sv11.set('')
                            messagebox.showinfo('','item has been removed')
                def edit_item():
                    connecet4=mysql.connector.connect(host='localhost',user='usr',password='123456789',database='supermarket')
                    my_cursor4=connecet4.cursor()
                    if sv11.get()=='':
                        messagebox.showerror('error','enter ID')
                        en1.focus()
                    else:
                        global mytree2
                        global clear_all2
                        clear_all2()
                        my_cursor4.execute("UPDATE inventory SET item ='%s' WHERE id='%s'"%(sv12.get(),sv11.get()))
                        my_cursor4.execute("UPDATE inventory SET quantity ='%s' WHERE id='%s'"%(sv13.get(),sv11.get()))
                        my_cursor4.execute("UPDATE inventory SET price ='%s' WHERE id='%s'"%(sv14.get(),sv11.get()))
                        connecet4.commit()
                        my_cursor4.execute("SELECT * FROM inventory ")
                        data3=my_cursor4.fetchall()
                        for a in data3:
                            mytree2.insert('','end',values=(a))
                        messagebox.showinfo('','Data has been changed')
                        sv11.set('')
                        sv12.set('')
                        sv13.set('')
                        sv14.set('')
                        en1.focus()
                def exi4():
                    inventory.destroy()
                    admin_form.state('zoomed')
                btn_search=Button(inventory,text='Search',image=image,width=120,height=60,border=0,font=fnt,fg='white',cursor='hand2',compound='center',command=search)
                btn_search.place(x=30,y=630)
                btn_add_item=Button(inventory,text='Add Item',image=image,width=120,height=60,border=0,font=fnt,fg='white',cursor='hand2',compound='center',command=add_item)
                btn_add_item.place(x=160,y=630)
                btn_remove_item=Button(inventory,text='Remove Item',image=image2,width=180,height=60,border=0,font=fnt,fg='white',cursor='hand2',compound='center',command=remove_item)
                btn_remove_item.place(x=280,y=630)
                btn_edit_item=Button(inventory,text='Edit Item',image=image,width=150,height=60,border=0,font=fnt,fg='white',cursor='hand2',compound='center',command=edit_item)
                btn_edit_item.place(x=450,y=630)
                btn_exit=Button(inventory,text='Exit',image=image,width=120,height=60,border=0,font=fnt,fg='white',cursor='hand2',compound='center',command=exi4)
                btn_exit.place(x=600,y=630)
                inventory.mainloop()
            def employees_list_page():
                employee_list=Toplevel()
                fnt= ('Helvetica 15 bold')
                global mytree
                global hashing
                sv7=StringVar()
                sv8=StringVar()
                sv9=StringVar()
                sv10=StringVar()
                sv11=StringVar()
                employee_list.state('zoomed')
                employee_list.config(bg='#83A3AD')
                employee_list.title('Employees List')
                employee_list.resizable(True,False)
                employee_list.iconbitmap('pictures\\supermarket.ico')
                lbl0=Label(employee_list,text='Employees List',bg='#83A3AD',font=('Helvetica 35 bold'))
                lbl0.place(relx=.35,rely=.001)
                frame0=LabelFrame(employee_list,text='Employees',bg='#eeeeee',width=720,border=3,height=600,font=fnt).place(x=20,y=110)
                lbl1=Label(employee_list,text="ID",font=fnt,bg="#EEEEEE")
                lbl1.place(x=80,y=170)
                en1=Entry(employee_list,fg='navy',textvariable=sv7,width=37,font=5)
                en1.place(x=250,y=170)
                en1.focus()
                lbl2=Label(employee_list,text="Name",font=fnt,bg="#EEEEEE")
                lbl2.place(x=80,y=270)
                en2=Entry(employee_list,fg='navy',textvariable=sv8,width=37,font=5)
                en2.place(x=250,y=270)
                lbl3=Label(employee_list,text="Password",font=fnt,bg="#EEEEEE")
                lbl3.place(x=80,y=370)
                lbl4=Label(employee_list,text="phone",font=fnt,bg="#EEEEEE")
                lbl4.place(x=80,y=470)
                en3=Entry(employee_list,fg='navy',textvariable=sv9,width=37,font=5)
                en3.place(x=250,y=370)
                en4=Entry(employee_list,fg='navy',textvariable=sv10,width=37,font=5)
                en4.place(x=250,y=470)
                lbl5=Label(employee_list,text="Address",font=fnt,bg="#EEEEEE")
                lbl5.place(x=80,y=570)
                en5=Entry(employee_list,fg='navy',textvariable=sv11,width=37,font=5)
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
                        global hashing
                        global mytree
                        global data
                        global clear_all
                        clear_all()
                        connecet2=mysql.connector.connect(host='localhost',user='usr',password='123456789',database='supermarket')
                        my_cursor2=connecet2.cursor()
                        my_cursor2.execute("insert into employees values ('%s','%s','%s','%s','%s')"%(sv7.get(),sv8.get(),hashing(sv9.get()),sv10.get(),sv11.get()))
                        connecet2.commit()
                        connecet3=mysql.connector.connect(host='localhost',user='usr',password='123456789',database='supermarket')
                        my_cursor3=connecet3.cursor()
                        my_cursor3.execute("select * from employees")
                        data3=my_cursor3.fetchall()
                        for x in data3:
                            mytree.insert('','end',values=(x))
                        messagebox.showinfo('','New employee has been added')
                        sv7.set('')
                        sv8.set('')
                        sv9.set('')
                        sv10.set('')
                        sv11.set('')
                        en1.focus()
                def search():
                    global mytree
                    global data
                    global clear_all
                    # clear_all()
                    if sv7.get()=='':
                        messagebox.showerror('error','enter ID')
                        en1.focus()
                    else:
                        clear_all()
                        my_cursor.execute("select * from employees where employee_id='%s' ;"%(sv7.get()))
                        data=my_cursor.fetchall()
                    for i in data:
                        mytree.insert('','end',values=(i))
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
                        sv7.set('')
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
                    admin_form.state('zoomed')
                btn=Button(employee_list,text='Search',image=image,width=120,height=60,border=0,font=fnt,fg='white',cursor='hand2',compound='center',command=search).place(x=30,y=630)
                btn=Button(employee_list,text='Add',image=image,width=120,height=60,border=0,font=fnt,fg='white',cursor='hand2',compound='center',command=add_item).place(x=160,y=630)
                btn=Button(employee_list,text='Remove',image=image2,width=180,height=60,border=0,font=fnt,fg='white',cursor='hand2',compound='center',command=remove_item).place(x=280,y=630)
                btn=Button(employee_list,text='Edit',image=image,width=150,height=60,border=0,font=fnt,fg='white',cursor='hand2',compound='center',command=edit_item).place(x=450,y=630)
                btn=Button(employee_list,text='Exit',image=image,width=120,height=60,border=0,font=fnt,fg='white',cursor='hand2',compound='center',command=exit).place(x=600,y=630)
                employee_list.mainloop()
            admin_form=Tk()
            fnt= ('Helvetica 15 bold')
            admin_form.state('zoomed')
            admin_form.config(bg='#FFFFFF')
            admin_form.iconbitmap('pictures//supermarket.ico')
            admin_form.title('Admin page')
            image=Image.open("pictures//supermarket.jpg")
            bck=ImageTk.PhotoImage(image)
            lbl=Label(admin_form,image=bck)
            lbl.place(x=-1,y=0)
            image = Image.open('pictures//inventory.jpg')
            image = image.resize((150,150))
            image_btn1= ImageTk.PhotoImage(image)
            def btn1():
                admin_form.iconify()
                inventory_page()
            btn1=Button(admin_form,text='Inventory',image=image_btn1,border=1,font=fnt,command=btn1,compound='top').place(relx=0.6, rely=0.5, anchor=CENTER)
            def btn2():
                admin_form.iconify()
                employees_list_page()
            image2 = Image.open('pictures//employees.png')
            image2 = image2.resize((150,100))
            image_btn2= ImageTk.PhotoImage(image2)
            btn2=Button(admin_form,text='employees',image=image_btn2,command=btn2,border=1,font=('Helvetica 20 bold'),compound='top').place(relx=0.4, rely=0.5, anchor=CENTER)
            admin_form.mainloop()
        def clear_all():
            global mytree
            for item in mytree.get_children():
                mytree.delete(item)
        def clear_all2():
            global mytree2
            for item in mytree2.get_children():
                mytree2.delete(item)
        def hashing(text):
            text=text.encode('utf-8')
            result = hashlib.md5(text).hexdigest()
            return result
        # def login(title):
        def hashing(text):
            text=text.encode('utf-8')
            result = hashlib.md5(text).hexdigest()
            return result
        admin_login_form=Toplevel()
        fnt= ('Helvetica 15 bold')
        w = 280
        h = 320
        sw = admin_login_form.winfo_screenwidth()
        sh = admin_login_form.winfo_screenheight()
        x = (sw-w)/2+60
        y = (sh-h)/2+30
        admin_login_form.iconbitmap('pictures//login-icon.ico')
        admin_login_form.title('Admin Login')
        admin_login_form.resizable(False,False)
        admin_login_form.geometry(('%dx%d+%d+%d') % (w, h, x, y))
        sv3=StringVar() 
        sv4=StringVar()
        lbl=Label(admin_login_form,text='User name',font=5).place(x=20,y=10)
        img = Image.open('pictures//username.png')
        img = img.resize((50,50))
        image_lbl= ImageTk.PhotoImage(img)
        lbl=ttk.Label(admin_login_form,image=image_lbl,text='User name',font=5)
        lbl.place(x=10,y=40)
        en1=Entry(admin_login_form,textvariable=sv3,width=19,fg='navy',font=fnt)
        en1.place(x=60,y=59)
        #=========================================================================
        passlbl=Label(admin_login_form,text='password',font=5).place(x=20,y=110)
        img2 = Image.open('pictures//password.png')
        img2 = img2.resize((50,50))
        image_lbl2= ImageTk.PhotoImage(img2)
        lbl2=Label(admin_login_form,image=image_lbl2,text='password',font=5).place(x=10,y=140)
        en2=Entry(admin_login_form,textvariable=sv4,width=19,fg='navy',font=fnt)
        en2.place(x=60,y=160)
        en2.config(show="*")
        #===========================================================================
        def admin_login():
            conn=mysql.connector.connect(host='localhost',user='usr',password='123456789',database='supermarket')
            cursor=conn.cursor()
            cursor.execute('SELECT adminpass FROM admin ;')
            conn2=mysql.connector.connect(host='localhost',user='usr',password='123456789',database='supermarket')
            cursor2=conn2.cursor()   
            cursor2.execute('SELECT name FROM admin ;')
            username=cursor2.fetchall()
            password=cursor.fetchall()
            global frm
            for i in password:
                for j in i:
                    admin_pass=j
            for w in username:
                for x in w:
                    admin_name=x
            admin_password=hashing(sv4.get())
            if admin_name==sv3.get() and admin_password==admin_pass:
                admin_login_form.destroy()
                frm.destroy()
                admin_page()
            else:
                messagebox.showerror('error', 'error in user name or password')
        image = Image.open('pictures//rounded.png')
        image = image.resize((150,60))
        image_btn1= ImageTk.PhotoImage(image)
        btn=Button(admin_login_form,text='login',image=image_btn1,border=0,font=fnt,command=admin_login,compound='center').place(relx=0.5, rely=0.8, anchor=CENTER)
        admin_login_form.mainloop()
    frm=Tk()
    fnt= ('Helvetica 15 bold')
    frm.config(bg='#FFFFFF')
    frm.iconbitmap('pictures//supermarket.ico')
    frm.title('Employee Login')
    image=Image.open("pictures//supermarket.jpg")
    bck=ImageTk.PhotoImage(image)
    lbl=Label(frm,image=bck)
    lbl.place(x=-1,y=0)
    image = Image.open('pictures//administrator.png')
    image = image.resize((100,100))
    image_btn1= ImageTk.PhotoImage(image)
    def admin_btn1():
        admin_button()
    admin_btn1=Button(frm,text='admin',image=image_btn1,border=1,font=fnt,command=admin_btn1,compound='top').place(relx=0.7, rely=0.5, anchor=CENTER)
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def employee_btn_function():
        def employee_btn_function():
            frm.destroy()
            billing_page=Tk()
            fnt= ('Helvetica 15 bold')
            billing_page.state('zoomed')
            billing_page.title('Billing Page')
            billing_page.config(bg='#5E7C71')
            sv5=StringVar()
            sv6=IntVar()
            sv6.set(1)
            text_area=Text(billing_page,font=fnt,fg='navy')
            text_area.place(relx=.45,rely=.1,height=700,width=830)
            scroll2=Scrollbar(billing_page,orient='vertical',width=20,bg='green')
            scroll2.place(x=1520,y=83,height=700)
            scroll2.config(command=text_area.yview)
            ti=(time.ctime(time.time()))
            txt=("""
                                                    Mg Chat's Grocery Store

                                            Open Daily :  7:30 AM to 9:0 PM

                                                *****************************************

                                        %s

                            Super Market                                       Mostafa Essam

    ========================================================================================================================================

            Quantity	                                        Name	                                         Price
        """%(time.ctime(time.time())))
            text_area.insert(1.1, txt)
            def add_to_cart():
                global sum
                global my_cursor
                tree_values=list()
                if sv5.get()=='':
                    messagebox.showerror('Error','Enter ID')
                    en1.focus()
                else:
                    my_cursor.execute("select item,price from inventory where id = '%s'"%(sv5.get()))
                    table_data=my_cursor.fetchall()  #   الداتا من sql
                    values2=[sv6.get()]
                    for my_table in table_data:
                            for v1 in my_table:
                                values2.append(v1)
                    values2[2]=(sv6.get())*(values2[2])
                    tree_values.append(tuple(values2)) #list of tuples=tree_values
                    for table2 in tree_values:
                            text_area_data=("""                '%s'                                           '%s'                                         '%s'       """%(table2[0],table2[1],table2[2])) 
                            text_area.insert(END,(text_area_data+'\n'))
                            sum=sum+table2[2]
                            return sum,tree_values
            def Total():
                global sum
                messagebox.showinfo('',"Total = '%s' "%(sum))
            def bill():
                global sum
                x=strftime('%I %M %S %p')
                text_area.insert(END,("\n\n                  ====================================  total= "+str(sum)+"  ===================================="))
                f = open(("bills//'%s'.txt"%(str(strftime('%I %M %S %p')))), "w")                  
                f.write(text_area.get(1.0,END))
                f.close()
                text_area.delete(1.1,"end")
                sum=0
                text_area.insert(1.1,txt)
            def exit():        
                billing_page.destroy()
            lbl=Label(billing_page,text='Billing Page',bg='#5E7C71',font=('Helvetica 35 bold')).place(relx=.4,rely=.01)
            frame1=LabelFrame(billing_page,text='Products',bg='#eeeeee',width=650,border=3,height=430,font=fnt).place(x=24,y=80)
            item_id=Label(billing_page,text='Item-ID',font=('Helvetica 15 bold')).place(x=44,y=120)
            en1=Entry(billing_page,textvariable=sv5,width=45,fg='navy',font=fnt)
            en1.place(x=100,y=150)
            quantity=Label(billing_page,text='Quantity',font=('Helvetica 15 bold')).place(x=44,y=350)
            en2=Entry(billing_page,textvariable=sv6,width=45,fg='navy',font=fnt)
            en2.place(x=100,y=380)
            img=Image.open('pictures//roundedbutton.png')
            img=img.resize((200,60))
            img_btn1=ImageTk.PhotoImage(img)
            add_to_cart_btn=Button(billing_page,width=150,height=60,command=add_to_cart,bg='#F0F0F0',text='Add To Cart',image=img_btn1,compound='center',border=0).place(x=220,y=430)
            frame2=LabelFrame(billing_page,text='Options',bg='#eeeeee',width=650,border=3,height=140,font=fnt).place(x=24,y=550)
            total_btn=Button(billing_page,width=150,height=60,bg='#F0F0F0',text='Total',command=Total,image=img_btn1,compound='center',border=0).place(x=26,y=600)
            Bill_btn=Button(billing_page,width=150,height=60,bg='#F0F0F0',text='Bill',image=img_btn1,command=bill,compound='center',border=0).place(x=250,y=600)
            exit_btn=Button(billing_page,width=150,height=60,bg='#F0F0F0',text='Exit',command=exit,image=img_btn1,compound='center',border=0).place(x=480,y=600)
            billing_page.iconbitmap('pictures//supermarket.ico')
            billing_page.mainloop()
        fnt= ('Helvetica 15 bold') 
        employee_login_page=Toplevel()
        sum=0
        connect=mysql.connector.connect(host='localhost',user='usr',password='123456789',database='supermarket')
        my_cursor=connect.cursor()
        employee_login_page.iconbitmap('pictures//login-icon.ico')
        w = 280
        h = 320
        sw = employee_login_page.winfo_screenwidth()
        sh = employee_login_page.winfo_screenheight()
        x = (sw-w)/2+60
        y = (sh-h)/2+30
        employee_login_page.geometry(('%dx%d+%d+%d') % (w, h, x, y))
        employee_login_page.resizable(False,False)
        sv3=StringVar() 
        sv4=StringVar()
        lbl=Label(employee_login_page,text='User name',font=5).place(x=20,y=10)
        img = Image.open('pictures//username.png')
        img = img.resize((50,50))
        image_lbl= ImageTk.PhotoImage(img)
        lbl=Label(employee_login_page,image=image_lbl,text='User name',font=5).place(x=10,y=40)
        en1_login_page=Entry(employee_login_page,textvariable=sv3,width=19,fg='navy',font=fnt)
        en1_login_page.place(x=60,y=59)
        #=========================================================================
        passlbl=Label(employee_login_page,text='password',font=5).place(x=20,y=110)
        img2 = Image.open('pictures//password.png')
        img2 = img2.resize((50,50))
        image_lbl2= ImageTk.PhotoImage(img2)
        lbl2=Label(employee_login_page,image=image_lbl2,text='password',font=5).place(x=10,y=140)
        en2=Entry(employee_login_page,textvariable=sv4,width=19,fg='navy',font=fnt)
        en2.place(x=60,y=160)
        en2.config(show="*")
        #===========================================================================
        image = Image.open('pictures//rounded.png')
        image = image.resize((150,60))
        image_btn1= ImageTk.PhotoImage(image)
        def employee_registration():
            conn=mysql.connector.connect(host='localhost',user='usr',password='123456789',database='supermarket')
            cursor=conn.cursor()
            cursor.execute('SELECT employee_name,employee_password FROM employees ;')   
            username_password=cursor.fetchall()
            for i in username_password:
                admin_name=i[0]
                admin_pass=i[1]
            admin_password=hashing(sv4.get())
            if admin_name==sv3.get() and admin_password==admin_pass:
                employee_login_page.destroy()
                employee_btn_function()
            else:
                messagebox.showerror('error', 'error in user name or password')
        btn=Button(employee_login_page,text='login',image=image_btn1,border=0,font=fnt,command=employee_registration,compound='center').place(relx=0.5, rely=0.8, anchor=CENTER)
        employee_login_page.mainloop()
    image2 = Image.open('pictures//employee.png')
    sb=PhotoImage(file="pictures//roundedbutton.png").subsample(5,5)
    image2 = image2.resize((100,100))
    image_btn2= ImageTk.PhotoImage(image2)
    frm.state('zoomed')
    employee_btn_1=Button(frm,text='employee',image=image_btn2,command=employee_btn_function,border=1,font=('Helvetica 20 bold'),compound='top').place(relx=0.4, rely=0.5, anchor=CENTER)
    frm.mainloop()
except mysql.connector.Error as err:
    messagebox.showerror("An error occurred:", 'you must run mysql server using xampp')
