#from squads_data import SQUADS_DATA
#from pprint import pprint

def player_to_dict(player_list):

    player_as_dict = {
        'number': player_list[0],
        'position': player_list[1],
        'name': player_list[2],
        'date_of_birth': player_list[3],
        'caps': player_list[4],
        'club': player_list[5],
        'country': player_list[6],
        'club_country': player_list[7],
        'year': player_list[8],
    }

    return player_as_dict

def players_by_position(squads_list):

    # initialize return dict
    dict_of_position = {}

    for player in squads_list:
        player_as_dict = player_to_dict(player)

        position = player[1]

        if position in dict_of_position.keys():
            dict_of_position[position].append(player_as_dict)
        elif position not in dict_of_position.keys():
            tmp_list = []
            tmp_list.append(player_as_dict)
            dict_of_position[position] = tmp_list
        else:
            return -127
        #print(position)

    return dict_of_position


#pprint(players_by_position(SQUADS_DATA))

