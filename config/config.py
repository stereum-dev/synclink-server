"""
Initialization and validation of the hierarchical config files and CLI arguments.
"""
from typing import Dict
from os.path import exists as file_exists
from .omegaconf import OmegaConfArgparse as OmegaConf, DictConfig
from .definition import Schema, cli_args
from os import environ
from sys import argv
import re

class Config():

    _schema: object
    _cli_args: Dict
    _strict: bool = True
    _config: DictConfig
    _user_config_filepath: str
    _initialized: bool = False

    @classmethod
    def init(
        cls,
        schema: object,
        cli_args: Dict = {},
        strict: bool = True
    ) -> DictConfig:
        cls._initialized = True
        cls._schema = schema
        cls._cli_args = cli_args
        cls._strict = strict
        cls._add_environment_variables()
        cls._setup_schema()
        cls._setup_user_config();
        #cls._setup_cli_config_omega();
        cls._setup_cli_config_argparse();
        cls._validate_and_resove();
        return cls._config

    @classmethod
    def _is_private(cls):
        if not cls._initialized: raise RuntimeError("invalid call on private method")

    @classmethod
    def _add_environment_variables(cls):
        cls._is_private()
        for k, v in environ.items():
            k =  k.upper()
            #if not k.startswith("SYLI_") or k == "SYLI_CONFIG": # all "SYLI_*" except config file
            if not k.startswith("SYLI_"): # all "SYLI_*"
                continue
            # support lists as environment variables, e.g.: SYLI_NODE_1, SYLI_NODE_2 -> --node val1 --node val2
            m = re.search(r'(.*)(_\d+)$', k)
            if m is not None:
                k=m.group(1)
            argv.append(f"--{k[5:].lower()}")
            if v != "":
                argv.append(v)

    @classmethod
    def _setup_schema(cls,lala="",lolo=""):
        cls._is_private()
        cls._config = OmegaConf.structured(cls._schema)
        cls._user_config_filepath = cls._config['config']

    @classmethod
    def _setup_user_config(cls):
        cls._is_private()
        if file_exists(cls._user_config_filepath):
            try:
                cls._config = OmegaConf.merge(cls._config, OmegaConf.load(cls._user_config_filepath))
                if cls._config['config'] != cls._user_config_filepath and (cls._strict or file_exists(cls._config['config'])):
                    cls._config = OmegaConf.merge(cls._config, OmegaConf.load(cls._config['config']))
                    cls._user_config_filepath = cls._config['config']
            except Exception as e:
                if cls._strict:
                    raise Exception(e)
                pass

    @classmethod
    def _setup_cli_config_omega(cls):
        cls._is_private()
        if file_exists(cls._user_config_filepath):
            try:
                cls._config = OmegaConf.merge(cls._config, OmegaConf.load(cls._user_config_filepath))
                if cls._config['config'] != cls._user_config_filepath and (cls._strict or file_exists(cls._config['config'])):
                    cls._config = OmegaConf.merge(cls._config, OmegaConf.load(cls._config['config']))
                    cls._user_config_filepath = cls._config['config']
            except Exception as e:
                if cls._strict:
                    raise Exception(e)
                pass

    @classmethod
    def _setup_cli_config_argparse(cls):
        cls._is_private()
        try:
            from_cli = OmegaConf.from_argparse(cls._cli_args)
            cls._config = OmegaConf.merge(cls._config, from_cli)
            if cls._config['config'] != cls._user_config_filepath and (cls._strict or file_exists(cls._config['config'])):
                cls._config = OmegaConf.merge(cls._config, OmegaConf.load(cls._config['config']))
                cls._config = OmegaConf.merge(cls._config, from_cli)
        except Exception as e:
            if cls._strict:
                raise Exception(e)
            pass

    @classmethod
    def _validate_and_resove(cls):
        cls._is_private()
        OmegaConf.to_object(cls._config)
        OmegaConf.resolve(cls._config)
        cls._initialized = False

config = Config.init(Schema,cli_args)