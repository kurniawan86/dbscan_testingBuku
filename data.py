import pandas as panda
import math

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
