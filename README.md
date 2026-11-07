# Quantum Dot Eigenvalue Calculation

This repository accompanies our paper on the calculation of eigenvalues in quantum dot systems using an operator method and exact diagonalization. It contains an equation-by-equation analysis of the paper, with errata and clarifications, and a baseline model for further numerical work.

## Published article

**Title:** Calculating the Eigenvalues of the Quantum Dot Operator Method and Exact Diagonalization Method

**Authors:** Mahdiyeh Ghasemi and Mohammad Reza Shokouhi

**Journal:** International Journal of Smart Electrical Engineering

**Publication details:**
- Volume 9, Issue 4, pp. 159–164, Fall 2020
- ISSN: 2251-9246
- E-ISSN: 2345-6221
- Received: 20 December 2020; Revised: 20 February 2021; Accepted: 25 February 2021

[Read the published article (PDF)](https://oiccpress.com/ijsee/article/download/16411/17967/42677)

## Abstract

We consider a quantum dot as a confined quantum system and write the Hamiltonian for the Coulomb potential arising from an electric dipole. Using special functions, we obtain the corresponding eigenvalues, and we compare two approaches: an operator-based method and numerical exact diagonalization. The Hamiltonian includes kinetic, confinement, Coulomb interaction, and magnetic-field contributions.

## Research topics

- Quantum dots and confined quantum systems
- Quantum Hamiltonians
- Coulomb interactions
- Magnetic-field effects
- Operator methods
- Exact diagonalization
- Energy eigenvalue calculations

## Repository contents

| File | Description |
|---|---|
| [`docs/equation-analysis.md`](docs/equation-analysis.md) | Analysis of Eqs. (5)–(24): conventions, derivation of the single-particle energy (Eq. 12), errata, and clarifications |
| [`docs/baseline-model.md`](docs/baseline-model.md) | Baseline definition of a one-dimensional two-electron quantum dot with a softened Coulomb interaction, in dimensionless form |

Both documents use the same conventions and notation, which are stated at the beginning of each file.

## Scope and reproducibility

The published article does not specify every parameter and numerical detail of its calculations, for example the quantities and values used in Fig. 2. For this reason, the documents in this repository state their conventions and assumptions explicitly.

We distinguish between:

- mathematical relations given in the article,
- corrections that follow from algebraic or dimensional consistency,
- modeling conventions that we state because the article does not,
- numerical results computed in this repository.

Numerical results computed here use the conventions of the documents above. They are not claimed to reproduce Fig. 2 of the article quantitatively, and any extension beyond the article is identified as such.

## Status

- [x] Equation analysis and errata
- [x] Baseline model definition
- [ ] Numerical implementation of the baseline model (planned)

## Citation

```bibtex
@article{ghasemi2020quantumdot,
  author  = {Ghasemi, Mahdiyeh and Shokouhi, Mohammad Reza},
  title   = {Calculating the Eigenvalues of the Quantum Dot Operator Method and Exact Diagonalization Method},
  journal = {International Journal of Smart Electrical Engineering},
  volume  = {9},
  number  = {4},
  pages   = {159--164},
  year    = {2020},
  issn    = {2251-9246}
}
```

## Acknowledgements

We thank Dr. Mohammad Reza Tanhayi for his valuable comments.
