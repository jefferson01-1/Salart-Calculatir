from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk

# Colours
plat = '#E5E4E2'
bgrey = '#2C3539'
co3 = '#4E5180'

#The Window
window = Tk ()
window.title("")
window.geometry('600x450')
window.configure(background=bgrey)
window.resizable(width=FALSE, height=FALSE) 

style = ttk.Style(window)
style.theme_use("clam")

# Frames
top_frame = Frame(window, width= 1043, height = 60, pady= 5, bg=bgrey)
top_frame.grid(row=0, column=0)

bottom_frame = Frame(window, width= 1043, height = 400, pady= 5, bg=bgrey, relief="flat")
bottom_frame.grid(row=1, column=0, pady=0, padx=0) 

# Salary Function
def salary():
    year = 356
    weeks = 52

    # Value to be insect
    name = e_name.get()
    hours_per_day = int(e_hours.get())
    working_days = float(e_days_work.get())
    annual_salary = float(e_salary.get())

    # Hourly salary
    hourly_salary = annual_salary / 2080

    #Daily salary
    daily_salary = hourly_salary * 8

    # Weekly salary
    weekly_salary = annual_salary / 52

    # Monthly salary 
    monthly_salary = annual_salary / 12

    # Annual salary
    annual_salary = monthly_salary * 12
    
    l_name['text'] = name
    l_days['text'] = "Working Hour Per Day: " + str(hours_per_day)
    l_h_days['text'] = "Working days Per Week: " + str(working_days)
    l_annual['text'] = '${:.2f}'.format(annual_salary)
    
    l_hour ['text'] = 'hourly wage : {:.2f}'.format(hourly_salary)
    l_day['text'] = 'Daily wage : {:.2f}'.format(daily_salary)
    l_week['text'] = 'Weekly salary : {:.2f}'.format(weekly_salary)
    l_month['text'] = 'Monthly salary : {:.2f}'.format(monthly_salary)
    l_year['text'] = 'Annual salary : {:.2f}'.format(annual_salary)



app_lg = Image.open('jj logo.png')
app_lg = app_lg.resize((25,25))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(top_frame, image=app_lg, text= "Salary Calculator", width=500, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 25 bold'), bg=bgrey, fg=plat)
app_logo.place(x=0, y=0)

# Label/ Entry
l_name = Label(bottom_frame, text="Write Your full Name - ", height=1, anchor=NW, font=('ivy 15'), bg=bgrey, fg=plat)
l_name.place(x=10, y=10)
e_name = Entry(bottom_frame, width=25, justify='left', relief="solid", bg=bgrey, borderwidth=1)
e_name.place(x=200, y=11)

l_hours = Label(bottom_frame, text="How many work hours per day? - ", height=1, anchor=NW, font=('ivy 15'), bg=bgrey, fg=plat)
l_hours.place(x=10, y=40)
e_hours = Entry(bottom_frame, width=15, justify='center', relief="solid", bg=bgrey, borderwidth=1)
e_hours.place(x=260, y=41)

l_days_work = Label(bottom_frame, text="How many work hours per week? - ", height=1, anchor=NW, font=('ivy 15'), bg=bgrey, fg=plat)
l_days_work.place(x=10, y=70)
e_days_work = Entry(bottom_frame, width=15, justify='center', relief="solid", bg=bgrey, borderwidth=1)
e_days_work.place(x=260, y=71)

l_salary = Label(bottom_frame, text="What is your Annual Salary? - ", height=1, anchor=NW, font=('ivy 15'), bg=bgrey, fg=plat)
l_salary.place(x=10, y=100)
e_salary = Entry(bottom_frame, width=15, justify='center', relief="solid", bg=bgrey, borderwidth=1)
e_salary.place(x=260, y=101)

#app_calculator = Image.open('jj logo.png')
#app_calculator = app_calculator.resize((20,20))
#app_calculator = ImageTk.PhotoImage(app_calculator)
calculate_button = Button(bottom_frame,  command=salary, text= "Calculate".upper(), width=10, height=1, compound=LEFT, overrelief=RIDGE, anchor=NW, font=('Ivg 15 bold'))
calculate_button.place(x=430, y=90)

l_name = Label(bottom_frame, width=25, text='', relief=RAISED, anchor=NW, padx=5, pady=5, font=('Ivy 10'), bg=bgrey, borderwidth=1)
l_name.place(x=10, y=150)

l_days = Label(bottom_frame, width=25, text='', relief=RAISED, anchor=NW, padx=5, pady=5, font=('Ivy 10'), bg=bgrey, borderwidth=1)
l_days.place(x=10, y=180)

l_h_days = Label(bottom_frame, width=25, text='', relief=RAISED, anchor=NW, padx=5, pady=5, font=('Ivy 10'), bg=bgrey, borderwidth=1)
l_h_days.place(x=10, y=210)

l_annual = Label(bottom_frame, width=25, text='', relief=RAISED, anchor=NW, padx=5, pady=5, font=('Ivy 10'), bg=bgrey, borderwidth=1)
l_annual.place(x=10, y=240)

l_hour = Label(bottom_frame, width=300, text='', compound=LEFT, font=('Ivy 10'), anchor=NW, bg=bgrey)
l_hour.place(x=253, y=140)

l_day = Label(bottom_frame, width=300, text='', compound=LEFT, font=('Ivy 10'), anchor=NW,bg=bgrey)
l_day.place(x=253, y=165)

l_week = Label(bottom_frame, width=300, text='', compound=LEFT, font=('Ivy 10'), anchor=NW,bg=bgrey)
l_week.place(x=253, y=195)

l_month = Label(bottom_frame, width=300, text='', compound=LEFT, font=('Ivy 10'), anchor=NW,bg=bgrey)
l_month.place(x=253, y=225)

l_year = Label(bottom_frame, width=300, text='', compound=LEFT, font=('Ivy 10'), anchor=NW,bg=bgrey)
l_year.place(x=253, y=255)



window.mainloop()