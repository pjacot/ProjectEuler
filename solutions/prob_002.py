''' https://projecteuler.net/problem=2
'''

def solution(n: int) -> int:
    even_fib_sum = 0
    i, j = 1, 2

    while j < n:
        if j % 2 == 0:
            even_fib_sum += j
        
        i, j = j, i + j
    
    return even_fib_sum

def test():
    assert solution(10) == 10
    assert solution(100) == 44

if __name__ == '__main__':
    print(solution(4000000))