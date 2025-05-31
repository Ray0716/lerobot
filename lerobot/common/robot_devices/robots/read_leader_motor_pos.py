
from lerobot.common.robot_devices.motors.feetech import FeetechMotorsBus
from lerobot.common.robot_devices.motors.configs import FeetechMotorsBusConfig
import time

# Port for the **leader** arm
port_leader = "/dev/tty.usbmodem5A4B0486781"

# Same motor config as before
motors = {
    "shoulder_pan": [1, "sts3215"],
    "shoulder_lift": [2, "sts3215"],
    "elbow_flex": [3, "sts3215"],
    "wrist_flex": [4, "sts3215"],
    "wrist_roll": [5, "sts3215"],
    "gripper": [6, "sts3215"],
}

# Leader config
config_leader = FeetechMotorsBusConfig(
    port=port_leader,
    motors=motors,
    mock=False
)

motor_leader = FeetechMotorsBus(config_leader)
motor_leader.connect()

try:
    while True:
        positions = motor_leader.read("Present_Position")
        position_dict = {name: pos for name, pos in zip(motor_leader.motor_names, positions)}
        print("Leader arm positions:", position_dict)
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    if motor_leader.is_connected:
        motor_leader.disconnect()
        print("Leader motor disconnected.")
