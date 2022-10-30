# getting the input from user 
n = int(input("Enter the number of elements for the array: "))
ar=list(map(int, input("Elements of the array: ").strip().split()))

print("Orignal Array: ",ar)
print(end="")

# sorting the array elements in ascending order
# ar.sort(reverse=False) 
# print("Ordered Array: ",*ar)

# initialing the array index 
maxidx = n - 1
minidx = 0
maxele = ar[n-1] + 1

'''Even index(largest) = ar[i]= ar[i]+(ar[maxldx]% max)* max;
Odd index(smallest) = ar[i]= ar[ i]+(ar[minldx]%max)*max;'''

'''we are not using any extra space for alternately re-arranging the elements,
   they are in combined form, lets say x'''
for i in range(0, n) : 
  
        # At even index : we need maximum element 
        if i % 2 == 0 : 
            ar[i] += (ar[maxidx] % maxele ) * maxele
            maxidx -= 1
  
        # At odd index : we need minimum element 
        else : 
            ar[i] += (ar[minidx] % maxele ) * maxele 
            minidx += 1
# getting the elements into the orignal form/singlular formula 
for i in range(0, n) : 
        ar[i] = ar[i] / maxele
  
print ("Modified Array: ") 
for i in range(0, n):
    print (int(ar[i]), end = " ") 