# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 11:47:32 2020

@author: Peter
"""

# l37   b15    e10     cal3    d8    m3     (l22)

def clear1():
    for widget in top3.winfo_children():
        if type(widget)!=Menu :
            widget.destroy()
def clear2():
    for widget in top1.winfo_children():
        if type(widget)==Label :
            widget.destroy()
def clear3():
    for widget in top2.winfo_children():
        if type(widget)==Label :
            widget.destroy()
def man():
    def st2():
        
        nam=e6.get()
        date1=cal2.selection_get()
        date2=cal3.selection_get()
        stime=d5.get()+':'+d6.get()
        etime=d7.get()+':'+d8.get()
        #print(nam.sdate,edate,stime,etime)
        c.execute('use {}'.format(name))
        c.execute("select max(sno) from man ")
        f=c.fetchall()
        for i in f:
            for e in i:
                
                if e==None:
                    sno=1
                else:
                    sno=int(e)+1
        c.execute("insert into man values({},'{}','{}','{}','{}','{}')".format(sno,nam,date1,stime,date2,etime))
        sql.commit()
        clear1()
        top3.geometry('500x500')
    clear1()
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
    d5.current(0)
    
    d6=ttk.Combobox(top3, width = 3,value=['00','15','30','45'])
    d6.grid(row=3,column=1,padx=100)
    d6.place(x=225,y=320)
    d6.current(0)
    
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
    d7.current(0)
    
    d8=ttk.Combobox(top3, width = 3,value=['00','15','30','45'])
    d8.grid(row=3,column=1,padx=100)
    d8.place(x=850,y=320)
    d8.current(0)
    
    b7=Button(top3,text='Submit',padx=35,pady=10,command=(st2))
    b7.place(x=200,y=390)
    

def one():
    def st1():
        date=cal1.selection_get()
        nam=e5.get()
        stime=s1.get()+':'+s2.get()
        etime=s3.get()+':'+s4.get()
        c.execute('use {}'.format(name))
        c.execute("select max(sno) from one ")
        f=c.fetchall()
        for i in f:
            for e in i:
                
                if e==None:
                    sno=1
                else:
                    sno=int(e)+1
        
        c.execute("insert into one values({},'{}','{}','{}','{}')".format(sno,nam,date,stime,etime))
        sql.commit()
        clear1()
        top3.geometry('500x500')
    clear1()
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
    
    s4=StringVar()
    d4=ttk.Combobox(top3, width = 3,textvariable=s4,value=['00','15','30','45'])
    d4.grid(row=3,column=1,padx=100)
    d4.place(x=250,y=365)
    d4.current(0)
    
    b6=Button(top3,text='Submit',padx=35,pady=10,command=(st1))
    b6.place(x=200,y=390)
        
def n1():
    def n2():
        s=e7.get()
        e7.destroy()
        l23.destroy()
        b10.destroy()
        c.execute("use {}".format(name))
        c.execute("select * from one where name='{}'".format(s))
        f=c.fetchall()
        if f==[]:
            l24=Label(top3,text='None Found',fg='red')
            l24.grid(row=1,column=0,columnspan=2)
        for i in f:
        
            l25=Label(top3,text='Name={};Start Date={};Start Time={};End Time={}'.format(i[1],i[2],i[3],i[4]),fg='blue')
            l25.grid(row=1,column=0,columnspan=2)
        b8['state']=NORMAL
        b9['state']=NORMAL
                    
    b8['state']=DISABLED
    b9['state']=DISABLED
    
    l23=Label(top3,text='Name of Project',fg='blue')
    l23.grid(row=1,column=0)
    
    e7=Entry(top3,width=24,borderwidth=5)
    e7.grid(row=1,column=1,pady=10)
    
    b10=Button(top3,text='Search',padx=35,pady=10,command=n2)
    b10.grid(column=0,row=2,columnspan=2)
    
def n3():
    def n4():
        s=e8.get()
        e8.destroy()
        l26.destroy()
        b11.destroy()
        c.execute("use {}".format(name))
        try:
            c.execute("select * from one where date='{}'".format(s))
            f=c.fetchall()
            if f==[]:
                l27=Label(top3,text='None Found',fg='red')
                l27.grid(row=1,column=0,columnspan=2)
            for i in f:
            
                l28=Label(top3,text='Name={};Start Date={};Start Time={};End Time={}'.format(i[1],i[2],i[3],i[4]),fg='blue')
                l28.grid(row=1,column=0,columnspan=2)
        except:
            l27=Label(top3,text='None Found',fg='red')
            l27.grid(row=1,column=0,columnspan=2)
        b8['state']=NORMAL
        b9['state']=NORMAL
        
        
    b8['state']=DISABLED
    b9['state']=DISABLED
    
    l26=Label(top3,text='Starting Date of the Project\n(YYYY-MM-DD)',fg='blue')
    l26.grid(row=1,column=0)
    
    e8=Entry(top3,width=24,borderwidth=5)
    e8.grid(row=1,column=1,pady=10)
    
    b11=Button(top3,text='Search',padx=35,pady=10,command=n4)
    b11.grid(column=0,row=2,columnspan=2)
    
def v1():
    clear1()
    top3.geometry('325x300')
    global b8
    global b9
    b8=Button(top3,text='Search By Name',padx=35,pady=10,command=n1)
    b8.grid(column=0,row=0)
    
    b9=Button(top3,text='Search By Date',padx=35,pady=10,command=n3)
    b9.grid(column=1,row=0)

def n5():
    def n6():
        s=e9.get()
        e9.destroy()
        l29.destroy()
        b14.destroy()
        c.execute("use {}".format(name))
        c.execute("select * from man where name='{}'".format(s))
        f=c.fetchall()
        if f==[]:
            l30=Label(top3,text='None Found',fg='red')
            l30.grid(row=1,column=0,columnspan=2)
        s=0
        for i in f:
            s=s+1
            l31=Label(top3,text='Name={};Start Date={};Start Time={};End Date={};End time={}'.format(i[1],i[2],i[3],i[4],i[5]),fg='blue')
            l31.grid(row=s,column=0,columnspan=3)
        b12['state']=NORMAL
        b13['state']=NORMAL
                    
    b12['state']=DISABLED
    b13['state']=DISABLED
    
    l29=Label(top3,text='Name of Project',fg='blue')
    l29.grid(row=1,column=0)
    
    e9=Entry(top3,width=24,borderwidth=5)
    e9.grid(row=1,column=1,pady=10)
    
    b14=Button(top3,text='Search',padx=35,pady=10,command=n6)
    b14.grid(column=0,row=2,columnspan=2)
    
def n7():
    def n8():
        s=e10.get()
        e10.destroy()
        l32.destroy()
        b15.destroy()
        c.execute("use {}".format(name))
        c.execute("select * from man where sdate='{}'".format(s))
        f=c.fetchall()
        try:
            if f==[]:
                l33=Label(top3,text='None Found',fg='red')
                l33.grid(row=1,column=0,columnspan=2)
            s=0
            for i in f:
                s=s+1
                l34=Label(top3,text='Name={};Start Date={};Start Time={};End Date={};End Time={}'.format(i[1],i[2],i[3],i[4],i[5]),fg='blue')
                l34.grid(row=s,column=0,columnspan=3)
            b8['state']=NORMAL
            b9['state']=NORMAL
        except:
            l33=Label(top3,text='None Found',fg='red')
            l33.grid(row=1,column=0,columnspan=2)
            b8['state']=NORMAL
            b9['state']=NORMAL
    b12['state']=DISABLED
    b13['state']=DISABLED
    
    l32=Label(top3,text='Start Date of Project',fg='blue')
    l32.grid(row=1,column=0)
    
    e10=Entry(top3,width=24,borderwidth=5)
    e10.grid(row=1,column=1,pady=10)
    
    b15=Button(top3,text='Search',padx=35,pady=10,command=n8)
    b15.grid(column=0,row=2,columnspan=2)
    
def v2():
    clear1()
    top3.geometry('325x300')
    global b12
    global b13
    b12=Button(top3,text='Search By Name',padx=35,pady=10,command=n5)
    b12.grid(column=0,row=0)
    
    b13=Button(top3,text='Search By Date',padx=35,pady=10,command=n7)
    b13.grid(column=1,row=0)
    
def per():
    global top3
    top3=Toplevel()
    top3.geometry('500x500')
    my_menu=Menu(top3)
    
    m1=Menu(my_menu,tearoff=0)
    m1.add_command(label='One Day Project',command=(one))
    m1.add_command(label='Multi Day Project',command=(man))
    my_menu.add_cascade(label='Add Project', menu=m1)
    
    m2=Menu(my_menu,tearoff=0)
    my_menu.add_cascade(label='Add Remainders',menu=m2)
    
    m3=Menu(my_menu,tearoff=0)
    m3.add_command(label='Viewing One Day Project',command=v1)
    m3.add_command(label='Viewing Many day Project',command=v2)
    my_menu.add_cascade(label='Viewing Projects',menu=m3)
    
    top3.config(menu=my_menu)

def cre():
    def sub():
        l2=Label(top1,text='Name:',fg='blue')
        l2.grid(row=0,column=0)
        l3=Label(top1,text='Password:',fg='blue')
        l3.grid(row=1,column=0)
        sign=-1
        global name
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
        file.seek(0)
        s=file.readlines()
        file.close()
        for i in s:
            i=i.strip('\n')
            i=i.split(',')
            if i[0]==name:
                l35=Label(top1,text='Use another User Name',fg='red')
                l35.grid(row=3,column=1)
                sign=2
        if name=='' or pas=='':
            sign=2
            l36=Label(top1,text='Please enter name or password',fg='red')
            l36.grid(row=3,column=1)
        if sign!=2:
            file=open('g.txt','a+')
            k='{},{}'.format(name,pas)
            file.write(k+'\n')
            file.close()
            
            c.execute('create database {}'.format(name))
            c.execute('use {}'.format(name))
            c.execute('create table one (sno int(20),name char(20),date date,stiime char(5),etime char(5)) ')
            c.execute('create table man (sno int(20),name char(20),sdate date,stiime char(5),edate date,etime char(5)) ')
            
            l7=Label(top1,text='account created',fg='blue')
            l7.grid(row=3,column=1)
            l7.after(500, lambda: (top1.destroy(),per()) )
    global top1
    top1=Toplevel()
    l2=Label(top1,text='Name:',fg='blue')
    l2.grid(row=0,column=0)
    l3=Label(top1,text='Password:',fg='blue')
    l3.grid(row=1,column=0)
    
    e1=Entry(top1,width=50,borderwidth=5)
    e1.grid(row=0,column=1)
    e2=Entry(top1,width=50,borderwidth=5)
    e2.grid(row=1,column=1)
    
    b5=Button(top1,text='Submit',padx=35,pady=10,command=lambda: (clear2(),sub()))
    b5.grid(row=2,column=1)

def sig():
    def ch():
        sign=-1
        l4=Label(top2,text='User Name:',fg='blue')
        l4.grid(row=0,column=0)
        l5=Label(top2,text='Password:',fg='blue')
        l5.grid(row=1,column=0)
        global name
        name=e3.get()
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
                change=change*-1
                s=s+j
            if i[0]==name and s==pa:
                sign=1
        if name=='' or pa=='':
            l37=Label(top2,text='Please do enter name or password',fg='red')
            l37.grid(row=3,column=0,columnspan=2)
        elif sign!=1:
            l6=Label(top2,text='Wrong User Name or Password',fg='red')
            l6.grid(row=3,column=0,columnspan=2)
            
        else:
            l8=Label(top2,text='Account Created',fg='blue')
            l8.grid(row=3,column=1)
            l8.after(500, lambda: (top2.destroy(),per()) )
            
        file.close()
    global top2
    top2=Toplevel()
    l4=Label(top2,text='User Name:',fg='blue')
    l4.grid(row=0,column=0)
    l5=Label(top2,text='Password:',fg='blue')
    l5.grid(row=1,column=0)
    
    e3=Entry(top2,width=50,borderwidth=5)
    e3.grid(row=0,column=1)
    e4=Entry(top2,width=50,borderwidth=5)
    e4.grid(row=1,column=1)
    
    b4=Button(top2,text='Submit',padx=35,pady=10,command=lambda:(clear3(),ch()))
    b4.grid(row=2,column=1)
    
from tkinter import *
from tkinter import ttk
from tkcalendar import *

root=Tk()
root.title('Personal Planner')
#root.iconbitmap('<path of the icon>') for changing Icon

import mysql.connector
sql=mysql.connector.connect(user='root',passwd='12345',host='localhost')
c=sql.cursor()


l1=Label(root,text='0.Exit\n1.Create an Account\n2.Sign in',fg='red')
l1.grid(row=0,column=1)

b1=Button(root,text='Exit',padx=35,pady=10,command= lambda:(root.destroy()))
b1.grid(row=3,column=0)
b2=Button(root,text='Create Account',padx=35,pady=10,command=cre)
b2.grid(row=3,column=1)
b3=Button(root,text='Sign In',padx=35,pady=10,command=sig)
b3.grid(row=3,column=2)

root.mainloop()

#please make the viewing of two tuples in mysql possible