#!/usr/bin/env python3
"""
Recoil Shift Calculator

This script calculates the recoil shift in absorption spectroscopy for a given
molecular mass and transition frequency.

Author: Hubert Jozwiak
Date: 18/09/2024
"""

from scipy.constants import physical_constants, c, h

def recoil_shift(mass_u, frequency):
    """
    Calculate the recoil shift in Hz for a given molecular mass and transition frequency.

    Parameters:
    mass_u (float): Molecular mass in atomic mass units (u)
    frequency (float): Transition frequency in Hz

    Returns:
    float: Recoil shift in Hz
    """
    # Constants
    atomic_mass_constant = physical_constants['atomic mass constant'][0]  # in kg

    # Convert molecular mass to kilograms
    mass_kg = mass_u * atomic_mass_constant

    # Calculate recoil shift
    delta_nu = (h * frequency**2) / (2 * mass_kg * c**2)

    return delta_nu

# Example usage for R(1) 2-0 transition in HD
# see Castrillo et al. Physical Review A 103, 069902(E) (2021)
# doi: 10.1103/PhysRevA.103.069902
if __name__ == "__main__":
    transition_label = "R(1) 2-0"
    molecule = "HD"
    print(f"Example usage of the program for the {transition_label} transition in {molecule}")
    # Mass of HD molecule in atomic mass units
    mass_u = 3.02204
    print(f"Molecular mass: {mass_u} a.m.u.")
    # Transition frequency in Hz
    frequency = 2.17105181e14
    print(f"Transition frequency: {frequency:.6e} Hz")
    shift = recoil_shift(mass_u, frequency)
    print(f"The recoil shift for the R(1) 2-0 transition in HD is {shift:.6e} Hz")
