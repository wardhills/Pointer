import time
import network

import secrets

def wifi(ssid, password):

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

     # Wait for connect or fail
    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
            max_wait -= 1
            print('waiting for connection...')
            time.sleep(1)

    # Handle connection error
    if wlan.status() != 3:
        raise RuntimeError('network connection failed')
    else:
        print('connected')
        status = wlan.ifconfig()
        print( 'ip = ' + status[0] )

def main():
    networks = secrets.wifi_networks()

    for key in networks:
        print(key)
        ssid = key
        password = networks[key]

        wifi(ssid, password)

if __name__ == "__main__":
    main()