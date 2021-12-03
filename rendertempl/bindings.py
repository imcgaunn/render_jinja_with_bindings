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
    # TODO: actually load the bindings
    # NB: this seems like a pretty good use for `collections.ChainMap`
    # Help on class ChainMap in collections:
    # collections.ChainMap = class ChainMap(collections.abc.MutableMapping)
    #  |  collections.ChainMap(*maps)
    #  |
    #  |  A ChainMap groups multiple dicts (or other mappings) together
    #  |  to create a single, updateable view.
    #  |
    #  |  The underlying mappings are stored in a list.  That list is public and can
    #  |  be accessed or updated using the *maps* attribute.  There is no other
    #  |  state.
    #  |
    #  |  Lookups search the underlying mappings successively until a key is found.
    #  |  In contrast, writes, updates, and deletions only operate on the first
    #  |  mapping.

    # all one would have to do is call `load_bindings_from_file` on each file
    # in the directory in the proper order and add each of the resulting dictionaries
    # to a chainmap in the same order.
    return {}
