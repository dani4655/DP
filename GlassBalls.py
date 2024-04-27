import numpy as np
# q1 calculate the minimal value for checks needed for n floors with k crystal balls
# <=> get the max floors possible with m tries and k balls
def checking_number(n: int, k: int) -> int:
    min = 0
    arr = [0] * (k + 1)
    while arr[k] < n:
        min = min + 1
        for x in range(k, 0, -1):
            arr[x] = 1 + arr[x] + arr[x - 1]
    return min

def index_floor(f_i: list[int], b: int) -> int:
    n = len(f_i)
    first = index_first_floor(n)
    k = 2


# def index_floor(f_i: list[int], b: int) -> int:
#     floors = len(f_i)
#     start = index_first_floor(floors)
#     step = start -1
#     k = 2
#     interval = [0,floors]
#     while k>0:
#         if f_i[start-1]> b: #ball broke
#             k=k-1
#             interval[1] = start
#             if interval[1]==interval[0]:
#                 if f_i[interval[0]-1]>b:
#                     return interval[0]
#             for i in range(interval[0],interval[1]):
#                 if f_i[i]>b:
#                     return i+1
#         elif f_i[start-1]<= b: #ball did not break
#             start += step
#             step = step -1
#             interval[0] = start
#             if step==0:
#                 if f_i[0]>b or f_i[floors-1]<=b:
#                     return -1
#
#     return -1

# def index_floor(f_i: list[int], b: int) -> int:
#     """
#     This function finds the highest floor from which you can drop a ball without it breaking
#     in a building with n floors (f_i) considering a threshold (b) for the balls to break,
#     using an optimal strategy with 2 balls.
#
#     Args:
#         f_i: List of floor heights (increasing order).
#         b: Threshold for the balls to break (ball breaks if f_i < b).
#
#     Returns:
#         The index of the highest safe floor (0-based indexing) or -1 if no safe floor exists.
#     """
#
#     floors = len(f_i)
#     start = index_first_floor(floors)  # Replace with function calculating optimal starting floor
#     step = start - 1
#     k = 2
#     interval = [0, floors]
#     if f_i[floors-1] <= b:
#         return -1
#     while k > 0:
#         if f_i[start - 1] > b:  # Ball breaks
#             k -= 1
#             interval[1] = start
#             if interval[0] == interval[1]:
#                 if f_i[interval[0] - 1] > b:
#                     return interval[0]
#             for i in range(interval[0], interval[1]):
#                 if f_i[i] > b:
#                     return i + 1
#
#         elif f_i[start - 1] <= b:  # Ball doesn't break
#             start += step
#             step = max(step - 1, 0)  # Ensure step doesn't become negative
#             interval[0] = start
#             if step == 0 and (f_i[0] > b or f_i[floors - 1] <= b):
#                 return -1
#
#     return -1

# def index_floor(f_i: list[int], b: int) -> int:
#     num =1
#     floors_number = len(f_i)
#     if f_i[floors_number-1] <= b or f_i[0]>= b:
#         return -1
#     while num*(num+1)/2 < floors_number:
#         num += 1
#     jump = num
#     step = num -1
#     while f_i[jump] < b:
#         jump = jump + step
#         step = step - 1
#     floor = jump - step + 1
#     while f_i[floor] < b:
#         floor +=1
#         if b==f_i[floor]:
#             floor +=1
#
#     return floor +1
#

def index_first_floor(n: int) -> int:
    a,b = np.roots([1,1,-2*n])
    ans = max(a,b)
    return int(np.ceil(ans))


floors1 =[1,2,3,4,5,6,7,8,9,10]
index_floor(floors1,9)
