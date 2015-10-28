
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


