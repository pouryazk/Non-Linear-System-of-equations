import numpy as np
from scipy import optimize
from matplotlib import pyplot as plt
small = 1e-30
def wealth_evolution(price, wealth=10, rate=0.01, q=1, realEstate=0.1, prev_price=56):
    sum_wantedEstate = 100
    for delta in range(1,4):
        z = rate - ((price-prev_price) / (price + q / rate))
        k = delta * np.divide(1.0, float(np.maximum(small, z)))
        wantedEstate = (wealth / (price + q / rate)) * np.minimum(k, 1) - realEstate
        sum_wantedEstate += wantedEstate
    return sum_wantedEstate




price_range = np.linspace(0,10000,10000)
we = [wealth_evolution(p) for p in price_range]

plt.plot(price_range,we)
plt.xlabel('price')
plt.ylabel('wealth_evolution(price)')
plt.show()