#!/usr/bin/env pypy3
from string import digits, ascii_letters
from time import sleep
from multiprocessing import Pool, Queue, Lock
from itertools import permutations
from collections import Counter

# Configurable variables
# 32C64T machine runtime, 17: 2.7s, 18: 14s, 19: 2m, 20: 8m
PROCESSES = 128
BASE = 20 # 17 or up

# Don't change anything below this line
WIDTH = 4
BOUND = int('2034', BASE)
PPPPP = int('11111', BASE)
NUMERALS = digits + ascii_letters
CF8Q = Queue()
exit_lock = Lock()

def baseN(num):
    return ((num == 0) and NUMERALS[0]) or (baseN(num // BASE).lstrip(NUMERALS[0]) + NUMERALS[num % BASE])

def check_last_8(ΝΞΟΠ):
    ΙΚΛΜ = PPPPP - ΝΞΟΠ
    c = Counter()
    c.update(baseN(ΙΚΛΜ * (BASE ** WIDTH) + ΝΞΟΠ))
    for i in c.items():
        if i[0] == '1' or i[1] > 1:
            return 0
    return ΙΚΛΜ

def check_first_8(i, ΙΚΛΜ):
    if i[0] == 0 or i[4] == 0:
        return 0
    ΑΒΓΔ, ΕΖΗΘ = i[0] * (BASE ** 3) + i[1] * (BASE ** 2) + i[2] * BASE + i[3], \
        i[4] * (BASE ** 3) + i[5] * (BASE ** 2) + i[6] * BASE + i[7]
    if ΑΒΓΔ - ΕΖΗΘ == ΙΚΛΜ:
        return 1

def check_first_8_worker(queue):
    while 1:
        used_digits, ΙΚΛΜ = queue.get()
        for j in permutations(set(range(BASE)) - set(used_digits) - {1}, 8):
            if check_first_8(j, ΙΚΛΜ):
                print(j, used_digits)
        if queue.qsize() == 0:
            try:
                exit_lock.release()
            except Exception as e:
                pass

if __name__ == '__main__':
    for ΝΞΟΠ in range(BOUND, BASE ** WIDTH):
        ΙΚΛΜ = check_last_8(ΝΞΟΠ)
        if ΙΚΛΜ != 0:
            used_digits = [int(i, BASE) for i in baseN(ΙΚΛΜ * (BASE ** WIDTH) + ΝΞΟΠ)]
            CF8Q.put((used_digits, ΙΚΛΜ,))
    exit_lock.acquire()
    pool = Pool(PROCESSES, check_first_8_worker, (CF8Q,))
    exit_lock.acquire()
