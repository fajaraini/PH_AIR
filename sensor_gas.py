from machine import Pin, ADC
from time import sleep
import math
import urequests
import esp
esp.osdebug(None)

RO_135= 4.82
b_CO = 0.59
m_CO = -0.22

pot = ADC(Pin(33))
pot.atten(ADC.ATTN_11DB)

pin = ADC(Pin(34))
pin.atten(ADC.ATTN_11DB)

put = ADC(Pin(35))
put.atten(ADC.ATTN_11DB)


def gas_1():
    MQ135_volt = pot.read()* 5/ 4095
    RS_MQ135 = ((5.0*2.7)/MQ135_volt)-2.7
    Ratio_MQ135 = RS_MQ135/RO_135
    #PPM
    global ppmCO_1
    ppmco_log = (math.log10(Ratio_MQ135)-b_CO)/m_CO
    ppmCO_1 = 10**ppmco_log
    
    print("ppm MQ135 1 : ", ppmCO_1)
    
def gas_2():
    MQ135_volt = pin.read()* 5/ 4095
    RS_MQ135 = ((5.0*2.7)/MQ135_volt)-2.7
    Ratio_MQ135 = RS_MQ135/RO_135
    #PPM
    global ppmCO_2
    ppmco_log = (math.log10(Ratio_MQ135)-b_CO)/m_CO
    ppmCO_2 = 10**ppmco_log
    
    print("ppm MQ135 2 : ", ppmCO_2)

def gas_3():
    MQ135_volt = put.read()* 5/ 4095
    RS_MQ135 = ((5.0*2.7)/MQ135_volt)-2.7
    Ratio_MQ135 = RS_MQ135/RO_135
    #PPM
    global ppmCO_3
    ppmco_log = (math.log10(Ratio_MQ135)-b_CO)/m_CO
    ppmCO_3 = 10**ppmco_log
    
    print("ppm MQ135 3 : ", ppmCO_3)
    
def send_gas():
    #send data sensor gas
    api_key = 'd1LV6yoFVxldM3RDRjt3pg'
    sensor_readings = {'value1':ppmCO_1,'value2':ppmCO_2, 'value3':ppmCO_3 }
    print(sensor_readings)

    request_headers = {'Content-Type': 'application/json'}

    request = urequests.post(
        'http://maker.ifttt.com/trigger/Gas/with/key/' + api_key,
         json=sensor_readings,
        headers=request_headers)
    print(request.text)
    request.close()
    sleep(5)
