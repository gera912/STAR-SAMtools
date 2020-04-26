#!/bin/bash



#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --job-name=PS8
#SBATCH --output=slurm-%j-%x.out

#SBATCH --time=0-01:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=7

conda deactivate
conda deactivate
conda deactivate
conda deactivate
conda activate bgmp_py3


/usr/bin/time -v samtools -bh aligned_Danio_rerio.GRCz11Aligned.out.sam > aligned_Danio_rerio.GRCz11Aligned.out.bam
