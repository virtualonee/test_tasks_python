import re


def change_string(string: str):
    list_string = re.findall(r'\d{2,4}\\\d{2,5}', string)

    if len(list_string) == 0:
        print("Not found")

    for i in list_string:
        str1, str2 = re.split(r"\\", i)

        while re.fullmatch(r'\d{2,3}', str1):
            str1 = '0'+str1

        while re.fullmatch(r'\d{2,4}', str2):
            str2 = '0'+str2

        print(str1+'\\'+str2)


if __name__ == '__main__':
    print("Input string in format int(2-4)\\int(2-5)")
    print()
    while True:
        s = input("Input string: ")
        change_string(s)
        print()
