import numpy as np
import scipy.stats as stats
from matplotlib import pyplot as plt


def load_data():
    bl_data = np.loadtxt("bl_udata.txt", skiprows=1)
    grid_data = np.loadtxt("grid_udata.txt", skiprows=1)
    return bl_data, grid_data


def calc_turb_intensity(u):
    u_mean = np.average(u)
    u_fluc = u - u_mean
    turb_intensity = np.std(u_fluc) / u_mean
    return turb_intensity


def calc_skewness(u): return stats.skew(u)


def calc_kurtosis(u): return stats.kurtosis(u, fisher=False)


def plot_pdf(u, title, xlabel, ylabel, logplot=False):
    u_mean = np.mean(u)
    u_fluc = u - u_mean
    n_bins = 50
    # Creating histogram
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.hist(u_fluc, bins=n_bins, density=True)
    ax2.hist(u_fluc, bins=n_bins, density=True)
    fig.suptitle(title)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)

    # Comparing to normal distribution
    mu = np.mean(u_fluc)
    sigma = np.std(u_fluc)
    x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 100)

    ax1.plot(x, stats.norm.pdf(x, mu, sigma), linewidth=3, color='k')
    ax2.semilogy(x, stats.norm.pdf(x, mu, sigma), linewidth=3, color='k')

    return None
