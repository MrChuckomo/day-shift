# day-shift

Small `python` script to do your day shift 👇⌨️

Run this script to keep your PC awake!

# Usage

```bash
$ python dayshift.py
```

Interrupt using `ctrl` + `c`

# Python environment 

## Setup using `conda`

```bash
# List you python envs
$ conda info --envs
$ conda env list

# Create new python envs
$ conda env create --prefix ./ops/pyenv/dayshift_env --file environment.yml
$ conda env create --prefix ./ops/pyenv/dayshift_env --file requirements.txt

# Init you shell to use conda activate
$ conda init
$ conda init zsh

# Activate your new created python env
$ conda activate ./ops/pyenv/dayshift_env
```

# Research 

- [Conda manage environments](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#specifying-a-location-for-an-environment)
- [Add channel to conda env](https://stackoverflow.com/questions/40616381/can-i-add-a-channel-to-a-specific-conda-environment#41816116)
- [`keyboard` package pypi](https://pypi.org/project/keyboard/)
- [`keyboard` package GitHub](https://github.com/boppreh/keyboard)
- [Gooey](https://github.com/chriskiehl/Gooey)
