# Non-interactive Zero-Knowledge (NIZK) proof system in the CRS model
## Scenario
1) P wants to prove to V that P knows value y such that y = g^a.
2) (Setup) P picks random value v from set of values Z, and computes t = g^v.
3) (Prove) P computes c = H(g, y, t) where H() is hash function.
4) (Prove) P computes d = v – c*a.
5) (Verify) V or anyone can then check if t = g^d * y^c.