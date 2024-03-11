def main():
    x = list(input())
    len_x = len(x)
    a = 0
    b = 0
    for i in range(len_x):
        if x[i] == '(':
            a += 1
        else:
            b += 1
    if a == b:
        print("YES")
    else:
        print("NO")


if __name__=="__main__":
    main()