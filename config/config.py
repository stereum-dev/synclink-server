"""
Initialization and validation of the hierarchical config files and CLI arguments.
"""
from os.path import exists as file_exists
from .omegaconf import OmegaConfArgparse as OmegaConf
from .definition import Config, cli_args

#
# DEV SETTINGS
#

# Use strict configuration?
# True = Abort if specified config files does not exist or invalid/unknon arguments are present
# False = Ignore none existing config files and unknown or invalid arguments and continue with default values instead
strict = True

#
# INIT
#

# Setup config schema with defaults
config = OmegaConf.structured(Config)
user_config_filepath = config['config']

# Setup user config (only if the file exists -> was created by the user)
if file_exists(user_config_filepath):
    try:
        config = OmegaConf.merge(config, OmegaConf.load(user_config_filepath))
        if config['config'] != user_config_filepath and (strict or file_exists(config['config'])):
            config = OmegaConf.merge(config, OmegaConf.load(config['config']))
            user_config_filepath = config['config']
    except Exception as e:
        if strict:
            raise Exception(e)
        pass

# Setup CLI config (the original omegaconf way - does not support dashed cli args)
# try:
#     config = OmegaConf.merge(config, OmegaConf.from_cli())
#     if config['config'] != user_config_filepath and (strict or file_exists(config['config'])):
#         config = OmegaConf.merge(config, OmegaConf.load(config['config']))
#         # config file was specified on CLI however at the end further CLI arguments must win
#         config = OmegaConf.merge(config, OmegaConf.from_cli())v[
# except Exception as e:
#     if strict:
#         raise Exception(e)
#     pass

# Setup CLI config via argparse (supports dashed CLI args, help and similar useful stuff)
try:
    from_cli = OmegaConf.from_argparse(cli_args)
    config = OmegaConf.merge(config, from_cli)
    if config['config'] != user_config_filepath and (strict or file_exists(config['config'])):
        config = OmegaConf.merge(config, OmegaConf.load(config['config']))
        # config file was specified on CLI however at the end further CLI arguments must win
        config = OmegaConf.merge(config, from_cli)
except Exception as e:
    if strict:
        raise Exception(e)
    pass

# Validate and resolve (but dont convert and keep as DictConfig)
OmegaConf.to_object(config)
OmegaConf.resolve(config)