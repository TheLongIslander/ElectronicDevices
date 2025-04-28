# Given values
i_d1 = 200e-6  # 200 μA
i_d2 = 205e-6  # 205 μA
v_ds1 = 1.0    # 1 V
v_ds2 = 1.5    # 1.5 V

# Calculate output resistance r_o
delta_vds = v_ds2 - v_ds1
delta_id = i_d2 - i_d1
r_o = delta_vds / delta_id

# Calculate channel-length modulation parameter lambda (λ)
lambda_ = 1 / (r_o * i_d1)

# Calculate Early voltage V_A
V_A = 1 / lambda_

# Print results
print(f"Output resistance r_o = {r_o:.2f} ohms")
print(f"Channel-length modulation parameter λ = {lambda_:.4f} V^-1")
print(f"Early voltage V_A = {V_A:.2f} V")
