import network

#ledPin = 13

def connect (ssid: str, password:str):
    conn = network.WLAN(network.STA_IF)
    if conn.isconnected() == True:
        print("Already connected")
        print(conn.ifconfig())
        return
    
    conn.active(True)
    conn.connect(ssid, password)
    
    while conn.isconnected() == False:
        pass
    
    print("Connected!")
    print(conn.ifconfig())
