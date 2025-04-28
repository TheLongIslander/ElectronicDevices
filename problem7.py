
import sympy as sp
# Given values
V_DD = 5  # V
R_D = 24e3  # Ohms
k_prime = 1e-3  # A/V^2
W_by_L = 1
V_t = 1  # V

# (a) Find points A and B

# Point A: minimum V_GS for saturation (just at threshold)
V_GS_A = V_t
I_D_A = 0  # No overdrive, no current
V_DS_A = V_DD  # Because i_D = 0, so v_DS = V_DD

# Point B: maximum V_GS before leaving saturation
# In saturation, v_DS >= v_GS - V_t
# At edge: v_DS = v_GS - V_t

# Assume v_DS = v_GS - V_t and solve:
# v_DS = V_DD - i_D * R_D
# i_D = (1/2) * k' * (W/L) * (V_GS - V_t)^2

# So: V_DD - i_D * R_D = V_GS - V_t

V_GS = sp.symbols('V_GS', real=True, positive=True)

I_D = 0.5 * k_prime * W_by_L * (V_GS - V_t)**2
V_DS = V_DD - I_D * R_D

# Set v_DS = v_GS - V_t at edge of saturation
eqn = sp.Eq(V_DS, V_GS - V_t)

# Solve for V_GS
V_GS_B_solution = sp.solve(eqn, V_GS)
V_GS_B = float(V_GS_B_solution[0])

# Now find i_D and v_DS at Point B
I_D_B = 0.5 * k_prime * W_by_L * (V_GS_B - V_t)**2
V_DS_B = V_DD - I_D_B * R_D

# (b) Bias at V_OV = 0.5V
V_OV = 0.5  # V
V_GS_Q = V_t + V_OV
I_D_Q = 0.5 * k_prime * W_by_L * V_OV**2
V_DS_Q = V_DD - I_D_Q * R_D

# Incremental gain A_v = -g_m * R_D
# g_m = k' (W/L) (V_GS - V_t) = k' (W/L) V_OV
g_m = k_prime * W_by_L * V_OV
A_v = -g_m * R_D

# Print results
print(f"(a) Point A: (V_GS = {V_GS_A} V, V_DS = {V_DS_A} V)")
print(f"(a) Point B: (V_GS = {V_GS_B:.3f} V, V_DS = {V_DS_B:.3f} V)")
print(f"(b) Bias Point Q: (V_GS = {V_GS_Q} V, V_DS = {V_DS_Q:.3f} V)")
print(f"(b) I_D at Q: {I_D_Q*1e3:.3f} mA")
print(f"(b) Incremental Gain A_v: {A_v:.2f}")
