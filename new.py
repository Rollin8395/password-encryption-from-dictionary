"""
Zipfile password cracker using a dictionary attack and, if not successful,
switches to bruteforce
"""

import itertools
import string
import time
import zipfile


ARCHIVE_PATH = 'enc.zip'
DICTIONARY_PATH = 'rockyou.txt'


def dictionary_attack():
    """Tries at first a dictionary attack"""

    t0 = time.time()
    with open(DICTIONARY_PATH) as f:
        for password in f:
            password = password.rstrip().encode()
            try:
                zipfile.ZipFile(ARCHIVE_PATH).extractall(pwd=password)
                t1 = time.time()
                print('Password found: {}\nTime spent: {} seconds'.format(password.decode(), t1 - t0))

                return True
            except RuntimeError:
                pass
    return False


def bruteforce_attack(nbcharmax):
    """If the password hasn't been found yet, the function switches to bruteforce"""

    alphabet = string.ascii_letters + string.digits + string.punctuation

    t0 = time.time()
    for i in range(1, nbcharmax):
        for j in itertools.product(alphabet, repeat=i):
            password = ''.join(j).encode()
            try:
                zipfile.ZipFile(ARCHIVE_PATH).extractall(pwd=password)
                t1 = time.time()
                print('Password found: {}\nTime spent: {} seconds'.format(password.decode(), t1 - t0))

                return True
            except RuntimeError:
                pass
    return False

if __name__ == "__main__":
    if not dictionary_attack():
        bruteforce_attack(4)