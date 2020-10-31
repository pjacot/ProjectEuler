''' https://projecteuler.net/problem=2

    Find the sum of even Fibonacci numbers less than n (n is 4,000,000 in the Project Euler problem).
    Two solutions to the problem are included. 
'''

def naive_solution(n: int) -> int:
    ''' Solution is found by calculating all Fibonacci numbers less than n and 
        summing the even ones. 
    '''
    even_fib_sum = 0
    i, j = 1, 2

    while j < n:
        if j % 2 == 0:
            even_fib_sum += j
        
        i, j = j, i + j
    
    return even_fib_sum

def solution(n: int):
    ''' Solution is found by observing that every 3rd Fibonnaci number is even.
        The reccurrence relation Fn = 4*Fn-3 + Fn-6 can be used to generate all 
        even Fibonacci numbers by starting with F3 = 2 and F6 = 8. 
    '''
    if n <= 2:
        return 0

    even_fib_sum = 2
    i, j = 2, 8

    while j < n:
        even_fib_sum += j
        i, j = j, 4*j + i

    return even_fib_sum 

def test():
    assert solution(10) == 10
    assert solution(100) == 44

    for n in range(1000):
        naive_ans = naive_solution(n)
        ans = solution(n)
        assert ans == naive_ans, f'Failed for {n}. Naive solution is {naive_ans} while solution is {ans}.'

if __name__ == '__main__':
    print(solution(4000000))