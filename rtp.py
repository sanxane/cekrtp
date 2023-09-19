import requests

## EXAMPLE USAGE
# Author by Expninja

#Mengambil Data RTP Pragmatic
getURL = "https://raw.githubusercontent.com/sanxane/cekrtp/main/assets/pragmatic.json"
#Melakukan Request Data
getData = requests.get(getURL)
#Menampilkan Data RTP Pragmatic Play
print(getData.json())
