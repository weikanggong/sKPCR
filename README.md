# sKPCR: A powerful and efficient multivariate approach for voxel-level connectome-wide association studies

## **Python Code for:**

```
Weikang Gong. et al, A powerful and efficient multivariate approach for voxel-level connectome-wide association studies, NeuroImage (2018)
```

This is the first development version of sKPCR, bug report is wellcome!

## **Requirement:**
1. System: Linux/Mac/Windows;
2. Python 2.7 or 3.6 (Anaconda is recommended);
3. Python modules: copy, glob, numpy, scipy, matplotlib, nilearn, nibabel, joblib, multiprocessing, PyPDF2;


## **Data structure and required files:**
1. Toolbox directory: The absolute directory of the sKPCR code;
2. fMRI data: Please put all your rfMRI data in a directory. The software will read data in alphabet order.
3. variable of interest file: One column. The file format should be either a ".txt" file or a ".npy" file, with each row representing a subject and column representing a variable.
4. covariates file: Multiple columns. The file format should be either a ".txt" file or a ".npy" file, with each row representing a subject and each column representing a variable.
5. mask_file: a binary mask (.nii.gz or .nii format) of your fMRI data;
6. Number of components to use: must be < your sample size (usually <100 is OK);
7. Number of permutations: > 1000 is recommended;
8. Number of cores: usually the more the faster;
9. Output directory: the absolute directory to save all the outputs.

## **How to use this package:**
1. All the source code is in the file: sKPCR_cpu.py
2. To run it in command line, please use the file: sKCPR_main.py; You can type: **python sKCPR_main.py -h** to see the help;
3. To run it in GUI, please use the file: sKPCR_gui.py; You can type: **python sKCPR_gui.py** to open the gui, the input should be the same as sKCPR_main.py. After enter all the things, press "run sKPCR interactively" or "run sKPCR in background" to perform the analysis.


## **Outputs:**

In the Output directory, 
1. sKPCR_Pval_map.nii.gz: the voxel-wise -log10(p-value) of the association statistic.
2. sKPCR_Pval_map_FDR0.05.nii.gz: the voxel-wise -log10(p-value) of the association statistic that pass the FDR corrected 0.05 threshold.
3. sKPCR_Pval_map_FDR0.01.nii.gz: the voxel-wise -log10(p-value) of the association statistic that pass the FDR corrected 0.01 threshold.

## **Question or report bug:**

Author: Weikang Gong (FMRIB Analysis group, NDCN, WIN, University of Oxford)

Email: weikang.gong@ndcn.ox.ac.uk; weikanggong@gmail.com


You may also find BWAS is useful: https://github.com/weikanggong/BWAS.

