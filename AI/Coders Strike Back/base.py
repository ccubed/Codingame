"""
Coders Strike Back
AI V 1
"""
import math
import sys

boost = True

while True:
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    if next_checkpoint_dist > 3000 and abs(next_checkpoint_angle ) in [0, 180] and boost:
        boost = False
        print(next_checkpoint_x, next_checkpoint_y, "BOOST")
    else:
        if next_checkpoint_dist > 3000:
                print(next_checkpoint_x, next_checkpoint_y, "100")
        else:
            if 45 <= abs(next_checkpoint_angle) <= 145:
                print(next_checkpoint_x, next_checkpoint_y, "15")
            else:
                print(next_checkpoint_x, next_checkpoint_y, "75")