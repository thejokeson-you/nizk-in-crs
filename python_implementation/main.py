# main.py

import numpy as np
import hashlib
import random

# Used for setup stage, generate (p, g) group which represents CRS string
class Group:
    def __init__(self, p, g):
    


# 2048-bit prime, for standard security against DLog attacks
p_hex = """
FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1
29024E088A67CC74020BBEA63B139B22514A08798E3404DD
EF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245
E485B576625E7EC6F44C42E9A63A3620FFFFFFFFFFFFFFFF
""".replace("\n", "").replace(" ", "")

p = int(p_hex, 16)

g = 2
q = (p-1) // 2

# Use Fiat-Shamir to hash given elements
def fiat_shamir_hash(*elements):
    data = b''.join(int(e).to_bytes((e.bit_length() + 7) // 8, 'big') for e in elements)
    return int.from_bytes(hashlib.sha256(data).digest(), 'big')


def prove(group, x):


def verify(group, y, proof):