from datetime import datetime
import pytz
from tkinter import *
from tkinter import ttk
import time
from time import strftime

root = Tk()
root.title('TimeZones')
root.geometry("590x230")
label = ttk.Label(root, text = "")
label.pack()
label.config(wraplength = 10)
#label.config(justify = '')
label.config(foreground = '', background = '')
label.config(font = ('Courier', 18, 'bold'),foreground = 'blue')
logo = PhotoImage(file = 'python_logo.png') # change path to image as necessar
label.config(image = logo)
label.place(x = 0,y = 10)
label.config(compound = 'left')
label.img = logo
label.config(image = label.img)
current_time=''



favicon = PhotoImage(file = 'python_logo.png')
# Icon set for program window
root.iconphoto(False, favicon)
# Button creation





def times():
    get_time=pytz.timezone('US/Pacific')
    local_time=datetime.now(get_time)
    current_time=local_time.strftime("%I:%M:%S %p")
    clock.config(text=current_time)
    name.config(text="Local Time")
    
    get_time=pytz.timezone('America/Indiana/Indianapolis')
    local_time=datetime.now(get_time)
    current_time=local_time.strftime("%I:%M:%S %p")
    clock1.config(text= current_time)
    name1.config(text="Minnesota")
  
    
    get_time=pytz.timezone('Asia/Shanghai')
    local_time=datetime.now(get_time)
    current_time=local_time.strftime("%I:%M:%S %p")
    clock2.config(text=current_time)
    name2.config(text=" Beijing")
    

    get_time=pytz.timezone('Europe/Paris')
    local_time=datetime.now(get_time)
    current_time=local_time.strftime("%I:%M:%S %p")
    clock3.config(text=current_time)
    name3.config(text=" Belgrade")
    clock3.after(200,times)



name=Label(root,font=("times",20,"bold"))
name.place(x=183,y=5)
clock=Label(root,font=("times",25,"bold"))
clock.place(x=183,y=40)
nota=Label(root,text="Hours  minutes seconds  ",font="times 10 bold" )
nota.place(x=184,y=80)


name1=Label(root,font=("times",20,"bold"))
name1.place(x=390,y=5)
clock1=Label(root,font=("times",25,"bold"))
clock1.place(x=390,y=40)
nota1=Label(root,text=" Hours  minutes seconds  ", font="times 10 bold")
nota1.place(x=390,y=80)



name2=Label(root,font=("times",20,"bold"))
name2.place(x=180,y=105)
clock2=Label(root,font=("times",25,"bold"))
clock2.place(x=184,y=140)
nota2=Label(root,text="Hours  minutes seconds   ",font="times 10 bold")
nota2.place(x=184,y=180)




name3=Label(root,font=("times",20,"bold"))
name3.place(x=386,y=105)
clock3=Label(root,font=("times",25,"bold"))
clock3.place(x=390,y=140)
nota3=Label(root,text="  Hours  minutes seconds   ",font="times 10 bold")
nota3.place(x=390,y=180)






times()

root.mainloop()
'''
get_time=pytz.timezone('Asia/Bangkok')
local_time=datetime.now(get_time)
current_time=local_time.strftime("%H:%M:%S")
print(current_time)'''

for tz in pytz.all_timezones():get_time=pytz.timezone('US/Pacific')
local_time=datetime.now(get_time)
current_time=local_time.strftime("%H:%M:%S")
clock.config(text=current_time)
name.config(text="Local Time")
print(tz)
