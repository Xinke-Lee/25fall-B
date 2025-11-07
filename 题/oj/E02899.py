def exchange(m, n, matrix):
    if m < 0 or m > 4 or n < 0 or n > 4:
        return 0
    else:
        matrix[m], matrix[n] = matrix[n], matrix[m]
        return 1

def main():
    matrix = []
    for i in range(5):
        a = list(map(int, input().split())) 
        matrix.append(a)
    
    m, n = map(int, input().split())
    
    if exchange(m, n, matrix) == 0:
        print('error')
    else:
        for i in range(5):
            for j in range(5):
                print(f"{matrix[i][j]:4d}", end="")
            print() 

if __name__ == '__main__': 
    main()