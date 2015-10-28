#!/usr/bin/env python3
#
# Example script that locates user defined "pathological" behavior
# This is where speed counts (maybe)
#

from capMatch import *
import numpy as np


def main():
    if len(sys.argv) == 2:
        f = float(sys.argv[1])
    else:
        f = 10

    error_sets = []
    for L in np.linspace(3, .001, 2000):
        for r in np.linspace(.01, 49.999, 2000):
            args = (f, 50, L, r)
            try:
                error = c_match(*args)/c_match_yi(*args) -1 
            except ValueError:
                pass
            error_sets.append([error,"L=", L,"r=", r])


    errors = []
    for j in range(len(error_sets)):
        errors.append(error_sets[j][0])
    
    top = max(errors)
    topind = errors.index(max(errors))

    print("top error set for f = {} MHz:".format(f), error_sets[topind])
    
if __name__=='__main__':
    main()
    

