# Independent Quantum-Dot Model: Physical Definition

## 1. Objective

This document defines the baseline physical model for an independent computational reconstruction of a one-dimensional two-electron quantum-dot system.

The model is developed independently because the published article does not provide sufficient information to reproduce all its numerical calculations unambiguously.

The baseline model will be mathematically defined and validated before additional spin-dependent interactions are introduced.

## 2. Physical System

The system consists of two identical electrons confined in a one-dimensional infinite potential well.

The spatial domain is:

\[
0<x_1<L,\qquad 0<x_2<L.
\]

The confinement potential is:

\[
V_{\mathrm{conf}}(x)=
\begin{cases}
0,&0<x<L,\\
\infty,&\text{otherwise}.
\end{cases}
\]

The model parameters are:

- \(L\): confinement length.
- \(m^*\): effective electron mass.
- \(\varepsilon_r\): relative dielectric constant.
- \(d\): effective transverse length scale used to regularize the interaction.

These parameters must be specified before numerical calculations.

## 3. Baseline Hamiltonian

The initial Hamiltonian is:

\[
H=H_0+V_{\mathrm{ee}},
\]

where the non-interacting contribution is:

\[
H_0=
-\frac{\hbar^2}{2m^*}
\left(
\frac{\partial^2}{\partial x_1^2}
+
\frac{\partial^2}{\partial x_2^2}
\right).
\]

The electron–electron interaction is modeled using a softened Coulomb potential:

\[
V_{\mathrm{ee}}(x_1,x_2)=
\frac{e^2}
{4\pi\varepsilon_0\varepsilon_r
\sqrt{(x_1-x_2)^2+d^2}}.
\]

The positive sign represents the repulsive electrostatic interaction between two electrons.

The parameter \(d>0\) prevents the interaction from diverging when the two longitudinal coordinates coincide. It represents an effective transverse length scale in this reduced one-dimensional model.

This is an effective quasi-one-dimensional interaction model, not an exact one-dimensional Coulomb potential.

## 4. Single-Particle Basis

The normalized eigenfunctions of the infinite square well are:

\[
\phi_n(x)=
\sqrt{\frac{2}{L}}
\sin\left(\frac{n\pi x}{L}\right),
\qquad n=1,2,3,\ldots
\]

The corresponding single-particle energies are:

\[
E_n=
\frac{n^2\pi^2\hbar^2}{2m^*L^2}.
\]

These functions satisfy:

\[
\int_0^L\phi_n(x)\phi_m(x)\,dx
=\delta_{nm}.
\]

## 5. Two-Electron Spatial Basis

The unsymmetrized product states are:

\[
\Phi_{nm}(x_1,x_2)
=\phi_n(x_1)\phi_m(x_2).
\]

Since the two particles are identical electrons, the total wave function must be antisymmetric under particle exchange.

For a spin-singlet state, the spatial wave function is symmetric:

\[
\Phi_{nm}^{(+)}
=
\frac{
\phi_n(x_1)\phi_m(x_2)
+
\phi_m(x_1)\phi_n(x_2)
}{
\sqrt{2(1+\delta_{nm})}
}.
\]

For a spin-triplet state, the spatial wave function is antisymmetric:

\[
\Phi_{nm}^{(-)}
=
\frac{
\phi_n(x_1)\phi_m(x_2)
-
\phi_m(x_1)\phi_n(x_2)
}{
\sqrt{2(1-\delta_{nm})}
},
\qquad n\ne m.
\]

The total two-electron wave function is constructed by combining the spatial and spin parts with the required exchange symmetry.

## 6. Dimensionless Formulation

For numerical convenience, define:

\[
\xi_i=\frac{x_i}{L},
\qquad
\delta=\frac{d}{L},
\]

and choose the characteristic energy:

\[
E_0=\frac{\hbar^2\pi^2}{2m^*L^2}.
\]

The dimensionless Hamiltonian becomes:

\[
\frac{H}{E_0}
=
-\frac{1}{\pi^2}
\left(
\frac{\partial^2}{\partial \xi_1^2}
+
\frac{\partial^2}{\partial \xi_2^2}
\right)
+
\frac{2L}{\pi^2a_B^*}
\frac{1}{
\sqrt{(\xi_1-\xi_2)^2+\delta^2}
},
\]

where the effective Bohr radius is:

\[
a_B^*=
\frac{4\pi\varepsilon_0\varepsilon_r\hbar^2}
{m^*e^2}.
\]

The dimensionless model is therefore controlled by the two parameters:

\[
\lambda=\frac{L}{a_B^*},
\qquad
\delta=\frac{d}{L}.
\]

## 7. Baseline Scope and Exclusions

The initial implementation will include:

- One-dimensional confinement.
- Two identical electrons.
- Kinetic energy.
- Repulsive softened Coulomb interaction.
- Fermionic exchange symmetry.
- Singlet and triplet spatial sectors.

The following contributions are deliberately excluded from the baseline model:

- External magnetic field.
- Zeeman interaction.
- Spin-orbit interaction.
- The exponential interaction potential used in the published article.

These contributions may be introduced in subsequent extensions after the baseline model has been validated.

## 8. Computational Strategy

The baseline calculation will use a finite set of single-particle basis functions.

The two-electron Hamiltonian matrix will be constructed from the kinetic and interaction matrix elements.

The resulting Hermitian matrix will be diagonalized numerically to obtain the energy eigenvalues and eigenstates.

Convergence will be examined by increasing the number of basis functions.

The singlet and triplet sectors will be calculated separately.

## 9. Scientific Status

This model is an independent, explicitly defined quasi-one-dimensional reconstruction.

It is not claimed to be an exact reproduction of the original article's unspecified numerical model.

All assumptions, parameters, approximations, and numerical results will be documented separately from the equations transcribed from the publication.
