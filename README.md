# Booster_T1

[![IsaacSim](https://img.shields.io/badge/IsaacSim-5.1.0-silver.svg)](https://docs.omniverse.nvidia.com/isaacsim/latest/overview.html)
[![Isaac Lab](https://img.shields.io/badge/IsaacLab-2.3.2-silver)](https://isaac-sim.github.io/IsaacLab)
[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://docs.python.org/3/whatsnew/3.11.html)
[![License](https://img.shields.io/badge/license-Apache2.0-yellow.svg)](https://opensource.org/license/apache-2-0)

## Overview

**Booster_T1** is a trimmed Isaac Lab extension for Booster T1 humanoid locomotion experiments. The project keeps the original Booster T1 velocity tasks from the original Isaac Lab extension and removes the unrelated robot/task registrations.

The Python module, installable distribution, and extension display name are all `Booster_T1`.

## Available Tasks

| Robot | Terrain | Task name |
|-------|---------|-----------|
| Booster T1 | Flat | `Isaac-Velocity-Flat-Booster-T1-v0` |
| Booster T1 | Rough | `Isaac-Velocity-Rough-Booster-T1-v0` |

You can confirm the registered tasks with:

```bash
python scripts/tools/list_envs.py
```

## Requirements

- Python 3.11
- Isaac Sim 5.1.0
- Isaac Lab 2.3.2
- A Python environment where Isaac Lab and Isaac Sim can be imported

Use the conda environment where Isaac Lab and Isaac Sim are installed.

## Installation

Install Isaac Lab first, then install this project in editable mode from the repository root without resolving extra dependencies:

```bash
python -m pip install --no-deps -e source/Booster_T1
```

If an older editable install is still present, reinstall cleanly:

```bash
python -m pip uninstall -y Booster_T1
python -m pip install --no-deps -e source/Booster_T1
```

The default package intentionally avoids installing transitive dependencies because Isaac Sim and Isaac Lab pin shared packages such as `click`, `typing_extensions`, `wrapt`, and `protobuf`. Install optional training stacks only when needed and verify they do not disturb the Isaac environment.

For cuSRL experiments, install `cusrl` separately in a compatible environment before running scripts under `scripts/reinforcement_learning/cusrl/`.

## RSL-RL Usage

Train the flat task:

```bash
python scripts/reinforcement_learning/rsl_rl/train.py --task=Isaac-Velocity-Flat-Booster-T1-v0 --headless
```

Train the rough task:

```bash
python scripts/reinforcement_learning/rsl_rl/train.py --task=Isaac-Velocity-Rough-Booster-T1-v0 --headless
```

Play a trained flat checkpoint:

```bash
python scripts/reinforcement_learning/rsl_rl/play.py --task=Isaac-Velocity-Flat-Booster-T1-v0 --checkpoint=logs/rsl_rl/booster_t1_flat/2026-07-04_00-26-31/model_1499.pt --num_envs=256
```

Play a trained rough checkpoint:

```bash
python scripts/reinforcement_learning/rsl_rl/play.py --task=Isaac-Velocity-Rough-Booster-T1-v0 --checkpoint=logs/rsl_rl/booster_t1_rough/2026-07-04_02-21-39/model_2999.pt --num_envs=256
```

Logs are written under:

```text
logs/rsl_rl/booster_t1_flat
logs/rsl_rl/booster_t1_rough
```

## Quick Environment Checks

Run a zero-action agent:

```bash
python scripts/tools/zero_agent.py --task=Isaac-Velocity-Flat-Booster-T1-v0 --headless
```

Run a random-action agent:

```bash
python scripts/tools/random_agent.py --task=Isaac-Velocity-Rough-Booster-T1-v0 --headless
```

## Project Layout

```text
source/Booster_T1/Booster_T1/assets/booster.py
source/Booster_T1/Booster_T1/tasks/booster_t1_velocity/
  __init__.py
  base_env_cfg.py
  flat_env_cfg.py
  rough_env_cfg.py
  rsl_rl_ppo_cfg.py
  cusrl_ppo_cfg.py
  mdp/
```

## Notes

- Keep using `import Booster_T1.tasks` in scripts; this is the Python module name.
- Use `Booster_T1` as the project/distribution name.
- Only the Booster T1 flat and rough velocity tasks should appear in the Isaac Lab task registry.

## Acknowledgements

This project is based on the original Isaac Lab extension by Ziqi Fan and the Isaac Lab project.
