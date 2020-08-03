from Motor import *
from servo import *          
import socketio

# Initialization
PWM=Motor()
PWM.setMotorModel(0,0,0,0)
speed=1000
car_control_server="https://example.com?username=rpicontrol"

servo_pwm=Servo()
servo_up_down=80
servo_right_left=100
servo_pwm.setServoPwm('0',servo_up_down)
servo_pwm.setServoPwm('1',servo_right_left)

# Number 1 = 49
# Number 2 = 50
# Number 3 = 51
# Number 4 = 52
# Number 5 = 53
# Number 6 = 54
# Number 7 = 55

# w = 87
# s = 83
# a = 65
# d = 68

# Arrow Up = 38
# Arrow Down = 40
# Arrow Left = 37
# Arrow Right = 39
# Space = 32

def code_to_action(code):

    global speed
    global servo_up_down
    global servo_right_left

    if code == "49":
        print("Speed= 1000")
        speed=1000
    elif code == "50":
        print("Speed= 1500")
        speed=1500
    elif code == "51":
        print("Speed= 2000")
        speed=2000
    elif code == "52":
        print("Speed= 2500")
        speed=2500
    elif code == "53":
        print("Speed= 3000")
        speed=3000
    elif code == "54":
        print("Speed= 3500")
        speed=3500
    elif code == "55":
        print("Speed= 4000")
        speed=4000


    elif code == "87":
        servo_up_down-=10
        print("Servo Up: " +str(servo_up_down))
        servo_pwm.setServoPwm('0',servo_up_down)
    elif code == "83":
        servo_up_down+=10
        print("Servo Down: " +str(servo_up_down))
        servo_pwm.setServoPwm('0',servo_up_down)
    elif code == "65":
        servo_right_left+=10
        print("Servo Left: " +str(servo_right_left))
        servo_pwm.setServoPwm('1',servo_right_left)
    elif code == "68":
        servo_right_left-=10
        print("Servo Right: " +str(servo_right_left))
        servo_pwm.setServoPwm('1',servo_right_left)


    elif code == "38":
        print("Arrow Up")
        PWM.setMotorModel(speed,speed,speed,speed)
    elif code == "40":
        print("Arrow Down")
        PWM.setMotorModel(-speed,-speed,-speed,-speed)
    elif code == "37":
        print("Arrow Left")
        PWM.setMotorModel(-speed,-speed,speed,speed)
    elif code == "39":
        print("Arrow Right")
        PWM.setMotorModel(speed,speed,-speed,-speed)
    elif code == "32":
        print("Space")
        PWM.setMotorModel(0,0,0,0)
    else:
        print("Not valid command")


# Socket IO Configuration
# Self Signed Certificate
sio = socketio.Client(ssl_verify=False)

@sio.event
def connect():
    print("Connected to Car Control Server!")

@sio.event
def connect_error():
    print("Connection Error to Car Control Server!")

@sio.event
def disconnect():
    print("Disconnected from Car Control Server!")

@sio.on('check_rpi_connectivity_ping')
def on_message(data):
    print("Received Ping from Car Control Server")
    sio.emit('check_rpi_connectivity_pong', 'pong')

@sio.on('rpi_car_control')
def on_message(data):
    code_to_action(str(data))

sio.connect(car_control_server)
