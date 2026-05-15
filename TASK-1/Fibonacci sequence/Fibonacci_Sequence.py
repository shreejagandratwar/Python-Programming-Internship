n = int(input("Enter the number of terms: "))

a,b,c,d = 0,1,0,1

for i in range(n):
    print(a,end=" ")
    a,b,c,d = b,c,d,a+b
