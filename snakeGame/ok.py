def repeated(s,n):
    temp = ""
    count = 0
    for i in range(0,n):
        temp += s
    for i in range(0,n):
        if temp[i] == 'a':
            count = count + 1

    print(count)
repeated("aba",10);