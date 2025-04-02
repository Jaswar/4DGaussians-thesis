import os
import random
import time
import argparse


TEMPLATE_CONFIG = '''
ModelHiddenParams = dict(
    kplanes_config = {
     'grid_dimensions': <grid_dimensions>,
     'input_coordinate_dim': <input_coordinate_dim>,
     'output_coordinate_dim': <output_coordinate_dim>,
     'resolution': <resolution>
    },
    multires = <multires>,
    defor_depth = <defor_depth>,
    net_width = <net_width>,
    plane_tv_weight = <plane_tv_weight>,
    time_smoothness_weight = <time_smoothness_weight>,
    l1_time_planes = <l1_time_planes>,
    no_do=<no_do>,
    no_dshs=<no_dshs>,
    no_ds=<no_ds>,
    render_process=True
)
OptimizationParams = dict(
    iterations = <iterations>,
    batch_size = <batch_size>,
    coarse_iterations = <coarse_iterations>,
    densify_until_iter = <densify_until_iter>,
    opacity_reset_interval = <opacity_reset_interval>,
    grid_lr_init = <grid_lr_init>,
    grid_lr_final = <grid_lr_final>,
    opacity_threshold_coarse = <opacity_threshold_coarse>,
    opacity_threshold_fine_init = <opacity_threshold_fine_init>,
    opacity_threshold_fine_after = <opacity_threshold_fine_after>,
    pruning_interval = <pruning_interval>,
    deformation_lr_init = <deformation_lr_init>,
    deformation_lr_final = <deformation_lr_final>,
    deformation_lr_delay_mult = <deformation_lr_delay_mult>
)
'''

SAMPLING_SETTINGS = {
    'grid_dimensions': [2],
    'input_coordinate_dim': [4],
    'output_coordinate_dim': [16, 32],
    'resolution': [[64, 64, 64, 250], [64, 64, 64, 150], [64, 64, 64, 100], [64, 64, 64, 80], 
                   [64, 64, 64, 75], [64, 64, 64, 50], [64, 64, 64, 25]],
    'multires': [[1,2,4], [1,2]],
    'defor_depth': [1, 0],
    'net_width': [128, 64],
    'plane_tv_weight': [0.0002, 0.0001],
    'time_smoothness_weight': [0.001, 0.01],
    'l1_time_planes': [0.0001],
    'no_do': [True, False],
    'no_dshs': [True, False],
    'no_ds': [True, False],

    'iterations': [14_000, 15_000, 20_000],
    'batch_size': [1, 2],
    'coarse_iterations': [3000],
    'densify_until_iter': [10_000, 15_000],
    'opacity_reset_interval': [3000, 3000000],
    'grid_lr_init': [0.0016],
    'grid_lr_final': [0.00016, 0.000016],
    'opacity_threshold_coarse': [0.005],
    'opacity_threshold_fine_init': [0.005],
    'opacity_threshold_fine_after': [0.005],
    'pruning_interval': [100, 8000],
    'deformation_lr_init': [0.00016],
    'deformation_lr_final': [0.000016, 0.0000016],
    'deformation_lr_delay_mult': [0.01]
}


def sample_config():
    config = {}
    for key, values in SAMPLING_SETTINGS.items():
        config[key] = random.choice(values)
    return config


def write_config(config, path):
    new_config = TEMPLATE_CONFIG
    for key, value in config.items():
        new_config = new_config.replace(f'<{key}>', str(value))
    with open(path, 'w') as f:
        f.write(new_config)


def execute_in_env(command, env):
    os.system(f'/bin/bash -c \"source /opt/miniconda3/etc/profile.d/conda.sh && conda activate {env} && {command} \"')

def run_experiment(data_path, model_path, config_path):
    os.makedirs(model_path, exist_ok=True)
    execute_in_env(f'python train.py -s \"{data_path}\" ' \
                   f'--port 6017 --expname \"{model_path}\" ' \
                   f'--configs \"{config_path}\"', 'Gaussians4D')

def main(data_path, model_path, timeout=5 * 60 * 60):
    configs_path = './arguments/ego_exo/random_configs'
    os.makedirs(configs_path, exist_ok=True)
    start_time = time.time()
    config_index = 0
    while time.time() - start_time < timeout:
        config = sample_config()
        config_path = os.path.join(configs_path, f'config_{config_index}.py')
        model_path_ = os.path.join(model_path, f'model_{config_index}')
        write_config(config, config_path)
        run_experiment(data_path, model_path_, config_path)
        config_index += 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', type=str)
    parser.add_argument('--model_path', type=str)
    args = parser.parse_args()
    data_path = args.data_path
    model_path = args.model_path
    main(data_path, model_path)