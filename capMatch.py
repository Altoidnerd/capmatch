#!/usr/bin/env python3

from __future__ import division
import sys
import math
import os

print("""\n\n\n\n\tPROGRAM CAPMATCH.v.0.1\trunning on:""", os.popen("date").read())
print("""
	\tAuthors: Allen Majewski, Morgan Walker (C) 2015
    	\tThis program is part of the open-source NMR-TANK-CIRCUITS suite
     	\tfor calculation of NMR design parameters; please cite:\n
     	\t"A. Majewski, M. Walker, et al., Awesome publication (2015) Journal of 1337;
     	\tURL http://github.com/altoidnerd/nmr-tank-circuits
     	\tin publications or presentations arising from this work. More details at
     	\thttp://www.phys.ufl.edu/~majewski
""")

if __name__ == '__main__':
    print("\tNote:\tC_2 -> c_tune\tC_1 -> c_match\n\n\n\t... waiting for input...\tspecify args = (f, z, L, r):\n\n\n")

def c_tune(f,z,L,r):
    w = f*1e6*2*math.pi
    l = L*1e-6
    return (l*w*w*z - math.sqrt(r*z*math.pow(l*w*w,2) + math.pow(r,3)*w*w*z - math.pow(r*w*z,2)))/(math.pow(l*w*w,2)*z + z*math.pow(r*w,2))

def c_match(f,z,L,r):
    w = f*1e6*2*math.pi
    l = L*1e-6
    return (-1+2*c_tune(f,z,L,r)*l*w*w - math.pow(c_tune(f,z,L,r)*r*w,2) - math.pow(c_tune(f,z,L,r)*l*w*w,2))/    (w*w*(-l + c_tune(f,z,L,r)*r*r + c_tune(f,z,L,r)*math.pow(l*w,2))) 

def c_tune_yi(f,z,L,r):
    w = f*1e6*2*math.pi
    l = L*1e-6
    return (1 - math.sqrt(r/z))/(l*w**2)

def c_match_yi(f,z,L,r):
    w = f*1e6*2*math.pi
    l = L*1e-6
    return (math.sqrt(r/z))/(l*w**2)

# Alternative definition for Q:  /reference/A\ od\ for\ Measuring\ the\ Q\ Value\ of\ an\ NMR\ Sample\ Coil.pdf 
# author has c_1 = c_match, c2_= c_tune
# doi: 10.1006/jmre.1999.1972

def Q_C(f, z, L, r):
    c_1 = c_match_yi(f, z, L, r)
    c_2 = c_tune_yi(f, z, L, r)
    w = f*1e6*2*math.pi
    return ((1 + c_2/c_1)/(w*z*c_1))

# Q = Lw/r, but use same args tuple for convenience (z is ignored)
def Q_L(f, z, L, r):
    w = f*1e6*2*math.pi
    l= L*1e-6 
    return l*w/r

def show_diff(f, z, L, r):
    w = 2*math.pi*1e6
    l = L*1e-6
    diffs = []
    CTer = c_tune(f,z,L,r)/c_tune_yi(f,z,L,r) - 1
    CMer = c_match(f,z,L,r)/c_match_yi(f,z,L,r) - 1
    diffs.append(CTer)
    diffs.append(CMer)
    return diffs

def full_tank(f, z, L, r):
    w = 2*math.pi*f
    CT = c_tune(f, z, L, r)
    CM = c_match(f, z, L, r)
    CTy = c_tune_yi(f, z, L, r)
    CMy = c_match_yi(f, z, L, r)
    CTer = CT/CTy
    CMer = CM/CMy
    QL = Q_L(f, z, L, r)
    QC = Q_C(f, z, L, r)
    wc2R_squared_error = (w*CT*r)**2
    wc2R_squared_upper_bound = (1 - L*CT*(w**2))**2
    c2RR_error = CT*(r**2)
    c2RR_upper_bound = L*(1 - L*CT*(w**2))
    over_Q_C_badness = (QL - QC)/QC
    over_Q_L_badness = (QL - QC)/QL
    norm_badness = math.sqrt(over_Q_C_badness**2 + over_Q_L_badness**2)
    avg_badness = (over_Q_C_badness + over_Q_L_badness)/2
    print("\n\n======INPUT PARAMETERS=====")
    print("f:\t{} MHz\nZo:\t{}\nL:\t{} uH\nRs:\t{} Ohms".format(f,z, L, r))
    print("======CAPACITANCES AND Q VALUES AT THE MATCHING CONDITION=====")
    print("c_tune:\t\t{} pF".format(CT*10**12))
    print("c_tune_yi:\t{} pF".format(CTy*10**12))
    print("c_match:\t{} pF".format(CM*10**12))
    print("c_match_yi:\t{} pF".format(CMy*10**12))
    print("QL:\t\t{}\t{}".format(QL, "= L w/r"))
    print("QC:\t\t{}\t{}".format(QC,"= (1 + c_tune/c_match)/(w z c_match)"))
    print("======ERROR ANALYSIS=====")
    print("Tuncap Error Ct/Cty-1:\t\t{}\nMatchcap Error Cm/Cmy-1:\t{}".format(CTer-1, CMer -1))
    print("(w c2 r)^2 << (1 - w^2 L c2)^2\n\n","(wcR)^2:\t\t", wc2R_squared_error, "\n(1 - w^2 L c2)^2:\t", wc2R_squared_upper_bound) 
    print("\nc2 r^2 << L(1 - w^2 L c2)\n\n","c2 r^2:\t\t", c2RR_error, "\nL(1 - w^2 L c2):\t", c2RR_upper_bound) 
#    print("\n=======BADNESSES========\n(QL-QC)/QL:\t{}\n(QL-QC)/QC:\t{}\nbadness norm:\t{}\naverage badness:\t{}".format(str(over_Q_L_badness),str(over_Q_C_badness), str(norm_badness), str(avg_badness)))
    print("done.\n")
