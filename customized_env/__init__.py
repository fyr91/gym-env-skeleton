from gym.envs.registration import register

register(
    id='customizd-env-v0',
    entry_point='customized_env.envs:CustomizedEnv',
)
register(
    id='customzied-extrahard-v0',
    entry_point='customized_extrahard_env.envs:CustomizedExtraHardEnv',
)
