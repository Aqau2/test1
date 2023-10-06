def gugu(n):
    for x in range(1, n+1):
        print("----[ {" +str(x)+ "} 단] ----")
        for y in range(1, n+1):
            print(x,"X",y,"=", x*y)

num = input("몇 단까지 출력할까요? ")

num = int(num)

gugu(num)
