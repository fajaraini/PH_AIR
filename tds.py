from machine import Pin, ADC
from time import sleep

import urequests
import esp
esp.osdebug(None)

api_key = 'd1LV6yoFVxldM3RDRjt3pg'

#ambil data ph di D32
pot = ADC(Pin(32))
pot.atten(ADC.ATTN_11DB)

def sensor_tds():
    #cari nilai konduktivitas
    data_value = pot.read()
    print("Nilai Konduktifitas ", data_value)
    
    #send data sensor
    sensor_readings = {'value1':data_value}
    print(sensor_readings)

    request_headers = {'Content-Type': 'application/json'}

    request = urequests.post(
        'http://maker.ifttt.com/trigger/Konduktivitas_Air/with/key/' + api_key,
         json=sensor_readings,
        headers=request_headers)
    print(request.text)
    request.close()
    sleep(5)
