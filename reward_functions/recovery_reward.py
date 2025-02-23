def recovery_reward(
    env: WarehouseBrawl
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
    reward = 0

    player_recovering = (
        opponent.body.velocity.x < 0 and opponent.body.position.x > 0 or 
        opponent.body.velocity.x > 0 and opponent.body.position.x < 0 or
        opponent.body.velocity.y < 0 and opponent.body.position.y > 0 or 
        opponent.body.velocity.y > 0 and opponent.body.position.y < 0
    )

    if isinstance(player.state, InAirState) and  player_recovering:
        reward += 1
    
    return reward * env.dt
