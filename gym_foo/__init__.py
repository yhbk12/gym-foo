
from gym.envs.registration import register


register(
    id="wikinav-v12",
    entry_point="gym_foo.envs:EmbeddingWikiNavEnv",
    timestep_limit=50)
