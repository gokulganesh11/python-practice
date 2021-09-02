from tkinter import *
import winsound 

root=Tk() 
root.geometry('300x200')
root.title('Checkbox Demo')

canvas1 = Canvas(root, width = 800, height = 500) 
canvas1['bg']= "light blue"
root.resizable(0,0)
canvas1.pack()

var1 = StringVar()
def sound():
    print(var1.get())
    if var1.get()=="on":
        winsound.Beep(400, 1000)

check_1=Checkbutton(root, text="Accept", variable=var1,onvalue="on",offvalue="off")
canvas1.create_window(50,50, window=check_1)
check_1.deselect()
btn1 =Button(root, text='Submit',command=sound, height =1, width = 12,font = "Verdana 12 bold")
canvas1.create_window(100,100, window=btn1)

root.mainloop()
