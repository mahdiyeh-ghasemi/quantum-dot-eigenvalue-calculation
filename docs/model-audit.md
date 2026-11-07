# Scientific Audit of the Published Quantum Dot Model

## 1. Reference Article

Ghasemi, M., and Shokouhi, M. R.,
"Calculating the Eigenvalues of the Quantum Dot Operator Method and Exact Diagonalization Method,"
International Journal of Smart Electrical Engineering,
Vol. 9, No. 4, pp. 159–164.

## 2. Available Source Material

The scientific reconstruction is based exclusively on the published article.
The original computational source code, numerical input files, and supplementary calculation records are unavailable.

## 3. Preliminary Model Identification

The article discusses a two-electron quantum-dot system and introduces a Hamiltonian containing:

- Single-particle kinetic energy terms.
- Confinement potentials.
- Magnetic-field contributions.
- Spin-dependent terms.
- Spin-orbit coupling terms.
- Two-particle interaction potential.

## 4. Issues Requiring Verification

### 4.1 Interaction Potential

The article presents different mathematical forms for the interaction potential, including a Coulomb-like expression and an exponential interaction.

Their equivalence and physical interpretation are not established.

### 4.2 Dimensionality

The introduction refers to a two-dimensional electron gas, whereas the mathematical formulation uses one-dimensional particle coordinates and sine basis functions.

The dimensionality of the computational model requires clarification.

### 4.3 Spin and Particle Symmetry

The treatment of spin states and the required fermionic antisymmetry of the two-electron wavefunction must be examined.

### 4.4 Exact Diagonalization

The origin and physical derivation of the matrix elements presented in the article are not sufficiently specified.

An independently constructed Hamiltonian matrix will therefore be required for a reproducible numerical implementation.

### 4.5 Operator Method

The operator formulation, basis-state definitions, and derivation of the reported energy expressions require independent verification.

## 5. Reconstruction Strategy

No numerical implementation will be considered a faithful reproduction of the published results until the mathematical model, physical assumptions, and required parameters have been identified and verified.

Any additional assumptions or modifications will be explicitly documented as independent computational choices.

## 6. Preliminary Analysis of the Basis Functions

### 6.1 Single-Particle Basis

Equation (10) introduces a single-particle state consisting of:

- A sine function associated with an infinite square-well basis.
- A position- and spin-dependent complex phase factor.
- A spin basis function.

The expression contains the parameters n, s, L, alpha, and a_B.

Their definitions, physical dimensions, and parameter conventions require further verification before numerical implementation.

### 6.2 Two-Particle Basis

Equation (16) introduces a two-particle construction involving products of single-particle spatial and spin functions.

The exchange structure appears to incorporate particle antisymmetry. However, the precise spin and spatial symmetry conventions must be verified before constructing the computational basis.

### 6.3 Open Questions

- What are the exact definitions and dimensions of alpha and a_B?
- What are the allowed values of the spin index s?
- How are the two-particle quantum numbers assigned?
- Does the basis satisfy fermionic antisymmetry?
- Is the basis orthonormal under the conventions used in the article?

## 2. Consolidated Scientific Audit and Reconstruction Decisions

This section consolidates the main scientific issues identified during the examination of Equations (5)–(24) of the published article.

The objective is to distinguish the published formulation from assumptions and corrections required for an independent computational reconstruction.

### 2.1 Model Definition and Dimensionality

The introduction describes a two-dimensional electron gas, whereas the Hamiltonian and wave functions developed in the mathematical sections use the one-dimensional coordinates \(x_1\) and \(x_2\).

The dimensionality of the physical model is therefore not consistently established.

**Decision:** The independent reconstruction will initially be treated as a one-dimensional two-electron model. This choice will be explicitly documented as a modeling assumption, not as a confirmed reproduction of the complete physical system described in the introduction.

### 2.2 Single-Particle Hamiltonian and Basis Functions

The article introduces a single-particle Hamiltonian containing kinetic energy, confinement potential, and a spin-dependent term.

The proposed basis function contains an exponential phase factor and a sine function. However, the normalization factor uses \(L\), while the sine argument in Equation (10) uses \(l\).

The definitions and units of the parameters appearing in the phase factor are also insufficiently specified.

**Decision:** The basis functions and their normalization must be derived and checked independently before constructing the Hamiltonian matrix.

### 2.3 Spin and Magnetic-Field Terms

The Hamiltonian contains spin-orbit terms involving \(S_z\), while Equation (15) considers a magnetic field along the \(x\)-axis and consequently introduces \(S_x\).

The article does not fully establish the spin convention, the quantization axis, or the basis transformation needed to evaluate all spin-dependent matrix elements consistently.

**Decision:** The spin operators will be represented explicitly using a clearly defined spin basis. The Zeeman and spin-orbit contributions will be derived separately before being combined.

### 2.4 Electron–Electron Interaction

The article introduces more than one mathematical form for the interaction potential.

The earlier expressions include a Coulomb-like term and an exponential interaction. Equation (17) contains an exponential involving the absolute particle separation, while its subsequent matrix-element expression appears to omit the absolute value.

The negative sign of the exponential interaction also requires physical justification because the electrostatic interaction between two electrons is repulsive.

**Decision:** The published exponential potential and the conventional Coulomb interaction will be treated as distinct models. Their equivalence will not be assumed.

The sign, units, parameter definitions, and spatial dependence of each candidate interaction must be established before implementation.

### 2.5 Two-Electron Basis and Antisymmetry

The article uses two-particle states containing spatial and spin components. However, the complete basis construction and exchange conventions are not sufficiently explained.

For two identical electrons, the total wave function must be antisymmetric under particle exchange.

**Decision:** The independent reconstruction will explicitly construct antisymmetric two-electron states and verify their normalization and exchange symmetry.

### 2.6 Exact Diagonalization Formulation

Equation (14) presents two numerical matrices, but their physical derivation and interpretation are not established.

The printed matrices are not symmetric. If they are intended to represent a Hamiltonian matrix and an overlap matrix, respectively, this raises a consistency problem.

A physically valid Hermitian Hamiltonian matrix must satisfy:

\[
H=H^\dagger.
\]

For a generalized eigenvalue problem, the overlap matrix must also have the appropriate Hermitian and positive-definite properties.

**Decision:** The numerical matrices printed in Equation (14) will be retained only as published examples. They will not be used as the physical Hamiltonian of the reconstructed quantum-dot model.

The actual Hamiltonian and overlap matrices must be calculated from the independently defined basis functions.

### 2.7 Energy Expressions

The energy expressions in Equations (12), (23), and (24) require independent verification.

In particular, adding the two single-particle contributions in Equation (23) gives:

\[
\varepsilon_n+\varepsilon_\ell
=
\frac{(n^2+\ell^2)\pi^2\hbar^2}{2mL^2}
-\frac{\alpha^2me^4}{\hbar^2}.
\]

The first form printed in Equation (24) appears to retain this doubled correction. However, the subsequent simplified expression appears to lose a factor of two.

**Decision:** The energy expressions will be re-derived from the Hamiltonian rather than copied directly into the numerical implementation.

### 2.8 Numerical Reproducibility

The original source code, numerical input parameters, and supplementary calculation records are unavailable.

The published article does not provide enough information to reconstruct every numerical matrix element and plotted result unambiguously.

**Decision:** All new numerical calculations will be identified as an independent computational reconstruction. Results will not be described as exact reproductions unless the required physical and numerical information can be independently established.

### 2.9 Overall Reconstruction Strategy

The independent reconstruction will follow these stages:

1. Define a mathematically consistent one-dimensional two-electron model.
2. Specify the confinement potential, material parameters, units, and boundary conditions.
3. Construct and normalize the single-particle basis.
4. Define the spin operators and magnetic-field contribution.
5. Construct properly antisymmetrized two-electron basis states.
6. Derive the interaction matrix elements.
7. Assemble the Hermitian Hamiltonian matrix.
8. Calculate the energy eigenvalues using exact diagonalization.
9. Verify numerical convergence and physical consistency.
10. Compare the independently calculated results with the published figures, while clearly distinguishing numerical reconstruction from graphical digitization.

The implementation will begin only after these model definitions and mathematical checks have been completed.
