# Copyright (c) 2024-2026 Ziqi Fan
# SPDX-License-Identifier: Apache-2.0

import gymnasium as gym


gym.register(
    id="Isaac-Velocity-Flat-Booster-T1-v0",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.flat_env_cfg:BoosterT1FlatEnvCfg",
        "rsl_rl_cfg_entry_point": f"{__name__}.agents.rsl_rl_ppo_cfg:BoosterT1FlatPPORunnerCfg",
        "cusrl_cfg_entry_point": f"{__name__}.agents.cusrl_ppo_cfg:BoosterT1FlatTrainerCfg",
    },
)

gym.register(
    id="Isaac-Velocity-Rough-Booster-T1-v0",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.rough_env_cfg:BoosterT1RoughEnvCfg",
        "rsl_rl_cfg_entry_point": f"{__name__}.agents.rsl_rl_ppo_cfg:BoosterT1RoughPPORunnerCfg",
        "cusrl_cfg_entry_point": f"{__name__}.agents.cusrl_ppo_cfg:BoosterT1RoughTrainerCfg",
    },
)