def ap(a):
    return len(a)*(a[0]+a[-1])//2

print ap(range(int(raw_input().split(" ")[0]) + 1))
