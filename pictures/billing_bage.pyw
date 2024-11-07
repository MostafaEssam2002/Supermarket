import tkinter as tk
from tkinter import *
from tkinter import messagebox
from datetime import date
import mysql.connector
from time import strftime
from PIL import ImageTk, Image
import time
sum=0
connect=mysql.connector.connect(host='localhost',user='usr',password='123456789',database='supermarket')
my_cursor=connect.cursor()
def employee_btn_function():
      # frm.destroy()
      # billing_page()
      billing_page=Tk()
      fnt= ('Helvetica 15 bold')
      w = 1920
      h = 1080
      sw = billing_page.winfo_screenwidth()
      sh = billing_page.winfo_screenheight()
      x = (sw-w)/2+180
      y = (sh-h)/2+105
      billing_page.title("Billing")
      billing_page.geometry(('%dx%d+%d+%d') % (w, h, x, y))
      billing_page.config(bg='#5E7C71')
      sv5=StringVar()
      sv6=IntVar()
      sv6.set(1)

      text_area=Text(billing_page,font=fnt,fg='navy')
      text_area.place(relx=.45,rely=.1,height=700,width=830)
      scroll2=Scrollbar(billing_page,orient='vertical',width=20,bg='green')
      scroll2.place(x=1520,y=85,height=700)
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
      tree_values=''
      def add_to_cart():
            global tree_values
            global sum
            global my_cursor
            tree_values=list()
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
                  text_area.insert(tk.END,(text_area_data+'\n'))
                  sum=sum+table2[2]
                  return sum,tree_values
      def Total():
            global sum
            messagebox.showinfo('',"Total = '%s' "%(sum))
            sv5.set(1)
      def bill():
            global sum
            x=strftime('%I %M %S %p')
            text_area.insert(tk.END,("\n\n                  ====================================  total= "+str(sum)+"  ===================================="))
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
      photo=PhotoImage(file="pictures//roundedbutton.png").subsample(3,3)
      img=img.resize((200,60))
      img_btn1=ImageTk.PhotoImage(img)
      add_to_cart_btn=Button(billing_page,width=150,height=60,command=add_to_cart,bg='#F0F0F0',text='Add To Cart',image=img_btn1,compound='center',border=0).place(x=220,y=430)
      frame2=LabelFrame(billing_page,text='Options',bg='#eeeeee',width=650,border=3,height=140,font=fnt).place(x=24,y=550)
      total_btn=Button(billing_page,width=150,height=60,bg='#F0F0F0',text='Total',command=Total,image=img_btn1,compound='center',border=0).place(x=26,y=600)
      Bill_btn=Button(billing_page,width=150,height=60,bg='#F0F0F0',text='Bill',image=img_btn1,command=bill,compound='center',border=0).place(x=250,y=600)
      exit_btn=Button(billing_page,width=150,height=60,bg='#F0F0F0',text='Exit',command=exit,image=photo,compound='center',border=0).place(x=480,y=600)
      billing_page.iconbitmap('pictures//supermarket.ico')
      billing_page.mainloop()
employee_btn_function()