import pyfirmata
import time

board = pyfirmata.Arduino('COM5')
it = pyfirmata.util.Iterator(board)
it.start()
led_pin = board.get_pin("d:10:o")

while True:
    led_pin.write(1)
    time.sleep(0.1)
    led_pin.write(0)
    time.sleep(0.1)