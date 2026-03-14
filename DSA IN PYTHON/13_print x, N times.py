def func(x,n):
    if x>n:
        return

    # Head recursion: prints 1 to n
    # print(x)
    # func(x + 1, n)

    # Tail recursion: prints n to 1
    func(x + 1, n)
    print(x)

func(1,12)