# coding: utf-8
# Author: Jianbo Qi
# Date: 2022/11/28
# This script demonstrate how to use MART3D model to simulate canopy reflectance using 3D radiative transfer

from ForestPlotGenerator import ForestPlot, OpticalRefTrans
from SimpleCrownGenerator import LAD
# from Prospect5AndD import prospectD   # If you want to use prospect to generate leaf optical properties

less_install_dir = r"D:\LESS"
dist_dir = r"D:\LESS\simulations\ForestplotGenerate"
sim_name = r"forestplot001"

plot = ForestPlot(less_install_dir, dist_dir, sim_name, scene_x_size=30, scene_y_size=30)

# spectral bands
plot.spectral_bands = [450, 550, 650, 850]   # 4 spectral bands in nm

# Config the layers
plot.has_grass_layer = True
plot.has_shrub_layer = True
plot.has_mediate_tree_layer = True
plot.has_big_tree_layer = True

# LAI of each layer
plot.lai_grass = 1.0
plot.lai_shrub = 1.0
plot.lai_mediate_tree = 1.0
plot.lai_big_tree = 2.0

# fraction of canopy cover of each layer
plot.fcc_shrub = 0.5
plot.fcc_mediate_tree = 0.2
plot.fcc_big_tree = 0.2

# hotspot factor, which is like the parameter in PROSAIL
plot.hotspot_grass = 0.05
plot.hotspot_shrub = 0.05
plot.hotspot_mediate_tree = 0.1
plot.hotspot_big_tree = 0.1

# diameter at breast height of trees
plot.dbh_mediate_tree = 0.15
plot.dbh_big_tree = 0.3

# grass height, trunk height, please note that crown_height+trunk_height = tree height
plot.grass_height = 0.5
plot.trunk_height_mediate_tree = 10
plot.trunk_height_big_tree = 16

# crown diameters
plot.crown_diameter_SN_shrub = 1.0
plot.crown_diameter_EW_shrub = 1.0
plot.crown_height_shrub = 1.0
plot.crown_diameter_SN_mediate_tree = 2.5
plot.crown_diameter_EW_mediate_tree = 2.5
plot.crown_height_mediate_tree = 4.0
plot.crown_diameter_SN_big_tree = 4
plot.crown_diameter_EW_big_tree = 4
plot.crown_height_big_tree = 8


# Leaf angle distribution
plot.lad_grass = LAD.ERECTOPHILE
plot.lad_shrub = LAD.SPHERICAL
plot.lad_mediate_tree = LAD.SPHERICAL
plot.lad_big_tree = LAD.SPHERICAL

# If branches are included, if not, only trunk is created.
plot.tree_has_branches = True

# optical properties of each components
plot.spectral_bands = [450, 550, 650, 850]  # "450:1,550:1,650:1,850:1"
plot.op_soil = OpticalRefTrans([0.0486,0.1376,0.2280,0.3382], [0.0000,0.0000,0.0000,0.0000], [0.0000,0.0000,0.0000,0.0000])
plot.op_grass = OpticalRefTrans([0.0454,0.1012,0.0389,0.4747], [0.0454,0.1012,0.0389,0.4747], [0.0005,0.1067,0.0187,0.4843])
plot.op_shrub = OpticalRefTrans([0.0454,0.1012,0.0389,0.4747], [0.0454,0.1012,0.0389,0.4747], [0.0005,0.1067,0.0187,0.4843])
plot.op_mediate_tree = OpticalRefTrans([0.0454,0.1012,0.0389,0.4747], [0.0454,0.1012,0.0389,0.4747], [0.0005,0.1067,0.0187,0.4843])
plot.op_big_tree = OpticalRefTrans([0.0454,0.1012,0.0389,0.4747], [0.0454,0.1012,0.0389,0.4747], [0.0005,0.1067,0.0187,0.4843])
plot.op_trunk_mediate_tree = OpticalRefTrans([0.0723,0.0942,0.1048,0.4523], [0.0000,0.0000,0.0000,0.0000], [0.0000,0.0000,0.0000,0.0000])
plot.op_trunk_big_tree = OpticalRefTrans([0.0723,0.0942,0.1048,0.4523], [0.0000,0.0000,0.0000,0.0000], [0.0000,0.0000,0.0000,0.0000])
plot.op_branch_mediate_tree = OpticalRefTrans([0.0723,0.0942,0.1048,0.4523], [0.0000,0.0000,0.0000,0.0000], [0.0000,0.0000,0.0000,0.0000])
plot.op_branch_big_tree = OpticalRefTrans([0.0723,0.0942,0.1048,0.4523], [0.0000,0.0000,0.0000,0.0000], [0.0000,0.0000,0.0000,0.0000])
plot.op_trunk_lower = OpticalRefTrans([0.0723,0.0942,0.1048,0.4523], [0.0000,0.0000,0.0000,0.0000], [0.0000,0.0000,0.0000,0.0000])

# view and solar parameters
plot.solar_zenith_angle = 45
plot.solar_azimuth_angle = 90
plot.view_zen_azi_angles = [(0, 0), (45, 0)]  # [(zenith angle, azimuth angle), ...] in degree

# perform the simulation
plot.generate()
plot.do_sim()