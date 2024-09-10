# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 11:47:32 2020

@author: Peter
"""

#l21   b7    e6     cal3    d8

sign=-1
def man():
    top3.geometry('1200x450')
    
    l15=Label(top3,text='Name of Project:',fg='blue')
    l15.grid(row=0,column=0,pady=10)
    e6=Entry(top3,width=50,borderwidth=5)
    e6.grid(row=0,column=1,pady=10)
    
    l16=Label(top3,text='Starting Date for The Project',fg='blue')
    l16.grid(row=1,column=0,pady=10)
    cal2 = Calendar(top3,
                   font="Arial 14", selectmode='day',
                   cursor="hand2", year=2018, month=2, day=5)
    cal2.grid(row=1,column=1,columnspan=2)
    
    l17=Label(top3,text='Starting Time for The Project',fg='blue')
    l17.place(x=0,y=320)
    
    l18=Label(top3,text='HH          MM',fg='blue')
    l18.grid(row=2,column=1)
    l18.place(x=175,y=300)
    
    d5=ttk.Combobox(top3, width = 3,value=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'])
    d5.grid(row=3,column=1,pady=100)
    d5.place(x=175,y=320)
    
    d6=ttk.Combobox(top3, width = 3,value=['00','15','30','45'])
    d6.grid(row=3,column=1,padx=100)
    d6.place(x=225,y=320)
    
    l21=Label(top3,text='Ending date for the Project',fg='blue')
    l21.grid(row=1,column=3)
    
    cal3 = Calendar(top3,
                   font="Arial 14", selectmode='day',
                   cursor="hand2", year=2018, month=2, day=5)
    cal3.place(x=790,y=50)
    
    l19=Label(top3,text='Ending Time for The Project',fg='blue')
    l19.grid(row=3,column=3,pady=30,padx=70)
    
    l20=Label(top3,text='HH          MM',fg='blue')
    l20.place(x=800,y=300)
    
    d7=ttk.Combobox(top3, width = 3,value=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'])
    d7.grid(row=3,column=1,pady=100)
    d7.place(x=800,y=320)
    
    d8=ttk.Combobox(top3, width = 3,value=['00','15','30','45'])
    d8.grid(row=3,column=1,padx=100)
    d8.place(x=850,y=320)
    
    b7=Button(top3,text='Submit',padx=35,pady=10)
    b7.place(x=200,y=390)
    

def one():
    def st1():
        date=cal1.selection_get()
        name=e5.get()
        stime=s1.get()+':'+s2.get()
        #print(name,date,time)
        etime=s3.get()+':'+s4.get()
        c.execute("select * form one where sno=max(sno) ")
        f=c.fetchall()
        #c.execute("insert into one values({},'{}',)")
    top3.geometry('500x450')
    
    l9=Label(top3,text='Name of Project:',fg='blue')
    l9.grid(row=0,column=0,pady=10)
    e5=Entry(top3,width=50,borderwidth=5)
    e5.grid(row=0,column=1,pady=10)
    
    l10=Label(top3,text='Date for The Project',fg='blue')
    l10.grid(row=1,column=0,pady=10)
    cal1= Calendar(top3,
                   font="Arial 14", selectmode='day',
                   cursor="hand2", year=2018, month=2, day=5)
    cal1.grid(row=1,column=1,columnspan=2)
    
    l12=Label(top3,text='The Starting Time for The Project',fg='blue')
    l12.place(x=10,y=320)
    
    l11=Label(top3,text='HH          MM',fg='blue')
    l11.grid(row=2,column=1)
    l11.place(x=200,y=300)
    
    s1=StringVar()
    d1=ttk.Combobox(top3, width = 3,value=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'],textvariable=s1)
    d1.grid(row=3,column=1,pady=100)
    d1.place(x=200,y=320)
    d1.current(0)
    
    s2=StringVar()
    d2=ttk.Combobox(top3, width = 3,value=['00','15','30','45'],textvariable=s2)
    d2.grid(row=3,column=1,padx=100)
    d2.place(x=250,y=320)
    d2.current(0)
    
    l13=Label(top3,text='The Ending Time for The Project',fg='blue')
    l13.place(x=10,y=365)
    
    l14=Label(top3,text='HH          MM',fg='blue')
    l14.grid(row=2,column=1)
    l14.place(x=200,y=345)
    
    s3=StringVar()
    d3=ttk.Combobox(top3, width = 3,textvariable=s3,value=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'])
    d3.grid(row=3,column=1,pady=100)
    d3.place(x=200,y=365)
    d3.current(0)
    
    s4=StrinVar()
    d4=ttk.Combobox(top3, width = 3,textvarible=s4,value=['00','15','30','45'])
    d4.grid(row=3,column=1,padx=100)
    d4.place(x=250,y=365)
    d4.current()
    
    b6=Button(top3,text='Submit',padx=35,pady=10,command=st1)
    b6.place(x=200,y=390)
def per():
    global top3
    top3=Toplevel()
    
    
    my_menu=Menu(top3)
    
    m1=Menu(my_menu,tearoff=0)
    m1.add_command(label='One Day Project',command=one)
    m1.add_command(label='Multi Day Project',command=man)
    my_menu.add_cascade(label='Add Project', menu=m1)
    
    m2=Menu(my_menu,tearoff=0)
    my_menu.add_cascade(label='Add Remainders',menu=m2)
    
    top3.config(menu=my_menu)

def cre():
    def sub():
        name=e1.get()
        pas=e2.get()
        file=open('g.txt','a+')
        change=1
        s=''
        for i in range(0,len(pas)):
            k=chr(ord(pas[i])+i*change)
            change=change*-1
            s=s+k
        pas=s
        k='{},{}'.format(name,pas)
        file.write(k+'\n')
        file.close()
        
        c.execute('create database {}'.format(name))
        c.execute('use {}'.format(name))
        c.execute('create table one (sno int(20),name char(20),date date,stiime char(5),etime char(5)) ')
        c.execute('create table man (sno int(20),name char(20),sdate date,stiime char(5),edate date,etime char(5)) ')
        
        sign=1
        l7=Label(top1,text='account created',fg='blue')
        l7.grid(row=3,column=1)
        l7.after(1000, lambda: (top1.destroy(),per()) )
    top1=Toplevel()
    l2=Label(top1,text='Name:',fg='blue')
    l2.grid(row=0,column=0)
    l3=Label(top1,text='Password:',fg='blue')
    l3.grid(row=1,column=0)
    
    e1=Entry(top1,width=50,borderwidth=5)
    e1.grid(row=0,column=1)
    e2=Entry(top1,width=50,borderwidth=5)
    e2.grid(row=1,column=1)
    
    b5=Button(top1,text='Submit',padx=35,pady=10,command=sub)
    b5.grid(row=2,column=1)

def sig():
    def ch():
        user=e3.get()
        pa=e4.get()
        file=open('g.txt','a+')
        file.seek(0)
        d=file.readlines()
        
        for i in d:
            i=i.strip('\n')
            i=i.split(',')
            change=-1
            s=''
            for k in range(0,len(i[1])):
                j=chr(ord(i[1][k])+k*change)
                #print(j,k)
                change=change*-1
                s=s+j
            if i[0]==user and s==pa:
                sign=1
        if sign!=1:
            l6=Label(top2,text='Something went wrong.',fg='red')
            l6.grid(row=3,column=0,columnspan=2)
            
        else:
            l8=Label(top2,text='account created',fg='blue')
            l8.grid(row=3,column=1)
            l8.after(1000, lambda: (top2.destroy(),per()) )
            
        file.close()
    top2=Toplevel()
    l4=Label(top2,text='User Name:',fg='blue')
    l4.grid(row=0,column=0)
    l5=Label(top2,text='Password:',fg='blue')
    l5.grid(row=1,column=0)
    
    e3=Entry(top2,width=50,borderwidth=5)
    e3.grid(row=0,column=1)
    e4=Entry(top2,width=50,borderwidth=5)
    e4.grid(row=1,column=1)
    
    b4=Button(top2,text='Submit',padx=35,pady=10,command=ch)
    b4.grid(row=2,column=1)
    
from tkinter import *
from tkcalendar import *

root=Tk()
root.title('Personal Planner')
#root.iconbitmap('<path of the icon>') for changing Icon

import mysql.connector
sql=mysql.connector.connect(user='root',passwd='12345',host='localhost')
c=sql.cursor()


l1=Label(root,text='0.Exit\n1.Create an Account\n2.Sign in',fg='red')
l1.grid(row=0,column=1)

b1=Button(root,text='Exit',padx=35,pady=10,)
b1.grid(row=3,column=0)
b2=Button(root,text='Create Account',padx=35,pady=10,command=cre)
b2.grid(row=3,column=1)
b3=Button(root,text='Sign In',padx=35,pady=10,command=sig)
b3.grid(row=3,column=2)

root.mainloop()
