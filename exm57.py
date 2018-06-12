n=int(raw_input())
k=int(raw_input())
list=[]
sum=0
for i in range(1,n+1):
	list.append(i)
for a in range(0,k):
	sum=sum+list[a]
print (sum)
