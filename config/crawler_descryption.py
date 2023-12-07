import sys

args = sys.argv
TYPE_BASE = 'BASE' if len(args) <= 1 else args[1]

MAX_THREADS = int(args[2]) if len(args) > 2 and args[2].isdigit() else 12

SCHEDULE = True

INVISIBLE = True

TYPE_SEARCH = 'CONCURRENT'

SEARCHS_METHODS = ['ID', 'XPATH', 'CLASS']
SEARCH_METHODS = SEARCHS_METHODS[1] # 0 - ID, 1 - XPATH, 2 - CLASS

SEARCHS_TYPES = ['DIRECTLY', 'TRY_EXCEPT']
SEARCH_TYPES = SEARCHS_TYPES[1] # 0 - DIRECTLY, 1 - TRY_EXCEPT