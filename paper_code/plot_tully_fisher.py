import matplotlib.pyplot as plt
import numpy as np
from hmgd_core import HMGD_Core

def generate_plots():
    engine = HMGD_Core()
    plt.style.use('dark_background')
    
    # Range of Galactic Masses (10^9 to 10^12.5 Solar Masses)
    masses_log = np.linspace(9, 12.5, 50)
    masses = 10**masses_log
    
    # ---------------------------------------------------------
    # PLOT 1: UNIVERSAL TULLY-FISHER (Figure 1)
    # ---------------------------------------------------------
    plt.figure(figsize=(10, 8))
    velocities = [engine.get_velocity(m, 50) for m in masses]
    plt.loglog(velocities, masses, color='gold', linewidth=4, label='HMGD Prediction (Slope 4.0)')
    
    plt.title("Figure 1: Universal Tully-Fisher Relation", fontsize=16, color='gold')
    plt.xlabel("Max Orbital Velocity (V) [km/s]", fontsize=12)
    plt.ylabel("Galactic Mass (M) [Solar Masses]", fontsize=12)
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.legend(fontsize=12)
    plt.annotate("Exact Mathematical Slope: 4.0\nDerived from Informational Horizon", 
                 xy=(200, 1e11), xytext=(40, 5e11),
                 arrowprops=dict(facecolor='gold', shrink=0.05),
                 fontsize=12, color='gold')
    plt.tight_layout()
    plt.savefig("theory_visuals/hmgd_tully_fisher.png")
    print("Success: Generated Figure 1 (Tully-Fisher).")

    # ---------------------------------------------------------
    # PLOT 2: RADIAL SCALE INVARIANCE (Figure 2)
    # ---------------------------------------------------------
    plt.figure(figsize=(10, 8))
    radii_kpc = [30, 100, 500]
    colors = ['#ff4444', '#44ff44', '#4444ff']
    
    for i, r in enumerate(radii_kpc):
        velocities = [engine.get_velocity(m, r) for m in masses]
        plt.loglog(velocities, masses, color=colors[i], label=f'Radius: {r} kpc', linewidth=2, alpha=0.8)

    plt.title("Figure 2: Radial Scale Invariance", fontsize=16, color='gold')
    plt.xlabel("Orbital Velocity (V) [km/s]", fontsize=12)
    plt.ylabel("Galactic Mass (M) [Solar Masses]", fontsize=12)
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.legend(fontsize=12)
    plt.annotate("Asymptotic Convergence\n(Flat Rotation Curves)", 
                 xy=(200, 5e11), xytext=(50, 2e12),
                 arrowprops=dict(facecolor='white', shrink=0.05),
                 fontsize=12, color='white')
    
    plt.tight_layout()
    plt.savefig("theory_visuals/hmgd_tully_fisher_comparison.png")
    print("Success: Generated Figure 2 (Scale Invariance).")

if __name__ == "__main__":
    generate_plots()
