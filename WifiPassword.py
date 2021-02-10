print('''In CMD type: 
wifipassword -> returns the wifipassword of the currnetly conected wifi
netsh wlan show profile key=clear -> returns the connected wifi devices of the comuter
netsh wlan show profile {name of the connected wifi device} key=clear-> returns the details of the wifi device with password
netsh wlan show profile {naem of the connected wifi device} -> returns the details of the wifi device wothout the wifipassword

''')