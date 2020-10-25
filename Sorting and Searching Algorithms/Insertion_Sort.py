from Strategy_Sort import Strategy_Sort

class Insertion_Sort(Strategy_Sort):
    def __init__(self, list):
        self.list = list
    
    def sort_algorithm(self):
        print("\n===============  插入排序  =================")
        print(self.list)
        for step in range(1, len(self.list)):
            key = self.list[step]
            j = step - 1
                   
            while j >= 0 and key < self.list[j]:
                self.list[j + 1] = self.list[j]
                j = j - 1
            
            self.list[j + 1] = key
            print(self.list)

        return self.list     