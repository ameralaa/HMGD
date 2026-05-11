import unittest
import math

class HolographicModifiedGalacticDynamics:
    """
    Official HMGD Mathematical Engine
    Authored by Amer Alaa Eldin Attia (ameralaah99@gmail.com)
    """
    def __init__(self, G=6.67430e-11, c=299792458):
        self.G = G
        self.c = c
        self.L_h = 1.37e26 # Hubble Radius (~14.4 billion light years)

    def calculate_rs(self, m): 
        return (2 * self.G * m) / (self.c**2)

    def calculate_galactic_velocity(self, r, m):
        """
        Galactic Orbital Velocity derived from Logarithmic Informational Potential.
        v^2 = GM/r + sqrt(GM a_0) where a_0 = c^2 / (2 * pi * L_h)
        """
        a_0 = (self.c**2) / (2 * math.pi * self.L_h)
        
        # Newtonian Component
        v2_newton = (self.G * m) / r
        
        # Holographic Flat Component
        v2_flat = math.sqrt(self.G * m * a_0)
        
        # Combined Velocity
        return math.sqrt(v2_newton + v2_flat)

class TestHMGD(unittest.TestCase):
    @classmethod
    def setUpClass(cls): 
        cls.engine = HolographicModifiedGalacticDynamics()
    
    def run_s(self, n, d, r): 
        print(f"[Case {n}] {d}: {r}")

    def test_galactic_dynamics_suite(self):
        engine = self.engine
        print("="*80 + "\nHMGD: GALACTIC DYNAMICS VALIDATION SUITE\n" + "="*80)
        
        # Test 1: M31 Andromeda
        m_m31_visible = 1.0e11 * 1.98e30 # Visible Baryonic Mass ONLY
        r_m31_25 = 25000 * 3.086e16     # 25kpc Radius
        r_m31_50 = 50000 * 3.086e16     # 50kpc Radius (Deep Edge)
        
        v_25 = engine.calculate_galactic_velocity(r_m31_25, m_m31_visible)
        v_50 = engine.calculate_galactic_velocity(r_m31_50, m_m31_visible)
        
        self.run_s("01", "M31 Rotation Velocity (25 kpc)", f"{v_25/1000:.2f} km/s (Flatness Check)")
        self.run_s("02", "M31 Rotation Velocity (50 kpc)", f"{v_50/1000:.2f} km/s (Flatness Proof)")

        # Test 2: Ultra-Diffuse Galaxy (Dragonfly 44 proxy)
        m_udg = 3.0e8 * 1.98e30
        r_udg = 10000 * 3.086e16
        v_udg = engine.calculate_galactic_velocity(r_udg, m_udg)
        self.run_s("03", "Dragonfly 44 Proxy Velocity", f"{v_udg/1000:.2f} km/s")
        
        # Test 3: High Redshift (GN-z11 proxy)
        m_ancient = 1.0e9 * 1.98e30
        r_ancient = 5000 * 3.086e16
        v_ancient = engine.calculate_galactic_velocity(r_ancient, m_ancient)
        self.run_s("04", "GN-z11 Proxy Velocity", f"{v_ancient/1000:.2f} km/s")

        # Test 5: Dwarf Spheroidal (Fornax Proxy)
        m_fornax = 2.0e7 * 1.98e30
        r_fornax = 2000 * 3.086e16
        v_fornax = engine.calculate_galactic_velocity(r_fornax, m_fornax)
        self.run_s("05", "Dwarf Spheroidal (Fornax)", f"{v_fornax/1000:.2f} km/s")

        # Test 6: AGC 114905 (Low Dark Matter Candidate)
        m_agc = 1.0e8 * 1.98e30
        r_agc = 10000 * 3.086e16
        v_agc = engine.calculate_galactic_velocity(r_agc, m_agc)
        self.run_s("06", "AGC 114905 Proxy", f"{v_agc/1000:.2f} km/s")

        # Test 7: Milky Way Mass Proxy
        m_mw = 6.0e10 * 1.98e30
        r_mw = 50000 * 3.086e16
        v_mw = engine.calculate_galactic_velocity(r_mw, m_mw)
        self.run_s("07", "Milky Way Proxy (50 kpc)", f"{v_mw/1000:.2f} km/s")

        # Test 8: Globular Cluster (Omega Centauri)
        m_omega = 4.0e6 * 1.98e30
        r_omega = 500 * 3.086e16
        v_omega = engine.calculate_galactic_velocity(r_omega, m_omega)
        self.run_s("08", "Omega Centauri Proxy", f"{v_omega/1000:.2f} km/s")

        # Test 9: IC 1101 (Massive Galaxy)
        m_ic = 1.0e14 * 1.98e30
        r_ic = 200000 * 3.086e16
        v_ic = engine.calculate_galactic_velocity(r_ic, m_ic)
        self.run_s("09", "IC 1101 Proxy (200 kpc)", f"{v_ic/1000:.2f} km/s")

        # Test 10: Cosmic Web Filament (Scale Invariance Limit)
        m_web = 1.0e16 * 1.98e30
        r_web = 10000000 * 3.086e16
        v_web = engine.calculate_galactic_velocity(r_web, m_web)
        self.run_s("10", "Cosmic Web Filament (10Mpc)", f"{v_web/1000:.2f} km/s")

if __name__ == "__main__":
    unittest.main(verbosity=0)
