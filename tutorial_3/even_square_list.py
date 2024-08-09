int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def square(list):
    even_list = []
    max = len(list)
    for i in range(max):
        x = int(list[i] * list[i])
        if (x % 2 == 0):
            even_list.append(x)
    return even_list
    
print(square(int_list))