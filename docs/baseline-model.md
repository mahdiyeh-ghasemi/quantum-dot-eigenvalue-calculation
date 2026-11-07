# Baseline Quantum-Dot Model: Physical Definition

## 1. Objective

This note defines a baseline physical model for a one-dimensional two-electron quantum dot. The published paper does not specify all parameters and numerical details needed to reproduce its calculations unambiguously. We therefore define here a self-contained model whose every ingredient is stated explicitly, so that it can be implemented and validated step by step.

The baseline model is defined and validated first. Spin-dependent interactions and the exponential interaction of the paper are treated as later extensions (Sec. 7). The model is not claimed to reproduce Fig. 2 of the paper.

The notation follows `equation-analysis.md`, with two exceptions that avoid clashes: the dimensionless interaction strength is called $`\gamma`$ (not $`\lambda`$) and the dimensionless softening length is called $`\eta`$ (not $`\delta`$, which denotes the Kronecker delta).

## 2. Physical system

Two identical electrons are confined in a one-dimensional infinite potential well. The spatial domain is

```math
0<x_1<L,\qquad 0<x_2<L
```

and the confinement potential is

```math
V_{\mathrm{conf}}(x)=0\ \text{ for } 0<x<L,\qquad V_{\mathrm{conf}}(x)=\infty\ \text{ otherwise}
```

The model parameters are:

- $`L`$: confinement length,
- $`m^{\ast}`$: effective electron mass,
- $`\varepsilon_r`$: relative dielectric constant,
- $`d`$: effective transverse length scale that regularizes the interaction.

These parameters must be specified before any numerical calculation.

## 3. Baseline Hamiltonian

The Hamiltonian is

```math
H=H_0+V_{\mathrm{ee}}
```

with the non-interacting part

```math
H_0=-\frac{\hbar^2}{2m^{\ast}}\left(\frac{\partial^2}{\partial x_1^2}+\frac{\partial^2}{\partial x_2^2}\right)
```

The electron-electron interaction is a softened Coulomb potential:

```math
V_{\mathrm{ee}}(x_1,x_2)=\frac{e^2}{4\pi\varepsilon_0\varepsilon_r\sqrt{(x_1-x_2)^2+d^2}}
```

The positive sign describes the repulsion between two electrons. The parameter $`d>0`$ prevents the divergence at $`x_1=x_2`$ and represents an effective transverse length scale in this reduced one-dimensional model. This is an effective quasi-one-dimensional interaction, not an exact one-dimensional Coulomb potential.

**Units.** This note uses SI units. In the Gaussian units of `equation-analysis.md`, the replacement is $`e^2/(4\pi\varepsilon_0)\to e^2`$.

## 4. Single-particle basis

The normalized eigenfunctions of the infinite well are

```math
\phi_n(x)=\sqrt{\frac{2}{L}}\,\sin\left(\frac{n\pi x}{L}\right),\qquad n=1,2,3,\dots
```

with energies

```math
E_n=\frac{n^2\pi^2\hbar^2}{2m^{\ast}L^2}
```

and orthonormality

```math
\int_0^L\phi_n(x)\,\phi_m(x)\,dx=\delta_{nm}
```

## 5. Two-electron spatial basis

The unsymmetrized product states are

```math
\Phi_{nm}(x_1,x_2)=\phi_n(x_1)\,\phi_m(x_2)
```

Because the electrons are identical fermions, the total wavefunction must be antisymmetric under exchange. The Hamiltonian of Sec. 3 does not act on spin, so the spin and spatial parts separate, and the two sectors are treated independently.

For a spin-singlet state the spatial part is symmetric:

```math
\Phi_{nm}^{(+)}=\frac{\phi_n(x_1)\,\phi_m(x_2)+\phi_m(x_1)\,\phi_n(x_2)}{\sqrt{2\,(1+\delta_{nm})}}
```

For a spin-triplet state the spatial part is antisymmetric:

```math
\Phi_{nm}^{(-)}=\frac{\phi_n(x_1)\,\phi_m(x_2)-\phi_m(x_1)\,\phi_n(x_2)}{\sqrt{2}},\qquad n\neq m
```

For $`n=m`$ the triplet state vanishes (Pauli principle). The total wavefunction is the product of the spatial and spin parts with the required exchange symmetry.

## 6. Dimensionless formulation

Define

```math
\xi_i=\frac{x_i}{L},\qquad \eta=\frac{d}{L},\qquad E_0=\frac{\hbar^2\pi^2}{2m^{\ast}L^2}
```

The Hamiltonian in units of $`E_0`$ becomes

```math
\frac{H}{E_0}=-\frac{1}{\pi^2}\left(\frac{\partial^2}{\partial\xi_1^2}+\frac{\partial^2}{\partial\xi_2^2}\right)+\frac{2\gamma}{\pi^2}\,\frac{1}{\sqrt{(\xi_1-\xi_2)^2+\eta^2}}
```

where the effective Bohr radius and the interaction strength are

```math
a_B^{\ast}=\frac{4\pi\varepsilon_0\varepsilon_r\hbar^2}{m^{\ast}e^2},\qquad \gamma=\frac{L}{a_B^{\ast}}
```

The dimensionless model is therefore controlled by the two parameters $`\gamma`$ and $`\eta`$. In these units the single-particle energies are simply $`E_n/E_0=n^2`$.

## 7. Scope and exclusions

The baseline model includes one-dimensional confinement, two identical electrons, the kinetic energy, the repulsive softened Coulomb interaction, fermionic exchange symmetry, and the singlet and triplet spatial sectors.

The following contributions are deliberately excluded from the baseline and may be added as extensions once the baseline is validated:

- an external magnetic field and the Zeeman interaction,
- the spin-orbit interaction,
- the exponential interaction potential of the paper (in the convention fixed in `equation-analysis.md`).

## 8. Computational strategy

We expand the two-electron states in a finite basis of the functions of Sec. 5, construct the Hamiltonian matrix, and diagonalize it numerically. Singlet and triplet sectors are computed separately, and convergence is tested by increasing the number of single-particle functions.

The non-interacting part is diagonal in the product basis, with entries $`n^2+m^2`$ in units of $`E_0`$. For the interaction, define the direct integral

```math
J_{ab,cd}=\frac{2\gamma}{\pi^2}\cdot 4\int_0^1\!\!\int_0^1\frac{\sin(a\pi\xi_1)\sin(b\pi\xi_1)\,\sin(c\pi\xi_2)\sin(d\pi\xi_2)}{\sqrt{(\xi_1-\xi_2)^2+\eta^2}}\,d\xi_1\,d\xi_2
```

Since the interaction is symmetric under $`x_1\leftrightarrow x_2`$, the matrix element in the symmetric (upper sign) or antisymmetric (lower sign) sector is

```math
\frac{\langle\Phi_{nm}^{(\pm)}|V_{\mathrm{ee}}|\Phi_{kl}^{(\pm)}\rangle}{E_0}=\frac{2}{N_{nm}N_{kl}}\left(J_{nk,ml}\pm J_{nl,mk}\right)
```

where $`N_{nm}`$ is the normalization denominator of Sec. 5. The resulting matrix is real and symmetric, so it is Hermitian. The integrals are smooth for $`\eta>0`$ and can be evaluated by Gauss-Legendre quadrature.

## 9. Scientific status

This is an explicitly defined quasi-one-dimensional model. It is not claimed to coincide with the numerical model behind the figures of the paper, whose parameters are not fully specified there. All assumptions, parameters, approximations, and numerical results will be documented separately from the equations transcribed from the publication.
