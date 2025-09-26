def funk(n):
    mid = (n + 1) // 2
    if n % 2 == 0:
         numbers = list(range(1, mid + 1)) + list(range(mid, 0, -1))
    else:
        numbers = list(range(1, mid + 1)) + list(range(mid - 1, 0, -1))
    print(*numbers)
Stroka = funk(int(input()))
