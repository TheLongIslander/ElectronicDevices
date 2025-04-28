# Given values
V_E = -0.7       # Emitter voltage in volts
V_neg = -3       # Negative supply voltage
V_pos = 3        # Positive supply voltage
R_E = 10e3       # Emitter resistor in ohms
R_C = 5e3        # Collector resistor in ohms
beta = 50        # Current gain

# Step 1: Find I_E
I_E = (V_E - V_neg) / R_E  # (V_E - (-3)) / R_E
# Step 2: Find I_C
I_C = (beta / (beta + 1)) * I_E
# Step 3: Find I_B
I_B = I_C / beta
# Step 4: Find V_C
V_C = V_pos - (I_C * R_C)

# Display results
print(f"I_E = {I_E*1e3:.3f} mA")
print(f"I_C = {I_C*1e3:.3f} mA")
print(f"I_B = {I_B*1e6:.3f} uA")
print(f"V_C = {V_C:.3f} V")
