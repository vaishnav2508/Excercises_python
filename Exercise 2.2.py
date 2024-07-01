# for i in range(101):
#     print(i)

# for i in range(101):
#     if i%7==0:
#         print(i)

# for i in range(1,100):
#     if (i%5 == 0 and i%3 !=0):
#         print(i)

for x in range(2,21):
    for i in range(2,21):
        if x % i == 0:
            if x != i:
                print(i)
    print('--------')