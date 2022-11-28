# MART3D

**MART3D** is a **M**ulti-l**A**yer heterogeneous **3D** **R**adiative **T**rasnfer framework for forest reflectance simulations based on the 3D radiative transfer model LESS (http://lessrt.org/). Therefore, MART3D actually provides a simple interface to the sophisticated 3D RT model. With MART3D, we can input some simple parameters instead of explicitly creating 3D scenes, e.g., leaf area index, trunk height, crown diameter and grass LAI. These parameters are then used by MART3D to generate heterogeneous 3D scenes automatically, based on which LESS simulates BRF with accurate 3D radiative transfer modeling.


<img width="400" src="https://user-images.githubusercontent.com/1770654/204232655-e9cef047-3c28-4e60-83cd-833042e3c72f.png"/>

## Usage
### Step 01: Install LESS

Since MART3D is built on the LESS model, therefore, you should first install LESS on your computer, please go to [Download LESS](http://lessrt.org/docs/installation/) to download the latest version of LESS. LESS is a ray-tracing based 3D radiative transfer model, which provides both graphic user interface (GUI) as well as Python SDK to perform 3D radiative transfer simulation over detailed 3D scenes (e.g., forests and city buildings). LESS can simulate bidirectional reflectance factor, multispectral/hyperspectral images, LiDAR waveforms/point cloud, thermal infared images, FPAR, etc. We recommend to install LESS in a path without spaces to avoid some possible issues during simulation, e.g., `D:\LESS`. (Note: recent LESS versions only support Windows)

<img width="300" src="https://user-images.githubusercontent.com/1770654/204241737-cc43cb05-f84c-43ec-8ab1-68f02eea6cdc.png"/>

### Step 02: Configure environment

The only thing you need to do is to set the LESS Python SDK before you using MART3D. If you are using editor like Pycharm. You can configure the python interpreter as the Python.exe provided by LESS, because this interpreter has already installed some necessary python modules. This interpreter is located in the LESS installation directory, e.g., `D:\LESS\app\bin\python\python.exe`. And then, the LESS SDK can be configured following the below figure (right), the SDK is located in LESS installation directory, e.g., `D:\LESS\app\Python_script\pyLessSDK`

<img width="300" src="https://user-images.githubusercontent.com/1770654/204243357-1af7506b-3dfb-4553-b0a1-5446f3d864a8.png"/> <img width="600" src="https://user-images.githubusercontent.com/1770654/204244982-239cb0be-2b20-4dd1-9dca-91470945dcf5.png"/>

If you are not using Pycharm, you can specify the pyLessSDK by using python code

```
import sys
sys.path.append(r"D:\LESS\app\Python_script\pyLessSDK")
```

### Step 03: Doing the simulations
The code in this repository (`MART3D.py`) shows the example to run the simulations.

```
import sys
sys.path.append(r"D:\LESS\app\Python_script\pyLessSDK")  # if you do not using pycharm, you can use this line

from ForestPlotGenerator import ForestPlot, OpticalRefTrans

less_install_dir = r"D:\LESS"  # The root installation directory of LESS
dist_dir = r"D:\LESS\simulations\ForestPlotGenerate"  # Specify a folder to store the simulation files and results
sim_name = r"forestplot001"  # The name of the simulation, all the files and results will be generated within this folder, you can name it as you want

plot = ForestPlot(less_install_dir, dist_dir, sim_name, scene_x_size=30, scene_y_size=30)

# spectral bands
plot.spectral_bands = [450, 550, 650, 850]   # 4 spectral bands in nm

# view and solar parameters
plot.solar_zenith_angle = 45
plot.solar_azimuth_angle = 90
plot.view_zen_azi_angles = [(0, 0)]


plot.generate()
plot.do_sim()
```

