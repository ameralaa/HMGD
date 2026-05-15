import numpy as np
import matplotlib.pyplot as plt
import os

def simulate_bullet_cluster_momentum():
    print("HMGD Bullet Cluster Entropic Momentum Simulator")
    print("===============================================")
    
    # Ensure directory exists
    if not os.path.exists("theory_visuals"):
        os.makedirs("theory_visuals")
    
    # Grid Setup
    size = 100
    x = np.linspace(-5, 5, size)
    y = np.linspace(-5, 5, size)
    X, Y = np.meshgrid(x, y)
    
    # Initial Conditions: Two colliding clusters
    # Baryonic Gas (Gaussian mass distributions)
    center_1 = [-2.0, 0.0]
    center_2 = [2.0, 0.0]
    
    # Velocity vectors
    v1 = 1.0
    v2 = -1.0
    
    # Time steps
    steps = 40
    dt = 0.1
    
    # Drag coefficient for baryons (Friction during collision)
    friction = 0.5
    
    # Track Informational Field centers separately (Collisionless)
    phi_c1 = center_1.copy()
    phi_c2 = center_2.copy()
    
    for t in range(steps):
        # Update Baryon centers
        dist = np.abs(center_1[0] - center_2[0])
        f_drag = 1.0 if dist < 1.0 else 0.0
        
        v1_eff = v1 * (1.0 - f_drag * friction)
        v2_eff = v2 * (1.0 - f_drag * friction)
        
        center_1[0] += v1_eff * dt
        center_2[0] += v2_eff * dt
        
        # Update Scalar Field centers (Entropic Momentum - No Friction)
        phi_c1[0] += v1 * dt
        phi_c2[0] += v2 * dt
        
    # Final state visualization
    gas = np.exp(-((X-center_1[0])**2 + Y**2)/0.5) + np.exp(-((X-center_2[0])**2 + Y**2)/0.5)
    lensing = np.exp(-((X-phi_c1[0])**2 + Y**2)/0.8) + np.exp(-((X-phi_c2[0])**2 + Y**2)/0.8)
    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.contourf(X, Y, gas, cmap='Oranges')
    plt.title("Baryonic Gas (Friction-Damped)")
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.contourf(X, Y, lensing, cmap='Blues')
    plt.title("Lensing Potential (Entropic Momentum)")
    plt.axis('off')
    
    plt.tight_layout()
    plt.savefig("theory_visuals/bullet_cluster_momentum_sim.png")
    print(f"Success: Simulated spatial offset at t={steps*dt:.1f}")
    print(f"Baryon Center: {center_1[0]:.2f} | Lensing Center: {phi_c1[0]:.2f}")
    print(f"Numerical Offset: {np.abs(phi_c1[0] - center_1[0]):.2f} units")

if __name__ == "__main__":
    simulate_bullet_cluster_momentum()
