# XenoDiffusionScope

> R. Peres, Y. Biondi

Code for diffusion studies with Xenoscope, a 2.6m LXe TPC for DARWIN R&D. 
Initial drift and diffusion [code from Y. Biondi](https://github.com/YaniBion/Diffusion_Xenon).


## Installation

The package is not yet in PyPI and must be installed locally with:

```bash
git clone git@github.com:ricmperes/XenoDiffusionScope.git
cd XenoDiffusionScope
pip install .
```

For an editable version use ``pip install -e .`` .

For an introduction, start with the example notebooks under ``notebooks``. ``Main.ipynb`` gives a start-to-finish introduction of the package and its usability.


### TO DO

Expected improvements to come:
 - ~~Adding light response (SiPM array)~~ - DONE
      - ~~Grids and extraction~~
      - ~~Photon production~~
      - ~~Photon detection~~
 - Electron transverse and longitudinal diffusion in LXe parameter limits
 - Proper LCE? (G4)
 - Proper focusing? (GARFIELD, Kassiopeia)
