import ipaddress # this one before the wifi import
import wifi

for ap in wifi.radio.start_scanning_networks():
  #print(ap, ap.ssid, ap.rssi, ap.channel, ap.bssid, ap.authmode)
  print(ap, ap.ssid, ap.rssi, ap.channel, ap.authmode)

# rssi: int --  Signal strength of the network
# authmode: str -- String id of the authmode
#wifi.radio.stop_scanning_networks()

print("\n\t\tscan done")
