from tkinter import * 
roof=Tk()
roof.title("Basic Calculator")

screen=Entry(roof,borderwidth="5",width="35")
screen.grid(row="0",column="0",columnspan="3",padx="10",pady="10")
def clickbutton(number):
    a=screen.get() 
    screen.delete(0,END)
    screen.insert(0,str(a) + str(number))
button1=Button(roof,text="1",fg="black",padx="40",pady="20", command=lambda: clickbutton(1))    
button0=Button(roof,text="0",fg="black",padx="40",pady="20",command=lambda :clickbutton(0))   
button2=Button(roof,text="2",fg="black",padx="40",pady="20",command=lambda :clickbutton(2))
button3=Button(roof,text="3",fg="black",padx="40",pady="20",command=lambda :clickbutton(3))   
button4 =Button(roof,text="4",fg="black",padx="40",pady="20",command=lambda: clickbutton(4)) 
button5=Button(roof,text="5",fg="black",padx="40",pady="20",command=lambda :clickbutton(5))
button6=Button(roof,text="6",fg="black",padx="40",pady="20",command=lambda :clickbutton(6))
button7=Button(roof,text="7",fg="black",padx="40",pady="20",command=lambda :clickbutton(7))
button8 =Button(roof,text="8",fg="black",padx="40",pady="20",command=lambda :clickbutton(8))
button9=Button(roof,text="9",fg="black",padx="40",pady="20",command=lambda :clickbutton(9))
  
button1.grid(column="0",row="3")
button2.grid(column="1",row="3")
button3.grid(column="2",row="3")

button4.grid(column="0",row="2")
button5.grid(column="1",row="2")
button6.grid(column="2",row="2")

button7.grid(column="0",row="1")
button8.grid(column="1",row="1")
button9.grid(column="2",row="1")
button0.grid(row="4",column="0")

   
    

def toplamaa():
    first_number=screen.get()                    
    num=int(first_number)
    global f_num 
    global math
    f_num=num
    screen.delete(0,END)
    math="toplama"
    


    
def cikartmaa():
    first_number=screen.get()
    num=int(first_number)
    global f_num 
    global math
    math="cıkartma"
    f_num=num
    screen.delete(0,END)
    
    
def carpmaa():

    first_number=screen.get()
    num=int(first_number)
    global f_num 
    global math
    f_num=num
    screen.delete(0,END)
    math="carpma"

def bolmee():
    
    first_number=screen.get()
    num=int(first_number)
    global f_num
    global math
    f_num=num
    screen.delete(0,END)
    math="bolme"


def temizle():
    screen.delete(0,END)




def esittir():
    screen.delete(0,END)
    secondnumber=screen.get()
    snum=int(secondnumber)

    
    if (math=="toplama"):
        screen.insert(0,f_num + snum)
    if math=="cıkartma":
        screen.insert(0,f_num-snum)
    if math=="carpma":
        screen.insert(0,f_num*snum)
    if math=="bolme":
       screen.insert(0,f_num/snum)
             




button_clear=Button(roof,text="Clear",fg="black",padx="79",pady="20",command=temizle)
button_add=Button(roof,text="+",fg="black",padx="39",pady="20",command=toplamaa )
button_eksi=Button(roof,text="-",fg="black",padx="39",pady="20",command=cikartmaa)
button_bolme=Button(roof,text="/",fg="black",padx="39",pady="20",command=bolmee)
Button_carpma=Button(roof,text="X",fg="black",padx="39",pady="20" ,command=carpmaa)
Button_equal=Button(roof,text="=",fg="black",padx="91",pady="20",command=esittir)


button_clear.grid(row="4",column="1",columnspan="2")
button_add.grid(row="5",column="0")
button_eksi.grid(row="6",column="0")
Button_carpma.grid(row="6",column="1")
button_bolme.grid(row="6",column="2")
Button_equal.grid(row="5",column="1",columnspan="2")
roof.mainloop()
