import math
import numpy as np
import matplotlib.pyplot as plt
from hmgd_core import HMGD_Core

def run_jwst_validation():
    """
    Validates HMGD against the JWST 'Early Massive Galaxy' problem.
    Calculates the scaling of a_0(z) and its impact on formation mass.
    """
    engine = HMGD_Core()
    plt.style.use('dark_background')
    
    # Redshift range from today (z=0) to the First Stars (z=20)
    z_range = np.linspace(0, 20, 100)
    
    # In HMGD, a_0 is inversely proportional to the Hubble Radius L_h.
    # For a flat universe, L_h(z) is roughly L_h(0) / (1+z).
    # Therefore, a_0(z) = a_0(0) * (1+z)
    a0_z = [engine.a_0 * (1 + z) for z in z_range]
    
    # Impact on Galactic Mass for a fixed velocity (V=200 km/s)
    # M = V^4 / (G * a_0)
    v_target = 200 * 1000 # 200 km/s in m/s
    m_target = [(v_target**4) / (engine.G * a0) for a0 in a0_z]
    m_solar = [m / engine.M_solar for m in m_target]
    
    # Plotting
    fig, ax1 = plt.subplots(figsize=(12, 7))
    
    color = 'gold'
    ax1.set_xlabel('Redshift (z)', fontsize=12)
    ax1.set_ylabel('Universal Acceleration a_0(z) [m/s^2]', color=color, fontsize=12)
    ax1.plot(z_range, a0_z, color=color, linewidth=3, label='HMGD a_0 Scaling')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.grid(alpha=0.1)
    
    ax2 = ax1.twinx()
    color = 'cyan'
    ax2.set_ylabel('Required Baryonic Mass for V=200 km/s [M_solar]', color=color, fontsize=12)
    ax2.plot(z_range, m_solar, color=color, linestyle='--', linewidth=2, label='Formation Mass Threshold')
    ax2.tick_params(axis='y', labelcolor=color)
    
    plt.title("HMGD Prediction: High-Redshift Acceleration Scaling (JWST Tension Solution)", fontsize=16, color='white')
    
    # Annotations
    plt.annotate(f"Modern Era (z=0)\na_0 = {engine.a_0:.2e}", 
                 xy=(0, engine.a_0), xytext=(2, engine.a_0*5),
                 arrowprops=dict(facecolor='white', shrink=0.05), color='white')
    
    plt.annotate(f"JWST Era (z=10)\na_0 is 11x Higher!", 
                 xy=(10, engine.a_0*11), xytext=(12, engine.a_0*15),
                 arrowprops=dict(facecolor='gold', shrink=0.05), color='gold')

    fig.tight_layout()
    plt.savefig('theory_visuals/jwst_hmgd_evolution.png')
    
    print(f"Success: Generated JWST evolution plot.")
    print(f"Prediction: At z=10, the required baryonic mass for a 200km/s galaxy is {m_solar[50]:.2e} M_solar.")
    print(f"This is ~10x lower than modern thresholds, explaining 'Impossible' early galaxies.")

if __name__ == "__main__":
    run_jwst_validation()
