import math

class HMGD_Math_Framework:
    """
    The Universal HMGD Calculator.
    Implements all steps of the math_framework.md to test across different cases.
    """
    def __init__(self, G=6.67430e-11, c=299792458, L_h=1.37e26):
        self.G = G
        self.c = c
        self.L_h = L_h
        # Fundamental Acceleration Constant (Axiom 1)
        self.a_0 = (self.c**2) / (2 * math.pi * self.L_h)
        
        self.solar_mass = 1.989e30
        self.kpc = 3.0857e19

    def calculate_rs(self, m_solar):
        """Schwarzschild Radius"""
        return (2 * self.G * m_solar * self.solar_mass) / (self.c**2)

    def galactic_rotation(self, m_solar, r_kpc):
        """Calculates Newtonian vs HMGD velocity (km/s)"""
        r = r_kpc * self.kpc
        m = m_solar * self.solar_mass
        
        v_n = math.sqrt((self.G * m) / r)
        # HMGD Formula: v^2 = GM/r + sqrt(GM * a0)
        v_hmgd = math.sqrt((v_n**2) + math.sqrt(self.G * m * self.a_0))
        
        return v_n / 1000, v_hmgd / 1000

    def lensing_deflection(self, m_solar, impact_kpc):
        """Calculates GR vs HMGD deflection (arcseconds)"""
        m = m_solar * self.solar_mass
        b = impact_kpc * self.kpc
        
        alpha_gr = (4 * self.G * m) / (b * self.c**2)
        v2_flat = math.sqrt(self.G * m * self.a_0)
        alpha_hmgd = alpha_gr + (2 * math.pi * v2_flat) / (self.c**2)
        
        # Convert radians to arcseconds
        to_arcsec = (180/math.pi) * 3600
        return alpha_gr * to_arcsec, alpha_hmgd * to_arcsec

    def cosmological_constant(self, omega_m=0.31):
        """Calculates theoretical Lambda based on matter dilution"""
        lambda_pure = 3 * ((self.a_0 * 2 * math.pi) / (self.c**2))**2
        lambda_obs = lambda_pure * (1 - omega_m)
        return lambda_pure, lambda_obs

def run_comprehensive_tests():
    calc = HMGD_Math_Framework()
    
    print("="*75)
    print("HMGD UNIFIED MATHEMATICAL FRAMEWORK: CASE STUDY SUITE")
    print("="*75)
    
    # 1. SPIRAL GALAXY: Andromeda (M31)
    # Mass: 1.0e11 Solar, Radius: 50 kpc
    vn, vh = calc.galactic_rotation(1.0e11, 50)
    print(f"[CASE: M31 SPIRAL]  R=50kpc | Newton: {vn:6.2f} km/s | HMGD: {vh:6.2f} km/s")
    
    # 2. DWARF SPHEROIDAL: Fornax
    # Mass: 2.0e7 Solar, Radius: 1 kpc
    vn, vh = calc.galactic_rotation(2.0e7, 1)
    print(f"[CASE: FORNAX DWARF] R=1kpc  | Newton: {vn:6.2f} km/s | HMGD: {vh:6.2f} km/s")

    # 3. ULTRA-DIFFUSE: AGC 114905 (No dark matter effect)
    # Mass: 1.3e8 Solar, Radius: 7 kpc
    # Note: Standard HMGD over-predicts, needs EFE suppression
    vn, vh = calc.galactic_rotation(1.3e8, 7)
    print(f"[CASE: AGC 114905]   R=7kpc  | Newton: {vn:6.2f} km/s | HMGD: {vh:6.2f} km/s (Raw)")

    print("-" * 75)
    
    # 4. GRAVITATIONAL LENSING: Massive Halo
    # Mass: 1.0e12 Solar, Impact: 20 kpc
    agr, ahmgd = calc.lensing_deflection(1.0e12, 20)
    print(f"[CASE: LENSING]      M=1e12  | GR:     {agr:6.4f}\" | HMGD: {ahmgd:6.4f}\"")
    
    print("-" * 75)
    
    # 5. COSMOLOGY: Dark Energy
    lp, lo = calc.cosmological_constant(0.31)
    planck = 1.11e-52
    err = abs(lo - planck) / planck * 100
    print(f"[CASE: COSMOLOGY]    Theoretical Lambda: {lo:.3e} m^-2 (Error vs Planck: {err:.2f}%)")
    
    print("="*75)

if __name__ == "__main__":
    run_comprehensive_tests()
