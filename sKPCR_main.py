
# Script name: sKCPR_main.py
#
# Description: Functions to run sKPCR analysis using CPU
#
# Author: Weikang Gong
#
#Gong, Weikang, et al. "A powerful and efficient multivariate approach for voxel-level connectome-wide association studies." NeuroImage (2018).
#
# Weikang Gong
# DPhil Student, WIN, FMRIB
# Nuffield Department of Clinical Neurosciences
# University of Oxford
# Oxford OX3 9DU, UK
# Email: weikang.gong@ndcn.ox.ac.uk or weikanggong@gmail.com
#
# Copyright 2018 University of Oxford
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#



import argparse
import sys
import os


def cli_parser():
    # Create a parser. It'll print the description on the screen.
    parser = argparse.ArgumentParser(description=__doc__)
    # Add a positional argument
    parser.add_argument('-toolbox_dir', help='The absolute directory of the sKPCR toolbox')
    parser.add_argument('-image_dir', help='The absolute directory of the rsfMRI images')
    parser.add_argument('-output_dir', help='The absolute directory for the sKPCR outputs')
    parser.add_argument('-mask_file', help='The absolute directory of the mask file')
    parser.add_argument('-target_file', help='The absolute directory of the variable of interests (nsub * 1 numpy matrix saved in .npy or .txt format)')
    parser.add_argument('-cov_file', help='The absolute directory of the variable of interests (nsub * p numpy matrix saved in .npy or .txt format)')
    parser.add_argument('-K_components', help='The number of components for analysis.',default='20')
    parser.add_argument('-nperm', help='The number of permutations',default='2000')
    parser.add_argument('-ncore', help='Number of CPU to use for this analysis ',default='1')
    
    return parser

parser = cli_parser()
args = parser.parse_args()

toolbox_dir=os.path.join(args.toolbox_dir,'')
output_dir=os.path.join(args.output_dir,'')
print('Result Directory = '+output_dir)
image_dir=os.path.join(args.image_dir,'')
mask_file=args.mask_file
target_file=args.target_file
cov_file=args.cov_file
K_components=int(args.K_components)
print('Number of components = '+str(K_components))
nperm=int(args.nperm)
print('Number of permutations = '+str(nperm))
ncore=int(args.ncore)
print('Number of cores = '+str(ncore))

sys.path.append(os.path.join(os.path.abspath(toolbox_dir)))

from sKPCR_cpu import sKPCR_run_full_analysis


sKPCR_run_full_analysis(output_dir,image_dir,mask_file,
                       toolbox_dir,target_file,cov_file,
                       K_components,nperm,ncore)






