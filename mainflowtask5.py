
import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import datetime
import requests
from PIL import ImageTk,Image
from tkinter import messagebox
r=tk.Tk()
r.geometry("600x270")
r.title("Currency Convertor")
r.iconbitmap('C:\\Users\\MARIMUTHU\\Downloads\\icon.ico')

r.maxsize(600,270)
r.minsize(600,270)

image = Image.open('C:\\Users\\MARIMUTHU\\Downloads\\currency.png')
zoom = 0.5

pixel_x,pixel_y=tuple([int(zoom * x) for x in image.size])

img = ImageTk.PhotoImage(image.resize((pixel_x,pixel_y)))
panel = Label(r, image=img)
panel.place(x=190,y=35)

def show_data():
    amt= E1.get()
    from_currency = c1.get()
    to_currency = c2.get()
    url = "https://currencylayer.com/"

    if amt == ' ':
        messagebox.showerror("currency convertor","please fill the amount")
    elif to_currency == ' ':
        messagebox.showerror("currency convertor","please choose the currency")
    else:
        data = requests.get(url).json()
        currency = from_currency.strip()+to_currency.strp()
        amt = int(amt)
        cc = data['quotes'][currency]
        cur_conv = cc*amount
        E2.insert(0,cur_conv)

        text.insert('end', f'{amount} United State Dollar Equals {cur_conv} {to_currency} \n\n Last Time Update \t {datetime.now()}')

def clear():
    E1.delete(0, 'end')
    E2.delete(0, 'end')
    text.delete(1.0, 'end')
l1 = Label(r, text="USD Currency Converter Using Python", font=('verdana', '10', 'bold'))
l1.place(x=150,y=15)

amnt = Label(r, text="Amount", font=('roboto', 10, 'bold'))
amnt.place(x=20,y=15)
E1 = Entry(r, width=20, borderwidth=1, font=('roboto', 10, 'bold'))
E1.place(x=20,y=40)

c1 = tk.StringVar()
c2 = tk.StringVar()
currencychoose1 = ttk.Combobox(r, width = 20, textvariable = c1, state='readonly', font=('verdana', 10, 'bold'))

currencychoose1 ['values'] = (
    'USD',
    )

currencychoose1.place(x=300,y=40)
currencychoose1.current(0)
E2 = Entry(r, width=28, borderwidth=1, font=('roboto', 10, 'bold'))
E2.place(x=20,y=80)
currencychoose2 =  ttk.Combobox(r, width =20, textvariable = c2, state = 'readonly', font=('verdana', '10', 'bold'))

currencychoose2['values'] = ('ALL',
                              'AFN',
                              'ARS',
                              'AWG',
                              'AUD',
                              'AZN',
                              'BSD',
                              'BBD',
                              'BYN',
                              'BZD',
                              'BAM',
                              'BWP',
                              'KHR',
                              'CAD',
                              'KYD',
                              'CLP',
                              'VND',
                              'YER',
                              'ZWD',)
currencychoose2.place( x = 360 ,y = 80 )
currencychoose2.current()
text = Text(r,height=7, width=52, font=('verdana', '10', 'bold'))
text.place(x=100, y = 120 )
B = Button (r, text="Search", command=show_data, font=('verdana', '10', 'bold'), borderwidth=2, bg="red", fg="white")
B.place( x = 20 ,y = 120 )
clear = Button(r, text="Clear", command=clear, font=('verdana', '10', 'bold'), borderwidth=2, bg="blue", fg="white")
clear.place(x = 20 ,y = 170 )
r.mainloop()

 

        
