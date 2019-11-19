import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from pyfirmata import Arduino, util
from tkinter import *
import time

placa = Arduino('COM3')
it = util.Iterator(placa)
it.start()

cred = credentials.Certificate('keys/key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://parcial-191119.firebaseio.com/'
})

led_9 = placa.get_pin('d:9:p')
led_10 = placa.get_pin('d:10:p')
led_11 = placa.get_pin('d:11:p')

ventana = Tk()
ventana.geometry('1280x800')
ventana.title("Parcial Final: punto 2")  

data1 = db.reference("Sensores/Sensor_0/valor") 
data2 = db.reference("Sensores/Sensor_1/valor")
data3 = db.reference("Sensores/Sensor_2/valor")

def pwn_9():
    led_9.write(data1.get())
    
def pwn_10():
    led_10.write(data2.get())
    
def pwn_11():    
    led_11.write(data3.get())

adc1_update = Button(ventana, text="adc1_update", command= pwn_9)
adc1_update.place(x=50,y=25)
adc2_update = Button(ventana, text="adc2_update", command= pwn_10)
adc2_update.place(x=50,y=50)
adc3_update = Button(ventana, text="adc3_update", command= pwn_11)
adc3_update.place(x=50,y=75)

ventana.mainloop()
