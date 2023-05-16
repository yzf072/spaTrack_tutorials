
# Introduction

Trajectory inference (TI) provides important insights into cell development and biological process. However,there is still much work to be done in developing a methodology that can fully leverage the potent capabilities of spatial transcriptomics (ST), which integrates both transcriptomic profiles and spatial locations to organize the spatiotemporal order of cells. 


We introduce an efficient method, spaTrack, for constructing cell trajectories that are both fast and lightweight using an optimal-transport (OT) matrix with single-cell resolution. This method sensitively considers both the profile of gene expression and the distance cost of cell transitions in a spatial context. With this approach, spaTrack can facilitate trajectory inference in a single section of spatial transcriptomics with fine local details, as well as enable the construction of cell dynamics across multiple tissue sections in a time series.

To capture potential dynamic drivers, spaTrack models the fate of a cell as a function of its expression profile along the time points driven by transcription factors. By enabling the study of cell kinetics from single cell spatial transcriptomics, spaTrack can reveal fine spatial trajectories and driven factors in one or across samples, providing new insights into the study of cell developmental problems across a wide area.

# Highlighted features:

**spaTrack could**

1. Reconstruct fine-spatial trajectories without the limitation of global topology. 

2. Integrate the spatial transition matrix of multiple samples to generate complete trajectories.

3. Trace cell trajectories across tissue sections through direct mapping among samples without data integration. 

4. Screen genes associated with trajectory to study the regulation of cell development. 

5. Capture driven factors of dynamics by modeling the fate of a cell as a function of its expression profile along the time points driven by transcription factors.

# Advantages:

1. The algorithm builds upon OT by incorporating both gene expression profiles and cell location information from ST data, the spatial distance could be naturally transferred into a cost function of the OT problem. 

2.  Most single cell TI methods don’t achieve true single cell resolution, but rather average or optimize cell clusters. In contrast, spaTrack fully captures the cell-to-cell transition matrix and predicts local developmental routes without the limitation of a global lineage topology. 

3. spaTrack facilitates the tracing of cell trajectories across multiple sections and vividly depicts the transition process. 

4. spaTrack can be applied extensively to both scRNA-seq data and ST data.

5. spaTrack requires lower computing memory and computing power than methods based on RNA-splicing velocity, making it a fast and effective option for TI study in ST or scRNA-seq data.

# Installation

```shell
pip install spaTrack
```

# Turorial:

We provide the following five tutorials as reference cases to illustrate the application of spaTrack in inferring cell trajectories on ST data of single slices with a single starting point and multiple starting points, as well as ST data of multiple time slices, and scRNA-seq data.

[01. Apply spaTrack to infer a trajectory on spatial transcriptomic data from axolotl brain regeneration after injury.](https://spatrack-tutorials.readthedocs.io/en/latest/notebooks/01.ST_data_of_axolotl_brain_regeneration_after_injury.html).

[02. Apply spaTrack to infer a trajectory on spatial transcriptomic data from 
 Intrahepatic cholangiocarcinoma cancer with multiple starting points.](https://spatrack-tutorials.readthedocs.io/en/latest/notebooks/02.ST_data_of_Intrahepatic_cholangiocarcinoma_cancer.html)

[03. Apply spaTrack to infer a trajectory on spatial transcriptomic data from multiple time slices of axolotl brain regeneration.](https://spatrack-tutorials.readthedocs.io/en/latest/notebooks/03.ST_data_of_axolotl_brain_slides_with_multiple_times.html)

[04. Apply spaTrack to infer cell transitions across multiple time points in spatial transcriptomic data from the mouse midbrain.](https://spatrack-tutorials.readthedocs.io/en/latest/notebooks/04.ST_data_of_mouse%20midbrain_with_multiple_times.html)

[05. Apply spaTrack to infer cell  trajectory in  scRNA-seq data from 
 hematopoietic stem cells development with multiple directions.]











