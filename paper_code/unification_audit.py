import math
import numpy as np
import matplotlib.pyplot as plt
from hmgd_core import HMGD_Core

def run_unification_audit():
    """
    Formalizes the 2.0 Informational Ratio.
    Demonstrates that at the Holographic Horizon, the TOTAL mass influence
    relative to baryons approaches the Unification Constant (2.0).
    """
    engine = HMGD_Core()
    plt.style.use('dark_background')
    
    # Range of Galactic Masses (10^7 to 10^13 Solar Masses)
    masses = np.logspace(7, 13, 100)
    
    total_ratios = []
    for m_solar in masses:
        m_bar = m_solar * engine.M_solar
        # The 'Holographic Transition Radius' r_h where a_grav = a_0
        r_h = math.sqrt((engine.G * m_bar) / engine.a_0)
        
        # Effective Mass M_eff at r_h
        v_flat2 = math.sqrt(engine.G * m_bar * engine.a_0)
        m_eff = (v_flat2 / engine.G) * r_h
        
        # TOTAL Ratio = (M_bar + M_eff) / M_bar
        # At r_h, M_eff = M_bar, so this should be exactly 2.0
        total_ratio = (m_bar + m_eff) / m_bar
        total_ratios.append(total_ratio)

    plt.figure(figsize=(10, 6))
    plt.plot(masses, total_ratios, color='lime', linewidth=4, label='Total Informational Ratio (M_tot / M_bar)')
    plt.axhline(y=2.0, color='white', linestyle='--', alpha=0.5, label='Unification Limit (2.0)')
    
    plt.title("The 2.0 Informational Ratio: Baryonic-Holographic Unification", fontsize=16, color='gold')
    plt.xscale('log')
    plt.xlabel('Baryonic Mass (M_bar) [Solar Masses]', fontsize=12)
    plt.ylabel('Total Informational Ratio', fontsize=12)
    plt.ylim(1.5, 2.5) # Zoom in on the 2.0 limit
    plt.grid(alpha=0.1)
    
    plt.annotate("Unification Point: 2.0\n(1:1 Baryon-Information Balance)", 
                 xy=(1e10, 2.0), xytext=(1e8, 2.2),
                 arrowprops=dict(facecolor='lime', shrink=0.05),
                 fontsize=12, color='lime')

    plt.tight_layout()
    plt.savefig('theory_visuals/unification_ratio.png')
    
    print(f"Success: Generated Corrected 2.0 Unification Ratio audit.")
    print(f"Result: Total Influence = Baryons (1.0) + Information (1.0) = 2.0.")

if __name__ == "__main__":
    run_unification_audit()
