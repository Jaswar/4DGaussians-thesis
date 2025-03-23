
ModelHiddenParams = dict(
    kplanes_config = {
     'grid_dimensions': 2,
     'input_coordinate_dim': 4,
     'output_coordinate_dim': 32,
     'resolution': [64, 64, 64, 100]
    },
    multires = [1, 2],
    defor_depth = 0,
    net_width = 64,
    plane_tv_weight = 0.0001,
    time_smoothness_weight = 0.01,
    l1_time_planes = 0.0001,
    no_do=True,
    no_dshs=False,
    no_ds=True,
    render_process=True
)
OptimizationParams = dict(
    iterations = 14000,
    batch_size = 1,
    coarse_iterations = 3000,
    densify_until_iter = 15000,
    opacity_reset_interval = 3000000,
    grid_lr_init = 0.0016,
    grid_lr_final = 0.00016,
    opacity_threshold_coarse = 0.005,
    opacity_threshold_fine_init = 0.005,
    opacity_threshold_fine_after = 0.005,
    pruning_interval = 8000,
    deformation_lr_init = 0.00016,
    deformation_lr_final = 1.6e-05,
    deformation_lr_delay_mult = 0.01
)
