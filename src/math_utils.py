# math_utils.py

def gcd(a, b):
    """
    Compute Greatest Common Divisor using Euclidean Algorithm
    """

    while b != 0:
        a, b = b, a % b

    return a


def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm

    Returns:
        gcd, x, y

    Such that:
        ax + by = gcd(a, b)
    """

    if a == 0:
        return b, 0, 1

    gcd_value, x1, y1 = extended_gcd(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcd_value, x, y


def mod_inverse(e, phi):
    """
    Compute modular inverse of e mod phi

    d = e^(-1) mod phi
    """

    gcd_value, x, y = extended_gcd(e, phi)

    if gcd_value != 1:
        raise Exception("Modular inverse does not exist")

    return x % phi


def mod_exp(base, exponent, modulus):
    """
    Fast Modular Exponentiation
    (Square-and-Multiply Algorithm)

    Efficiently computes:
        (base ^ exponent) % modulus
    """

    result = 1

    base = base % modulus

    while exponent > 0:

        # If exponent is odd
        if exponent % 2 == 1:
            result = (result * base) % modulus

        exponent = exponent >> 1

        base = (base * base) % modulus

    return result

if __name__ == "__main__":

    print("GCD:", gcd(48, 18))

    gcd_value, x, y = extended_gcd(30, 20)
    print("Extended GCD:", gcd_value, x, y)

    print("Mod Inverse:", mod_inverse(7, 40))

    print("Mod Exp:", mod_exp(4, 13, 497))