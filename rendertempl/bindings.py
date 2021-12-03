import logging
from pathlib import Path
from typing import Dict, Any

logger = logging.getLogger(__name__)


class BadBindingsPathError(Exception):
    pass


def load_bindings_from_file(yaml_path: Path) -> Dict[Any, Any]:
    """ load bindings from a single .yml file """
    if not yaml_path.is_file():
        raise BadBindingsPathError(f"{yaml_path} is not a yaml file")
    return {}


def load_bindings_from_directory(dir_path: Path) -> Dict[Any, Any]:
    """ load bindings from a directory of .yml files in lexicographical precedence order """ 
    if not dir_path.is_dir():
        raise BadBindingsPathError(f"{dir_path} is not a directory and can't contain yaml files with bindings")
    return {}
