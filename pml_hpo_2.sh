#!/bin/bash
#SBATCH --account=arcc-students
##SBATCH --job-name autosklearn_fail
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=mwolff3@uwyo.edu
#SBATCH --time=0-2:00:00
#SBATCH --partition=teton-gpu
#SBATCH --nodes=4 
#SBATCH --ntasks-per-node=16
#SBATCH --mem=64GB
module load miniconda3
conda activate hpo_env
python3 /home/mwolff3/pml_hpo_2.py > pml_hpo_1_iter.txt
