PATH_LENGTH = 17.0666894
SQRT2, SQRT5 = 2**(1/2), 5**(1/2)


def fraction_part(val):
    return val - int(val)


def is_equal(a, b, precision=5):
    return abs(a - b) < 10**-precision


PATH_LENGTH_FRAC = fraction_part(PATH_LENGTH)
for b in range(20):
    for c in range(20):
        if is_equal(fraction_part(b*SQRT2 + c*SQRT5), PATH_LENGTH_FRAC):
            a = int(PATH_LENGTH - (b*SQRT2 + c*SQRT5))
            print(f'{a} + {b}√2 + {c}√5 = {PATH_LENGTH}')

print("So: 0 straight lines, 1 diagonals, 7 knight diagonal lines")
