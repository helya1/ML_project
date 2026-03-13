from smoothing import Smoothing


def compute_fourier_coeffs(X, n_fourier=10):
    """
    Compute Fourier coefficients for signals
    """
    sm = Smoothing(fit='fourier', n=n_fourier, data=X)
    return sm.coeffs


def compute_bspline_coeffs(X, smoothing_str=0.3, terms=20):
    """
    Compute B-spline coefficients for signals
    """
    sm = Smoothing(
        fit='bspline',
        smoothing_str=smoothing_str,
        terms=terms,
        data=X
    )
    return sm.coeffs