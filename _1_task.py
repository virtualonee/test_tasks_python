import re


def change_string(string):
    string = re.search(r'\d{2,4}\\\d{2,5}', string)

    if string is None:
        return 'Not found'

    string = string.group(0)

    str1, str2 = re.split(r"\\", string)

    while re.fullmatch(r'\d{2,3}', str1):
        str1 = '0'+str1

    while re.fullmatch(r'\d{2,4}', str2):
        str2 = '0'+str2

    return str1+'\\'+str2


if __name__ == '__main__':
    print("Input string in format int(2-4)\\int(2-5)")
    while True:
        s = input()
        print(change_string(s))
