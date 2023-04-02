"""
This sample bot reads the message from game server every turn but ignores it and performs a random action.
"""

import comms
import random
import math

message = comms.read_message()

while message:
    random_number = random.randint(1, 3)
    if random_number == 1:
        comms.post_message({
            "path": [random.randint(100, 250), random.randint(100, 250)]
        })
    elif random_number == 2:
        comms.post_message({
            "shoot": random.uniform(0, math.pi*2)
        })
    else:
        comms.post_message({
            "path": [0, 0]
        })

    message = comms.read_message()
