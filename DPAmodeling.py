import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------
# Physical Constants
# ------------------------------------

eV = 1.602176634e-19  # Joules/eV
amu = 1.66053906660e-27  # kg/amu
N_a = 6.02214076e23  # Avogadro's number

# ------------------------------------
# Neutron Parameters
# ------------------------------------

neutron_energy_eV = 14.1e6  # D-T fusion neutron energy

total_time = 86400  # seconds
dt = 1
time_steps = int(total_time / dt)

# Flux varies During Exposure
min_neutron_flux = 1e14 # neutrons/cm^2/s
max_neutron_flux = 2e14 # neutrons/cm^2/s

neutron_flux_cm = np.linspace(min_neutron_flux, max_neutron_flux, time_steps)  # neutrons/cm^2/s in increasing linearly from 1e14 to 2e14
neutron_flux = neutron_flux_cm * 1e4  # convert to neutrons/m^2/s

# ------------------------------------
# Tungsten Properties
# ------------------------------------

A_W = 0.18384  # kg/mol
m_W = A_W / N_a  # kg/atom
m_n = 1.008665 * amu  # neutron mass

rho_W = 19250  # kg/m^3
displacement_energy_W_eV = 90

# ------------------------------------
# Beryllium Properties
# ------------------------------------

A_Be = 0.009012182  # kg/mol
m_Be = A_Be / N_a    # kg/atom

rho_Be = 1850 # kg/m^3
displacement_energy_Be_eV = 25

# ------------------------------------
# Sample Geometry
# ------------------------------------

W_thickness = 0.001
W_area = 1e-4  # 1 cm^2

Be_thickness = 0.001
Be_area = 1e-4

# ------------------------------------
# Atoms in Samples
# ------------------------------------

W_atoms_total = (rho_W * W_thickness * W_area) / m_W
Be_atoms_total = (rho_Be * Be_thickness * Be_area) / m_Be

# ------------------------------------
# Energy Transfer (Elastic Scattering) 
# Derived from Conservation of Momentum and Energy
# ------------------------------------

T_W = (4 * m_n * m_W / (m_n + m_W)**2) * neutron_energy_eV # Maximum energy transferred to W atom
T_Be = (4 * m_n * m_Be / (m_n + m_Be)**2) * neutron_energy_eV # Maximum energy transferred to Be atom

# Norgett-Robinson-Torrens (NRT) displacement model estimate
disp_per_neutron_W = 0.8 * T_W / (2 * displacement_energy_W_eV)
disp_per_neutron_Be = 0.8 * T_Be / (2 * displacement_energy_Be_eV)

# ------------------------------------
# Storage Arrays
# ------------------------------------

time = np.arange(0, total_time, dt)
dpa_history = np.zeros((time_steps, 2))

total_displacements_W = 0
total_displacements_Be = 0

# ------------------------------------
# Monte Carlo Simulation
# ------------------------------------

for step in range(time_steps):

    flux = neutron_flux[step]

    neutrons_W = flux * W_area * dt
    neutrons_Be = flux * Be_area * dt

    displacements_W = neutrons_W * disp_per_neutron_W
    displacements_Be = neutrons_Be * disp_per_neutron_Be

    total_displacements_W += displacements_W
    total_displacements_Be += displacements_Be

    dpa_history[step,0] = total_displacements_W / W_atoms_total
    dpa_history[step,1] = total_displacements_Be / Be_atoms_total

# ------------------------------------
# Plot Results
# ------------------------------------

plt.figure()

plt.plot(time/60, dpa_history[:,0], label="Tungsten")
plt.plot(time/60, dpa_history[:,1], label="Beryllium")

plt.xlabel("Time (minutes)")
plt.ylabel("Displacements Per Atom (DPA)")
plt.title("Radiation Damage from 14.1 MeV Fusion Neutrons")

plt.legend()
plt.grid()

plt.show()