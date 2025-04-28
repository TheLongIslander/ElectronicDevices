import sympy as sp

# Define variables
I = sp.symbols('I')  # current through 1k resistor
V = sp.symbols('V')  # voltage at the V node

# Circuit assumptions:
# D1 is ON (short circuit to ground), D2 is OFF (open circuit)
# Because if D1 is ON, voltage at its anode = 0V.
# Thus, V = 0V ideally, because D2 is not conducting.

# Set up the equation for current I:
# Voltage drop across 1k ohm resistor = 3V - 0V = 3V
# So I = (3V - 0V) / 1kΩ
eq1 = sp.Eq(I, 3 / 1000)  # Ohm's Law

# Solve for I
current_solution = sp.solve(eq1, I)[0]

# Voltage V is 0V because D1 shorts the node to ground.
voltage_solution = 0

# Display results
print(f"Current I = {current_solution*1000:.2f} mA")
print(f"Voltage V = {voltage_solution:.2f} V")
