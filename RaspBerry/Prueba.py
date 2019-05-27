import RPi.GPIO as GPIO
import time

from uuid import uuid4 as uuid
import pyqrcode
from collections import OrderedDict
import requests
import qrcode


#__variable de ejemplo para los codigos
ejemplo=uuid().hex[:15]

code = pyqrcode.create(ejemplo)

url = 'https://hci-server-uvg.herokuapp.com/machine/code'
params = OrderedDict([('code', ejemplo), ('points', 10)])

results = requests.post(url, data={'code': ejemplo, 'points':10})
print(results)

code.png('code.png', scale=8)

GPIO.setmode(GPIO.BOARD)
PIN_TRIGGER = 7
PIN_ECHO = 11
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)
GPIO.output(PIN_TRIGGER, GPIO.LOW)
time.sleep(2)
GPIO.output(PIN_TRIGGER, GPIO.HIGH)
time.sleep(0.00001)
GPIO.output(PIN_TRIGGER, GPIO.LOW)

while True:
	while GPIO.input(PIN_ECHO)==0:
		pulse_start_time = time.time()
	while GPIO.input(PIN_ECHO)==1:
		pulse_end_time = time.time()

	pulse_duration = pulse_end_time - pulse_start_time
	distance = round(pulse_duration * 17150, 2)
	print(distance)
	if distance < 10:
		qrcode.code()
	time.sleep(1)

