import logging
import pytest

from rich.logging import RichHandler
from pathlib import Path

logging.basicConfig(level=logging.DEBUG, handlers=[RichHandler()])
this_directory = Path(__file__).parent.absolute()


@pytest.fixture(scope="session")
def jinja_templates_dir():
    return this_directory.joinpath("jinja")
