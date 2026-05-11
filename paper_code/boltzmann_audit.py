import camb
from camb import model
import numpy as np
import matplotlib.pyplot as plt
from hmgd_core import HMGD_Core
import math

def run_boltzmann_audit():
    """
    Standardized Relativistic Boltzmann Audit using CAMB.
    Compares Standard LambdaCDM vs HMGD Holographic Resonance.
    """
    engine = HMGD_Core()
    # 1. Standard LambdaCDM (Benchmark)
    pars = camb.CAMBparams()
    pars.set_cosmology(H0=67.5, ombh2=0.022, omch2=0.122)
    pars.InitPower.set_params(As=2e-9, ns=0.965)
    pars.set_for_lmax(2500)
    
    results = camb.get_results(pars)
    totCL_lcdm = results.get_cmb_power_spectra(pars, CMB_unit='muK')['total']
    ls = np.arange(totCL_lcdm.shape[0])
    
    # 2. No-CDM Universe
    pars_no = camb.CAMBparams()
    pars_no.set_cosmology(H0=67.5, ombh2=0.022, omch2=0.0001)
    pars_no.InitPower.set_params(As=2e-9, ns=0.965)
    pars_no.set_for_lmax(2500)
    
    results_no = camb.get_results(pars_no)
    totCL_no = results_no.get_cmb_power_spectra(pars_no, CMB_unit='muK')['total']
    
    # 3. HMGD HOLOGRAPHIC SCALING (Strict Axiomatic Derivation)
    # The characteristic multipole scale is determined by the 
    # informational resolution at recombination.
    # Axiom: l_scale = z_recomb (The compression factor of the causal horizon)
    l_scale = 1100.0 
    # Holographic Dimension: Mean of Surface (2) and Volume (3) scaling
    holographic_dim = 2.5
    
    hmgd_gain = 1.0 + (ls / l_scale)**holographic_dim
    totCL_hmgd = totCL_no[:,0] * hmgd_gain
    
    # Normalization to first peak
    totCL_hmgd = totCL_hmgd * (totCL_lcdm[220,0] / totCL_hmgd[220])
    
    # Output Results
    print(f"LCDM P3/P1 Ratio : {totCL_lcdm[800,0]/totCL_lcdm[220,0]:.4f}")
    print(f"HMGD P3/P1 Ratio : {totCL_hmgd[800]/totCL_hmgd[220]:.4f}")
    
    # PLOTTING
    plt.figure(figsize=(10, 6))
    plt.style.use('dark_background')
    plt.plot(ls, totCL_lcdm[:,0], color='white', label='Standard LambdaCDM', alpha=0.7)
    plt.plot(ls, totCL_no[:,0], color='red', linestyle='--', label='No Dark Matter', alpha=0.5)
    plt.plot(ls, totCL_hmgd, color='cyan', linewidth=2, label='HMGD Holographic Resonance')
    
    plt.xlim([2, 2000])
    plt.title("Relativistic Boltzmann Audit: HMGD vs Standard Model", fontsize=14, color='gold')
    plt.xlabel("Multipole Moment (l)")
    plt.ylabel("Power Amplitude")
    plt.legend()
    plt.savefig("theory_visuals/hmgd_boltzmann_audit.png")
    print("Success: Generated Boltzmann audit plot.")
    
    return ls, totCL_lcdm, totCL_hmgd

if __name__ == "__main__":
    run_boltzmann_audit()
