# Holographic Modified Galactic Dynamics (HMGD) - Reproducibility Suite

This repository contains the complete computational verification suite for the HMGD framework, as presented in the manuscript and its three technical appendices.

## Repository Structure

### 1. `docs/`
Contains the peer-review-ready manuscripts:
- `Holographic Modified Galactic Dynamics (HMGD).md`: Main Research Paper.
- `HMGD_Technical_Appendix.md`: Appendix A (Relativistic Implementation).
- `derivation_of_constants.md`: Appendix B (First-Principles Constants).
- `paper_2/The_Microscopic_Topologies_of_HMGD.md`: Appendix C (Microscopic Topology).
- `HMGD_Thermodynamics_Appendix.md`: Appendix D (Informational Thermodynamics).
- `HMGD_Master_Equation_Appendix.md`: Appendix E (The Master Equation).

### 2. `paper_code/` (Phenomenology & Macroscopic Proofs)
- `hmgd_core.py`: The central mathematical engine.
- `plot_tully_fisher.py`: Derivation of the Baryonic Tully-Fisher Relation.
- `plot_rar.py`: The Universal Radial Acceleration Relation (RAR).
- `bullet_cluster_momentum_sim.py`: 2D numerical proof of Entropic Momentum decoupling.
- `hmgd_mg_camb_proxy.py`: 3D Boltzmann integration for CMB verification.
- `mg_camb_hmgd_module.py`: Formal integration module for Cobaya/MG-CAMB MCMC fitting.
- `jwst_early_galaxies.py`: High-redshift scaling of a0(z).
- `wide_binaries_audit.py`: GAIA wide-binary anomaly validation.

### 3. `paper_code_2/` (Quantum & Microscopic Foundations)
- `lattice_topology_simulator.py`: Regge Calculus and the derivation of alpha (~1/137).
- `gauge_group_emergence.py`: Proof of SU(3) and SU(2) symmetry from simplicial operations.
- `dirac_spinor_emergence.py`: Derivation of the Dirac Equation from a discrete quantum walk.
- `entanglement_entropy_simulator.py`: Ryu-Takayanagi Area Law and ER=EPR graph proofs.

## Getting Started

### Prerequisites
- Python 3.8+
- Required Libraries: `numpy`, `matplotlib`, `networkx`, `scipy`

### Execution
To verify all major claims of the theory sequentially, run the master validation script:
```bash
python run_all_proofs.py
```

## Abstract
HMGD provides a zero-parameter geometric solution to the dark sector. By identifying the Hubble Radius ($L_h$) as the physical holographic screen of the universe, we derive a universal acceleration $a_0 = c^2/(2\pi L_h)$ that recovers galactic dynamics and cosmic expansion without Dark Matter or Dark Energy. The framework is unified from the quantum scale (Standard Model gauge groups) to the cosmic scale (CMB and lensing).
