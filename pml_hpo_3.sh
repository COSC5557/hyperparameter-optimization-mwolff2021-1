#!/bin/bash
#SBATCH --account=arcc-students
##SBATCH --job-name pml_hpo_3
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=mwolff3@uwyo.edu
#SBATCH --time=0-05:10:00
#SBATCH --partition=teton-gpu
#SBATCH --nodes=1 
#SBATCH --ntasks-per-node=16
#SBATCH --mem=256GB
python3 /home/mwolff3/untitled8.py > pml_hpo_4.txt
