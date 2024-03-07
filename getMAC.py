# get MAC

import wifi

macList =  [hex(i) for i in wifi.radio.mac_address]
macStr = ""

length = len(macList)
counter = 1

for x in macList:
#  print(x[2:5]) 
  macStr = macStr + x[2:5]
  if counter < length:
    macStr = macStr  + ':'

  counter = counter + 1

print(macStr)
