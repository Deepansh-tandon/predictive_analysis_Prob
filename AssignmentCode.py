import pandas as pd
import numpy as np

ROLL_NUMBER = 102317257
CSV_PATH = "data.csv"

df = pd.read_csv(CSV_PATH, encoding="latin1", low_memory=False)

x = df["no2"].dropna().astype(float).values

a_r = 0.05 * (ROLL_NUMBER % 7)
b_r = 0.3 * (ROLL_NUMBER % 5 + 1)

z = x + a_r * np.sin(b_r * x)

mean = np.mean(z)
variance = np.var(z)

lam = 1 / (2 * variance)
c = np.sqrt(lam / np.pi)

print("a_r =", a_r)
print("b_r =", b_r)
print("Mean =", mean)
print("Lambda =", lam)
print("c =", c)