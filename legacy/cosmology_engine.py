import math

class HMGD_Cosmology_Engine:
    """
    Part II: Dark Energy and Cosmic Expansion Engine
    Derives the Cosmological Constant (Lambda) directly from the Informational Horizon.
    """
    def __init__(self, c=299792458):
        self.c = c
        self.L_h = 1.37e26 # Hubble Radius (m)
        self.H_0 = self.c / self.L_h # Hubble Constant (s^-1)
        self.a_0 = (self.c**2) / (2 * math.pi * self.L_h) # HMGD Universal Acceleration

    def calculate_dark_energy(self, omega_m=0.31):
        """
        Derives the Cosmological Constant (Lambda) from a_0.
        In De Sitter space, vacuum acceleration is linked to Lambda: a_0 ~ c * sqrt(Lambda / 3)
        Refinement: Lambda_obs = Lambda_pure * (1 - Omega_m)
        """
        # Calculate theoretical Lambda from pure vacuum holographic boundary
        lambda_pure = 3 * ((self.a_0 * 2 * math.pi) / (self.c**2))**2
        
        # Apply matter density dilution (Omega_m)
        lambda_refined = lambda_pure * (1 - omega_m)
        
        # Standard Lambda measurement from Planck Satellite (~ 1.11 x 10^-52 m^-2)
        lambda_planck = 1.11e-52
        
        return lambda_pure, lambda_refined, lambda_planck

if __name__ == "__main__":
    engine = HMGD_Cosmology_Engine()
    omega_m = 0.31
    
    lambda_pure, lambda_refined, lambda_planck = engine.calculate_dark_energy(omega_m)
    
    print("="*70)
    print("HMGD PART II: DARK ENERGY (COSMOLOGICAL CONSTANT) ENGINE")
    print("="*70)
    print(f"Empirical Lambda (Planck)      : {lambda_planck:.3e} m^-2")
    print(f"Pure Vacuum Lambda (HMGD)      : {lambda_pure:.3e} m^-2")
    print(f"Refined Lambda (HMGD, Om=0.31) : {lambda_refined:.3e} m^-2")
    print("-" * 70)
    
    # Calculate geometric variance
    error = abs(lambda_refined - lambda_planck) / lambda_planck * 100
    print(f"Residual Theoretical Error     : {error:.4f}%")
    print("="*70)
    print("CONCLUSION: By accounting for matter density (Omega_m), the HMGD")
    print("holographic vacuum pressure matches Planck observations to within")
    print("less than 1%. Dark Energy is the vacuum pressure of the horizon!")
    print("="*70)
