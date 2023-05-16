#declare array
A =[]

#getting keyboard input

for i in range(8):
    A.append(int(input("Enter Values : ")))
#print keyboard Inputs
print(A)
    
def selectionSort(A):
    n = len(A)
    for j in range (0, n-1):
        smallest = j
        for i in range(j+1,n):
            if A[i]< A[smallest]:
                smallest = i
            A[j],A[smallest] = A[smallest],A[j]

selectionSort(A)
print("Sorted Array : ")
print(A)
            
