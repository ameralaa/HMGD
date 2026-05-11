import math
import numpy as np
import matplotlib.pyplot as plt

class HMGD_Unity_Audit:
    def __init__(self, G=6.67430e-11, c=299792458, L_h=1.37e26):
        self.G = G
        self.c = c
        self.L_h = L_h
        self.a_0 = (self.c**2) / (2 * math.pi * self.L_h)
        
    def get_boost_ratio(self, m, r):
        v2_n = (self.G * m) / r
        v2_b = math.sqrt(self.G * m * self.a_0)
        return math.sqrt(v2_n + v2_b) / math.sqrt(v2_n)

def analyze_unity():
    audit = HMGD_Unity_Audit()
    
    # Logarithmic range of mass and radius
    masses = np.logspace(-60, 60, 100)
    radii = np.logspace(-35, 26, 100)
    
    M, R = np.meshgrid(masses, radii)
    Z = np.zeros_like(M)
    
    for i in range(len(radii)):
        for j in range(len(masses)):
            Z[i, j] = audit.get_boost_ratio(masses[j], radii[i])
            
    plt.figure(figsize=(12, 8))
    plt.pcolormesh(masses, radii, np.log10(Z), shading='auto', cmap='magma')
    plt.colorbar(label='Log10(Boost Ratio)')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Mass (kg)')
    plt.ylabel('Radius (m)')
    plt.title('HMGD Holographic Boost Dominance Map (120+ Orders of Magnitude)')
    
    # Annotate regions
    plt.text(1e-27, 1e-15, 'Proton', color='white', fontweight='bold')
    plt.text(1e30, 1e11, 'Solar', color='white', fontweight='bold')
    plt.text(1e41, 1e21, 'Galaxy', color='white', fontweight='bold')
    plt.text(1e53, 1.3e26, 'Cosmic', color='white', fontweight='bold')
    
    plt.savefig('theory_visuals/hmgd_unity_stress_test.png')
    print("Success: Generated Unity Stress Test map.")

if __name__ == "__main__":
    analyze_unity()
