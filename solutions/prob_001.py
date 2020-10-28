''' https://projecteuler.net/problem=1
'''

def solution(n):
    result = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result

def test():
    assert solution(10) == 23

if __name__ == '__main__':
    print(solution(1000))