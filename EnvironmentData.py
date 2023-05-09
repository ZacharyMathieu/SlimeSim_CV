import Constants


class EnvironmentData:
    display_pheromones: bool = Constants.DISPLAY_PHEROMONES
    display_slime: bool = Constants.DISPLAY_SLIME
    display_slime_size: int = Constants.DISPLAY_SLIME_SIZE
    display_slime_opacity: int = Constants.DISPLAY_SLIME_OPACITY
    display_slime_color: list[int] = Constants.DISPLAY_SLIME_COLOR
    display_highlight_pheromone_color: list[int] = Constants.DISPLAY_HIGHLIGHT_PHEROMONE_COLOR
    display_inactive_pheromone_color: list[int] = Constants.DISPLAY_INACTIVE_PHEROMONE_COLOR
    grid_width: int = Constants.GRID_WIDTH
    grid_height: int = Constants.GRID_HEIGHT
    loop_grid: bool = Constants.LOOP_GRID
    random_natural_pheromones_count: int = Constants.RANDOM_NATURAL_PHEROMONES_COUNT
    natural_pheromones_strength: int = Constants.NATURAL_PHEROMONES_STRENGTH
    slime_count: int = Constants.SLIME_COUNT
    slime_avoid_walls: bool = Constants.SLIME_AVOID_WALLS
    slime_speed: float = Constants.SLIME_SPEED
    slime_wall_detection_range: int = Constants.SLIME_WALL_DETECTION_RANGE
    slime_wall_turn_angle: float = Constants.SLIME_WALL_TURN_ANGLE
    slime_seek_pheromones: bool = Constants.SLIME_SEEK_PHEROMONES_PERIOD
    slime_seek_pheromones_period: int = Constants.SLIME_SEEK_PHEROMONES_PERIOD
    slime_pheromone_detection_range: int = Constants.SLIME_PHEROMONE_DETECTION_RANGE
    slime_pheromone_turn_angle: float = Constants.SLIME_PHEROMONE_TURN_ANGLE
    slime_pheromone_level: int = Constants.SLIME_PHEROMONE_LEVEL
    slime_ignore_self_pheromone: bool = Constants.SLIME_IGNORE_SELF_PHEROMONE
    slime_align_direction: bool = Constants.SLIME_ALIGN_DIRECTION
    slime_other_detection_range: int = Constants.SLIME_OTHER_DETECTION_RANGE
    slime_align_turn_angle: float = Constants.SLIME_ALIGN_TURN_ANGLE
    slime_random_rotation_chance: float = Constants.SLIME_RANDOM_ROTATION_CHANCE
    slime_random_rotation_angle: float = Constants.SLIME_RANDOM_ROTATION_ANGLE
    slime_bias_direction: bool = Constants.SLIME_BIAS_DIRECTION
    slime_bias_direction_x: int = Constants.SLIME_BIAS_DIRECTION_X
    slime_bias_direction_y: int = Constants.SLIME_BIAS_DIRECTION_Y
    slime_bias_rotation_angle: float = Constants.SLIME_BIAS_ROTATION_ANGLE
    pheromone_max_level: int = Constants.PHEROMONE_MAX_LEVEL
    pheromone_high_level_diffusion_multiplier: float = Constants.PHEROMONE_HIGH_LEVEL_DIFFUSION_MULTIPLIER
    pheromone_low_level_diffusion_multiplier: int = Constants.PHEROMONE_LOW_LEVEL_DIFFUSION_MULTIPLIER
    pheromone_diffusion_constant: int = Constants.PHEROMONE_DIFFUSION_CONSTANT
    pheromone_max_level_reset_value: int = Constants.PHEROMONE_MAX_LEVEL_RESET_VALUE
