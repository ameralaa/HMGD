# HMGD: Unified Mathematical Framework

This document formalizes the mathematical steps of the **Holographic Modified Galactic Dynamics (HMGD)** theory. This framework serves as a universal calculator for emergent gravity across all scales, from galactic rotation to cosmic expansion.

---

## 1. Fundamental Constants and Axioms

The HMGD framework is parameter-free, relying exclusively on fundamental geometric and physical constants:
- **Speed of Light ($c$):** $299,792,458$ m/s
- **Gravitational Constant ($G$):** $6.6743 \times 10^{-11}$ m³ kg⁻¹ s⁻²
- **Hubble Radius ($L_h$):** $\approx 1.37 \times 10^{26}$ m

### Axiom 1: The Informational Acceleration ($a_0$)
Gravity is an entropic force bounded by the holographic surface area of the Hubble sphere. The minimum acceleration resolution of the universe is:
$$ a_0 = \frac{c^2}{2\pi L_h} \approx 1.04 \times 10^{-10} \text{ m/s}^2 $$

---

## 2. The Spacetime Metric

The static, spherically symmetric spacetime metric for a mass $M$ is modified by the **Logarithmic Informational Potential ($\Phi_H$)**:

$$ ds^2 = -\left(1 - \frac{r_s}{r} - \Phi_H(r)\right)c^2 dt^2 + \left(1 - \frac{r_s}{r} - \Phi_H(r)\right)^{-1} dr^2 + r^2 d\Omega^2 $$

Where $r_s = \frac{2GM}{c^2}$ is the Schwarzschild radius and:
$$ \Phi_H(r) = \sqrt{\frac{r_s}{\pi L_h}} \ln(r) $$

---

## 3. Kinematics and Galactic Dynamics

### 3.1 Modified Orbital Velocity
For a test particle in a circular orbit at radius $r$, the velocity $v$ is derived from the geodesic equation:
$$ v^2 = \frac{GM}{r} + \sqrt{GM a_0} $$

### 3.2 The Tully-Fisher Limit
As $r \to \infty$, the Newtonian term $\frac{GM}{r} \to 0$, yielding the perfectly flat rotation curve and the exact Tully-Fisher relation:
$$ v^4 = GM a_0 \implies M \propto v^4 $$

---

## 4. Relativistic Phenomena

### 4.1 Gravitational Lensing (Deflection Angle)
The total deflection angle $\alpha$ for a photon with impact parameter $b$ accounts for both the Newtonian mass and the holographic boost:
$$ \alpha = \frac{4GM}{bc^2} + \frac{2\pi \sqrt{G M a_0}}{c^2} $$

---

## 5. Global Cosmology

### 5.1 The Cosmological Constant ($\Lambda$)
The vacuum energy emerges from the vacuum pressure of the holographic expansion, diluted by the matter density $\Omega_m$:
$$ \Lambda = 3 \left( \frac{a_0 \cdot 2\pi}{c^2} \right)^2 \cdot (1 - \Omega_m) $$

### 5.2 The 0.64% Refinement
When $\Omega_m = 0.31$, this formula predicts $\Lambda \approx 1.103 \times 10^{-52} \text{ m}^{-2}$, matching the Planck Satellite measurement to within **0.64% error**.

---

## 6. Usage Guide
To calculate any property, first determine the baryonic mass $M$ of the system and the scale $r$. 
1. **Galactic Scale:** Use $v^2$ to find rotation curves.
2. **Cluster Scale:** Use $\alpha$ to find lensing mass.
3. **Cosmic Scale:** Use $\Lambda$ to find expansion rate.
