# main.py

import numpy as np
import hashlib
import random

# Used for setup stage, generate (p, g) group which represents CRS string
class Group:
    def __init__(self, p, g):
      self.p = p  # Large prime
      self.g = g  # Generator g
      self.q = (p - 1) // 2  # order of the subgroup
    
    # Exponential operation method base^exponent (for convenience)
    def exp(self, base, exponent):
        return pow(base, exponent, self.p)


# 2048-bit prime, for standard security against DLog attacks. Included for demonstration purposes
# p_hex = """
# FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1
# 29024E088A67CC74020BBEA63B139B22514A08798E3404DD
# EF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245
# E485B576625E7EC6F44C42E9A63A3620FFFFFFFFFFFFFFFF
# """.replace("\n", "").replace(" ", "")

# p = int(p_hex, 16)

# 2048-bit prime number without converting first. 
p = 208351617316091241234326746312124448251235562226470491514186331217050270460481 

g = 2

# Use Fiat-Shamir to hash given elements
def fiat_shamir_hash(*elements):
    data = b''.join(int(e).to_bytes((e.bit_length() + 7) // 8, 'big') for e in elements)
    return int.from_bytes(hashlib.sha256(data).digest(), 'big')


def prove(group, x):
  g = group.g
  p = group.p
  q = group.q
  y = group.exp(g, x)  # y = g^x; P wants to prove x such that this is true

  r = random.randrange(1, q)
  t = group.exp(g, r)  # Commitment

  c = fiat_shamir_hash(g, y, t) % q  # Challenge
  s = (r + c * x) % q  # Response

  return y, (t, s)


def verify(group, y, proof):
  g = group.g
  p = group.p
  q = group.q
  (t, s) = proof # Consists of (commitment, response)

  c = fiat_shamir_hash(g, y, t) % q # Retrieve challenge
  
  left = group.exp(g, s)  # Get y = g^s, where s is the given solution, and P wants to prove that it knows x, so s == x ideally
  right = (t * group.exp(y, c)) % p  # Do t * y^c and compare to given proof   

  return left == right
