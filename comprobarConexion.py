import time
import os
from ctypes import windll, byref
from ctypes.wintypes import DWORD
from playsound import playsound

def comprobarConexion():
    flags = DWORD()
    conexion = windll.wininet.InternetGetConnectedState(byref(flags), None)
    return conexion

while(True):
    if not comprobarConexion():
        playsound('Winding_Alarm_Clock.mp3')
    else:
        playsound('Bugle_Tune.mp3')
    time.sleep(5)
