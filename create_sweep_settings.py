import yaml

out = {}
out['name'] = 'CustomSweep'

grid = [
    ["theta_training.approx_decay", "0.99", "0.993", "0.999", "0.9993", "0.9999"],
    ['seed', "42", "43"],
    ['data.F_min_eigval', "0.5", "0"]
]

def recurse(grid, grid_idx, settings, output):
    if grid_idx == len(grid):
        output.append(settings)
    else:
        for i in range(1, len(grid[grid_idx])):
            settings[grid[grid_idx][0]] = grid[grid_idx][i]
            recurse(grid, grid_idx+1, settings.copy(), output)

grid_as_list = []
settings = {}
recurse(grid, 0, settings, grid_as_list)

for i, job in enumerate(grid_as_list):
    job_dict = {}
    for j, key in enumerate(job.keys()):
        job_dict[j] = {"LHS": key, "RHS": job[key]}
    out[i] = job_dict


with open('sweep_settings.yaml', 'w') as f:
    yaml.dump(out, f)