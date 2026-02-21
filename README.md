# Decaying Cold Dark Matter Simulations, Halo Finding, & Particle Tracking

_Code for finding and analyzing the halos from a CONCEPT decaying cold dark matter (DCDM) simulation and tracking their particles._

Software used: CONCEPT, yt, Rockstar-Galaxies, pygadgetreader

This code was produced during research work under the advising of Professor Jessie Shelton at the University of Illinois Urbana-Champaign and in collaboration with Professor Joshua Foster at the University of Wisconsin-Madison.

## **Summaries & descriptions for each of the files in this repository:**

## Simulations:
I ran two DCDM simulations through CONCEPT and included both of their snapshots at various scale factors (in Gadget2 form). Snapshots for Simulation 1 and Simulation 2 are in folders **dcdm_snapshots1** and **dcdm_snapshots2** respectively. Similarly, the CONCEPT parameter files for the two simulations are the files called **concept_paramfile1** and **concept_paramfile2**. They are basically the same simulation, except for the second simulation, I did not specify the density parameter of the baryons and I output the snapshots at a larger amount of scale factors. Additionally, **dcdm_snapshots1** includes the "effective" versions of each snapshot with the density parameters changed to their "effective" values, as described under the ***Halo Finding*** section of this document.

**Select Parameters of Simulation 1:**
* size: N = 96^3 particles
* decay rate: 100 * km/(s * Mpc)
* total amount of stable and decaying cold dark matter (CDM): 0.27
* fraction of total CDM that is decaying: 0.999
* boxsize: 128*Mpc
* amount of baryons: 0.049
* snapshot scale factors: a = 0.02, 0.6, 0.7, 0.8, 0.87, 0.9, 1.00

**Select Parameters of Simulation 2:**
* size: N = 96^3 particles
* decay rate: 100 * km/(s * Mpc)
* total amount of stable and decaying cold dark matter (CDM): 0.27
* fraction of total CDM that is decaying: 0.999
* boxsize: 128*Mpc
* amount of baryons: not specified. I thought this would lead to no baryons at all in the simulation, but I do not know if that was successful or not.
* snapshot scale factors: a = 0.02, 0.5, 0.6, 0.7, 0.73, 0.75, 0.76, 0.765, 0.77, 0.775, 0.78, 0.79, 0.8, 0.85, 0.9, 1

## Halo Finding
To find halos (or, for our purposes, just locate the positions, velocities, etc, of gravitationally self-bound clumps of particles, and then track them manually), we can pass the simulation snapshots through Rockstar. I used the file **run_rockstar.py** to do this.

Since Rockstar assumes a Lambda-CDM background cosmology, it is possible to feed Rockstar "effective" density parameters from the true CONCEPT density parameters such that Rockstar will compute & use the correct densities for the simulations' DCDM/early matter-dominated era (EMDE) cosmology. To do this, I used the Jupyter notebook **modify_snapshot_bkgcosmology.ipynb**. It includes functions that will be able to handle & modify the Gadget2-type snapshot file headers, as well as a function that will calculate the "effective" background cosmology parameters given true parameters, and create a new snapshot file with the header updated to the new values.

After creating "effective" snapshots for Simulation 1, I ran each one through the Rockstar halo finder and stored the outputs in the **halos_simulation1** folder. The Rockstar outputs are stored in folders labeled by the corresponding scale factor _a_ for each simulation. The halos and their particles can be accessed through the _halos_0.0.bin_ files as explained in the Rockstar/yt documentation. 




## Halo Analysis & Particle Tracking
Included are some of the Jupyter notebooks that I used to write functions for halo/particle tracking and do some preliminary analysis on my DCDM simulation halos. The notebooks are inside the folder **halo particle tracking**. Here is what can be found in each notebook:

**halo_tracking.ipynb**:
* This notebook contains the first, most basic functions that I wrote to work with the halo files and compare halos. For example, I have functions that will take the halo files and turn them into convenient dictionaries where each key is a halo, and the value is the array of member particle IDs. It also includes functions to plot the 2d surface density of particles, compare member particle ID overlap between halos, turn halos with all their properties into pandas dataframes to work with, to find matches between halos based on percentage of particle ID overlap, building halo descendant maps over time (scale factor) based on particle ID membership matches, tracing halo growth history, etc. I did a bit of analysis on the simulation files inside this notebook, and left their outputs and plots in for example. To use the same things, the snapshot files will need to be updated.
* Some of the functions in this notebook were written assuming that the halos found by Rockstar were accurate, which, for the dcdm/emde cosmology, they are not after reheating, so some functions that track particles specifically rather than relying on Rockstar's halo finding, can be found in the next notebook (**particle_tracking.ipynb**).


**particle_tracking.ipynb**:
* In this notebook, I attempted to focus more on the particles and analyzing their evolution through a simulation (the simulation in this notebook is Simulation 1 as described above). It repeats some of the same helper functions from the **halo_tracking.ipynb** notebook, such as functions that group halos into member particle ID dictionaries and turns them into pandas dataframes. I also added some new, similar helper functions as I was trying to make working with the halo data easier. In this notebook, there are functions to map particles to halos, track the particles that were initially in a halo through the simulation (not using Rockstar's halo catalogs after the initial halos found before reheating), plotting the particle spreads (radius wrt to center of mass) in a halo through reheating, tracking the fraction of particles in halos, tracking unbound particles in phase space, computing velocity dispersions and comparing the trajectories to the universe's expansion (to assess particle free-streaming property), and more.





## Background Energy Density Solutions & Overdensity Parameter Numerical Estimations
Inside the folder creatively named **background densities & overdensity parameter estimation**, I calculate background energy density solutions and estimate the overdensity parameter \Delta(z).

**EMDE_bkgdensities_overdensityparam.ipynb**:
* This notebook contains my code for calculating the energy density solution for an EMDE cosmology from the energy continuity differential equations (as described in the paper Barenboim et al 2021), then plotting the solutions. After that, using the density solutions, I do a spherical top-hat analysis using the EMDE background cosmology but assuming constant mass for the actual tophat density. The calculations are based off those in the _Galaxy Formation and Evolution_ textbook by Houjun Mo, Frank van den Bosch, and Simon White. From this estimate a solution for the overdensity parameter as a function of redshift z and plot it. I also plot the overdensity parameter approximations derived by Bryan & Norman (1998) as a comparison.


**matter+curvature_overdensityparam.ipynb**:
* This notebook is the exact same thing as the **EMDE_bkgdensities_overdensityparam.ipynb** notebook, except instead of a DCDM background cosmology, I use a matter + curvature background cosmology and compare it to the same Bryan & Norman 1998 formula as a check on my calculation method.



## Miscellaneous: CONCEPT density parameter plots
I included my Jupyter notebook **concept_simulation_densityplots.ipynb** where I extracted the background cosmology quantities & parameters (scale factor, matter & radiation density parameters, etc) from my CONCEPT simulation and plotted them, as an example of using/working with them. Getting these values requires using the CONCEPT class utility to produce a class_processed.hdf5 file, as explained here in the CONCEPT docs: https://jmd-dk.github.io/concept/utilities/class.html




## Credits, Citations, & Code Used:
* CONCEPT: Dakin, J., Hannestad, S., & Tram, T. 2022, MNRAS, 513, 991
* yt: Turk, M. J., Smith, B. D., Oishi, J. S., Skory, S., Skillman, S. W., Abel, T., & Norman, M. L. 2011, ApJS, 192, 9
* Rockstar-galaxies: Behroozi, P. S., Wechsler, R. H., & Wu, H.-Y. 2012, ApJ, 762, 109
* pygadgetreader: Thompson, R. 2014, Astrophysics Source Code Library, ascl:1411.001
* Jupyter: Kluyver, T., Ragan-Kelley, B., Pérez, F., Granger, B. E., Bussonnier, M., Frederic, J., et al. 2016, in Proc. 20th Int. Conf. on Electronic Publishing, 87
* Python 3.12
* Scipy
* NumPy
* Matplotlib
* pandas
* collections
* h5py
* _Galaxy Formation and Evolution_ textbook by Houjun Mo, Frank van den Bosch, and Simon White, published by the Cambridge University Press.
* Bryan, G. L., & Norman, M. L. 1998, ApJ, 495, 80
* Gabriela Barenboim et al JCAP12(2021)026
* I used ChatGPT to assist in documenting the code and improving its readability: OpenAI. (2023). ChatGPT
* others (this list of sources will be completed soon)

* This code was produced during research work under the advising of Professor Jessie Shelton at the University of Illinois Urbana-Champaign and in collaboration with Professor Joshua Foster at the University of Wisconsin-Madison.
