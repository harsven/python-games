#Timer
#import modules

import simplegui

#global Varibles
a=0
b=0
c=0
lalit=""
chances=0
total=0
#draw handlers
def display_timer(canvas):
    global a,b,c
    if (a<10):
        a='0'+str(a)
    if (b<10):
        b='0'+str(b)
    canvas.draw_text("Timer",[118,30],25,"cornflowerblue")
    canvas.draw_text(str(chances)+'/'+str(total),[250,30],20,"cornflowerblue")
    canvas.draw_text(str(a)+':'+str(b)+'.'+str(c),[110,100],25,"cornflowerblue")
    canvas.draw_text(lalit, [250,180], 15, "cornflowerblue")
    if (total==5):
        if (chances<3):
            canvas.draw_text("Your reflexes could be improved",[35,145],20,"cornflowerblue")
        elif (chances>2):
            canvas.draw_text("Your reflexes are reasonable",[35,145],20,"cornflowerblue")
        elif (chances==5):
            canvas.draw_text("Your reflexes are incredible",[35,145],20,"cornflowerblue")
    a=int(a)
    b=int(b)
    c=int(c)
    if (a>=1):
        canvas.draw_text("You didn't reset your timer for long time",[35,150],20,"cornflowerblue")

def time_handler(): 
    global a,b,c
    c+=1
    if (c==10):
        b+=1
        c=0
        if (b==60):
            a+=1
            b=0    

def start_timer():
    global chances,total
    timer.start()
     
def pause_timer():
    global chances
    global total
    timer.stop()
    if (c==0):
        chances+=1
    total+=1

def stop_timer():
    global chances
    global total
    global a,b,c
    timer.stop()
    total=0
    chances=0
    a=0 
    b=0 
    c=0
    
#create frame
frame= simplegui.create_frame("Timer",300,300)
frame.set_canvas_background('White')

#register event handlers
screen=frame.set_draw_handler(display_timer)
timer=simplegui.create_timer(100, time_handler)
button1=frame.add_button("Start",start_timer,150)
button2=frame.add_button("Stop",pause_timer,150)
button3=frame.add_button("Reset",stop_timer,150)
label_d=frame.add_label("Description:")
label_d2=frame.add_label("Press START to start the timer.\nStop timer using STOP button.\nStop timer on 0th milisecond\n")
label_d3=frame.add_label("Press RESET to reset the timer and score.") 

#start frame
frame.start()
