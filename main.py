import tkinter 

def main():
    if start_typing():
        window.after(3000,no_typing)
    else:
        window.after(100,main)
       
def start_typing():
    if len(text_entry.get("1.0","end-1c")) > 0 :
        session_count_down(SESSION_TIME)
        return True

def no_typing():
    global old_lenght
    new_lenght = len(text_entry.get("1.0","end-1c").split())
    if new_lenght == old_lenght:
        delete_count_down(DELETE_TIME)
    else:
        old_lenght = new_lenght
        window.after(3000,no_typing)    
   
def session_count_down(count):
    global x, main_timer
    secends = (count * 60) - x
    count_sec = secends % 60
    if count_sec < 10:
        session_timer.config(text=f"{count}:0{count_sec}",font=('Time New Roman',18,'normal'),fg='blue')
    else:
        session_timer.config(text=f"{count}:{count_sec}",font=('Time New Roman',18,'normal'),fg='blue')
    if secends > 0:
        x += 1
        main_timer = window.after(1000, session_count_down,count)

def delete_count_down(delete_time):
    global count, main_timer, seconde_timer,text_entry
    window.after_cancel(main_timer)  
    session_timer.config(text=f"{delete_time}",font=('Time New Roman',18,'bold'),fg='red')
    if delete_time > 0 :
        new_lenght = len(text_entry.get("1.0","end-1c").split())
        if new_lenght != old_lenght:
            window.after_cancel(seconde_timer)
            session_count_down(SESSION_TIME)
            no_typing()
        else:
            seconde_timer = window.after(1000,delete_count_down,delete_time-1)
    else:
        text_entry.delete("1.0","end-1c")
            

old_time = 0
x = 0
#session time in minute
SESSION_TIME = 5
#after how many second delete all texts? 
DELETE_TIME = 5

window = tkinter.Tk()
window.title('most dangerous app')
window.minsize(width=800,height=800)

session_timer = tkinter.Label(text='00:00',font=('Time New Roman',18,'normal'),fg='blue')
session_timer.grid(column=0,row=0,pady=10)
description = tkinter.Label(text="Type your thoughts,idea and what's on your mind continuously \n don't stop! \n caution: if you don't type any ''new word'' after some seconds all efforts whould be delete! ",
                            font=('Time New Roman',12,'normal'))
description.grid(column=0,row=1,pady=10)

text_entry = tkinter.Text(width=90,height=40)
text_entry.grid(column=0,row=2,padx=50)


old_lenght = len(text_entry.get("1.0","end-1c").split())
window.after(100,main)
   

window.mainloop()


