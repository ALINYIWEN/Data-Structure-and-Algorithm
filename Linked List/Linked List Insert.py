import sys

class employee:
    def __init__(self):
        self.number = 0
        self.salary = 0
        self.name = ''
        self.next = None

def findnode(head, number):
    ptr = head
    
    while ptr != None:
        if ptr.number == number:
            return ptr
        ptr = ptr.number
    return ptr
            
def insert(head, ptr, number, salary, name):
    InsertNode = employee()
    if not InsertNode:
        return None
    InsertNode.number = number
    InsertNode.salary = salary
    InsertNode.name = name
    InsertNode.next = None
    if ptr == None:                     # 插入第一個節點
        InsertNode.next = head         
        return InsertNode
    else:
        if ptr.next == None:            # 插入最後一個節點
            ptr.next = InsertNode
        else:                           # 插入中間節點
            InsertNode.next = ptr.next 
            ptr.next = InsertNode
    return head               

position = 0
data=[[1001,32367],[1002,24388],[1003,27556],[1007,31299],
      [1012,42660],[1014,25676],[1018,44145],[1043,52182],
      [1031,32769],[1037,21100],[1041,32196],[1046,25776]]

name=['Allen','Scott','Marry','John','Mark','Ricky','Lisa','Jasica','Hanson','Amy','Bob',        'Jack']
print('員工編號 薪水 員工編號 薪水 員工編號 薪水 員工編號 薪水')
print('-------------------------------------------------------------')
for i in range(3):      # row
    for j in range(4):  # column
        print('[%4d] $5d' %(data[j*3+i][0],data[j*3+i][1]),end='')
    print()    
print('-------------------------------------------------------------')
head=employee()
head.next=None

if not head:
    print('Error!! 記憶體配置失敗!\n')
    sys.exit(0)

