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

led_8 = placa.get_pin('d:8:o')
led_9 = placa.get_pin('d:9:o')
led_10 = placa.get_pin('d:10:o')
led_11 = placa.get_pin('d:11:o')
led_12 = placa.get_pin('d:12:o')
led_13 = placa.get_pin('d:13:o')

ventana = Tk()
ventana.geometry('1280x800')
ventana.title("Parcial Final: punto 3")

led8 = db.reference("Leds/led_8")
led9 = db.reference("Leds/led_9")
led10 = db.reference("Leds/led_10")
led11 = db.reference("Leds/led_11")
led12 = db.reference("Leds/led_12")
led13 = db.reference("Leds/led_13")

def save():
    print(leds.get())
    num = leds.get()
    print(OnOff.get())
    data = OnOff.get()
    if num == 8:
        led8.set({'Valor': data})
    if num == 9:
        led9.set({'Valor': data})
    if num == 10:
        led10.set({'Valor': data})
    if num == 11:
        led11.set({'Valor': data})
    if num == 12:
        led12.set({'Valor': data})
    if num == 13:
        led13.set({'Valor': data})
    
def update():
    led_8.write(led8.get())
    led_9.write(led9.get())
    led_10.write(led10.get())
    led_11.write(led11.get())
    led_12.write(led12.get())
    led_13.write(led13.get())
    

Label(ventana, text="Ingresa numero del 8-13 ").place(x=50, y=25)
leds = Entry(ventana)
leds.place(x=50,y=50)
Label(ventana, text="ON = 1, OFF = 0 ").place(x=50, y=75)
OnOff = Entry(ventana)
OnOff.place(x=50,y=100)


guardar = Button(ventana, text="Guardar", command= save)
guardar.place(x=200,y=50)
actualizar = Button(ventana, text="Actualizar", command= update)
actualizar.place(x=200,y=100)


ventana.mainloop()

