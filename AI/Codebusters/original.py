"""

The original code that got to Bronze all on its own.

"""
import sys
import math
import random


def calc_distance(buster, ghost):
    return math.sqrt(((ghost[0] - buster[0]) ** 2) + ((ghost[1] - buster[1]) ** 2))


busters_per_player = int(input())  # the amount of busters you control
ghost_count = int(input())  # the amount of ghosts on the map
my_team_id = int(input())  # if this is 0, your base is on the top left of the map, if it is one, on the bottom right
my_base_location = (0, 0) if my_team_id == 0 else (16000, 9000)
gtwg = {}
idest = {}


def move_to_corner(bid):
    if bid % 5 == 0:
        idest[bid] = (16000, 0)
        print("MOVE 16000 0")
    elif bid % 5 == 1:
        idest[bid] = (0, 9000)
        print("MOVE 0 9000")
    elif bid % 5 == 2:
        idest[bid] = (12000, 3300)
        print("MOVE 12000 3300")
    elif bid % 5 == 3:
        idest[bid] = (8000, 4500)
        print("MOVE 8000 4500")
    elif bid % 5 == 4:
        idest[bid] = (4500, 8000)
        print("MOVE 4500 8000")


while True:
    entity_data = {'amount': 0, 'busters': {}, 'ghosts': []}
    entity_data['amount'] = int(input())
    for i in range(entity_data['amount']):
        entity_id, x, y, entity_type, state, value = [int(j) for j in input().split()]
        if entity_type == my_team_id:
            entity_data['busters'][entity_id] = {'location': (x, y), 'ghost': True if state == 1 else False,
                                                 'value': value}
        elif entity_type == -1:
            entity_data['ghosts'].append({'id': entity_id, 'location': (x, y), 'state': value})
    for i in sorted(entity_data['busters'].keys()):
        if entity_data['busters'][i]['ghost']:
            if calc_distance(entity_data['busters'][i]['location'], my_base_location) <= 1500:
                print("RELEASE")
            else:
                print("MOVE {} {}".format(my_base_location[0], my_base_location[1]))
        elif len(entity_data['ghosts']) > 0 and entity_data['ghosts']:
            gtwg = {}
            idest = {}
            ghost_distances = {}
            captured_g = False
            for ghost in entity_data['ghosts']:
                gdc = calc_distance(entity_data['busters'][i]['location'], ghost['location'])
                ghost_distances[gdc] = ghost['location']
                if 900 <= gdc <= 1700:
                    print("BUST {}".format(ghost['id']))
                    captured_g = True
                    break
            if not captured_g:
                print("MOVE {} {}".format(ghost_distances[min(ghost_distances.keys())][0],
                                          ghost_distances[min(ghost_distances.keys())][1]))
        else:
            if i in gtwg:
                gtwg[i] += 1
            else:
                gtwg[i] = 1
            if gtwg[i] >= 3:
                loc = entity_data['busters'][i]['location']
                if idest.get(i) is not None:
                    if calc_distance(loc, idest[i]) > 0:
                        print("MOVE {} {}".format(idest[i][0], idest[i][1]))
                    else:
                        idest[i] = (random.randint(0, 16000), random.randint(0, 9000))
                        print("MOVE {} {}".format(idest[i][0], idest[i][1]))
                elif my_team_id == 0:
                    if calc_distance(loc, (16000, 9000)) > 2000:
                        print("MOVE 16000 9000")
                    else:
                        idest[i] = (random.randint(0, 16000), random.randint(0, 9000))
                        print("MOVE {} {}".format(idest[i][0], idest[i][1]))
                else:
                    if calc_distance(loc, (0, 0)) >= 2000:
                        print("MOVE 0 0")
                    else:
                        idest[i] = (random.randint(0, 16000), random.randint(0, 9000))
                        print("MOVE {} {}".format(idest[i][0], idest[i][1]))
            else:
                move_to_corner(i)
