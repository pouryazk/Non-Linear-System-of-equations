import scipy.optimize as opt
from numpy import exp, array
from matplotlib import pyplot as plt

import numpy as np


def system_of_equations(variables, *data):
    wi, g_dot = data
    phi_xx, phi_xy, phi_xz, phi_yy, phi_yz, phi_zz = variables
    equation_1 = -2 * wi * g_dot * phi_xx + (0.2/0.9)*wi*(phi_xx ** 2 + phi_xy ** 2 + phi_xz ** 2) + phi_xx
    equation_2 = -1 * wi * g_dot * phi_yy \
                 + (0.2/0.9)*wi*(phi_xx * phi_xy + phi_xy * phi_yy + phi_xz * phi_yz) + phi_xy - 0.9*g_dot
    equation_3 = -1 * wi * g_dot * phi_yz + (0.2/0.9)*wi*(phi_xx * phi_xz + phi_xy * phi_xz + phi_xz * phi_zz) + phi_xz
    equation_4 = (0.2/0.9) * wi * (phi_xy ** 2 + phi_yy ** 2 + phi_yz ** 2) + phi_yy
    equation_5 = (0.2/0.9) * wi * (phi_xz * phi_xy + phi_yz * phi_yy + phi_zz * phi_yz) + phi_yz
    equation_6 = phi_zz + (0.2/0.9) * wi * (phi_xz ** 2 + phi_yz ** 2 + phi_zz ** 2)
    return [equation_1, equation_2, equation_3, equation_4, equation_5, equation_6]


weissenberg_list = np.linspace(0, 150, 800)
gamma_dot = 1
initial_guess = (0.1,)*6
initial_guess_array = array(initial_guess)
solution_list = [
    opt.fsolve(system_of_equations, initial_guess_array, args=(weissenberg, gamma_dot)).flat[1] for weissenberg in weissenberg_list
]
plt.plot(weissenberg_list, solution_list)
plt.title("Shear Stress vs Weissenberg Number")
plt.xlabel(f'Wi')
plt.ylabel(r'$\sigma_{xx}$')
# plt.ylim([0.1, 0.3])
plt.show()
