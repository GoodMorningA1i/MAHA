def vert_danger_zone_reward(
    env: WarehouseBrawl,
    zone_penalty: int = 1
) -> float:
    """
    Applies a penalty for every time frame player surpases a certain height threshold in the environment.

    Args:
        env (WarehouseBrawl): The game environment.
        zone_penalty (int): The penalty applied when the player is in the danger zone.
        zone_height (float): The height threshold defining the danger zone.

    Returns:
        float: The computed penalty as a tensor.
    """
    # Get player object from the environment
    player: Player = env.objects["player"]
    reward = 0

    stage_top = env.stage_height_tiles / 2
    stage_bottom = -env.stage_height_tiles / 2

    # Apply penalty if the player is in the danger zone
    if player.body.position.y >= (stage_top * 0.8) or player.body.position.y <= (stage_bottom * 0.8):
        reward -= zone_penalty

    return reward * env.dt

def hori_danger_zone_reward(
    env: WarehouseBrawl,
    zone_penalty: int = 1) -> float:
    """
    Applies a penalty for every time frame player surpases a certain height threshold in the environment.

    Args:
        env (WarehouseBrawl): The game environment.
        zone_penalty (int): The penalty applied when the player is in the danger zone.
        zone_height (float): The height threshold defining the danger zone.

    Returns:
        float: The computed penalty as a tensor.
    """
    # Get player object from the environment
    player: Player = env.objects["player"]
    reward = 0

    stage_right = env.stage_width_tiles / 2
    stage_left = -env.stage_width_tiles / 2

    # Apply penalty if the player is in the danger zone
    # Apply penalty if the player is in the danger zone
    if player.body.position.x >= (stage_right * 0.8) or player.body.position.x <= (stage_left * 0.8):
        reward -= zone_penalty

    return reward * env.dt
