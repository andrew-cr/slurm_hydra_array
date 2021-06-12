import subprocess
import yaml
import argparse

print("In calling script")

parser = argparse.ArgumentParser()
parser.add_argument('slurm_array_task_id', type=int)
args, unknown_args = parser.parse_known_args()

with open('sweep_settings.yaml') as f:
    settings = yaml.safe_load(f)

p = subprocess.Popen(
    [
        "python", "myscript.py", "myparam={}".format(
            settings[args.slurm_array_task_id]['myparam']
        )
    ])
p.wait()