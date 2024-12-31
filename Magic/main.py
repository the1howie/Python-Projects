from magic_square import *

if __name__ == '__main__':
    n = int(input("Enter dimension: "))
    M = magic(n)
    print(M)
    valid = validate(M)
    print("\nMagic? {}\n".format(valid[0]))
    if not valid[0]:
        print("WARNINGS: {}\n".format(valid[1]))
