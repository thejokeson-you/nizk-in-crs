# Non-interactive Zero-Knowledge (NIZK) proof system in the CRS model
## Scenario
1) P wants to prove to V that P knows value y such that y = g^a.
2) (Setup) Generate CRS string
3) (Setup) P knows a witness w for statement x (i.e., y=g^a), such that R(x, w) = true, and uses the CRS and w to compute t = g^v.
4) (Prove) P computes c = H(g, y, t) where H() is hash function.
5) (Prove) P computes d = v – c*a.
6) (Verify) V or anyone can then check if t = g^d * y^c.