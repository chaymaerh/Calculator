import RPi.GPIO as GPIO
import time
from RPLCD import CharLCD


L1 = 25
L2 = 8
L3 = 7
L4 = 1

C1 = 12
C2 = 16
C3 = 20
C4 = 21

lcd = CharLCD(numbering_mode=GPIO.BCM,cols=16, rows=2, pin_rs=26, pin_e=19, pins_data=[13, 6, 5, 11])
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

num=''
def  readLine (ligne, characters) :
    if ligne==25:

        GPIO.output(ligne, GPIO.HIGH)
        if(GPIO.input(C1) == 1):
            lcd.clear()
            display(1)
        if(GPIO.input(C2) == 1):
            lcd.clear()
            display(2)
        if(GPIO.input(C3) == 1):
            lcd.clear()
            display(3)
        if(GPIO.input(C4) == 1):
            lcd.clear()
            display('+')
                 
            
        GPIO.output(ligne, GPIO.LOW)
        
    if ligne==8:
        GPIO.output(ligne, GPIO.HIGH)
        if(GPIO.input(C1) == 1):
            lcd.clear()
            display(4)
        if(GPIO.input(C2) == 1):
            lcd.clear()
            display(5)
        if(GPIO.input(C3) == 1):
            lcd.clear()
            display(6)
        if(GPIO.input(C4) == 1):
            lcd.clear()
            display('-')   
        GPIO.output(ligne, GPIO.LOW)
    if ligne==7:

        GPIO.output(ligne, GPIO.HIGH)
        if(GPIO.input(C1) == 1):
            lcd.clear()
            display(7)
        if(GPIO.input(C2) == 1):
            lcd.clear()
            display(8)
        if(GPIO.input(C3) == 1):
            lcd.clear()
            display(9)
        if(GPIO.input(C4) == 1):
            lcd.clear()
            display('*')   
        GPIO.output(ligne, GPIO.LOW)
    if ligne==1:

        GPIO.output(ligne, GPIO.HIGH)
        if(GPIO.input(C1) == 1):
            lcd.clear()
            clear_scr()
        if(GPIO.input(C2) == 1):
            lcd.clear()
            display(0)
        if(GPIO.input(C3) == 1):
            lcd.clear()
            equal_btn()
        if(GPIO.input(C4) == 1):
            lcd.clear()
            display('/')   
        GPIO.output(ligne, GPIO.LOW)

# 

# 


def display(number):
    global num 
    num = num + str(number)
    lcd.write_string(num)

def clear_scr():
    global num
    num =''
    lcd.write_string(num)

def equal_btn():
     global num
     add=str(eval(num))
     lcd.write_string(add)
     num=''
def equal_btn():
     global num
     sub=str(eval(num))
     lcd.write_string(sub)
     num=''     
def equal_btn():
     global num
     mul=str(eval(num))
     lcd.write_string(mul)
     num=''
def equal_btn_div():
     global num
     div=str(eval(num))
     lcd.write_string(mul)
     num=''    

try :
     while  True :
         
        readLine(L1, [ "1" , "2" , "3" , "+" ])
        readLine(L2, [ "4" , "5" , "6" , "-" ])
        readLine(L3, [ "7" , "8" , "9" , "x" ])
        readLine(L4, [ "c" , "0" , "=" , "/" ])
        time.sleep( 0.1 )
except KeyboardInterrupt :
    print( "\nApplication arrêtée !" )