# Zener regulator problem

# Given values
Vz_nominal = 7.5    # V (zener nominal voltage)
Iz_nominal = 10e-3  # A (zener specified at 10mA)
rz = 30             # Ohms (zener incremental resistance)
Iknee = 0.5e-3      # A (knee current)
Vsupply_nominal = 10 # V (nominal supply voltage)
Iload_nominal = 5e-3 # A (nominal load current)

# Part (a): Find the value of R
# IR = Iz_nominal + Iload_nominal
IR_nominal = Iz_nominal + Iload_nominal
R = (Vsupply_nominal - Vz_nominal) / IR_nominal

print(f"(a) Value of R = {R:.2f} ohms")

# Part (b): Output voltage when supply is 10% high and load is removed
Vsupply_high = 1.1 * Vsupply_nominal
# With no load: IR = Iz
Iz_high = (Vsupply_high - Vz_nominal) / R
Vo_high = Vz_nominal + Iz_high * rz

print(f"(b) Output voltage with 10% high supply and no load = {Vo_high:.2f} V")

# Part (c): Largest load current while keeping Iz >= Iknee and supply 10% low
Vsupply_low = 0.9 * Vsupply_nominal
IR_low = (Vsupply_low - Vz_nominal) / R
# IR = Iz + Iload
Iload_max = IR_low - Iknee

print(f"(c) Maximum load current while keeping Iz >= Iknee with 10% low supply = {Iload_max*1e3:.2f} mA")
