import logging
import os
import yaml
from pathlib import Path
from typing import Dict, Any
from collections import ChainMap

logger = logging.getLogger(__name__)


class BadBindingsPathError(Exception):
    pass


def load_from_file(yaml_path: Path) -> Dict[Any, Any]:
    """load bindings from a single .yml file"""
    if not yaml_path.is_file():
        raise BadBindingsPathError(f"{yaml_path} is not a yaml file")
    with open(yaml_path) as f:
        return yaml.safe_load(f)


def load_from_directory(dir_path: Path) -> ChainMap[Any, Any]:
    """load bindings from a directory of .yml files in lexicographical precedence order"""
    if not dir_path.is_dir():
        raise BadBindingsPathError(
            f"{dir_path} is not a directory and can't contain yaml files with bindings"
        )
    entries = [dir_path.joinpath(p) for p in os.listdir(dir_path)]
    logger.debug(f"found the following entries in {dir_path}: [{entries}]")
    # latest entries should have highest precedence
    sorted_entries = reversed(sorted(entries))
    bindings_maps = [load_from_file(ep) for ep in sorted_entries]
    bindings_chainmap = ChainMap(*bindings_maps)
    return bindings_chainmap
