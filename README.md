# sKPCR: A powerful and efficient multivariate approach for voxel-level connectome-wide association studies (v0.1-beta)

Latest update: 2019-04-01

## **Python Code for:**

```
Weikang Gong. et al, A powerful and efficient multivariate approach for voxel-level connectome-wide association studies, NeuroImage (2018)
```

This is the first development version of sKPCR, bug report is wellcome!

## **Requirement:**
1. System: Linux/Mac/Windows.
2. Python 2.7 or 3.6 (Anaconda is recommended).
3. Python modules: copy, glob, numpy, scipy, matplotlib, nilearn, nibabel, joblib, multiprocessing, PyPDF2.
4. Your CPU memory should be enough to put all your rfMRI data into it.

## **Data structure and required files:**
1. **Toolbox directory:** The absolute directory of the sKPCR code.

2. **fMRI data:** Please put all your preprocessed rfMRI data in a directory (.nii.gz or nii format). The software will read data in alphabetical order according to the names of your rfMRI data.

3. **Variable of interest file:** One column. The file format should be either a ".txt" file or a ".npy" file, with each row representing a subject and column representing a variable. The number of rows should be the same as the number of subjects, the order should be also in alphabetical order according to the names of your rfMRI data. (Note: we only support binary and continuous phenotypes, e.g. for case-control study, the labels of two groups are 0 and 1).

4. **Covariates file:** Multiple columns. The file format should be either a ".txt" file or a ".npy" file, with each row representing a subject and each column representing a variable. (Note: you can only include binary and continuous variables here, categorical variable should be transformed to dummy variables (multiple columns of 0 and 1)).

5. **Mask file:** a binary mask (.nii.gz or .nii format) of your fMRI data.

6. **Number of components:** must be < your sample size (usually <100 is OK).

7. **Number of permutations:** > 1000 is recommended.

8. **Number of cores:** usually the more the faster.

9. **Output directory:** the absolute directory to save all the outputs.

## **How to use this package:**
1. All the source code is in the file: sKPCR_cpu.py.
2. To run it in command line, please use the file: sKCPR_main.py; You can type: **python sKCPR_main.py -h** to see the help.
3. To run it in GUI, please use the file: sKPCR_gui.py; You can type: **python sKCPR_gui.py** to open the gui, the input should be the same as sKCPR_main.py. After enter all the things, press "run sKPCR interactively" or "run sKPCR in background" to perform the analysis (Do not forget to press the save button after you enter Number of components, Number of permutations and Number of cores).


## **Outputs:**

In the Output directory, 
1. sKPCR_Pval_map.nii.gz: the voxel-wise -log10(raw p-value) of the association statistic.
2. sKPCR_Pval_map_FDR0.05.nii.gz: the voxel-wise -log10(raw p-value) of the association statistic that pass the FDR corrected 0.05 threshold.
3. sKPCR_Pval_map_FDR0.01.nii.gz: the voxel-wise -log10(raw p-value) of the association statistic that pass the FDR corrected 0.01 threshold.

Tip: if you want to analyse another variable of interest using the same data, just copy the current result (.nii.gz files) to another place and replace the old "Variable of interest file" a new variable of interest, and rerun the analysis using exactly the same setting. The software will automatically omit the step of estimating PCs which are only computed from the image data.

## **Question or report bug:**

Author: Weikang Gong

Email: weikanggong@gmail.com.


You may also find BWAS is useful: https://github.com/weikanggong/BWAS.

