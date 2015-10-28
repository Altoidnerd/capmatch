Python calculation of matching parameters from A.R. Majewski, M. Walker; "Rapid Design of Impedance Matching Networks for NMR and NQR Studies in the HF and VHF Bands." Journal of Nowhere, 2015 doi: ####-##-###"

![example-output](https://github.com/Altoidnerd/capmatch/blob/master/img/Selection_001.png?raw=true)
![matching-network-a](https://raw.githubusercontent.com/Altoidnerd/nmr-tank-circuits/master/circuit_diagrams/matching-a.jpg)
![matching-network-b](https://raw.githubusercontent.com/Altoidnerd/nmr-tank-circuits/master/circuit_diagrams/matching-b.jpg)

### Interactive mode for matching circuit A

    git clone https://github.com/altoidnerd/nmr-tank-circuits
    cd nmr-tank-circuits/python
    ipython3 -i capMatch.py

then set

    In[1]:	args = (FREQUENCY, CHAR_IMPEDANCE, INDUCTANCE, RESISTANCE)
    In[2]:	full_tank(*args)

or run the script

    ./main.py


