import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

road = int(input())  # the length of the road before the gap.
gap = int(input())  # the length of the gap.
platform = int(input())  # the length of the landing platform.
line_pos = (0+road-1, (0+road)+gap-1, ((0+road)+gap)+platform-1)

print(road, gap, platform, line_pos, file=sys.stderr)
# game loop
while True:
    speed = int(input())  # the motorbike's speed.
    coord_x = int(input())  # the position on the road of the motorbike.

    if speed != (gap+1) and coord_x < line_pos[1]:
        if speed < (gap+1):
            print("SPEED")
        else:
            print("SLOW")
    else:
        if coord_x + speed > line_pos[0] and coord_x < line_pos[1]:
            print("JUMP")
        elif coord_x > line_pos[1]:
            print("SLOW")
        else:
            print("WAIT")