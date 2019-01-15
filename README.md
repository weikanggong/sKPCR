# sKPCR: A powerful and efficient multivariate approach for voxel-level connectome-wide association studies

**Python Code for:**

```
Weikang Gong. et al, A powerful and efficient multivariate approach for voxel-level connectome-wide association studies, NeuroImage (2018)
```

This is the first development version of sKPCR, bug report is wellcome!

**Requirement:**
1. System: Linux/Mac/Win;
2. Python 2.7 or 3.6 (Anaconda is recommended);
3. Python modules: copy, glob, numpy, scipy, matplotlib, nilearn, nibabel, joblib, multiprocessing, PyPDF2;


**Data structure and required files:**
1. fMRI data: Please put all your rfMRI data in a directory. The software will read data in alphabet order.
2. variable of interest file: One column. The file format should be either a ".txt" file or a ".npy" file, with each row representing a subject and column representing a variable.
3. covariates file: Multiple columns. The file format should be either a ".txt" file or a ".npy" file, with each row representing a subject and each column representing a variable.
4. mask_file: a binary mask (.nii.gz or .nii format) of your fMRI data;
5. Number of components to use: must be < your sample size (usually <100 is OK);
6. Number of permutations: > 1000 is recommended;
7. Number of cores: 
8. Output directory:

**How to use this package:**
1. All the source code is in the file: sKPCR_cpu.py
2. To run it in command line, please use the file: sKCPR_main.py; You can type: **python sKCPR_main.py** -h to see the help;
3. To run it in GUI, please use the file: sKPCR_gui.py; You can type: **python sKCPR_gui.py** to open the gui, the input should be the same as sKCPR_main.py. After enter all the things, press "run sKPCR interactively" or "run sKPCR in background" to perform the analysis.


**Question or report bug:**
Author: Weikang Gong
Email: weikang.gong@ndcn.ox.ac.uk; weikanggong@gmail.com



