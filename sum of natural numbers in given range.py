num1=int(input("enter starting number of sequence : "))
num2=int(input("enter ending number of sequence : "))
sum=0
for i in range(num1,num2):
    sum=sum+i

print(sum,"is the total sum of natural numbers in given range")