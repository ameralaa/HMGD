# Holographic Modified Galactic Dynamics (HMGD)

**A geometric, parameter-free derivation of the Tully-Fisher relation and flat galactic rotation curves from the Informational Horizon ($r_0$).**

## The Missing Mass Problem Solved
For decades, the discrepancy between the visible mass of galaxies and their flat rotation curves has been attributed to the existence of Cold Dark Matter (CDM). While Modified Newtonian Dynamics (MOND) empirically fits this data using an arbitrary acceleration constant ($a_0$), it lacks a fundamental physical derivation.

**HMGD bridges this gap.** By treating spacetime as a substrate bounded by informational capacity (via the Bekenstein bound), we introduce a dynamic Informational Horizon that modifies the Schwarzschild metric.

## The Mathematical Framework
The HMGD engine derives gravity as an emergent entropic force constrained by the Hubble radius ($L_h$). The informational resolution of a galactic halo is governed by a fundamental acceleration constant derived purely from cosmological bounds (incorporating the $2\pi$ spherical geometry):

$$ a_0 = \frac{c^2}{2\pi L_h} $$

This yields a Logarithmic Informational Potential that modifies the Newtonian orbital velocity:

$$ v = \sqrt{ \frac{GM}{r} + \sqrt{GM a_0} } $$

### Key Theoretical Achievements:
1. **100% Flat Rotation Curves:** At infinite distances ($r \to \infty$), the Newtonian term vanishes, and the velocity permanently stabilizes at $v = (GM a_0)^{1/4}$.
2. **Exact Tully-Fisher Slope:** Squaring the asymptotic velocity yields exactly $V^4 = GM a_0$, proving a perfect $M \propto V^4$ relation without free parameters.
3. **No Dark Matter Required:** The framework accurately calculates galactic orbital velocities using *exclusively Baryonic Mass*.

## Repository Structure

*   `docs/full_paper.md`: The complete, unified theoretical manuscript covering galactic dynamics, relativistic lensing, and cosmology.
*   `docs/HMGD_Technical_Appendix.md`: High-level summary of mathematical equations and data results.
*   `paper_code/`: The official research codebase.
    *   `hmgd_core.py`: The central mathematical engine.
    *   `boltzmann_audit.py`: CAMB-based relativistic Boltzmann analysis.
    *   `anomalous_galaxies.py`: Modeling of AGC 114905 with background suppression.
    *   `plot_rotation_curves.py`: Generates the rotation curve evolution plots.
    *   `plot_tully_fisher.py`: Generates the Tully-Fisher and scale invariance plots.
    *   `unity_stress_test.py`: Validates HMGD across 120 orders of magnitude (Planck to Hubble).
*   `theory_visuals/`: Directory containing generated scientific plots (Figures 1–5).
*   `legacy/`: Archive of initial research and validation scripts.

## Running the Reproducibility Suite

To regenerate all figures and validation results:

```bash
# Generate visual artifacts
python paper_code/plot_rotation_curves.py
python paper_code/plot_tully_fisher.py
python paper_code/boltzmann_audit.py
python paper_code/unity_stress_test.py

# Run anomalous galaxy modeling
python paper_code/anomalous_galaxies.py
```

## Author
**Amer Alaa Eldin Attia**  
*Independent Researcher*  
ameralaah99@gmail.com
