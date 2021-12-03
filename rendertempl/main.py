import argparse
import logging
import sys
from rich.logging import RichHandler
from pathlib import Path

logging.basicConfig(level=logging.INFO, handlers=[RichHandler()])
logger = logging.getLogger(__name__)


def parse_arguments(args):
    parser = argparse.ArgumentParser(
        prog="rendertempl",
        description="render a jinja2 template with the specified variable bindings",
    )
    bindings_group = parser.add_mutually_exclusive_group()
    bindings_group.add_argument(
        "--file",
        "-f",
        type=Path,
        dest="file",
        default="vars.yml",
        required=False,
    )
    bindings_group.add_argument(
        "--directory",
        "-d",
        type=Path,
        dest="directory",
        required=False,
        help="an optional directory of yaml files containing bindings. The files will be concatenated in lexicographical order",
    )
    parser.add_argument(
        "template", metavar="tmpl", type=Path, help="the template to render"
    )

    logger.debug(f"parsing command line args: [{args}]")
    opts = parser.parse_args(args)
    return opts


def main(args):
    options = parse_arguments(args)
    logger.info(f"parsed options: [{options}]")
    sys.exit(0)
