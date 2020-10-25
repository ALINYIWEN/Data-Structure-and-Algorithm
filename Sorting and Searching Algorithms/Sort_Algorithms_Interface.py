from Bubble_Sort import Bubble_Sort
from Insertion_Sort import Insertion_Sort 

class Sort_Interface():
    def __init__(self):
        pass
    
    def set_sort(self, sort_type):
        self.sort_type = sort_type
    
    def sort(self):
        return self.sort_type.sort_algorithm()
    
if __name__ == '__main__': 
    
    sort_list=[]
    number = int(input("請輸入要排序的數量 : ")) 
    for i in range(0, number): 
        element = int(input("請輸入需排序的 list["+str(i)+"]: ")) 
        sort_list.append(element)   

    # 建立排序物件
    bubble_sort = Bubble_Sort(sort_list)
    insertion_sort = Insertion_Sort(sort_list)
    
    # Interface 實體化    
    sort_interface = Sort_Interface()  
    
    sort_interface.set_sort(insertion_sort)
    sort_interface.sort()
    
    print("===========================================")