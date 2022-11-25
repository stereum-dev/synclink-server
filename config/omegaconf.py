"""
Extends OmegaConf to get CLI arguments via argparse that are mergeable with an equal *structured* omegaconf DictConfig.
"""
from argparse import ArgumentParser
from typing import Dict, List
from omegaconf import DictConfig, OmegaConf
from copy import deepcopy

class OmegaConfArgparse(OmegaConf):

    @classmethod
    def _format_cli_args(
        cls,
        args_setup: Dict,
        parent: str = ""
    ) -> Dict:
        """
        Private method that formats an argparse setup dict to make it ready for flatten and dynamic calls of argparse.add_argument()
        """
        parent = parent.strip('-.')
        formated_args = {}
        for name, opts in args_setup.items():
            if len(opts)<1:
                continue
            if name[-1] == "-":
                sub = f"{parent}-{name}" if parent != "" else name
                formated_args[name] = cls._format_cli_args(args_setup[name],sub)
                continue
            formated_args[name] = {"xargs":{},"xkwargs":{}}
            for k, v in opts.items():
                if k == "args":
                    if parent != "":
                        for i in range(len(v)):
                            fix = f"--{parent}"
                            arg = v[i].strip("-")
                            v[i] = f"{fix}-{arg}"
                    formated_args[name]["xargs"] = v
                elif k == "dest" and parent != "":
                        fix = parent.replace('-','.')
                        formated_args[name]["xkwargs"][k] = f"{fix}.{v}"
                else:
                    formated_args[name]["xkwargs"][k] = v
        return formated_args

    @classmethod
    def _flatten_cli_args(
        cls,
        formated_args: Dict,
        _result: List = [],
    ) -> Dict:
        """
        Private method that flattens an already formated argparse setup dict.
        """
        for name, opts in formated_args.items():
            if name[-1] == "-":
                _result = cls._flatten_cli_args(formated_args[name],_result)
            else:
                for k, v in opts.items():
                    if 'dest' in v:
                        key = f"--{v['dest']}"
                        _result.append({
                            key.replace(".","-"):{
                                'xargs': opts['xargs'],
                                'xkwargs': opts['xkwargs'],
                            }
                        })
        return _result

    @classmethod
    def _adjust_cli_args(
        cls,
        formated_args: Dict,
        parsed_args: Dict,
    ) -> Dict:
        """
        Private method that adjusts parsed argparse CLI arguments dict to make it mergeable with omegaconf DictConfig object.
        """
        result = {}
        for k, v in formated_args.items():
            if k[-1] == "-":
                result[k.strip('-')] = cls._adjust_cli_args(v,parsed_args)
            if "xkwargs" in v:
                if v['xkwargs']['dest'] in parsed_args:
                    result[k.strip('-')] = parsed_args[v['xkwargs']['dest']]
        return result

    @classmethod
    def from_argparse(
        cls,
        args_setup: Dict,
    ) -> DictConfig:
        """
        Public method that takes an argparse setup dict and returns an omegaconf DictConfig that is mergeable with an
        equal *structured* omegaconf DictConfig.
        Note that the argparse setup dict must match the *structured* omegaconf DictConfig in structure & typing.
        Otherwise either the merge will fail or the CLI will return errors for the given user input.
        Also, argparse setup dict must not use "default" keys (they will simply ignored). Instead specify the default
        value of the specific argument in the structued omegaconf DictConfig.
        """
        remove_keys_with_defaults = []
        parser = ArgumentParser()
        formated_args = cls._format_cli_args(deepcopy(args_setup))
        for i in cls._flatten_cli_args(formated_args):
            for k, v in i.items():
                if "default" in v["xkwargs"]:
                    v['xkwargs']["default"] = ''
                    if v['xkwargs']["type"] == int:
                        v['xkwargs']["default"] = "0"
                    if "action" in v['xkwargs'] and v['xkwargs']["action"].lower().strip() == "append":
                        v['xkwargs']["default"] = []
                parser.add_argument(*v["xargs"],**v["xkwargs"])
        parsed_args = vars(parser.parse_args())
        parsed_args = {k: v for k, v in parsed_args.items() if v}
        return OmegaConf.create(cls._adjust_cli_args(formated_args,parsed_args))