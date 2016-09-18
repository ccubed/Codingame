"""
'I will ram all of you.' - The Bot says
Aggressive Version of the AI
V2
"""
import math
import sys

boost = True


def calc_distance(x,y,x2,y2):
    return math.sqrt(((x2-x)**2)+((y2-y)**2))


while True:
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    if next_checkpoint_dist > 3000:
        if calc_distance(x, y, opponent_x, opponent_y) < 1000 and opponent_x > x and next_checkpoint_dist > 2000:
            if boost:
                print(opponent_x, opponent_y, "BOOST")
                boost = False
            else:
                print(opponent_x, opponent_y, "100")
        else:
            print(next_checkpoint_x, next_checkpoint_y, "100")
    else:
        if 45 <= abs(next_checkpoint_angle) <= 145:
            print(next_checkpoint_x, next_checkpoint_y, "15")
        else:
            if abs(next_checkpoint_angle) in [0,180]:
                print(next_checkpoint_x, next_checkpoint_y, "85")
            else:
                print(next_checkpoint_x, next_checkpoint_y, "75")
