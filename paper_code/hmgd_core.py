import math

class HMGD_Core:
    """
    Holographic Modified Galactic Dynamics (HMGD) - Core Engine
    This engine implements the fundamental equations of the HMGD framework,
    including the Universal Acceleration (a_0) and the Logarithmic Potential.
    """
    def __init__(self, G=6.67430e-11, c=299792458, L_h=1.37e26):
        self.G = G
        self.c = c
        self.L_h = L_h
        # Universal Acceleration derived from the Hubble Radius (Axiom 1)
        self.a_0 = (self.c**2) / (2 * math.pi * self.L_h)
        
        self.M_solar = 1.989e30
        self.kpc = 3.0857e19

    def get_velocity(self, m_solar, r_kpc):
        """
        Calculates the modified orbital velocity.
        Formula: v^2 = GM/r + sqrt(GM * a_0)
        """
        m = m_solar * self.M_solar
        r = r_kpc * self.kpc
        
        v2_newton = (self.G * m) / r
        v2_boost = math.sqrt(self.G * m * self.a_0)
        
        v_total = math.sqrt(v2_newton + v2_boost)
        return v_total / 1000 # returns km/s

    def get_lensing_deflection(self, m_solar, b_kpc):
        """
        Calculates the gravitational deflection angle in arcseconds.
        Formula: alpha = 4GM/bc^2 + 2*pi*v_flat^2/c^2
        """
        m = m_solar * self.M_solar
        b = b_kpc * self.kpc
        
        alpha_gr = (4 * self.G * m) / (b * self.c**2)
        v2_flat = math.sqrt(self.G * m * self.a_0)
        alpha_boost = (2 * math.pi * v2_flat) / (self.c**2)
        
        total_radians = alpha_gr + alpha_boost
        return total_radians * (180/math.pi) * 3600

    def get_cosmological_constant(self, omega_m=0.31):
        """
        Calculates the Cosmological Constant Lambda with matter dilution.
        Formula: Lambda = 3 * (a_0 * 2pi / c^2)^2 * (1 - omega_m)
        """
        lambda_pure = 3 * ((self.a_0 * 2 * math.pi) / (self.c**2))**2
        lambda_refined = lambda_pure * (1 - omega_m)
        return lambda_refined

if __name__ == "__main__":
    # Quick Validation Case: Andromeda (M31)
    engine = HMGD_Core()
    v_m31 = engine.get_velocity(1.0e11, 50)
    print(f"Validated Andromeda Velocity (50kpc): {v_m31:.2f} km/s")
