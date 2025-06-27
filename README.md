# Non-interactive Zero-Knowledge (NIZK) proof system in the CRS model
## Scenario
1) P wants to prove to V that P knows value such that y = g^a to base g.
2) P picks random value v from set of values Z, and computes t = g^v.
3) P computes c = H(g, y, t) where H() is hash function.
4) P computes d = v – c*a.
5) V or anyone can then check if t = g^d * y^c.