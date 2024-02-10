x = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]


# def find_it(arr: list) -> int:
#     count_num_dict = {}
#
#     for num in arr:
#         if num in count_num_dict:
#             count_num_dict[num] += 1
#         else:
#             count_num_dict[num] = 1
#     for num, count in count_num_dict.items():
#         if count % 2 != 0:
#             return num
#
#
# result = find_it(arr=x)
# print(result)


def find_it(arr: list) -> int:
    count_dict = {el : arr.count(el) for el in arr}
    for key, value in count_dict.items():
        if value % 2 != 0:
            return key


print(find_it(arr=x))


