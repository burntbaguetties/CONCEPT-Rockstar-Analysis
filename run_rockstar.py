import yt
import yt_astro_analysis
from yt_astro_analysis.halo_analysis import HaloCatalog


yt.enable_parallelism()

# EDIT THE FILE NAME HERE!
filename = '/mnt/c/Users/doman/OneDrive/Desktop/dcdm_nob/snapshot_a=1.000'
# EDIT THE OUTPUT DIRECTORY HERE!
output_dir = "/mnt/c/Users/doman/OneDrive/Desktop/rs_dcdm3/1.00"

data_ds = yt.load(filename)
#data_ds.parameters["format_revision"] = 2
hc = HaloCatalog(data_ds=data_ds, finder_method="rockstar",
    finder_kwargs={"num_readers": 1, "num_writers": 1,
                   "outbase": output_dir},)
hc.create()



#from yt.extensions.astro_analysis.halo_analysis import HaloCatalog


# https://yt-astro-analysis.readthedocs.io/en/latest/halo_finding.html
# running rockstar on one dataset/snapshot
# to run Rockstar, script must be run with mpirun using a minimum
# of three processors. Rockstar processes are divided into three groups:
# readers (specify num), writers (specify num), and server (always one).

# https://yt-project.org/docs/dev/cookbook/yt_gadget_analysis.html

# CL: mpirun -np [total # processers = 1 + n_readers + n_writers] python run_rockstar.py

# Rockstar halo catalogs are saved to the directory associated to the output_dir
# keyword provided to the HaloCatalog

# https://yt-project.org/docs/dev/reference/api/yt.loaders.html#yt.loaders.load_simulation