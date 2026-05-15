import matplotlib.pyplot as plt
import numpy as np
import math
from hmgd_core import HMGD_Core

def generate_rotation_curves():
    engine = HMGD_Core()
    plt.style.use('dark_background')
    
    # Radii range for the curve
    r_kpc = np.linspace(0.1, 100, 500)
    
    # Different Galactic Scales
    scenarios = [
        {'name': 'Massive Spiral', 'mass': 1e12, 'color': 'cyan'},
        {'name': 'Milky Way-like', 'mass': 1e11, 'color': 'lime'},
        {'name': 'Dwarf Galaxy',   'mass': 1e9,  'color': 'magenta'}
    ]
    
    plt.figure(figsize=(12, 7))
    
    for sc in scenarios:
        # HMGD Velocities
        v_hmgd = [engine.get_velocity(sc['mass'], r) for r in r_kpc]
        # Newtonian Velocities (for comparison)
        m = sc['mass'] * engine.M_solar
        v_newton = [math.sqrt((engine.G * m) / (r * engine.kpc)) / 1000 for r in r_kpc]
        
        plt.plot(r_kpc, v_hmgd, color=sc['color'], linewidth=3, label=f"HMGD: {sc['name']}")
        plt.plot(r_kpc, v_newton, color=sc['color'], linestyle='--', alpha=0.5, label=f"Newton: {sc['name']}")

    plt.title("HMGD Rotation Curve Evolution: Newtonian Decay vs. Holographic Flatness", fontsize=16, color='gold')
    plt.xlabel("Galactocentric Radius (r) [kpc]", fontsize=12)
    plt.ylabel("Orbital Velocity (V) [km/s]", fontsize=12)
    plt.ylim(0, 350)
    plt.grid(alpha=0.2)
    plt.legend(ncol=2)
    
    plt.tight_layout()
    plt.savefig("theory_visuals/hmgd_rotation_curves.png")
    print("Success: Generated Rotation Curve evolution plots.")

if __name__ == "__main__":
    generate_rotation_curves()
