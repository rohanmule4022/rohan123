# Selection Sort Program

# Taking input from user
arr = list(map(int, input("Enter numbers separated by space: ").split()))

n = len(arr)

# Selection Sort
for i in range(n):

    # Assume current index has minimum value
    min_index = i

    # Find smallest element in remaining array
    for j in range(i + 1, n):

        if arr[j] < arr[min_index]:

            min_index = j

    # Swap smallest element with current element
    arr[i], arr[min_index] = arr[min_index], arr[i]

# Output
print("Sorted Array:")

print(arr) EXPLAIN LIN WISE
