#!/bin/bash

# Create a writable directory in the user's home directory
RECORD_DIR="$HOME/lerobot_datasets"
mkdir -p "$RECORD_DIR"

# Set the HF_USER environment variable if not already set
if [ -z "$HF_USER" ]; then
    export HF_USER="local_user"
    echo "HF_USER environment variable was not set, using 'local_user' as default."
fi

# Run the lerobot.record command with the corrected path
python -m lerobot.record \
    --robot.type=so101_follower \
    --robot.port=/dev/tty.usbmodem5A4B0486671 \
    --robot.id=my_awesome_follower_arm \
    --robot.cameras="{ front: {type: opencv, index_or_path: 0, width: 1920, height: 1080, fps: 30}}" \
    --teleop.type=so101_leader \
    --teleop.port=/dev/tty.usbmodem5A4B0486781 \
    --teleop.id=my_awesome_leader_arm \
    --display_data=true \
    --dataset.repo_id="${HF_USER}/record-test" \
    --dataset.root_dir="$RECORD_DIR" \
    --dataset.num_episodes=10 \
    --dataset.single_task="Grab the lego brick and put it in the bin"

echo "Dataset recording completed. Files saved to $RECORD_DIR"

