#import library dan connect wifi
from time import sleep
import uos, machine
from wifi import connect
connect("Mau nyambung?", "kosongsatu")
import gc
gc.collect()

#import dari monitor_voltage
from monitor_voltage import cari_ph
from sensor_gas import gas_1
from sensor_gas import gas_2
from sensor_gas import gas_3
from sensor_gas import send_gas

while True:
    print ("------------------------------------------------")
    gas_1()
    gas_2()
    gas_3()
    send_gas()
    print ("------------------------------------------------")
    cari_ph()
    sleep(5)
