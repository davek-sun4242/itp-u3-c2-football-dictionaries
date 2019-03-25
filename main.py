from football_dictionaries.squads_data import SQUADS_DATA
from football_dictionaries.assignment_1 import players_as_dictionaries
from football_dictionaries.assignment_2 import *
from pprint import pprint

#result = players_as_dictionaries(SQUADS_DATA)
result = players_by_position(SQUADS_DATA)
pprint(result)
