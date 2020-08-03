from gps import *
import time
import socketio

# Server URL
car_gps_server="https://example.com?username=rpigps"

# Socket IO Configuration
# Self Signed Certificate
sio = socketio.Client(ssl_verify=False)

@sio.event
def connect():
    print("Connected to Car GPS Server!")

@sio.event
def connect_error():
    print("Connection Error to Car GPS Server!")

@sio.event
def disconnect():
    print("Disconnected from Car GPS Server!")

sio.connect(car_gps_server)

# GPS Configuration
running = True

def getPositionData(gps):
    nx = gpsd.next()
    # For a list of all supported classes and fields refer to:
    # https://gpsd.gitlab.io/gpsd/gpsd_json.html
    if nx['class'] == 'TPV':
        latitude = getattr(nx,'lat', "Unknown")
        longitude = getattr(nx,'lon', "Unknown")

        if latitude != "Unknown" and longitude != "Unknown":
            print str(latitude)+","+str(longitude)
            gps_data={}
            gps_data['latitude'] = str(latitude)
            gps_data['longitude'] = str(longitude)
            sio.emit('rpi_car_gps',gps_data)
        else:
            print str(latitude)+","+str(longitude)

gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

try:
    print "GPS Application started!"
    while running:
        getPositionData(gpsd)
        time.sleep(1.0)

except (KeyboardInterrupt):
    running = False
    sio.disconnect()
    print "GPS Application closed!"
