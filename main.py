import prob3


def main():
    bl_data, grid_data = prob3.load_data()
    u_bl = bl_data[:, 1]
    u_grid = grid_data[:, 1]
    ti_bl = prob3.calc_turb_intensity(u_bl)
    ti_grid = prob3.calc_turb_intensity(u_grid)

    skew_bl = prob3.calc_skewness(u_bl)
    skew_grid = prob3.calc_skewness(u_grid)

    kurtosis_bl = prob3.calc_kurtosis(u_bl)
    kurtosis_grid = prob3.calc_kurtosis(u_grid)

    print("a)")
    print(f"The turbulence intensity for the wall bounded flow is {ti_bl}.")
    print(f"The turbulence intensity for the wall bounded flow is {ti_grid}.")
    print()
    print("b)")
    print(f"The skewness for the boundary layer is S = {skew_bl}.")
    print(f"The skewness for the grid is S = {skew_grid}.")
    print()
    print("c)")
    print(f"The kurtosis for the boundary layer is k = {kurtosis_bl}.")
    print(f"The kurtosis for the grid is k = {kurtosis_grid}.")

    prob3.plot_pdf(u_bl, "BL PDF", "x", "y")
    prob3.plot_pdf(u_grid, "Grid PDF", "x", "y")
    prob3.plt.show()

    return


if __name__ == '__main__':
    main()



#Console:
"""
a)
The turbulence intensity for the wall bounded flow is 0.029072768651233653.
The turbulence intensity for the wall bounded flow is 0.04448035119001293.

b)
The skewness for the boundary layer is S = -0.361558714908824.
The skewness for the grid is S = -0.01458851194362283.

c)
The kurtosis for the boundary layer is k = 3.5513316454327444.
The kurtosis for the grid is k = 3.1622375450201106.

Process finished with exit code 0

"""
