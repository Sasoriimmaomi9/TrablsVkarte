def funk(n):
    mid = (n + 1) // 2
    if n % 2 == 0:
        numbers = list()
        for i in range(1, mid+1):
            numbers.append(i)
        for i in range(mid, 0,-1):
            numbers.append(i)
    else:
        for i in range(1, mid+1):
            numbers.append(i)
        for i in range(mid-1, 0,-1):
            numbers.append(i)
    print(*numbers)
Stroka = funk(int(input()))
