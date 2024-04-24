#!/bin/bash
#SBATCH --account=arcc-students
##SBATCH --job-name pml_hpo
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=mwolff3@uwyo.edu
#SBATCH --time=0-15:00:00
#SBATCH --mem=32GB
#SBATCH --partition=teton-gpu
#SBATCH --gres=gpu:2
python3 /home/mwolff3/pml_hpo.py > pml_hpo_6.out

