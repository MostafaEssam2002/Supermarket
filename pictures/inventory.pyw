from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from PIL import ImageTk, Image
def inventory():
    inventory=Tk()
    fnt= ('Helvetica 15 bold')
    sv11=StringVar()
    sv12=StringVar()
    sv13=StringVar()
    sv14=StringVar()
    w = 1920
    h = 1080
    sw = inventory.winfo_screenwidth()
    sh = inventory.winfo_screenheight()
    x = (sw-w)/2+180
    y = (sh-h)/2+105
    inventory.geometry(('%dx%d+%d+%d') % (w, h, x, y))
    inventory.config(bg='#5D534A')
    inventory.title('Inventory')
    lbl0=Label(inventory,text='inventory',bg='#5D534A',font=('Helvetica 35 bold')).place(relx=.45,rely=.001)
    frame0=LabelFrame(inventory,text='Items',bg='#eeeeee',width=720,border=3,height=600,font=fnt).place(x=20,y=110)
    lbl1=Label(frame0,text="ID",font=fnt,bg="#EEEEEE").place(x=80,y=200)
    en1=Entry(frame0,fg='navy',textvariable=sv11,width=37,font=5)
    en1.place(x=250,y=200)
    en1.focus()
    lbl2=Label(frame0,text="Item",font=fnt,bg="#EEEEEE").place(x=80,y=300)
    en2=Entry(frame0,fg='navy',textvariable=sv12,width=37,font=5)
    en2.place(x=250,y=300)
    lbl3=Label(frame0,text="In Stock",font=fnt,bg="#EEEEEE").place(x=80,y=400)
    lbl4=Label(frame0,text="Price",font=fnt,bg="#EEEEEE").place(x=80,y=500)
    en3=Entry(frame0,fg='navy',textvariable=sv13,width=37,font=5)
    en3.place(x=250,y=400)
    en4=Entry(frame0,fg='navy',textvariable=sv14,width=37,font=5)
    en4.place(x=250,y=500)
    img=Image.open('pictures//roundedbutton.png')
    img1=img.resize((200,60))
    image=ImageTk.PhotoImage(img1)
    img2=img.resize((270,60))
    image2=ImageTk.PhotoImage(img2)
    style=ttk.Style()
    style.theme_use("alt")
    style.configure("Treeview",font="Verdana 15",background="FFFFFF",foreground="navy",rowheight=50)
    mytree=ttk.Treeview(inventory,style='Treeview')
    mytree['columns']=("item_id","item","in_stock","price")
    mytree.column("#0",width=0,minwidth=0,anchor='center')
    mytree.column("#1",width=187,minwidth=25,anchor='center')
    mytree.column("#2",width=187,minwidth=25,anchor='center')
    mytree.column("#3",width=187,minwidth=25,anchor='center')
    mytree.column("#4",width=187,minwidth=25,anchor='center')
    mytree.heading("#0",text='',anchor='center')
    mytree.heading("#1",text='item_id',anchor='center')
    mytree.heading("#2",text='item',anchor='center')
    mytree.heading("#3",text='in_stock',anchor='center')
    mytree.heading("#4",text='price',anchor='center')
    connecet1=mysql.connector.connect(host='localhost',user='usr',password='123456789',database='supermarket')
    my_cursor1=connecet1.cursor()
    my_cursor1.execute("select * from inventory ;")
    data1=my_cursor1.fetchall()
    for s in data1:
        mytree.insert('','end',values=(s))
    mytree.place(x=750,y=90,height=670)
    scroll=Scrollbar(inventory,orient='vertical',width=20,bg='green',command=mytree.yview)
    scroll.place(x=1480,y=110,height=650)
    def clear_all():
        global mytree
        for item in mytree.get_children():
            mytree.delete(item)
    def search():
        global mytree
        global data
        global clear_all
        if sv11.get()=='':
            messagebox.showerror('error','enter ID')
            en1.focus()
        else:
            clear_all()
            connecet0=mysql.connector.connect(host='localhost',user='usr',password='123456789',database='supermarket')
            my_cursor0=connecet0.cursor()
            my_cursor0.execute("select * from inventory where id='%s' ;"%(sv11.get()))
            data10=my_cursor0.fetchall()
            for i in data10:
                mytree.insert('','end',values=(i))
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
            global mytree
            global clear_all
            clear_all()
            connecet2=mysql.connector.connect(host='localhost',user='usr',password='123456789',database='supermarket')
            my_cursor2=connecet2.cursor()
            my_cursor2.execute("insert into inventory values ('%s','%s','%s','%s')"%(sv11.get(),sv12.get(),sv13.get(),sv14.get()))
            connecet2.commit()
            my_cursor2.execute("select * from inventory")
            data2=my_cursor2.fetchall()
            for x in data2:
                mytree.insert('','end',values=(x))
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
                global mytree
                global clear_all
                my_cursor3.execute("DELETE FROM inventory WHERE id ='%s'"%(sv11.get()))
                connecet3.commit()
                my_cursor3.execute("SELECT * FROM inventory ")
                data3=my_cursor3.fetchall()
                for b in data3:
                    mytree.insert('','end',values=(b))
                sv11.set('')
                messagebox.showinfo('','item has been removed')
    def edit_item():
        connecet4=mysql.connector.connect(host='localhost',user='usr',password='123456789',database='supermarket')
        my_cursor4=connecet4.cursor()
        if sv11.get()=='':
            messagebox.showerror('error','enter ID')
            en1.focus()
        else:
            global mytree
            global clear_all
            clear_all()
            my_cursor4.execute("UPDATE inventory SET item ='%s' WHERE id='%s'"%(sv12.get(),sv11.get()))
            my_cursor4.execute("UPDATE inventory SET quantity ='%s' WHERE id='%s'"%(sv13.get(),sv11.get()))
            my_cursor4.execute("UPDATE inventory SET price ='%s' WHERE id='%s'"%(sv14.get(),sv11.get()))
            connecet4.commit()
            my_cursor4.execute("SELECT * FROM inventory ")
            data3=my_cursor4.fetchall()
            for a in data3:
                mytree.insert('','end',values=(a))
            messagebox.showinfo('','Data has been changed')
            sv11.set('')
            sv12.set('')
            sv13.set('')
            sv14.set('')
            en1.focus()
    def exi4():
        inventory.destroy()
    btn_search=Button(inventory,text='Search',image=image,width=120,height=60,border=0,font=fnt,fg='white',cursor='hand2',compound='center',command=search).place(x=30,y=630)
    btn_add_item=Button(inventory,text='Add Item',image=image,width=120,height=60,border=0,font=fnt,fg='white',cursor='hand2',compound='center',command=add_item).place(x=160,y=630)
    btn_remove_item=Button(inventory,text='Remove Item',image=image2,width=180,height=60,border=0,font=fnt,fg='white',cursor='hand2',compound='center',command=remove_item).place(x=280,y=630)
    btn_edit_item=Button(inventory,text='Edit Item',image=image,width=150,height=60,border=0,font=fnt,fg='white',cursor='hand2',compound='center',command=edit_item).place(x=450,y=630)
    btn_exit=Button(inventory,text='Exit',image=image,width=120,height=60,border=0,font=fnt,fg='white',cursor='hand2',compound='center',command=exit).place(x=600,y=630)
    inventory.mainloop()
# inventory()