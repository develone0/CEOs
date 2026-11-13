def find_intersection_count(A, B):
    intersection = []
    for element in A:
        if element in B and element not in intersection:
            intersection.append(element)
            
    return len(intersection), intersection

N = int(input("Введіть розмір послідовності A: "))
M = int(input("Введіть розмір послідовності B: "))

print("\nВведіть елементи послідовності A:")
A = [int(input(f"A[{i}] = ")) for i in range(N)]

print("\nВведіть елементи послідовності B:")
B = [int(input(f"B[{i}] = ")) for i in range(M)]

result_count, common_elements = find_intersection_count(A, B)

print("\n--- Результати ---")
print(f"Спільні унікальні елементи: {common_elements}")
print(f"Кількість елементів у перетині: {result_count}")

print(type(find_intersection_count(A, B)))


