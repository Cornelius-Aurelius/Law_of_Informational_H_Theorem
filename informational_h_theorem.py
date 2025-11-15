# Informational H-Theorem / Entropy Law Verification (vOmega Law 39)

import numpy as np

# Initial non-uniform distribution
p = np.random.rand(1000)
p /= p.sum()

# Uniform equilibrium distribution
q = np.ones(1000) / 1000

def kl(p, q):
    return np.sum(p * np.log(p / q))

def step(p, rate=0.01):
    p = p - rate * (p - q)
    p = np.clip(p, 1e-12, None)
    p /= p.sum()
    return p

history = []
for _ in range(500):
    history.append(kl(p, q))
    p = step(p)

print("KL initial:", history[0])
print("KL final:", history[-1])
