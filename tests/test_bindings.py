import logging
import rendertempl.bindings as bindings

logger = logging.getLogger(__name__)


def test_can_load_bindings_from_file(bindings_dir):
    bindings_path = bindings_dir.joinpath("single_file.yml")
    variable_map = bindings.load_from_file(bindings_path)
    assert variable_map['test_key'] == 'abcdefg'


def test_can_load_directory_of_files(bindings_dir):
    bindings_path = bindings_dir.joinpath("easy_dir_one")
    variable_map = bindings.load_from_directory(bindings_path)
    # files loaded later should have higher precedence
    assert variable_map["override_me"] == 'third_val'
