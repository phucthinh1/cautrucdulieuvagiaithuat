# # 8 quân hậu
# import numpy as n
#
# def kiemtra(banco,hang,cot):
#     for i in range(cot):
#         if banco[hang][i] == 1:
#             return False
#     for i,j in zip(range(hang, -1, -1), range(cot, -1, -1)):
#         if banco[i][j] == 1:
#             return False
#     for i, j in zip(range(hang, 8, 1), range(cot, -1, -1)):
#         if banco[i][j] == 1:
#             return False
#     return True
#
# def giai(banco, cot):
#     if cot >= N:
#         return True
#     for i in range(N):
#         if kiemtra(banco, i , cot) == True:
#             banco[i][cot] = 1
#             if giai(banco, cot +1) == True:
#                 return True
#
#             banco[i][cot] = 0
#     return False
#
# if __name__ == '__main__':
#     N = int(input("So quan Hau:"))
#     banco = [[0]*N for i in range(N)]
#     banco = n.reshape(banco, [N, N])
#     if giai(banco, 0) == False:
#         print('Khong co loi giai')
#     else:
#         print(banco)

#mã đi tuần
# Recursive Python function to solve the tower of hanoi

def towerofhanoi(n,source,destination,auxiliary):
    if n==1:
        print("chuyển đĩa 1 từ cột",source,"tới cột",destination)
        return
    towerofhanoi(n-1,source,auxiliary,destination)
    print("chuyển đĩa",n,"từ cột ",source,"tới cột",destination)
    towerofhanoi(n-1,auxiliary,destination,source)

if __name__ == '__main__':
    n = int(input("số đĩa : "))
    towerofhanoi(n,'A','B','C')





