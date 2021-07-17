from tkinter import *

root=Tk() 
root.title("Interest calulater")

canvas1 = Canvas(root, width = 800, height = 500) 
canvas1['bg']= "light blue"
canvas1.create_line(400, 40, 400, 450,fill="Black", tags="line",width=5)
canvas1.create_line(0, 250, 800, 250,fill="Black", tags="line",width=5)
root.resizable(0,0)
canvas1.pack()

#FIRST
def calci_1():
    try:
        principle_1=float(txtinp_11.get("1.0", "end-1c"))
        no_of_years_1=float(txtinp_12.get("1.0", "end-1c"))
        rate_of_interest_1=float(txtinp_13.get("1.0", "end-1c"))
        output_1=principle_1*(1+((rate_of_interest_1/100)*no_of_years_1))
        result_1 = Label (root,text = output_1,height=1,width=10,font="Arial 14 bold",fg="green",bg="white")
        canvas1.create_window(300,210,window=result_1)
    except:
        result_1 = Label (root,text ="Invalid Input",height=1,width=10,font="Arial 14 bold",fg="#ff1a1a",bg="white")
        canvas1.create_window(300,210,window=result_1)

txtinp_11 = Text(root, height = 1.4,width = 12,bg = "white",font="Arial 12 bold")
canvas1.create_window(300,100, window=txtinp_11)
txtinp_12= Text(root, height = 1.4,width = 12,bg = "white",font="Arial 12 bold")
canvas1.create_window(300,135, window=txtinp_12)
txtinp_13= Text(root, height = 1.4,width = 8,bg = "white",font="Arial 12 bold")
canvas1.create_window(320,170, window=txtinp_13)

canvas1.create_text(60,85,text="Principle :",font = "Verdana 14 bold",anchor='nw')
canvas1.create_text(60,120,text="No of years :",font = "Verdana 14 bold",anchor='nw')
canvas1.create_text(60,155,text="Rate Of Interest :",font = "Verdana 14 bold",anchor='nw')

#SECOND
def calci_2():
    try:
        total_amount_2=float(txtinp_21.get("1.0", "end-1c"))
        no_of_years_2=float(txtinp_22.get("1.0", "end-1c"))
        rate_of_interest_2=float(txtinp_23.get("1.0", "end-1c"))
        output_2=total_amount_2/(1+((rate_of_interest_2/100)*no_of_years_2))
        result_2 = Label (root,text = output_2,height=1,width=10,font="Arial 14 bold",fg="green",bg="white")
        canvas1.create_window(700,210,window=result_2)
    except:
        result_2 = Label (root,text ="Invalid Input",height=1,width=10,font="Arial 14 bold",fg="#ff1a1a",bg="white")
        canvas1.create_window(700,210,window=result_2)

txtinp_21 = Text(root, height = 1.4,width = 12,bg = "white",font="Arial 12 bold")
canvas1.create_window(700,100, window=txtinp_21)
txtinp_22= Text(root, height = 1.4,width = 12,bg = "white",font="Arial 12 bold")
canvas1.create_window(700,135, window=txtinp_22)
txtinp_23= Text(root, height = 1.4,width = 8,bg = "white",font="Arial 12 bold")
canvas1.create_window(700,170, window=txtinp_23)

canvas1.create_text(450,85,text="Total Amount :",font = "Verdana 14 bold",anchor='nw')
canvas1.create_text(450,120,text="No of years :",font = "Verdana 14 bold",anchor='nw')
canvas1.create_text(450,155,text="Rate Of Interest :",font = "Verdana 14 bold",anchor='nw')

#Third
def calci_3():
    try:
        total_amount_3=float(txtinp_31.get("1.0", "end-1c"))
        principle_3=float(txtinp_32.get("1.0", "end-1c"))
        rate_of_interest_3=float(txtinp_33.get("1.0", "end-1c"))
        output_3=round(1/(rate_of_interest_3/100)*(total_amount_3/ principle_3-1),2)
        result_3 = Label (root,text = output_3,height=1,width=10,font="Arial 14 bold",fg="green",bg="white")
        canvas1.create_window(300,450,window=result_3)
    except:
        result_3 = Label (root,text ="Invalid Input",height=1,width=10,font="Arial 14 bold",fg="#ff1a1a",bg="white")
        canvas1.create_window(300,450,window=result_3)

txtinp_31 = Text(root, height = 1.4,width = 12,bg = "white",font="Arial 12 bold")
canvas1.create_window(300,315, window=txtinp_31)
txtinp_32= Text(root, height = 1.4,width = 12,bg = "white",font="Arial 12 bold")
canvas1.create_window(300,350, window=txtinp_32)
txtinp_33= Text(root, height = 1.4,width = 8,bg = "white",font="Arial 12 bold")
canvas1.create_window(320,385, window=txtinp_33)

canvas1.create_text(60,300,text="Total Amount :",font = "Verdana 14 bold",anchor='nw')
canvas1.create_text(60,335,text="Principle :",font = "Verdana 14 bold",anchor='nw')
canvas1.create_text(60,370,text="Rate Of Interest :",font = "Verdana 14 bold",anchor='nw')

#Four
def calci_4():
    try:
        total_amount_4=float(txtinp_41.get("1.0", "end-1c"))
        principle_4=float(txtinp_42.get("1.0", "end-1c"))
        no_of_years_4=float(txtinp_43.get("1.0", "end-1c"))
        output_4=round((1/(no_of_years_4)*(total_amount_4/ principle_4-1)*100),2)
        result_4 = Label (root,text = output_4,height=1,width=10,font="Arial 14 bold",fg="green",bg="white")
        canvas1.create_window(700,450,window=result_4)
    except:
        result_4 = Label (root,text = "Invalid Input",height=1,width=10,font="Arial 14 bold",fg="#ff1a1a",bg="white")
        canvas1.create_window(700,450,window=result_4)

txtinp_41 = Text(root, height = 1.4,width = 12,bg = "white",font="Arial 12 bold")
canvas1.create_window(700,315, window=txtinp_41)
txtinp_42= Text(root, height = 1.4,width = 12,bg = "white",font="Arial 12 bold")
canvas1.create_window(700,350, window=txtinp_42)
txtinp_43= Text(root, height = 1.4,width = 8,bg = "white",font="Arial 12 bold")
canvas1.create_window(700,385, window=txtinp_43)

canvas1.create_text(450,300,text="Total Amount :",font = "Verdana 14 bold",anchor='nw')
canvas1.create_text(450,335,text="Principle :",font = "Verdana 14 bold",anchor='nw')
canvas1.create_text(450,370,text="No of years :",font = "Verdana 14 bold",anchor='nw')

#tiltle
canvas1.create_text(260,10,text="Simple interest calculator",font = "Summit 18 bold",anchor='nw',fill="#660066")
canvas1.create_text(80,40,text="Total Amount",font = "Verdana 14 bold",anchor='nw',fill="#cc0066")
canvas1.create_text(500,40,text="Principle Amount",font = "Verdana 14 bold",anchor='nw',fill="#cc0066")
canvas1.create_text(80,260,text=" No of Years",font = "Verdana 14 bold",anchor='nw',fill="#cc0066")
canvas1.create_text(520,260,text="Interest",font = "Verdana 14 bold",anchor='nw',fill="#cc0066")


# bottom
btn1 = Button (root, text='Submit',command=calci_1, height =1, width = 12,font = "Verdana 12 bold")
canvas1.create_window(100,210, window=btn1)

btn2 = Button (root, text='Submit',command=calci_2, height =1, width = 12,font = "Verdana 12 bold")
canvas1.create_window(500,210, window=btn2)

btn3 = Button (root, text='Submit',command=calci_3, height =1, width = 12,font = "Verdana 12 bold")
canvas1.create_window(100,450, window=btn3)

btn4 = Button (root, text='Submit',command=calci_4, height =1, width = 12,font = "Verdana 12 bold")
canvas1.create_window(500,450, window=btn4)
root.mainloop()
