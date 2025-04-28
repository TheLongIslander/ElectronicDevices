# Given values
gm_target = 20e-3  # 20 mA/V
rpi_min = 4000     # 4000 ohms
VT = 25e-3         # 25 mV (thermal voltage at room temp)

# Find collector current
Ic = gm_target * VT

# Find minimum beta
beta_min = rpi_min * gm_target

print(f"Collector-bias current (Ic): {Ic * 1e3:.2f} mA")
print(f"Minimum beta (β): {beta_min:.2f}")
