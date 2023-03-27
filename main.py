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
    return


if __name__ == '__main__':
    main()
