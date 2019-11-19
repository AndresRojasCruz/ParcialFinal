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

led_9 = placa.get_pin('d:9:p')
led_10 = placa.get_pin('d:10:p')
led_11 = placa.get_pín('d:11:p')

ventana = Tk()
ventana.geometry('1280x800')
ventana.title("Parcial Final: punto 2")  

data1 = db.reference("Sensores/sensor1/valor") 
data2 = db.reference("Sensores/sensor2/valor")
data3 = db.reference("Sensores/sensor3/valor")

def pwn_9():
    led_9.write(data1.read())
    
def pwn_10():
    led_10.write(data2.read())
    
def pwn_11():    
    led_11.write(data3.read())

adc1_update = Button(ventana, text="adc1_update", command= pwn_9)
adc1_update.grid(0,0)
adc2_update = Button(ventana, text="adc2_update", command= pwn_10)
adc2_update.grid(1,0)
adc3_update = Button(ventana, text="adc3_update", command= pwn_11)
adc3_update.grid(2,0)

ventana.mainloop()
