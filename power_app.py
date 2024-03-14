from tkinter import *
import os

def sleep():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def restart():
    os.system("shutdown -r -t 1")

def shutdown():
    os.system("shutdown -s -t 1")

st = Tk()
st.title("Power Window")
st.geometry("500x500")
st.config()
#sleep
buttons = Button(st,text="Sleep",font=('arial narrow',20,'bold'),cursor="hand2",command=sleep)
buttons.place(x=150, y=60, width=200, height=50)
#Restart button
buttons = Button(st,text="Restart",font=('arial narrow',20,'bold'),cursor="hand2",command=restart)
buttons.place(x=150, y=170, width=200, height=50)
#Shut down button
buttons = Button(st,text="Shut down",font=('arial narrow',20,'bold'),cursor="hand2",command=shutdown)
buttons.place(x=150, y=270, width=200, height=50)
#Cancel button
buttons = Button(st,text="Cancel",font=('arial narrow',20,'bold'),cursor="hand2",command=st.destroy)
buttons.place(x=150, y=370, width=200, height=50)

st.mainloop()