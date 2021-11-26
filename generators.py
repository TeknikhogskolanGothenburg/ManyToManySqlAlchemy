def gen(n):
    i = 0
    while i < n:
        yield i
        i += 1


def main():
    comp_gen = (i*2 for i in range(4))
    g = gen(3)
    print(next(comp_gen))
    print(next(comp_gen))
    print(next(comp_gen))
    print(next(comp_gen))


if __name__ == '__main__':
    main()
