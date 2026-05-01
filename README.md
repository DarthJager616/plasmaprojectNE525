# ITER Pulsed Neutron Irradiation Damage Model

This Python simulation estimates radiation damage accumulation in two ITER plasma-facing materials:

- Tungsten (W) – Divertor target material
- Beryllium (Be) – First wall material

The code models Displacements Per Atom (DPA) caused by 14.1 MeV fusion neutrons during ITER-style pulsed operation using the NRT (Norgett-Robinson-Torrens) damage approximation.

--------------------------------------------------
OVERVIEW
--------------------------------------------------

Fusion neutrons can knock atoms out of their lattice sites, creating defects in reactor materials. Over time, this can lead to:

- Embrittlement
- Swelling
- Thermal conductivity degradation
- Surface erosion
- Reduced component lifetime

This script simulates how damage accumulates during repeated ITER plasma pulses.

--------------------------------------------------
FEATURES
--------------------------------------------------

- Models ITER pulse structure:
  Plasma pulse = 7.5 minutes
  Dwell time   = 23 minutes

- Uses neutron flux:
  1 × 10^14 n/cm²/s

- Calculates:
  - Maximum neutron energy transfer
  - NRT displacement damage
  - Cumulative DPA over time

- Produces publication-style plots using Matplotlib

--------------------------------------------------
PHYSICS MODEL
--------------------------------------------------

1. Pulsed Neutron Flux

Neutron flux is applied only during plasma burn time:

Φ(t) = Φ_0
Φ(t) = 0 during dwell

2. Maximum Elastic Energy Transfer

T = (4mnmt / (mn + mt)^2) En

Where:

mn = neutron mass
mt = target atom mass
En = neutron energy

3. NRT Damage Model

D = 0.8T / (2Ed)

Where:

Ed = displacement threshold energy

An empirical correction factor is then applied to account for defect recombination at high temperatures:

kappa = 0.33

4. Displacements Per Atom (DPA)

DPA = total displacements / total atoms

--------------------------------------------------
MATERIAL PROPERTIES
--------------------------------------------------

Tungsten:
Density = 19250 kg/m^3
Threshold Energy = 90 eV

Beryllium:
Density = 1850 kg/m^3
Threshold Energy = 25 eV

--------------------------------------------------
SIMULATION PARAMETERS
--------------------------------------------------

Total runtime     = 4 hours
Time step         = 1 second
Surface area      = 1 cm^2
Thickness         = 2 cm
Neutron energy    = 14.1 MeV

--------------------------------------------------
OUTPUT
--------------------------------------------------

The script generates a graph showing:

- Tungsten DPA vs Time
- Beryllium DPA vs Time

Orange shaded regions represent active plasma pulse periods.

--------------------------------------------------
EXPECTED RESULTS
--------------------------------------------------

- Damage increases during pulse windows
- Flat regions occur during dwell time
- Beryllium may accumulate damage faster due to lower threshold energy

--------------------------------------------------
REQUIREMENTS
--------------------------------------------------

pip install numpy
pip install matplotlib
Note: Make sure that python is installed on your computer

--------------------------------------------------
POSSIBLE FUTURE IMPROVEMENTS
--------------------------------------------------

- Temperature-dependent annealing
- arc-dpa damage model
- Neutron attenuation through material depth
- Helium / hydrogen transmutation effects
- Thermal stress coupling
- OpenMC or MCNP neutron transport data
- Reducing computation times

--------------------------------------------------
DISCLAIMER
--------------------------------------------------

This model is a simplified engineering estimate and should not replace validated reactor materials simulations.
This program is only for short time scales. Longer time scales will take significantly longer times to generate data.

--------------------------------------------------
AUTHOR
--------------------------------------------------

Created as a fusion materials / nuclear engineering modeling project.
