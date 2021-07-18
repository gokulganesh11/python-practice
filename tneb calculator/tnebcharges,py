from tkinter import *

root=Tk() 
root.title("TANGEDCO")
canvas1 = Canvas(root, width = 700, height = 400)
canvas1['bg']= "#666699"
root.resizable(0,0)
canvas1.pack()

txtinp_1 = Text(root, height = 1.4,width = 12,bg = "white",font="Arial 20 bold")
canvas1.create_window(340,140, window=txtinp_1)
canvas1.create_text(240,80,text="Units Consumed",font = "Verdana 16 bold",anchor='nw',fill="#cc0066")

def calci():
    try:
        userinput=float(txtinp_1.get("1.0", "end-1c"))
        if 0<=userinput<=100:
            service=0
        elif 101<=userinput<=200:
            service=(userinput*1.50)-150+20
        elif 201<=userinput<=500:
            third=userinput-200
            service=(third*3)+150+200+30-150
        elif 501<=userinput:
            fourth=userinput-500
            service=(fourth*6.60)+1380+350+150+50-150
        result = Label (root,text = service,height=1,width=10,font="Arial 18 bold",fg="green",bg="white")
        canvas1.create_window(340,265,window=result)
    except:
        service="Invalid Input"
        result = Label (root,text = service,height=1,width=10,font="Arial 18 bold",fg="#ff0000",bg="white")
        canvas1.create_window(340,265,window=result)
canvas1.create_text(220,10,text="TNEB Bill Calculator",font = "Summit 18 bold",anchor='nw',fill="#000099")

btn1 = Button (root, text='Calulate',command=calci, height =1, width = 12,font = "Verdana 12 bold")
canvas1.create_window(340,210, window=btn1)

root.mainloop()
