# Equation Analysis, Errata and Clarifications

**Paper:** M. Ghasemi and M. R. Shokouhi, *Calculating the Eigenvalues of the Quantum Dot Operator Method and Exact Diagonalization Method*, International Journal of Smart Electrical Engineering, Vol. 9, No. 4, pp. 159–164 (2020).

This note revisits Eqs. (5)–(24) of our paper. Its purpose is to make the model easier to follow and to reproduce. We fix the notation and units, derive the single-particle result of Eq. (12), and list the typographical errors and ambiguities that we found in the published equations, together with the convention we adopt for each.

Throughout, we distinguish between (i) results that follow directly from the published equations, (ii) corrections suggested by algebraic or dimensional consistency, and (iii) modeling conventions that we state explicitly because the paper does not.

## 0. Summary of issues

| ID | Equation(s) | Issue | Treatment here |
|---|---|---|---|
| E1 | (5) | The exponential interaction has no absolute value in the separation, so it is not symmetric under exchange of the particles | Symmetric form adopted |
| E2 | (5), (17)–(21) | Signs and exponent forms differ between these equations | One convention fixed in Sec. 6 |
| E3 | (6), (12) | Unit system and the meaning of the dielectric parameter are not specified; Eq. (6) is singular at coinciding positions | Gaussian units for the single-particle derivation; regularization stated in Sec. 2.2 |
| E4 | (8), (9) | The relation between the masses is not specified | Identical electrons, equal masses |
| E5 | (8)–(10) | The confinement potential is not defined | Infinite square well adopted |
| E6 | (10), (22), (24) | The well width is written both as L and as ℓ (ℓ is also a state index) | L is the well width; ℓ is an orbital index |
| E7 | (13) | The spin-dependent expression conflicts with the result derived from Eq. (9) and is not dimensionally consistent | Not used here |
| E8 | (14) | Both printed matrices are non-symmetric | Treated as an algebraic illustration only |
| E9 | (15), (16) | The field points along x while the spin basis is defined by S_z | Spin-flip structure described in the S_z basis |
| E10 | (16), (18)–(21) | Normalization and antisymmetry of the two-electron states are not specified | Explicit states defined; prefactor derived from them |
| E11 | (24) | The final expression loses a factor of two in the spin-orbit term | Corrected from Eq. (23) |
| E12 | Fig. 2 | Axis quantity, units and parameters are not specified | Treated as qualitative |

## 1. Conventions and assumptions

We use the following conventions throughout.

**Units.** Gaussian units are used in the derivation of Eq. (12).

**Particles.** Two identical electrons, $`m_1=m_2=m`$.

**Spin basis.** The spinors $`\chi_s`$ are eigenstates of $`S_z`$, with $`s=\pm1`$:

```math
S_z\chi_s=\frac{s\hbar}{2}\chi_s
```

**Bohr radius.** In Gaussian units, without dielectric screening or effective-mass corrections,

```math
a_B=\frac{\hbar^2}{me^2}
```

For a material-specific value, the effective Bohr radius is

```math
a_B^{\ast}=\frac{\varepsilon_r\hbar^2}{m^{\ast}e^2}
```

where $`m^{\ast}`$ is the effective mass and $`\varepsilon_r`$ is the relative dielectric constant.

**Confinement.** An infinite square well of width $`L`$:

```math
u(x)=0\ \text{ for } 0<x<L,\qquad u(x)=\infty\ \text{ otherwise}
```

**Indices.** $`n,m,k,\ell=1,2,3,\dots`$. The symbol $`L`$ is reserved for the well width.

These choices give a consistent mathematical starting point. They are conventions, and we state them here because the published text does not.

## 2. Equations (5)–(10)

### 2.1 Eq. (5): exponential interaction

In the published version the exponent does not contain the absolute value of the separation:

```math
V(x_1,x_2)=\frac{Ve^2}{2a}\exp\left(-\frac{x_1-x_2}{a}\right)
```

This expression is not symmetric under $`x_1\leftrightarrow x_2`$, and it grows exponentially for $`x_1<x_2`$. For an interaction between identical particles that depends only on their distance, the appropriate form is

```math
V_{\exp}(x_1,x_2)=\frac{Ve^2}{2a}\exp\left(-\frac{|x_1-x_2|}{a}\right)
```

Here $`a`$ is a characteristic length and $`V`$ is a dimensionless strength. This is the form we use, and it is also the form that appears in Eq. (17).

### 2.2 Eq. (6): Coulomb interaction

The published expression is

```math
V_C(x_1,x_2)=\frac{1}{4\pi\varepsilon^*}\,\frac{e^2}{x_1-x_2}
```

Two points need attention.

First, the separation should enter as $`|x_1-x_2|`$.

Second, the prefactor depends on the unit system and on what $`\varepsilon^*`$ denotes (an SI permittivity, a relative dielectric constant, or an effective parameter). We therefore do not change the prefactor without defining $`\varepsilon^*`$. In Gaussian units, with $`\varepsilon_r`$ the relative dielectric constant, the three-dimensional form is $`e^2/(\varepsilon_r r)`$.

A strictly one-dimensional Coulomb potential is singular at $`x_1=x_2`$. For numerical work, one possible effective regularization is

```math
V_{\mathrm{soft}}(x_1,x_2)=\frac{e^2}{\varepsilon_r\sqrt{(x_1-x_2)^2+\epsilon^2}},\qquad \epsilon>0
```

where $`\epsilon`$ plays the role of an effective transverse length. If it is not derived from a transverse confinement model, it should be treated as a free parameter and varied to test sensitivity. The exponential interaction of Eq. (17) is finite at $`x_1=x_2`$ and does not need this regularization.

### 2.3 Eq. (7): total Hamiltonian

```math
H=H_1+H_2+\vartheta(x_1,x_2)
```

Two single-particle Hamiltonians plus the interaction between the particles.

### 2.4 Eq. (8): two-particle Hamiltonian

For equal masses, the Hamiltonian reads

```math
H=\sum_{i=1}^{2}\left[\frac{P_{x_i}^{2}}{2m}+u(x_i)+\frac{eg}{2mc}\,\mathbf{B}\cdot\mathbf{S}_i+\frac{2e^2\alpha}{\hbar^2}\,P_{x_i}S_{z_i}\right]+\vartheta(x_1,x_2)
```

The values and physical meaning of $`g`$, $`m`$, $`\alpha`$ and the interaction parameters are not fixed by the published equations.

### 2.5 Eq. (9): single-particle Hamiltonian

```math
H_1=-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}+u(x)+\frac{2e^2\alpha}{\hbar^2}\,P_xS_z
```

With $`S_z\chi_s=\frac{s\hbar}{2}\chi_s`$ and $`P_x=-i\hbar\,\partial_x`$, the spin-orbit term becomes $`\lambda s p`$, where

```math
\lambda=\frac{\alpha e^2}{\hbar},\qquad p=P_x
```

Inside the well,

```math
H_1=\frac{p^2}{2m}+\lambda s p
```

In Gaussian units $`e^2/\hbar`$ has the dimension of a velocity, so $`\lambda p`$ is an energy when $`\alpha`$ is dimensionless.

### 2.6 Eq. (10): single-particle basis

```math
\psi_{n,s}(x)=\sqrt{\frac{2}{L}}\;e^{-i\alpha s x/a_B}\,\sin\left(\frac{n\pi x}{L}\right)\chi_s
```

Here $`L`$ is the well width (E6). With $`a_B=\hbar^2/(me^2)`$ we have $`\alpha/a_B=m\lambda/\hbar`$, so the phase factor equals $`e^{-im\lambda s x/\hbar}`$. Its role is derived in the next section.

## 3. Equations (11)–(13): single-particle energy

### 3.1 Eq. (11)

```math
H\Psi=E\Psi
```

In the context of Eqs. (9)–(13), $`H`$ is the single-particle Hamiltonian $`H_1`$. The two-particle problem is treated in Secs. 4–8.

### 3.2 Eq. (12): derivation

Inside the well, $`H_1=\frac{p^2}{2m}+\lambda s p`$. Since $`s^2=1`$, completing the square gives

```math
H_1=\frac{(p+m\lambda s)^2}{2m}-\frac{m\lambda^2}{2}
```

Write $`\psi(x)=e^{-im\lambda s x/\hbar}\,\varphi(x)`$. Then $`(p+m\lambda s)\psi=e^{-im\lambda s x/\hbar}\,p\,\varphi`$, and therefore

```math
H_1\psi=e^{-im\lambda s x/\hbar}\left[\frac{p^2}{2m}-\frac{m\lambda^2}{2}\right]\varphi
```

The phase factor has unit modulus, so the boundary conditions $`\psi(0)=\psi(L)=0`$ are equivalent to $`\varphi(0)=\varphi(L)=0`$. Hence $`\varphi_n\propto\sin(n\pi x/L)`$, which is exactly the spatial part of Eq. (10), and

```math
E_n=\frac{n^2\pi^2\hbar^2}{2mL^2}-\frac{m\lambda^2}{2}=\frac{n^2\pi^2\hbar^2}{2mL^2}-\frac{\alpha^2 m e^4}{2\hbar^2}
```

This reproduces Eq. (12). The spin-orbit correction is independent of both $`s`$ and $`n`$: in this model it is a uniform energy shift.

### 3.3 Eq. (13): spin-dependent expressions

In the published version, Eq. (13) gives spin-dependent energies containing terms of the form

```math
\alpha^2e^2\left(\frac12\pm\frac1{a_B}\right)+E_n
```

Under the conventions above, there are two problems (E7):

1. The spin-dependent splitting contradicts the derivation of Sec. 3.2. With the spin-orbit term along $`S_z`$ and hard-wall boundary conditions, the correction does not depend on $`s`$.
2. The sum $`\frac12+\frac1{a_B}`$ adds a dimensionless number to an inverse length, so it is not dimensionally consistent.

We therefore do not use Eq. (13). Eq. (12) is not affected. This conclusion refers to the equation as published and to the conventions stated in this note.

## 4. Eq. (14): exact diagonalization

We illustrated the matrix formulation with

```math
H_{\alpha\beta}=\begin{pmatrix}1&2&0\\2&1&3\\-1&0&1\end{pmatrix},\qquad
u_{\alpha\beta}=\begin{pmatrix}2&3&1\\3&1&0\\2&0&1\end{pmatrix}
```

The corresponding system is

```math
\sum_j\left(H_{ij}-E\,u_{ij}\right)\Psi_j=0
```

and a non-trivial solution requires $`\det(H-Eu)=0`$. This is the form of a generalized eigenvalue problem,

```math
H\mathbf{c}=E\,S\,\mathbf{c}
```

where $`S`$ is the overlap matrix of a non-orthogonal basis. Here $`u_{\alpha\beta}`$ plays the role of $`S`$ (E8).

A qualification is needed. For a Hermitian Hamiltonian in a basis of real functions, $`H`$ must be symmetric, and $`S`$ must be symmetric and positive definite. Both printed matrices are non-symmetric, so taken literally they are not admissible Hamiltonian and overlap matrices, and their generalized eigenvalues are not guaranteed to be real. They illustrate the algebraic form of the method only. They are not built from the Hamiltonian of Eq. (8), and their eigenvalues are not quantum-dot energy levels.

For the sine basis of Eq. (10), the spatial functions are orthonormal on $`[0,L]`$,

```math
\int_0^L \phi_n^*(x)\,\phi_m(x)\,dx=\delta_{nm}
```

so $`S_{ij}=\delta_{ij}`$ and the problem reduces to the ordinary eigenvalue problem $`H\mathbf{c}=E\mathbf{c}`$.

## 5. Eqs. (15)–(16): Zeeman term

Eq. (15) takes the magnetic field along $`x`$:

```math
\mathbf{B}=B\,\hat{x},\qquad \mathbf{B}\cdot\mathbf{S}=B\,S_x
```

The spin basis is the eigenbasis of $`S_z`$ (E9). In this basis,

```math
S_x=\frac{\hbar}{2}\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
\langle\chi_{s'}|S_x|\chi_s\rangle=\frac{\hbar}{2}\,\delta_{s',-s}
```

so the Zeeman term produces spin-flip matrix elements. Because it acts only on spin, the spatial part of its matrix elements is an overlap of orbital functions, which for the orthonormal sine basis imposes the corresponding selection rules on the orbital indices.

## 6. Eq. (17): interaction potential

In the published version,

```math
\vartheta(x_1,x_2)=-\frac{Ve^2}{2a}\exp\left(-\frac{|x_1-x_2|}{a}\right)
```

This is an effective exponential interaction, not the Coulomb potential of Eq. (6). The length $`a`$ sets its range and $`V`$ its strength.

The sign is not consistent across the published equations (E2): Eq. (17) carries a negative prefactor, Eqs. (18)–(21) carry a positive one, and the intermediate lines of Eq. (17) also mix signs and exponent forms. We adopt the convention

```math
\vartheta(x_1,x_2)=+\frac{Ve^2}{2a}\exp\left(-\frac{|x_1-x_2|}{a}\right),\qquad V>0
```

which is repulsive, as the electron-electron interaction is. This is a modeling convention. An attractive interaction is obtained by reversing the sign, and any calculation must use one stated sign throughout.

## 7. Eqs. (18)–(21): interaction matrix elements

### 7.1 Antisymmetrized two-electron states

For two identical fermions the wavefunction must be antisymmetric under exchange. For two distinct orthonormal spin-orbitals we use

```math
|n,s_n;\ell,s_\ell\rangle=\frac{1}{\sqrt{2}}\left[\psi_{n,s_n}(x_1)\,\psi_{\ell,s_\ell}(x_2)-\psi_{\ell,s_\ell}(x_1)\,\psi_{n,s_n}(x_2)\right]
```

If the two spin-orbitals coincide, this state vanishes (Pauli principle).

### 7.2 Structure of the matrix element

Expanding the bra and the ket in

```math
\langle m,s_m;k,s_k|\,\vartheta\,|n,s_n;\ell,s_\ell\rangle
```

gives four terms (direct and exchange). The product of the two normalization factors is $`\frac{1}{\sqrt2}\cdot\frac{1}{\sqrt2}=\frac12`$. A typical spatial integral is

```math
I=\frac{Ve^2}{2a}\cdot\frac12\cdot\frac{4}{L^2}\int_0^L\!\!\int_0^L \Phi(x_1,x_2)\,\exp\left(-\frac{|x_1-x_2|}{a}\right)dx_1\,dx_2
```

with, for example,

```math
\Phi=\sin\frac{n\pi x_1}{L}\,\sin\frac{m\pi x_1}{L}\,\sin\frac{\ell\pi x_2}{L}\,\sin\frac{k\pi x_2}{L}
```

The four terms differ in how the orbital indices are assigned to $`x_1`$ and $`x_2`$, and the Kronecker deltas of the spin indices select the direct and exchange contributions.

### 7.3 Points to note (E10)

1. **Prefactor.** With normalized antisymmetric bra and ket, the expansion gives $`1/2`$, whereas the published equations show $`1/\sqrt2`$. This correction depends on the basis-state definition of Sec. 7.1. The factor $`4/L^2`$ comes from the four sine normalizations.
2. **Absolute value.** With $`|x_1-x_2|`$ in the exponent, each double integral is evaluated by splitting the domain into $`x_1>x_2`$ and $`x_1<x_2`$, analytically or by numerical quadrature.
3. **Signs.** The relative signs of direct and exchange terms follow from the antisymmetrization and should be taken from the full bra-ket expansion.
4. **Hermiticity.** With a real symmetric interaction and an orthonormal basis, the interaction matrix is Hermitian.

## 8. Eqs. (22)–(24): non-interacting two-particle energies

### 8.1 Eq. (22)

Eq. (22) gives the matrix element of the non-interacting part of the Hamiltonian between two-particle states. It has direct and exchange parts with Kronecker deltas, and its spin-orbit term is the sum of the two single-particle shifts of Eq. (12).

### 8.2 Eq. (23)

```math
\varepsilon_n=\frac{n^2\pi^2\hbar^2}{2mL^2}-\frac{\alpha^2 m e^4}{2\hbar^2},\qquad
\varepsilon_\ell=\frac{\ell^2\pi^2\hbar^2}{2mL^2}-\frac{\alpha^2 m e^4}{2\hbar^2}
```

Adding them,

```math
\varepsilon_n+\varepsilon_\ell=\frac{(n^2+\ell^2)\pi^2\hbar^2}{2mL^2}-\frac{\alpha^2 m e^4}{\hbar^2}
```

### 8.3 Eq. (24): missing factor of two (E11)

The intermediate line of Eq. (24) contains $`-\frac{2\alpha^2me^4}{2\hbar^2}`$, which agrees with the sum above. The final line, however, reads

```math
-\frac{\alpha^2 m e^4}{2\hbar^2}+(n^2+\ell^2)\,\frac{\pi^2\hbar^2}{2mL^2}
```

so a factor of two is lost in the spin-orbit term, and the symbol $`\ell`$ appears in the denominator where the well width $`L`$ is meant (E6). The corrected expression is

```math
E_{n\ell}=\frac{(n^2+\ell^2)\pi^2\hbar^2}{2mL^2}-\frac{\alpha^2 m e^4}{\hbar^2}
```

in agreement with Eq. (22), Eq. (23) and the sum of the two single-particle energies of Eq. (12).

## 9. Figure 2

Fig. 2 shows eigenvalues as a function of a parameter. In the text we described the values as approximately constant over $`(0,\,0.1)`$ and rising steeply over $`(0.2,\,0.4)`$. The published paper does not specify the quantity on the horizontal axis, its units, the values of $`L`$, $`a`$, $`V`$, $`\alpha`$ and $`B`$, the basis size, or the numerical procedure.

For this reason the figure is treated as a qualitative illustration here. This note makes no quantitative claim based on the constant or the steep region, and it does not present Fig. 2 as a verified consequence of Eqs. (5)–(24).

## 10. Status of the equations

| Equation(s) | Assessment |
|---|---|
| (5) | Symmetry issue identified; symmetric form adopted |
| (6) | Prefactor depends on the definition of the dielectric parameter; regularization is an explicit model choice |
| (7) | Decomposition is well defined |
| (8), (9) | Well defined under the conventions of Sec. 1; parameter values not fixed by the paper |
| (10) | Interpreted with the infinite-well assumption and the stated Bohr radius |
| (11), (12) | Single-particle energy derived by completing the square |
| (13) | Inconsistent with the derivation and dimensionally problematic as published; not used |
| (14) | Valid generalized eigenvalue form; printed matrices are illustrative only |
| (15), (16) | Spin-flip structure clarified in the $`S_z`$ basis |
| (17) | Sign inconsistency identified; repulsive convention adopted |
| (18)–(21) | Antisymmetric construction made explicit; prefactor depends on the stated normalization |
| (22), (23) | Consistent with the sum of single-particle energies |
| (24) | Missing factor of two and the width notation corrected |
| Fig. 2 | Treated as qualitative |

## 11. Scope

This note clarifies the mathematical structure of the published equations and fixes the conventions needed to implement the model. It does not claim that every parameter or approximation coincides with those used for the figures in the paper. Numerical results computed from these conventions will be added to the repository with their parameters, basis size, integration and diagonalization methods, and convergence checks documented alongside them.
