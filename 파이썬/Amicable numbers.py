def count_divisor(n):
    d_list = []
    for i in range(1,n):
        if n % i == 0:
            d_list.append(int(i))
    return sum(d_list)

def find_Amicable(n):
    count = 0
    num_list = [i for i in range(4,n+1)]
    while num_list != []:
        a = count_divisor(num_list[0])
        if a > num_list[-1] or a <= num_list[0]:
            num_list.remove(num_list[0])
            continue

        if count_divisor(a) == num_list[0]:
            count += 1
            print(num_list[0],"-",a,'\n',"----------")
            num_list.remove(num_list[0])
            num_list.remove(a)
            
        else:
            num_list.remove(num_list[0])
    print(f"The Amicable number between 1 to {n} is {count}")

find_Amicable(10000)

#### Bito review
import math

def count_divisor2(n, divisor_cache):
    if n in divisor_cache:
        return divisor_cache[n]
    
    d_sum = 1  # Start with 1 as a divisor
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            d_sum += i
            if i != n // i:  # Add the complementary divisor if it's not the same
                d_sum += n // i
    
    divisor_cache[n] = d_sum
    return d_sum

def find_Amicable2(n):
    count = 0
    divisor_cache = {}
    num_list = list(range(4, n + 1))  # Create a list of numbers from 4 to n
    to_remove = set()  # Use a set to track numbers to remove
    
    for num in num_list:
        if num in to_remove:
            continue
        
        a = count_divisor2(num, divisor_cache)
        
        if a > n or a <= num or a in to_remove:
            continue
        
        if count_divisor2(a, divisor_cache) == num:
            count += 1
            print(num, "-", a, '\n', "----------")
            to_remove.add(num)
            to_remove.add(a)
    
    print(f"The Amicable number between 1 to {n} is {count}")

find_Amicable2(10000)

