#finding a factorial of a number, n

def find_factorial(n):
    #base case
    if n==0:
        return 1
    return n*find_factorial(n-1) #find_factorial(n-1) is the recursion case


result=find_factorial(4)
print(result)