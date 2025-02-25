def recovery_reward(
    env: WarehouseBrawl,
    recover_weight: float = 0.6
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

    # Conditions to check if you need horizontal recover
    hori_danger = abs(player.body.position.x) >= 5.335

    hori_recover = (player.body.velocity.x < 0 and player.body.position.x > 0 or 
        player.body.velocity.x > 0 and player.body.position.x < 0)

    stage_top = env.stage_height_tiles / 2
    
    #Conditions to check for 
    vert_danger_below = player.body.position.y <= 2.03
    vert_recover_up = player.body.velocity.y > 0 and player.body.position.y < 0
    
    vert_danger_up = player.body.position.y > (0.8 * stage_top)
    vert_recover_down = player.body.velocity.y < 0 and player.body.position.y > 0

    if isinstance(player.state, InAirState):
        if hori_danger:
            if hori_recover:
                reward += recover_weight
            
            if vert_danger_below and vert_recover_up:
                reward += recover_weight
            
            if vert_danger_up and vert_recover_down:
                reward -= recover_weight
        elif vert_danger_up and vert_recover_down:
            reward += recover_weight

    return reward * env.dt
