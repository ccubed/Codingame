"""

Version 2 of the Codebusters AI with what I call the LOS Focal Point code which generates a list of overlapping
circles inside squares spread across the whole map which the busters then move around circularly continuously
thereby enabling me to survey the maps entire surface area.

"""
import math

busters_per_player = int(input())  # the amount of busters you control
ghost_count = int(input())  # the amount of ghosts on the map
my_team_id = int(input())  # if this is 0, your base is on the top left of the map, if it is one, on the bottom right
my_base_location = (0, 0) if my_team_id == 0 else (16000, 9000)
idest = {}
size = int(16000 / busters_per_player)
cx = int(size / 2200)
squares = []
FP = {}
captures = {}
abandoned_ghosts = []


def calc_distance(buster, ghost):
    """
    Return distance between two objects.
    :param buster: Object a (I just typically use this for busters)
    :param ghost: Object b (I just typically use this for ghosts)
    :return:
    """
    return math.sqrt(((ghost[0] - buster[0]) ** 2) + ((ghost[1] - buster[1]) ** 2))

def patrol(loc, i):
    """
    Generate the next patrol point or continue the line.

    :param loc: current location tuple
    :param i:  which buster
    :return: the move string
    """
    if idest[i]['current'] is not None:
        if calc_distance(loc, FP[i][idest[i]['path_xy'][0]][idest[i]['path_xy'][1]]) > 0:
            return "MOVE {} {}".format(idest[i]['current'][0], idest[i]['current'][1])
        else:
            new_y = idest[i]['path_xy'][1] + 1 if idest[i]['path_xy'][1] + 1 <= 3 else 0
            if new_y != 0:
                idest[i]['current'] = FP[i][idest[i]['path_xy'][0]][new_y]
                idest[i]['path_xy'] = (idest[i]['path_xy'][0], new_y)
            else:
                new_x = idest[i]['path_xy'][0] + 1
                if new_x >= cx:
                    new_x = 0
                idest[i]['current'] = FP[i][new_x][new_y]
                idest[i]['path_xy'] = (new_x, new_y)
            return "MOVE {} {}".format(idest[i]['current'][0], idest[i]['current'][1])
    else:
        idest[i]['path_xy'] = (0, 0)
        idest[i]['current'] = FP[i][0][0]
        return "MOVE {} {}".format(idest[i]['current'][0], idest[i]['current'][1])

for i in range(busters_per_player):
    FP[i] = {}
    idest[i] = {'current': None, 'path_xy': (0, 0)}
    for circles in range(cx):
        FP[i][circles] = {}

for i in range(busters_per_player):
    squares.append(
        [(0 + (size * i), 0), (0 + (size * (i + 1)), 0), (0 + (size * i), 9000), (0 + (size * (i + 1)), 9000)])

for idx, item in enumerate(squares):
    for x in range(cx):
        for y in range(4):
            FP[idx][x][y] = (item[0][0] + (1100 + (2200 * x)), item[0][1] + (1100 + (2200 * y)))

while True:
    entity_data = {'amount': 0, 'busters': {}, 'ghosts': []}
    entity_data['amount'] = int(input())
    for i in range(entity_data['amount']):
        entity_id, x, y, entity_type, state, value = [int(j) for j in input().split()]
        if entity_type == my_team_id:
            entity_data['busters'][entity_id] = {'location': (x, y), 'ghost': True if state == 1 else False,
                                                 'value': value, 'stunned': True if state == 3 else False}
        elif entity_type == -1:
            entity_data['ghosts'].append({'id': entity_id, 'location': (x, y), 'state': value})
    for i in sorted(entity_data['busters'].keys()):
        if entity_data['busters'][i]['ghost']:
            if entity_data['busters'][i]['value'] in captures:
                del captures[entity_data['busters'][i]['value']]
            if calc_distance(entity_data['busters'][i]['location'], my_base_location) <= 1500:
                print("RELEASE")
            else:
                print("MOVE {} {}".format(my_base_location[0], my_base_location[1]))
        elif len(entity_data['ghosts']) > 0 and entity_data['ghosts']:
            ghost_distances = {}
            captured_g = False
            existing_g = False
            for ghost in entity_data['ghosts']:
                if ghost['id'] in captures:
                    if i in captures[ghost['id']]:
                        print("BUST {}".format(ghost['id']))
                        existing_g = True
                        captured_g = True
                        break
                if not existing_g:
                    gdc = calc_distance(entity_data['busters'][i]['location'], ghost['location'])
                    if 900 <= gdc <= 1700:
                        print("BUST {}".format(ghost['id']))
                        if ghost['id'] in captures:
                            captures[ghost['id']].append(i)
                        else:
                            captures[ghost['id']] = [i]
                        captured_g = True
                        break
                    elif gdc <= 899:  # Too close, move away
                        print("MOVE {} {}".format(entity_data['busters'][i]['location'][0] + 800,
                                                  entity_data['busters'][i]['location'][1] + 800))
                        captured_g = True
                        break
                    else:
                        ghost_distances[gdc] = ghost['location']  # Add ghost to list of ghosts in sight
            if not captured_g:  # Move towards closest ghost
                if len(ghost_distances):
                    print("MOVE {} {}".format(ghost_distances[min(ghost_distances.keys())][0],
                                              ghost_distances[min(ghost_distances.keys())][1]))
                else:
                    print(patrol(entity_data['busters'][i]['location'], i%busters_per_player))
        else:
            print(patrol(entity_data['busters'][i]['location'], i%busters_per_player))
