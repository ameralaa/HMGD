import math

class HMGD_Refinement_Lab:
    def __init__(self):
        self.G = 6.67430e-11
        self.c = 299792458
        self.L_h = 1.37e26 # Hubble Radius (m)
        self.a_0 = (self.c**2) / (2 * math.pi * self.L_h)
        self.solar_mass = 1.989e30
        self.kpc = 3.0857e19

    def point_2_lambda_refinement(self, omega_m=0.31):
        """
        Refines the Lambda derivation by including matter density dilution.
        """
        # Theoretical pure-vacuum Lambda
        lambda_pure = 3 * ((self.a_0 * 2 * math.pi) / (self.c**2))**2
        
        # Refined Lambda accounting for matter density
        # Hypothesis: Lambda_observed = Lambda_pure * (1 - Omega_m)
        lambda_refined = lambda_pure * (1 - omega_m)
        
        lambda_planck = 1.11e-52
        
        error = abs(lambda_refined - lambda_planck) / lambda_planck * 100
        
        return lambda_pure, lambda_refined, lambda_planck, error

    def point_3_agc114905_simulation(self):
        """
        Simulates AGC 114905, an anomalous ultra-diffuse galaxy.
        Baryonic Mass: 1.3e8 Solar Masses
        Radius: ~7 kpc
        Observed Velocity: ~23 km/s (at large radii)
        """
        m_bar = 1.3e8 * self.solar_mass
        r_obs = 7 * self.kpc
        v_obs_target = 23000 # 23 km/s
        
        # Schwarzschild Radius
        r_s = (2 * self.G * m_bar) / (self.c**2)
        # Informational Horizon
        r_0 = math.sqrt(r_s * self.L_h)
        
        # Newtonian Prediction
        v_newton = math.sqrt((self.G * m_bar) / r_obs)
        
        # HMGD Prediction
        v_hmgd = v_newton * math.sqrt(1.0 + (r_obs / r_0))
        
        return v_newton, v_hmgd, v_obs_target, r_0 / self.kpc

if __name__ == "__main__":
    lab = HMGD_Refinement_Lab()
    
    print("--- Point 2: Lambda Refinement ---")
    pure, refined, planck, err = lab.point_2_lambda_refinement()
    print(f"Pure HMGD Lambda: {pure:.3e}")
    print(f"Refined (with Omega_m=0.31): {refined:.3e}")
    print(f"Planck Measured Lambda: {planck:.3e}")
    print(f"Residual Error: {err:.2f}%")
    
    print("\n--- Point 3: AGC 114905 Anomalous Galaxy ---")
    vn, vh, vt, r0_kpc = lab.point_3_agc114905_simulation()
    print(f"Newtonian Velocity: {vn/1000:.2f} km/s")
    print(f"HMGD Velocity: {vh/1000:.2f} km/s")
    print(f"Observed Target: {vt/1000:.2f} km/s")
    print(f"HMGD Horizon (r_0): {r0_kpc:.4f} kpc")
    
    # Analysis of AGC 114905
    if vh > vt * 1.5:
        print("\nWARNING: HMGD significantly over-predicts AGC 114905.")
        print("Hypothesis: The informational horizon r_0 might need scaling with global background.")
