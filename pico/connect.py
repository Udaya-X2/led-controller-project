# Read settings.json
from lib.at_client import io_util
ssid, password, atSign = io_util.read_settings()
del io_util  # Make space in memory

# Connect to wifi
from lib import wifi
print(f'Connecting to WiFi {ssid}...')
wifi.init_wlan(ssid, password)
del ssid, password, wifi  # Make space in memory

# Connect and pkam authenticate into secondary
from lib.at_client import at_client
atClient = at_client.AtClient(atSign, writeKeys=False)
atClient.pkam_authenticate(verbose=True)
del at_client  # Make space in memory

# Receive data from app
key = 'instructions'
appAtSign = '@computer0'

while True:
    data = atClient.get_public(key, appAtSign)
    print(data)