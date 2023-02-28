import matplotlib.pyplot as plt
from typing import List
from axis import Axis

def plot_3d(listOfPoints: List[List[float]], pair1: List[float], pair2: List[float]) -> None:
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    for point in listOfPoints:
        if (all(a1==a2 for a1, a2 in zip(point, pair1)) or all(a1==a2 for a1, a2 in zip(point, pair2))):
            color = '#EE4B2B'
        else:
            color = '#add8e6'
        ax.scatter(point[Axis.X.value], point[Axis.Y.value], point[Axis.Z.value], marker='o', c=color)

    plt.show()