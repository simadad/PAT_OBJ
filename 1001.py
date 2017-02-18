# coding: utf-8
def main():
    n = int(eval(input('请输入1000以内的正整数n：')))
    times = 0
    while n != 1:
        if n < 1 or n > 1000:
            n = int(eval(input('请输入1000以内的正整数n：')))
        elif n % 2 != 0:
            n = n*3+1
        n /= 2
        times += 1
    print(times)

main()
