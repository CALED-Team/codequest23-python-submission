"""
This sample bot reads the message from game server every turn but ignores it and performs a random action.
"""

import comms
import random
import math


def initialize_game():
    message = comms.read_message()
    while message != "END_INIT":
        message = comms.read_message()


def play_game():
    message = comms.read_message()
    while message:
        random_number = random.randint(1, 20)
        if random_number == 1:
            comms.post_message({
                "path": [random.randint(100, 250), random.randint(100, 250)]
            })
        else:
            comms.post_message({
                "shoot": random.uniform(0, math.pi*2)
            })

        message = comms.read_message()


if __name__ == "__main__":
    initialize_game()
    play_game()
