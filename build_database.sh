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



genomeDir=Danio_rerio.GRCz11.dna.ens97.STAR_2.7.1a
genomeFastaFiles=dre/Danio_rerio.GRCz11.dna.chromosome.*.fa
sjdbGTFfile=Danio_rerio.GRCz11.97.gtf

mkdir -p $genomeDir



/usr/bin/time -v STAR --runThreadN 7 --runMode genomeGenerate \
    --genomeDir $genomeDir \
    --genomeFastaFiles $genomeFastaFiles \
    --sjdbGTFfile $sjdbGTFfile
