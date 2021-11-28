with open('file1.txt', 'r') as f1, open('file2.txt', 'r') as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

xk = float(int(lines1[0][0]))
yk = float(int(lines1[0][2]))
r = float(int(lines1[1][0]))

i = 0
for line in lines2:
    x = float(int(lines2[i][0]))
    y = float(int(lines2[i][2]))
    i += 1
    print(i, '- ', end='')
    if i >= 100:
        break
    elif ((x - xk) ** 2 + (y - yk) ** 2 < r ** 2):
        print("точка внутри", end='\n')
    elif (((x - xk) ** 2) + ((y - yk) ** 2) == r ** 2):
        print("точка лежит на окружности", end='\n')
    else:
        print("точка снаружи", end='\n')



