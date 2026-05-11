import math

class HMGD_Galaxy_Audit:
    """
    Validation engine for anomalous galaxies (Ultra-Diffuse, Ancient, etc.)
    Specifically addresses the AGC 114905 "too little dark matter" challenge.
    """
    def __init__(self, G=6.67430e-11, c=299792458):
        self.G = G 
        self.c = c 
        self.L_h = 1.37e26 
        self.a_0 = (self.c**2) / (2 * math.pi * self.L_h)

    def calculate_rs(self, m_solar):
        m = m_solar * 1.989e30
        return (2 * self.G * m) / (self.c**2)

    def hmgd_velocity(self, r_kpc, m_solar, use_efe=False):
        """
        Calculates orbital velocity. 
        If use_efe is True, the boost is suppressed by a global field (approximate).
        """
        r = r_kpc * 3.0857e19
        m = m_solar * 1.989e30
        r_s = self.calculate_rs(m_solar)
        r_0 = math.sqrt(r_s * self.L_h)
        
        v_n = math.sqrt((self.G * m) / r)
        
        if use_efe:
            # External Field Effect Simulation: 
            # In high-field or low-gradient regimes, the boost is dampened.
            # Here we simulate a 'Cosmological Friction' for diffuse systems.
            efe_factor = 0.25 # Hypothetical suppression factor for ultra-diffuse systems
            boost = math.sqrt(1.0 + (r / r_0) * efe_factor)
        else:
            boost = math.sqrt(1.0 + (r / r_0))
            
        return v_n * boost

def run_audit():
    audit = HMGD_Galaxy_Audit()
    
    # CASE: AGC 114905
    # Mass: 1.3e8 M_solar, Radius: 7 kpc, Observed: 23 km/s
    m_agc = 1.3e8
    r_agc = 7.0
    v_obs = 23.0
    
    v_std = audit.hmgd_velocity(r_agc, m_agc, use_efe=False) / 1000
    v_efe = audit.hmgd_velocity(r_agc, m_agc, use_efe=True) / 1000
    
    print("="*70)
    print("HMGD GALAXY AUDIT: THE AGC 114905 CHALLENGE")
    print("="*70)
    print(f"Target Observed Velocity : {v_obs} km/s")
    print(f"HMGD Standard Prediction : {v_std:.2f} km/s (Error: {abs(v_std-v_obs)/v_obs*100:.1f}%)")
    print(f"HMGD EFE-Suppressed      : {v_efe:.2f} km/s (Error: {abs(v_efe-v_obs)/v_obs*100:.1f}%)")
    print("-" * 70)
    print("ANALYSIS: Standard HMGD over-predicts low-mass diffuse galaxies.")
    print("By introducing a 'Cosmological Friction' or External Field Effect (EFE),")
    print("HMGD can recover the near-Newtonian behavior of AGC 114905.")
    print("="*70)

if __name__ == "__main__":
    run_audit()
