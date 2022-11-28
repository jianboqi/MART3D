# coding: utf-8
# Author: Jianbo Qi
# Date: 2022/11/28
# This script demonstrate how to use MART3D model to simulate canopy reflectance using 3D radiative transfer

from ForestPlotGenerator import ForestPlot, OpticalRefTrans

less_install_dir = r"D:\LESS"
dist_dir = r"D:\LESS\simulations\ForestPlotGenerate"
sim_name = r"forestplot001"

plot = ForestPlot(less_install_dir, dist_dir, sim_name, scene_x_size=30, scene_y_size=30)

# spectral bands
plot.spectral_bands = [450, 550, 650, 850]   # 4 spectral bands in nm

# view and solar parameters
plot.solar_zenith_angle = 45
plot.solar_azimuth_angle = 90
plot.view_zen_azi_angles = [(0, 0)]


plot.generate()
plot.do_sim()