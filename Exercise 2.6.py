for x in range(2,21):
    for i in range(2,21):
        if x % i == 0:
            if x != i:
                print(i)
    print('--------')