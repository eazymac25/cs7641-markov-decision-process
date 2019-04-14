import gym
from gym.envs.registration import register

from .cliff_walking import *
from .frozen_lake import *

__all__ = ['RewardingFrozenLakeEnv', 'WindyCliffWalkingEnv']

register(
    id='RewardingFrozenLake-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '4x4'},
)

register(
    id='RewardingFrozenLake8x8-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '8x8'}
)

register(
    id='RewardingFrozenLakeNoRewards20x20-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '20x20', 'rewarding': False}
)

register(
    id='RewardingFrozenLakeWithRewards20x20-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '20x20', 'rewarding': True, 'is_slippery': False}
)

register(
    id='RewardingFrozenLakeNoRewards8x8-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '8x8', 'rewarding': False}
)

register(
    id='WindyCliffWalking-v0',
    entry_point='environments:WindyCliffWalkingEnv',
)

register(
    id='RewardingFrozenLakeWithRewards15x15-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '15x15', 'rewarding': True, 'is_slippery': False}
)

register(
    id='FrozenLakeWithoutRewardsAndIsSlippery15x15-v0',
    entry_point='environments:RewardingFrozenLakeEnv',
    kwargs={'map_name': '15x15', 'rewarding': True, 'is_slippery': True}
)


def get_rewarding_frozen_lake_environment():
    return gym.make('RewardingFrozenLake8x8-v0')


def get_frozen_lake_environment():
    return gym.make('FrozenLake-v0')


def get_rewarding_no_reward_frozen_lake_environment():
    return gym.make('RewardingFrozenLakeNoRewards8x8-v0')


def get_large_rewarding_no_reward_frozen_lake_environment():
    return gym.make('RewardingFrozenLakeNoRewards20x20-v0')


def get_cliff_walking_environment():
    return gym.make('CliffWalking-v0')


def get_windy_cliff_walking_environment():
    return gym.make('WindyCliffWalking-v0')


def get_rewarding_large_frozen_lake():
    return gym.make('RewardingFrozenLakeWithRewards20x20-v0')


def get_rewarding_medium_frozen_lake():
    return gym.make('RewardingFrozenLakeWithRewards15x15-v0')


def get_medium_frozen_lake_without_rewards_and_slippery():
    return gym.make('FrozenLakeWithoutRewardsAndIsSlippery15x15-v0')