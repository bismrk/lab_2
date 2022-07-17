
class Array:
    def __init__(self, array=[]):
        self.array = array

    def bubbleSort(self):
        n = len(self.array)
        for i in range(0,   n - 1):
            for j in range(0, n - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
        return self.array

    def printArr(self):
        print(self.array)
