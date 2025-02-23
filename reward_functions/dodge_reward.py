def dodge_reward(
    env: WarehouseBrawl,
    desired_state: Type[PlayerObjectState]=BackDashState,
) -> float:
    """
    A function to promote dodges, but penalize it for lasting too long.
    """
    # Get player object from the environment
    player: Player = env.objects["player"]
    opponent: Player = env.objects["opponent"]
    reward = 0

    if isinstance(player.state, DodgeState) and isinstance(opponent.state, AttackState):
        reward += 1
        
    return reward * env.dt