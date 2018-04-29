# py/pyext - python script objects for PD and MaxMSP
#
# Copyright (c) 2002-2005 Thomas Grill (gr@grrrr.org)
# For information on usage and redistribution, and for a DISCLAIMER OF ALL
# WARRANTIES, see the file, "license.txt," in this distribution.  
#

"""Several functions to show the py script functionality"""

import sys

print "Finished loading chord dictionary"
try:
    print "Script arguments: ", sys.argv
except:
    print "Could not load the script!"


chord_dict = {(0, 0): [0],  # x=0 >>> locrian
              (0, 1): [0, 3],
              (0, 2): [0, 3, 6],
              (0, 3): [0, 3, 6, 10],
              (0, 4): [0, 3, 6, 10, 13],
              (0, 5): [0, 3, 6, 10, 13, 17],
              (0, 6): [0, 3, 6, 10, 13, 17, 20],
              # x=1 >>> phrygian
              (1, 0): [0],
              (1, 1): [0, 3],
              (1, 2): [0, 3, 7],
              (1, 3): [0, 3, 7, 10],
              (1, 4): [0, 3, 7, 10, 13],
              (1, 5): [0, 3, 7, 10, 13, 17],
              (1, 6): [0, 3, 7, 10, 13, 17, 20],
              # x=2 >>> aeolian
              (2, 0): [0],
              (2, 1): [0, 3],
              (2, 2): [0, 3, 7],
              (2, 3): [0, 3, 7, 10],
              (2, 4): [0, 3, 7, 10, 14],
              (2, 5): [0, 3, 7, 10, 14, 17],
              (2, 6): [0, 3, 7, 10, 14, 17, 20],
              # x=3 >>> dorian
              (3, 0): [0],
              (3, 1): [0, 3],
              (3, 2): [0, 3, 7],
              (3, 3): [0, 3, 7, 10],
              (3, 4): [0, 3, 7, 10, 14],
              (3, 5): [0, 3, 7, 10, 14, 17],
              (3, 6): [0, 3, 7, 10, 14, 17, 21],
              # x=4 >>> mixolydian
              (4, 0): [0],
              (4, 1): [0, 4],
              (4, 2): [0, 4, 7],
              (4, 3): [0, 4, 7, 10],
              (4, 4): [0, 4, 7, 10, 14],
              (4, 5): [0, 4, 7, 10, 14, 17],
              (4, 6): [0, 4, 7, 10, 14, 17, 21],
              # x=5 >>> ionian
              (5, 0): [0],
              (5, 1): [0, 4],
              (5, 2): [0, 4, 7],
              (5, 3): [0, 4, 7, 11],
              (5, 4): [0, 4, 7, 11, 14],
              (5, 5): [0, 4, 7, 11, 14, 17],
              (5, 6): [0, 4, 7, 11, 14, 17, 21],
              # x=6 >>> lydian
              (6, 0): [0],
              (6, 1): [0, 4],
              (6, 2): [0, 4, 7],
              (6, 3): [0, 4, 7, 11],
              (6, 4): [0, 4, 7, 11, 14],
              (6, 5): [0, 4, 7, 11, 14, 18],
              (6, 6): [0, 4, 7, 11, 14, 18, 21],
              # x=7 >>> lydian augmented
              (7, 0): [0],
              (7, 1): [0, 4],
              (7, 2): [0, 4, 8],
              (7, 3): [0, 4, 8, 11],
              (7, 4): [0, 4, 8, 11, 14],
              (7, 5): [0, 4, 8, 11, 14, 18],
              (7, 6): [0, 4, 8, 11, 14, 18, 21],
              }


def readdict(x, y):
    coordinates = (x, y)
    return chord_dict.get(coordinates)






