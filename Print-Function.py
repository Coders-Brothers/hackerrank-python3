if __name__ == '__main__':
    n = int(input())

    if n > 150 or n < 1:
        n = int(input())

    for x in range(1, n+1):
        print(x, end='') 

