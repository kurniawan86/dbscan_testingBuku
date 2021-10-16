import numpy as np
import pandas as panda
import math
import matplotlib.pyplot as plt
import numpy as np

class classData:
    __data = []
    __tempCluster = []

    def __init__(self):
        self.__readExcel()

    def __readExcel(self):
        file = panda.read_excel(open('dataset.xlsx', 'rb'))
        df = panda.DataFrame(file, columns=(['x', 'y']))
        dataset = df.values.tolist()
        self.__data = dataset

    def viewDataset(self):
        print("DATASET \n", self.__data)

    def plottingScatterDataset(self):
        fix, ax = plt.subplots()
        x = self.__data
        temp = np.array(x)
        ax.scatter(temp[:, 0], temp[:, 1], marker='o')
        for i in range(temp.shape[0]):
           ax.annotate(i+1, (temp[i, 0]+0.1, temp[i, 1]+0.1))
        plt.title("Scatter Dataset")
        plt.xlabel(' X ')
        plt.ylabel(' Y ')
        plt.show()