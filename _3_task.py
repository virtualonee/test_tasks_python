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

    len_list = len(list_with_nat_num)

    for i in range(0, len_list):
        max_value_str = str(find_max_value_num(list_with_nat_num, ''))
        return_str = return_str + max_value_str
        list_with_nat_num.remove(max_value_str)

    if len(list_with_zero) != 0:
        return_str = return_str + build_str_with_num_begin_with_zero(list_with_zero)

    return return_str


def find_max_value_num(list_with_nat_num: list[str], additional_str: str):
    result_list = []

    for num in range(9, 0, -1):
        result_list.clear()

        for i in list_with_nat_num:
            if re.fullmatch(additional_str + str(num) + r'\d*', i):
                result_list.append(i)

            if re.fullmatch(additional_str, i):
                return i

        if len(result_list) == 1:
            return result_list[0]

        if len(result_list) > 1:
            if check_equals(result_list):
                return result_list[0]

            if all_str_have_same_len(result_list):
                max_str = find_max_str(result_list)
                return max_str

            max_temp = 0
            for i in result_list:
                if max_temp < int(i[0:len(additional_str) + 1]):
                    max_temp = int(i[0:len(additional_str) + 1])

            additional_str += str(max_temp)[len(additional_str)]
            return find_max_value_num(result_list, additional_str)


def check_equals(result_list: list[str]):
    for i in range(0, len(result_list) - 1):
        if result_list[i] != result_list[i+1]:
            return False
    return True


def all_str_have_same_len(result_list: list[str]):
    temp_len = len(result_list[0])
    for i in result_list:
        if temp_len != len(i):
            return False
    return True


def find_max_str(result_list: list[str]):
    max_temp = 0
    for i in result_list:
        if max_temp < int(i):
            max_temp = int(i)

    return str(max_temp)

def build_str_with_num_begin_with_zero(num_list: list[str]):
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
