from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
import sys

from euclidAlg import findGCD

bnd = int(sys.argv[1])

val = np.empty((bnd, bnd), dtype='uint8')
for index, gcd in np.ndenumerate(val):
    val[index[0]][index[1]] = findGCD(index[0], index[1])

ax = sns.heatmap(val,
     square=True,
     cmap="YlGnBu",
     xticklabels=int(bnd/5),
     yticklabels=int(bnd/5))

ax.set(xlabel='a', ylabel='b')
plt.title('Iterations required to find gcd(a, b) by the Euclidean Algorithm')
plt.show()

