import pyfirmata
import time
import threading
board = pyfirmata.Arduino("/dev/cu.usbmodem14201")

green1 = board.digital[1]
green2 = board.digital[2]
green3 = board.digital[3]
green4 = board.digital[4]
yellow1 = board.digital[5]
yellow2 = board.digital[6]
yellow3 = board.digital[7]
yellow4 = board.digital[8]
red1 = board.digital[9]
red2 = board.digital[10]
red3 = board.digital[11]
red4 = board.digital[12]

#normal traffic light rotation
def normalday():
    threading.Timer(61200.0, normalday).start()
        green1.write[1]
        green2.write[1]
        red3.write[1]
        red4.write[1]
        time.sleep(25)
        green1.write[0]
        green2.write[0]
        yellow1.write[1]
        yellow2.write[1]
        time.sleep(5)
        yellow1.write[0]
        yellow2.write[0]
        red1.write[1]
        red2.write[1]
        red3.write[0]
        red4.write[0]
        green3.write[1]
        green4.write[1]
        time.sleep(25)
        green3.write[0]
        green4.write[0]
        yellow3.write[1]
        yellow4.write[1]
        time.sleep(5)
        yellow3.write[0]
        yellow4.write[0]
        red1.write[0]
        red2.write[0]

#A blinking red light indicates a four-way stop
def nighttime():
    threading.Timer(2520.0, nighttime).start()
        red1.write[1]
        red2.write[1]
        red3.write[1]
        red4.write[1]
        time.sleep(1)
        red1.write[0]
        red2.write[0]
        red3.write[0]
        red4.write[0]
        time.sleep(1)

   #start it at 6am
    normalday()
    nighttime()







