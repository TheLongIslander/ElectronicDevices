# Given values
V_t = -0.5  # V
mu_p_Cox = 100e-6  # A/V^2
L = 0.18e-6  # meters
V_DD = 1.8  # V
V_D = 0.8  # V
I_D = 160e-6  # A

# Calculate VSG
V_SG = V_DD - V_D

# Solve for W
W = (2 * I_D * L) / (mu_p_Cox * (V_SG - abs(V_t))**2)

# Solve for R
R = V_D / I_D

# Print results
print(f"W = {W*1e6:.2f} μm")
print(f"R = {R:.2f} Ω")
