def opponent_offstage_reward(
    env: WarehouseBrawl,
    zone_penalty: int = 1
) -> float:
    """
    A reward for keeping opponent off of the stage

    Args:
        env (WarehouseBrawl): The game environment.
        zone_penalty (int): The penalty applied when the player is in the danger zone.
    Returns:
        float: The computed penalty as a tensor.
    """
    # Get player object from the environment
    player: Player = env.objects["player"]
    opponent: Player = env.objects["opponent"]
    reward = 0

    if isinstance(opponent.state, InAirState):
        reward += zone_penalty / 10
        stage_right = env.stage_width_tiles / 2
        multiplier = 1

        if abs(opponent.body.position.x) > (0.8 * stage_right):
            multiplier *= 1.5
        
        multiplier *= abs(opponent.prev_x) / abs(opponent.body.position.x)

        reward = multiplier * (zone_penalty / 5)
    
    return reward * env.dt

def guard_reward(
    env: WarehouseBrawl,
    zone_penalty: int = 1
) -> float:
    """
    A reward for keeping opponent airborne

    Args:
        env (WarehouseBrawl): The game environment.
        zone_penalty (int): The penalty applied when the player is in the danger zone.
    Returns:
        float: The computed penalty as a tensor.
    """
    # Get player object from the environment
    player: Player = env.objects["player"]
    opponent: Player = env.objects["opponent"]
    reward = 0
    multiplier = 1

    opponent_recovering = (
        opponent.body.velocity.x < 0 and opponent.body.position.x > 0 or 
        opponent.body.velocity.x > 0 and opponent.body.position.x < 0 or
        opponent.body.velocity.y < 0 and opponent.body.position.y > 0 or 
        opponent.body.velocity.y > 0 and opponent.body.position.y < 0
    )

    if isinstance(player.state, AttackState) and opponent_recovering:
        multiplier *= 1.5
    
    if isinstance(player.state, InAirState):
        multiplier *= 0.8
    
    return reward * multiplier * env.dt
