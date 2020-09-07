N = 2
print("| a1 b1 |")
print("| a2 b2 |") 
arr = [[None] * N for row in range(N)]

arr[0][0] = input("請輸入 a1: ")
arr[0][1] = input("請輸入 b1: ")
arr[1][0] = input("請輸入 a2: ")
arr[1][1] = input("請輸入 b2: ")

print("| " + arr[0][0] + " " + arr[0][1] + " |")
print("| " + arr[1][0] + " " + arr[1][1] + " |")

result = (int(arr[0][0]) * int(arr[1][1])) - (int(arr[1][0]) * int(arr[0][1])) 
print("行列式的值為: " + str(result))