# Given values
Vt = 1.0  # V
kn = 4e-3  # A/V^2
Vgs = 1.5  # V
Id = 0.5e-3  # A
Vd = 7.0  # V
VA = 100  # V

# Resistor values
Rg1 = 10e6  # 10 MΩ
Rg2 = 200e3  # 200 kΩ
Rd = 16e3  # 16 kΩ
Rl = 16e3  # 16 kΩ
Rs1 = 5e6  # 5 MΩ
Rs2 = 7e3  # 7 kΩ

# (a) Verify values
# Check if Id is consistent with Vgs using equation:
# Id = kn/2 * (Vgs - Vt)^2

Id_calc = (kn / 2) * (Vgs - Vt)**2
print(f"(a) Calculated Id = {Id_calc*1e3:.3f} mA (given Id = 0.5 mA)")

# Calculate Vs (source voltage)
# Source resistors are Rs1 || Rs2
Rs_parallel = 1 / (1/Rs1 + 1/Rs2)
Vs = Id * Rs_parallel
print(f"Calculated Vs = {Vs:.3f} V")

# Calculate Vd
Vd_calc = 15 - Id * Rd
print(f"Calculated Vd = {Vd_calc:.3f} V (given Vd = 7.0 V)")

# (b) Find gm and ro
# gm = 2 * Id / (Vgs - Vt)
gm = 2 * Id / (Vgs - Vt)
print(f"(b) gm = {gm*1e3:.3f} mA/V")

# ro = VA / Id
ro = VA / Id
print(f"ro = {ro/1e3:.3f} kΩ")

# (c) Find Rin, vgs/vsig, vo/vgs, and vo/vsig
# Rin = Rg1 || Rg2
Rin = 1 / (1/Rg1 + 1/Rg2)
print(f"(c) Rin = {Rin/1e3:.3f} kΩ")

# Small signal analysis:
# vgs/vsig = Rin / (Rin + Rsig)
Rsig = 200e3  # 200 kΩ
vgs_vsig = Rin / (Rin + Rsig)
print(f"vgs/vsig = {vgs_vsig:.3f}")

# vo/vgs = -gm * (Rd || Rl || ro)
Ro_parallel = 1 / (1/Rd + 1/Rl + 1/ro)
vo_vgs = -gm * Ro_parallel
print(f"vo/vgs = {vo_vgs:.3f}")

# vo/vsig = (vo/vgs) * (vgs/vsig)
vo_vsig = vo_vgs * vgs_vsig
print(f"vo/vsig = {vo_vsig:.3f}")
