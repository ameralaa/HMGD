import math
import sys

class HolographicModifiedGalacticDynamics:
    """
    The core mathematical engine of HMGD.
    Authored by Amer Alaa Eldin Attia (ameralaah99@gmail.com)
    """
    def __init__(self, G=6.67430e-11, c=299792458):
        self.G, self.c = G, c
        self.L_h = 1.37e26 # Hubble Radius (~14.4 billion light years)

    def rs(self, m): 
        return (2 * self.G * m) / (self.c**2)

    def a0(self):
        """Universal Informational Acceleration"""
        return (self.c**2) / (2 * math.pi * self.L_h)

    def v_newton(self, r, m):
        return math.sqrt((self.G * m) / r)

    def v_hmgd(self, r, m):
        """Holographic Modified Velocity (Logarithmic Potential)"""
        v2_newton = (self.G * m) / r
        v2_flat = math.sqrt(self.G * m * self.a0())
        return math.sqrt(v2_newton + v2_flat)

def clear_screen():
    print("\n" * 2)

def main():
    engine = HolographicModifiedGalacticDynamics()
    
    while True:
        clear_screen()
        print("="*70)
        print("   HOLOGRAPHIC MODIFIED GALACTIC DYNAMICS (HMGD) - CALCULATOR")
        print("="*70)
        print(" [1] Schwarzschild Radius (Input: Mass)")
        print(" [2] Universal Informational Acceleration a_0")
        print(" [3] Galactic Orbital Velocity (Input: Radius, Mass)")
        print(" [4] Compare Newtonian vs HMGD Velocity (Input: Radius, Mass)")
        print(" [Q] Quit")
        print("="*70)
        
        choice = input("\nSelect an option: ").strip().lower()
        
        if choice == 'q':
            print("\nExiting HMGD Calculator.")
            break
            
        try:
            if choice == '1':
                m = float(input("Enter Baryonic Mass (kg): "))
                print(f"\n>> Schwarzschild Radius (rs): {engine.rs(m):.2e} meters")
                
            elif choice == '2':
                print(f"\n>> Universal Informational Acceleration (a_0): {engine.a0():.2e} m/s^2")
                print(f"   (The transition acceleration derived from c^2 / L_h)")

            elif choice == '3':
                r = float(input("Enter Radius from core (m): "))
                m = float(input("Enter Baryonic Mass (kg): "))
                v = engine.v_hmgd(r, m)
                print(f"\n>> HMGD Orbital Velocity: {v/1000:.2f} km/s")

            elif choice == '4':
                r = float(input("Enter Radius from core (m): "))
                m = float(input("Enter Baryonic Mass (kg): "))
                vn = engine.v_newton(r, m)
                vh = engine.v_hmgd(r, m)
                print(f"\n>> Newtonian Velocity:    {vn/1000:.2f} km/s")
                print(f">> HMGD Velocity:         {vh/1000:.2f} km/s")
                print(f">> Dark Matter Boost Eq:  {vh/vn:.4f}x multiplier")
            
            else:
                print("\nInvalid choice. Please try again.")
                
        except ValueError:
            print("\nError: Please enter valid numerical values.")
            
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
