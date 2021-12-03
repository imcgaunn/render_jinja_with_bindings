import logging
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

logger = logging.getLogger(__name__)


class BadTemplatePathError(Exception):
    pass


def render_template(template_path: Path, **bindings):
    """ given a set of bindings passed as keyword arguments, render the jinja template
    at the filesystem path identified by :template_path: """
    # instantiate a FileSystemLoader at the parent directory of template
    # load template by basename from FileSystemLoader
    if not(template_path.parent.is_dir()):
        raise BadTemplatePathError(f"{template_path} does not appear to be a valid path")

    template_parent_dir = template_path.parent
    env = Environment(loader=FileSystemLoader(template_parent_dir))
    templ = env.get_template(template_path.name)
    rendered = templ.render(**bindings)
    return rendered
