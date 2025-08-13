# Python program to calculate pow(b, e)

# Recursive function to calculate pow(b, e)
def power(b, e):

    # Base Case: pow(b, 0) = 1
    if e == 0:
        return 1

    if e < 0:
        return 1 / power(b, -e)

    temp = power(b, e // 2)

    if e % 2 == 0:
        return temp * temp
    else:
        return b * temp * temp

if __name__ == "__main__":
    b = 3.0
    e = 5
    res = power(b, e)
    print(res)
