from paper_code.hmgd_core import HMGD_Core
import math

engine = HMGD_Core()

print("--- Andromeda (M31) ---")
v_m31 = engine.get_velocity(1.0e11, 50)
print(f"Prediction: {v_m31:.2f} km/s")

print("\n--- Lensing Deflection (M=1e11, b=10kpc) ---")
alpha = engine.get_lensing_deflection(1.0e11, 10)
print(f"Prediction: {alpha:.2f}\"")

print("\n--- Cosmological Constant ---")
lam = engine.get_cosmological_constant(0.31)
print(f"Prediction: {lam:.3e} m^-2")

print("\n--- CMB P3/P1 Ratio ---")
# This requires CAMB, but we can check what the audit script says
import subprocess
result = subprocess.run(['python', 'paper_code/boltzmann_audit.py'], capture_output=True, text=True)
for line in result.stdout.split('\n'):
    if "Ratio" in line:
        print(line)
