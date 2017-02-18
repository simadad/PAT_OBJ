# coding: utf-8
def get_not_key_set(numb):
    not_key_set = {1}
    while numb != 1:
        if numb % 2 != 0:
            numb = numb*3+1
        numb /= 2
        not_key_set.add(numb)
    # print(not_key_set)
    return not_key_set


def get_numb_list():
    k = input('请输入100以内的正整数k：')
    numbs = input('请输入%s个100以内的正整数，空格隔开：' % k)
    numb_list = numbs.split(' ')
    return numb_list


def get_key_set(numb_list):
    # numb_list = get_numb_list()
    key_set = {1}
    not_key_set = {1}
    for numb in numb_list:
        numb = int(numb)
        key_set.add(numb)
        not_key_set |= get_not_key_set(numb)
    key_list = list(key_set)
    # print('key', key_list)
    # print('not', not_key_set)
    for numb in key_list:
        # print(numb, numb in not_key_set)
        if numb in not_key_set:
            key_set.remove(numb)
    # print(222, key_set)
    return key_set


def main():
    numb_list = get_numb_list()
    key_set = get_key_set(numb_list)
    key_list = sorted(list(key_set), reverse=True)
    print('关键数字：', end='')
    for key in key_list[:-1]:
        print(key, end=' ')
    print(key_list[-1])

while True:
    main()
    print()
