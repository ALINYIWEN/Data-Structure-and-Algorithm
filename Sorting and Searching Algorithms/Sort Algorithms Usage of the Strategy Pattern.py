from abc import ABC, abstractmethod

class Sort_Interface(ABC):
    @abstractmethod
    def sort_algorithm(self, list):
        pass
    
class Bubble_Sort(Sort_Interface):
    def __init__(self, list):
        self.list = list
        
    def sort_algorithm(self):
    
        for i in range(len(self.list)):
            for j in range(0, len(self.list) - i - 1):

                # To sort in descending order, change > to < in this line.
                if self.list[j] > self.list[j + 1]:
                    
                    # swap if greater is at the rear position
                    (self.list[j], self.list[j + 1]) = (self.list[j + 1], self.list[j])
                    
        return self.list            


class Insertion_Sort(Sort_Interface):
    def __init__(self, list):
        self.list = list
        
    def sort_algorithm(self):
    
        for step in range(1, len(self.list)):
            key = self.list[step]
            j = step - 1
                   
            while j >= 0 and key < self.list[j]:
                self.list[j + 1] = self.list[j]
                j = j - 1
            
            # Place key at after the element just smaller than it.
            self.list[j + 1] = key
            
        return self.list          
        
class Sort():
    def __init__(self):
        pass
    
    def sort(self, sort_type):
        return sort_type.sort_algorithm()
 
if __name__ == '__main__':
    sort_list=[]
    number = int(input("請輸入排序數量 : ")) 
    for i in range(0, number): 
        element = int(input("請輸入需排序的 list["+str(i)+"]: ")) 
        sort_list.append(element) 
        

    bubble_sort = Bubble_Sort(sort_list)
    insertion_sort = Insertion_Sort(sort_list)
        
    sort = Sort()    
    sort_result = sort.sort(bubble_sort)
    
    print("排序結果: "+ str(sort_result))