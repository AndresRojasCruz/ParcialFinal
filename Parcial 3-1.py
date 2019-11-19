import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from pyfirmata import Arduino, util
from tkinter import *
import time

placa = Arduino('COM5')
it = util.Iterator(placa)
it.start()

cred = credentials.Certificate('keys/key')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://parcial-191119.firebaseio.com/'
})

analog_0 = placa.get_pin('a:0:i')
analog_1 = placa.get_pin('a:1:i')
analog_2 = placa.get_pin('a:2:i')

ventana = Tk()
ventana.geometry('1280x800')
ventana.title("Parcial Final: punto 1")  

frame1 = Frame(ventana, bg="gray", highlightthickness=1, width=1280, height=800, bd= 5)
frame1.place(x=0, y=0)

read_data0 = analog_0.read()
read_data1 = analog_1.read()
'''read_data2 = analog_2.read()'''

ref = db.reference("Sensores")

ref.set({'sensor1': {'valor': read_data0}})
ref.set({'sensor2': {'valor': read_data1}})
'''ref.set({'sensor3': {'valor': read_data2}})'''

label1 = Label(frame1, bg="white", text=read_data0, font=("Arial Bold", 15), fg="black", width=5)
label1.place(x=20, y=30)
label2 = Label(frame1, bg="white", text=read_data1, font=("Arial Bold", 15), fg="black", width=5)
label2.place(x=20, y=60)
'''label3 = Label(frame1, bg="white", text=read_data2, font=("Arial Bold", 15), fg="black", width=5)
label3.place(x=20, y=90)'''

ventana.mainloop()
