
"""
Baseline model: two electrons in a 1D infinite square well
with a softened Coulomb interaction.

Documentation:
    docs/baseline-model.md

Dimensionless units:
    Energy: E0 = hbar^2 pi^2 / (2 m* L^2)
    Length: L

Hamiltonian:
    H/E0 = -(1/pi^2)(d^2/dxi1^2 + d^2/dxi2^2)
           + (2*gamma/pi^2) /
             sqrt((xi1 - xi2)^2 + eta^2)

Parameters:
    gamma = L / a_B*
    eta   = d / L

Basis:
    phi_n(xi) = sqrt(2) sin(n pi xi)

The spatial wavefunctions are:
    - symmetric for the singlet sector
    - antisymmetric for the triplet sector

This is an independent baseline model using a softened
Coulomb interaction. It should not be interpreted as a
numerical reproduction of the original paper's Figure 2.
"""

import numpy as np


def _validate_parameters(n_basis, gamma, eta, n_quad):
    """Validate the main numerical parameters."""

    if not isinstance(n_basis, (int, np.integer)) or n_basis < 1:
        raise ValueError("n_basis must be a positive integer.")

    if not np.isfinite(gamma) or gamma < 0:
        raise ValueError("gamma must be finite and non-negative.")

    if not np.isfinite(eta) or eta <= 0:
        raise ValueError("eta must be finite and strictly positive.")

    if not isinstance(n_quad, (int, np.integer)) or n_quad < 2:
        raise ValueError("n_quad must be an integer greater than or equal to 2.")


def _gauss_legendre_01(m):
    """Gauss-Legendre quadrature points and weights on [0, 1]."""

    x, w = np.polynomial.legendre.leggauss(m)
    return 0.5 * (x + 1.0), 0.5 * w


def direct_integrals(n_basis, gamma, eta, n_quad=400):
    """
    Calculate the direct two-particle interaction integrals.

    J[a,b,c,d] =
        (2 gamma / pi^2) *
        integral integral
        phi_a(x1) phi_b(x1)
        K(x1,x2)
        phi_c(x2) phi_d(x2)
        dx1 dx2

    where:

        K(x1,x2) = 1 / sqrt((x1-x2)^2 + eta^2)

    Indices are stored using zero-based Python indexing.
    """

    _validate_parameters(n_basis, gamma, eta, n_quad)

    xi, w = _gauss_legendre_01(n_quad)

    n = np.arange(1, n_basis + 1)[:, None]

    phi = np.sqrt(2.0) * np.sin(n * np.pi * xi[None, :])

    # Products phi_a(x) * phi_b(x)
    pair = phi[:, None, :] * phi[None, :, :]

    # Softened Coulomb kernel
    kernel = 1.0 / np.sqrt(
        (xi[:, None] - xi[None, :]) ** 2 + eta ** 2
    )

    # First integration
    t = np.einsum(
        "abi,ij,i->abj",
        pair,
        kernel,
        w,
        optimize=True
    )

    # Second integration
    j = np.einsum(
        "abj,cdj,j->abcd",
        t,
        pair,
        w,
        optimize=True
    )

    return (2.0 * gamma / np.pi**2) * j


def build_hamiltonian(
    n_basis,
    gamma,
    eta,
    sector="singlet",
    n_quad=400
):
    """
    Construct the dimensionless Hamiltonian matrix.

    Parameters
    ----------
    n_basis : int
        Number of single-particle spatial basis functions.

    gamma : float
        Dimensionless interaction strength.

    eta : float
        Dimensionless softening length; must be positive.

    sector : str
        'singlet' or 'triplet'.

    n_quad : int
        Number of Gauss-Legendre quadrature points.

    Returns
    -------
    h : ndarray
        Hamiltonian matrix in units of E0.

    states : list
        Two-particle spatial basis states.
    """

    _validate_parameters(n_basis, gamma, eta, n_quad)

    if sector not in ("singlet", "triplet"):
        raise ValueError("sector must be 'singlet' or 'triplet'.")

    sign = 1.0 if sector == "singlet" else -1.0

    if sector == "singlet":
        states = [
            (n, m)
            for n in range(1, n_basis + 1)
            for m in range(n, n_basis + 1)
        ]
    else:
        states = [
            (n, m)
            for n in range(1, n_basis + 1)
            for m in range(n + 1, n_basis + 1)
        ]

    def norm(n, m):
        if sector == "singlet":
            return np.sqrt(2.0 * (1.0 + (n == m)))
        return np.sqrt(2.0)

    j = direct_integrals(n_basis, gamma, eta, n_quad)

    size = len(states)
    h = np.zeros((size, size), dtype=float)

    for p, (n, m) in enumerate(states):

        for q, (k, l) in enumerate(states):

            # Non-interacting two-particle energy
            if p == q:
                h[p, q] += n**2 + m**2

            # Direct and exchange interaction contributions
            direct = j[n - 1, k - 1, m - 1, l - 1]

            exchange = j[n - 1, l - 1, m - 1, k - 1]

            h[p, q] += (
                2.0
                / (norm(n, m) * norm(k, l))
                * (direct + sign * exchange)
            )

    # Remove negligible numerical asymmetry
    h = 0.5 * (h + h.T)

    return h, states


def energies(
    n_basis,
    gamma,
    eta,
    sector="singlet",
    n_quad=400,
    k=None
):
    """
    Calculate the lowest eigenvalues of the Hamiltonian.

    If k is None, all eigenvalues are returned.
    Otherwise, only the lowest k eigenvalues are returned.
    """

    h, _ = build_hamiltonian(
        n_basis=n_basis,
        gamma=gamma,
        eta=eta,
        sector=sector,
        n_quad=n_quad
    )

    eigenvalues = np.linalg.eigvalsh(h)

    if k is None:
        return eigenvalues

    if not isinstance(k, (int, np.integer)) or k < 1:
        raise ValueError("k must be a positive integer or None.")

    return eigenvalues[:k]
