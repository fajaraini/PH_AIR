from machine import Pin, ADC
from time import sleep

import urequests
import esp
esp.osdebug(None)

api_key = 'd1LV6yoFVxldM3RDRjt3pg'

#ambil data ph di D32
pot = ADC(Pin(32))
pot.atten(ADC.ATTN_11DB)

#nilai_kalibrasi
PH4 = 3.3
PH7 = 2.90


def cari_ph():
    # if(PH4 = 3.1 and PH7 = 2.6)
    #cari nilai voltage
    global pot_value
    pot_value = pot.read()* 3.3 / 4095
    #Voltage = pot_value * (3.3 / 1023.0)
    print("Nilai PH pot-value ", pot_value)
    
    #cari nilai ph
    PH_step = (PH4-PH7)/3
    po= 4.00 + (PH7-pot_value)/PH_step
    print("Nilai PH saat ini", po)
    
    #send data sensor
    sensor_readings = {'value1':pot_value,'value2 ':po,}
    print(sensor_readings)

    request_headers = {'Content-Type': 'application/json'}

    request = urequests.post(
        'http://maker.ifttt.com/trigger/Konduktivitas_Ph/with/key/' + api_key,
         json=sensor_readings,
        headers=request_headers)
    print(request.text)
    request.close()
    sleep(5)