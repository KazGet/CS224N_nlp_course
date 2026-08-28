import torch
import numpy as np


rng = np.random.default_rng()
np.random.seed(42)


grad1 = [4, 5, 4.5, 4.2, 4.3, 4.6]
grad2 = [0.01, 0.1, 0.05, 0.2, 0.3, 0.05]

tetta1 = [0] * 7
tetta2 = [0] * 7

v1 = v2 = 0
m1 = m2 = 0

for i in range(6):
    # v1 = 0.99*v1 + 0.01*grad1[i]**2
    # v2 = 0.99*v2 + 0.01*grad2[i]**2

    # m1 = 0.9 * m1 + 0.1*grad1[i]
    # m2 = 0.9 * m2 + 0.1*grad2[i]

    tetta1[i + 1] = np.round(tetta1[i] - 1*grad1[i], 2)
    tetta2[i + 1] = np.round(tetta2[i] - 1*grad2[i], 2)

    print(f'===== Итерация {i} ======')
    print(
        f"tetta1 = {round(tetta1[i + 1], 2)}; tetta2 = {round(tetta2[i + 1], 2)}")

print(tetta1)
print(tetta2)
