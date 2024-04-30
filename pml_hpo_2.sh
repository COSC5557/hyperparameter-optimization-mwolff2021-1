#!/bin/bash
#SBATCH --account=arcc-students
##SBATCH --job-name autosklearn_fail
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=mwolff3@uwyo.edu
#SBATCH --time=0-05:10:00
#SBATCH --partition=teton-gpu
#SBATCH --mem=32GB
module load miniconda3
conda activate hpo_env
python3 -c "import sklearn;"
python3 /home/mwolff3/pml_hpo_2.py > pml_hpo_3.txt
