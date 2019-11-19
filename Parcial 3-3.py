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

led_8 = placa.get_pin('d:8:o')
led_9 = placa.get_pin('d:9:o')
led_10 = placa.get_pín('d:10:o')
led_11 = placa.get_pin('d:11:o')
led_12 = placa.get_pin('d:12:o')
led_13 = placa.get_pín('d:13:o')

ventana = Tk()
ventana.geometry('1280x800')
ventana.title("Parcial Final: punto 3")

def entrada(input):
    content = entry.get()
    if int(content) == 


ref = db.reference("Leds")

ref.set({'led9': {'valor': }})



