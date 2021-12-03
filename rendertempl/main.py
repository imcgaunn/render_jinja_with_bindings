import argparse
import logging
import rich
import sys

import rendertempl.bindings as bindings
import rendertempl.render as render

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


def main():
    options = parse_arguments(sys.argv[1:])
    logger.info(f"parsed options: [{options}]")
    rendered_template = ""
    if options.directory:
        logger.debug(
            f"rendering template {options.template} with bindings files from {options.directory}"
        )
        rendered_template = render.render_template(
            options.template, **bindings.load_from_directory(options.directory)
        )
    elif options.file:
        logger.debug(
            f"rendering template {options.template} with bindings from file {options.file}"
        )
        rendered_template = render.render_template(
            options.template, **bindings.load_from_file(options.file)
        )
    else:
        rich.print(
            "i don't know what to do because neither a directory or file with bindings was specified"
        )
        sys.exit(42)

    rich.print(rendered_template)
    sys.exit(0)
