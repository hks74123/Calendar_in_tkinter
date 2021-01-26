from tkinter import*

import calendar

screen1=Tk()
screen1.title('Calendar')
screen1.geometry("500x300")
screen1.configure(background='black')

def calendars():
    screen2=Tk()
    screen2.title('Calendar')
    screen2.geometry("600x600")

    year=int(i1.get())
    see=calendar.calendar(year)

    t=Label(screen2,text=see,font='Consolas 10 bold')
    t.grid(row=4,column=1,padx=15)

    screen2.mainloop()

def Exit():
    screen1.destroy()
    
t1=Label(screen1,text='CALENDAR',font=("Arial",40,'bold'),fg='black',bg='yellow').place(x=90,y=0)
t2=Label(screen1,text='ENTER YEAR:',font=("Arial",15,'bold'),fg='olivedrab1',bg='black').place(x=40,y=120)

i1=Entry(screen1,font=("Arial",15,'bold'),fg='red',width=15)
i1.place(x=180,y=120)

b1=Button(screen1,text="Go and See",font=("Arial",15,'bold'),bg='yellow',command=calendars).place(x=175,y=165)

b2=Button(screen1,text="Exit",font=("Arial",15,'bold'),bg='yellow',command=Exit).place(x=215,y=206)

screen1.mainloop()

