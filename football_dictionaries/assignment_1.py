def players_as_dictionaries(squads_list):


    squad_list_of_dictionaries = []

    for squad in squads_list:

        build_dict = {}

        build_dict['number']        = squad[0]
        build_dict['position']      = squad[1]
        build_dict['name']          = squad[2]
        build_dict['date_of_birth'] = squad[3]
        build_dict['caps']          = squad[4]
        build_dict['club']          = squad[5]
        build_dict['country']       = squad[6]
        build_dict['club_country']  = squad[7]
        build_dict['year']          = squad[8]

        # append the dictionary to squad l of d
        squad_list_of_dictionaries.append(build_dict)


    return squad_list_of_dictionaries
