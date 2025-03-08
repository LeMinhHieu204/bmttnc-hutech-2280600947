def dao_nguoc_list(lst):
    return lst[::-1]

# Nhập danh sách số
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
reversed_list = dao_nguoc_list(numbers)
print("Danh sách sau khi đảo ngược:", reversed_list)