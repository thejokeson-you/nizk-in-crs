# Non-interactive Zero-Knowledge (NIZK) proof system in the CRS model
## Scenario - DLog problem
1) P wants to prove to V that it knows value x such that y = g^x.
2) (Setup) Generate CRS string used for verification & proof generation; (p, g), where p is a large prime
3) (Setup) Generate a secret witness w. P knows a witness w for x, such that R(x, w) = true.
4) (Prove) P computes proof pi = (t, s) using witness w and crs.
5) (Verify) V then verifies proof pi given CRS and statement.

Utilises Fiat-Shamir heuristic in order to transform a given proof system into a NIZK proof system, thereby allowing a proof to be generated without needing a challenge.
