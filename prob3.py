import numpy as np
import scipy.stats as spt
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


def calc_skewness(u): return spt.skew(u)
def calc_kurtosis(u): return spt.kurtosis(u, fisher=False)

def calc_PDF(u):
    np.pdf()
