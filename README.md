Python calculation of matching parameters from A.R. Majewski, M. Walker; "Rapid Design of Impedance Matching Networks for NMR and NQR Studies in the HF and VHF Bands." Journal of Nowhere, 2015 doi: ####-##-###"

![example-output](https://github.com/Altoidnerd/capmatch/blob/master/img/Selection_001.png?raw=true)
![matching-network-a](https://raw.githubusercontent.com/Altoidnerd/nmr-tank-circuits/master/circuit_diagrams/matching-a.jpg)

### Interactive mode for matching circuit A

    ipython3 -i capMatch.py

then set

    In[1]:	args = (FREQUENCY_IN_MHz, CHAR_IMPEDANCE_IN_OHMS, INDUCTANCE_IN_MICROHENRIES, RESISTANCE_IN_OHMS)
    In[2]:	full_tank(*args)

for example:

```
$ ipython3 -i capMatch.py 
Python 3.4.3 (default, Jul 28 2015, 18:20:59) 
Type "copyright", "credits" or "license" for more information.

IPython 1.2.1 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.




	PROGRAM CAPMATCH.v.0.1	running on: Wed Oct 28 08:18:24 EDT 2015


		Authors: Allen Majewski, Morgan Walker (C) 2015
    		This program is part of the open-source NMR-TANK-CIRCUITS suite
     		for calculation of NMR design parameters; please cite:

     		"A. Majewski, M. Walker, et al., Awesome publication (2015) Journal of 1337;
     		URL http://github.com/altoidnerd/nmr-tank-circuits
     		in publications or presentations arising from this work. More details at
     		http://www.phys.ufl.edu/~majewski

	Note:	C_2 -> c_tune	C_1 -> c_match


	... waiting for input...	specify args = (f, z, L, r):




In [1]: args = (3.3, 50, 1.55, .238)

In [2]: full_tank(*args)


======INPUT PARAMETERS=====
f:	3.3 MHz
Zo:	50
L:	1.55 uH
Rs:	0.238 Ohms
======CAPACITANCES AND Q VALUES AT THE MATCHING CONDITION=====
c_tune:		1397.6387614753617 pF
c_tune_yi:	1397.1201193911195 pF
c_match:	104.1330106597596 pF
c_match_yi:	103.53427858183238 pF
QL:		135.0356842278302	= L w/r
QC:		135.03568422783022	= (1 + c_tune/c_match)/(w z c_match)
======ERROR ANALYSIS=====
Tuncap Error Ct/Cty-1:		0.0003712222571585766
Matchcap Error Cm/Cmy-1:	0.00578293572069466
(w c2 r)^2 << (1 - w^2 L c2)^2

 (wcR)^2:		 4.756980858962668e-17 
(1 - w^2 L c2)^2:	 0.9999981372951526

c2 r^2 << L(1 - w^2 L c2)

 c2 r^2:		 7.916785000501037e-11 
L(1 - w^2 L c2):	 1.5499985564030712
done.

```

Or use main.py to be prompted for input

```

$ chmod +x ./main.py




	PROGRAM CAPMATCH.v.0.1	running on: Wed Oct 28 08:22:31 EDT 2015


		Authors: Allen Majewski, Morgan Walker (C) 2015
    		This program is part of the open-source NMR-TANK-CIRCUITS suite
     		for calculation of NMR design parameters; please cite:

     		"A. Majewski, M. Walker, et al., Awesome publication (2015) Journal of 1337;
     		URL http://github.com/altoidnerd/nmr-tank-circuits
     		in publications or presentations arising from this work. More details at
     		http://www.phys.ufl.edu/~majewski

input frequency in MHz: 

...

```



