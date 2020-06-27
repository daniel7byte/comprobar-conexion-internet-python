import time
import os
from ctypes import windll, byref
from ctypes.wintypes import DWORD
from socket import gethostbyname, create_connection, error
from playsound import playsound

def comprobarConexion():
    flags = DWORD()
    conexion = windll.wininet.InternetGetConnectedState(byref(flags), None)
    return conexion

def comprobarConexionAlterno():
    try:
        gethostbyname("google.com")
        conexion = create_connection(("google.com", 80), 1)
        conexion.close()
        return True
    except error:
        return False

while(True):
    if not (comprobarConexion() or comprobarConexionAlterno()):
        print("No hay internet")
        playsound('Winding_Alarm_Clock.mp3')
    else:
        print("Hay internet")
        playsound('Bugle_Tune.mp3')
    time.sleep(5)
