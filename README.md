# RecoilCalc

This Python script calculates the recoil shift in absorption spectroscopy for a given molecular mass and transition frequency.
It utilizes constants from the `scipy.constants` library and includes an example calculation for the R(1) 2-0 transition in HD.

## Table of Contents

- [Formula](#formula)
- [Requirements](#requirements)
- [Usage](#usage)
- [Example](#example)
- [License](#license)

## Formula

The recoil shift (\(\Delta \nu\)) is calculated using the formula:

\[
\Delta \nu = \frac{h \nu^2}{2 M c^2}
\]

Where:

- \( \Delta \nu \): Recoil shift in Hz
- \( h \): Planck's constant (\(6.62607015 \times 10^{-34}\) J·s)
- \( \nu \): Transition frequency in Hz
- \( M \): Molecular mass in kilograms
- \( c \): Speed of light in a vacuum (\(2.99792458 \times 10^8\) m/s)

## Requirements

- Python 3.x
- `scipy` library

Install the required library using:

```bash
pip install scipy
```

## Usage

Clone the repository and navigate to the directory containing the script.
```bash
git clone https://github.com/hjozwiak-umk/RecoilCalc.git
cd RecoilCalc
```

Run the script:
```bash
python recoil_shift.py
```

## Example

The script includes an example calculation for the R(1) 2-0 transition in HD:
- **Molecular Mass**: 3.02204 u
- **Transition Frequency**: \(2.17105181 \times 10^{14}\)

**Output**
```scss
Example usage of the program for the R(1) 2-0 transition in HD
Molecular mass: 3.02204 a.m.u.
Transition frequency: 2.171052e+14 Hz
The recoil shift for the R(1) 2-0 transition in HD is 3.462388e+04 Hz
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.
