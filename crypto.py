import random


def encrypt(x, Q):
    """
    3-party Encryption
    :param x: values expecting to be encrypted
    :param Q: Secret-key for encryption
    :return: encrypted shared for each party (len == 3)
    """
    share_a = random.randint(0, Q)
    share_b = random.randint(0, Q)
    share_c = (x - share_a - share_b) % Q
    return share_a, share_b, share_c


def decrypt(shares, Q):
    return sum(shares) % Q


def add(x, y, Q):
    """
    Addition of Encrypted Values
    :param x: encrypted val
    :param y: encrypted val
    :return: 3-shares of result of addition (encrypted)
    """
    # the first worker adds their shares together
    # the second worker adds their shares together
    # the third worker adds their shares together

    shares = [(x[0] + y[0]) % Q,
              (x[1] + y[1]) % Q,
              (x[2] + y[2]) % Q]

    return shares
