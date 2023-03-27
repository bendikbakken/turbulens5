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
    turb_intensity = np.std(u_fluc)/u_mean
    return turb_intensity


def calc_skewness(u): return stats.skew(u)
def calc_kurtosis(u): return stats.kurtosis(u, fisher=False)


def plot_pdf(u, title, xlabel, ylabel):
    u_mean = np.mean(u)
    u_fluc = u - u_mean
    n_bins = 50
    # Creating histogram
    plt.subplots(1, 1, figsize=(10, 7), tight_layout=True)

    plt.hist(u_fluc, bins=n_bins, density=True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    mu = np.mean(u_fluc)
    sigma = np.std(u_fluc)
    x = np.linspace(mu - 5 * sigma, mu + 5 * sigma, 100)
    plt.plot(x, stats.norm.pdf(x, mu, sigma), linewidth=5)

    return None
