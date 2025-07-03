# main.py

import numpy as np
import hashlib
import random


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

# Use Fiat-Shamir
def fiat_shamir_hash():


# Generate CRS string from trusted third party, assuming TTP exists
def generate_crs():


def setup():


def prove():


def verify():