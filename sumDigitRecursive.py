# Mohammad Zafari
# mhdzafari80@gmail.com

def sum_num(n):
    if 0 <= n and  n < 10:
        return n
    return sum_num(n//10) + n % 10
n = int(input('Enter the number:'))
print(sum_num(n))
