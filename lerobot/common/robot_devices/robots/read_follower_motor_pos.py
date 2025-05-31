from lerobot.common.robot_devices.motors.feetech import FeetechMotorsBus
from lerobot.common.robot_devices.motors.configs import FeetechMotorsBusConfig

# Replace with your actual motor port
port = "/dev/tty.usbmodem5A4B0486671"

# Define the motors dictionary (name -> [id, type])
motors = {
    "shoulder_pan": [1, "sts3215"],
    "shoulder_lift": [2, "sts3215"],
    "elbow_flex": [3, "sts3215"],
    "wrist_flex": [4, "sts3215"],
    "wrist_roll": [5, "sts3215"],
    "gripper": [6, "sts3215"],
}

# Create configuration for the motor bus
config = FeetechMotorsBusConfig(
    port=port,
    motors=motors,
    mock=False
)

# Initialize the motor bus with the configuration
motor = FeetechMotorsBus(config)

motor.connect()

import time
try:
    while True:
        positions = motor.read("Present_Position")
        # Use motor.motor_names property to get the names in correct order
        position_dict = {name: pos for name, pos in zip(motor.motor_names, positions)}
        print("Motor positions:", position_dict)
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    # Ensure we disconnect properly when the script ends
    if motor.is_connected:
        motor.disconnect()
        print("Motor disconnected.")
