# coding: utf-8
def get_number_list(numb):
    # numb = input('请输入10000以内的正整数：')
    numb_list = []
    for i in range(4):
        try:
            if int(numb[i]) in range(10):
                numb_list.append(numb[i])
            else:
                raise ValueError
        except IndexError:
            numb_list.append('0')
    return numb_list


def get_max_and_min(numb_list):
    max_list = sorted(numb_list, reverse=True)
    min_list = sorted(numb_list, reverse=False)
    max_numb = int(''.join(max_list))
    min_numb = int(''.join(min_list))
    new_numb = max_numb - min_numb
    print('%d - %d = %d' % (max_numb, min_numb, new_numb))
    return str(new_numb)


def main(origin):
    numb_list = get_number_list(origin)
    new_numb = get_max_and_min(numb_list)
    if new_numb == origin:
        pass
    else:
        main(new_numb)

while True:
    origin_numb = input('请输入10000以内的正整数：')
    main(origin_numb)
