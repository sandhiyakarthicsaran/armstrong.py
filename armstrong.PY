lower_range=int(input("Enter lower range:"))
upper_range=int(input("Enter upper range:"))
for n in range(lower_range,upper_range+1);
sum=0
temp=1
while(temp>0):
digit=temp%10
sum=sum+digit**3
temp=temp//10

if n==sum:
print(n)
