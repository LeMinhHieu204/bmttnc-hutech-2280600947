def truy_cap_phan_tu(input_data):
    first_element = input_data[0]
    last_element = input_data[-1]
    return first_element, last_element

# Nhập Tuple
input_tuple =eval(input("Nhập ví dụ(1,2,3): "))
first, last = truy_cap_phan_tu(input_tuple)
print("Phần tử đầu tiên trong là:", first)
print("Phần tử cuối cùng trong là:", last)