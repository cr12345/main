a=int(raw_input())
b=int(raw_input())
def arm(a):
        b=a%10
        c=a/10
        d=c%10
        e=c/10
        f=b**3+d**3+e**3
        if(f==a): 
          print(num)
for num in range(a,b+1):
	y=arm(num)

