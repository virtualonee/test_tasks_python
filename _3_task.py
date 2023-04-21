import re
import math
from natsort import natsorted


def build_result_str(num_list: list[str]):
    return_str = ''
    list_with_zero = []
    list_with_nat_num = []

    for i in num_list:
        if re.fullmatch(r'0+\d*', i):
            list_with_zero.append(i)
        else:
            list_with_nat_num.append(i)
    num_list.clear()

    if len(list_with_nat_num) == 0:
        return "All strings begin from 0"

    for i in range(0, len(list_with_nat_num)):
        return_str = return_str + str(find_max_value_num(list_with_nat_num))

    if len(list_with_zero) != 0:
        return_str = return_str + build_str_with_num_beg_zero(list_with_zero)

    return return_str


def find_max_value_num(list_with_nat_num: list[str]):
    result_list = []

    for num in range(9, 0, -1):
        result_list.clear()

        for j in list_with_nat_num:
            if re.fullmatch(str(num)+r'\d*', j):
                result_list.append(j)

        if len(result_list) == 1:
            list_with_nat_num.remove(result_list[0])
            return result_list[0]
        elif len(result_list) > 1:
            min_element = min(result_list)
            list_with_nat_num.remove(min_element)
            return min_element


def build_str_with_num_beg_zero(num_list: list[str]):
    result_str = ''
    for i in natsorted(num_list, reverse=True):
        result_str = result_str + i

    return result_str


if __name__ == '__main__':
    number_list = []
    while True:
        number_list.clear()

        try:
            amount = int(math.fabs(int(input("Input numbers of lines: "))))
            print()
        except ValueError:
            print("Wrong data type")
            continue

        print("Input elements of list: ")
        for i in range(0, amount):
            number_list.append(input("L[" + str(i) + "] = "))
            try:
                if int(number_list[i]) < 0:
                    print("Number < 0")
                    break
            except ValueError:
                print("Wrong data type")
                break

        print("Result: " + build_result_str(number_list))
        print()
