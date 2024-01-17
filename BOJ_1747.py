import sys
input = sys.stdin.readline
N = int(input())

def find_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5 + 1)):
        if n % i == 0:
            return False
    return True

def palindrome(n):
    arr = str(n)
    end = len(arr) - 1
    start = 0
    while start <= end:
        if arr[start] != arr[end]:
            return False
        start += 1
        end -= 1
    return True

start_num = N
while True:
    if palindrome(start_num) and find_prime(start_num):
        print(start_num)
        break
    start_num += 1
