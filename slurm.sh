#!/bin/bash

#SBATCH --job-name=testarray
#SBATCH --partition=ziz-small
#SBATCH --cpus-per-task=1
#SBATCH --time=00-00:10:00
#SBATCH --mem=2G
#SBATCH --ntasks=1

#SBATCH --array=0-2%2

# For job arrays we need to use "slurm-%A-%a" pattern.
#SBATCH --output=/tmp/slurm-%A_%a.out
#SBATCH --error=/tmp/slurm-%A_%a.out

export PATH_TO_CONDA="/data/localhost/not-backed-up/$USER/utils/miniconda3"
source $PATH_TO_CONDA/bin/activate var_fil

export LOCAL_LOGDIR="/data/localhost/not-backed-up/$USER/logs/misc"
mkdir -p $LOCAL_LOGDIR
mkdir -p $LOCAL_LOGDIR/slurm

export CENTRAL_LOGDIR="/data/ziz/not-backed-up/$USER/logs/misc"
mkdir -p $CENTRAL_LOGDIR

python -u /data/ziz/campbell/misc/testslurmarrayhydra/callingscript.py ${SLURM_ARRAY_TASK_ID}

echo "Job ${SLURM_ARRAY_TASK_ID} completed."

cp /tmp/slurm-${SLURM_ARRAY_JOB_ID}_${SLURM_ARRAY_TASK_ID}.out ${LOCAL_LOGDIR}/slurm/.
rsync -r ${LOCAL_LOGDIR}/* ${CENTRAL_LOGDIR}/.