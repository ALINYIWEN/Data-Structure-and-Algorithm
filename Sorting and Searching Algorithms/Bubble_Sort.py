from Strategy_Sort import Strategy_Sort

class Bubble_Sort(Strategy_Sort):
    def __init__(self, list):
        self.list = list
        
    def sort_algorithm(self):
        print("\n===============  氣泡排序  =================")
        print(self.list)
        
        # 跑兩次:一次用於遍歷陣列, 一次用於比較。
        for i in range(len(self.list)):
            for j in range(0, len(self.list) - i - 1):
                
                # 生序: 如果前一個大於後一個 就交換
                if self.list[j] > self.list[j + 1]:
                    (self.list[j], self.list[j + 1]) = (self.list[j + 1], self.list[j])
                    print(self.list)
                    
        return self.list     