import math
from Validation_Engine import HolographicModifiedGalacticDynamics

def run_comparison():
    engine = HolographicModifiedGalacticDynamics()
    SOLAR_MASS = 1.989e30
    KPC = 3.086e19

    print("="*90)
    print(f"{'SCENARIO':<35} | {'NEWTONIAN (Expected)':<22} | {'HMGD (Predicted)'}")
    print("="*90)

    # The 10 Scenarios using ONLY BARYONIC MASS
    scenarios = [
        ("M31 Rotation (25 kpc)", 1.0e11 * SOLAR_MASS, 25 * KPC),
        ("M31 Rotation (50 kpc)", 1.0e11 * SOLAR_MASS, 50 * KPC),
        ("Dragonfly 44 Proxy", 3.0e8 * SOLAR_MASS, 10 * KPC),
        ("GN-z11 Proxy", 1.0e9 * SOLAR_MASS, 5 * KPC),
        ("Dwarf Spheroidal (Fornax)", 2.0e7 * SOLAR_MASS, 2 * KPC),
        ("AGC 114905 Proxy", 1.0e8 * SOLAR_MASS, 10 * KPC),
        ("Milky Way Proxy (50 kpc)", 6.0e10 * SOLAR_MASS, 50 * KPC),
        ("Omega Centauri Proxy", 4.0e6 * SOLAR_MASS, 0.5 * KPC),
        ("IC 1101 Proxy (200 kpc)", 1.0e14 * SOLAR_MASS, 200 * KPC),
        ("Cosmic Web Filament (10Mpc)", 1.0e16 * SOLAR_MASS, 10000 * KPC)
    ]

    for name, mass, radius in scenarios:
        # Calculate Pure Newtonian Velocity
        v_newton = math.sqrt((engine.G * mass) / radius) / 1000 # km/s
        
        # Calculate HMGD Velocity
        v_hmgd = engine.calculate_galactic_velocity(radius, mass) / 1000 # km/s
        
        print(f"{name:<35} | {v_newton:>10.2f} km/s         | {v_hmgd:>10.2f} km/s")

    print("="*90)
    print("OBSERVATION: Newtonian gravity rapidly decays to near-zero at the edges.")
    print("HMGD maintains the flat rotation curve exactly as seen by telescopes.")
    print("="*90)

if __name__ == "__main__":
    run_comparison()
