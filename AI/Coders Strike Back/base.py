"""
Coders Strike Back
First attempt AI

if nextCheckpointAngle > 90 or nextCheckpointAngle < -90 then
    thrust = 0
else
    thrust = 100
end if
print x y thrust


Input for one game turn
First line: 6 integers x & y for your pod's position. nextCheckpointX & nextCheckpointY for the coordinates of the next checkpoint the pod must go through. nextCheckpointDist for the computed distance between your pod and the next checkpoint, nextCheckpointAngle for the angle in degrees between your pod orientation and the direction of the next checkpoint (from -180 to 180).

Second line: 2 integers opponentX & opponentY for the opponent pod's position.
Output for one game turn
One line: 2 integers for the target coordinates of your pod followed by thrust, the thrust to give to your pod.
Constraints
0 ≤ thrust ≤ 100
Response time first turn ≤ 1000ms
Response time per turn ≤ 150ms
"""
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " 80")
