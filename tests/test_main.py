import logging
import rendertempl.main as main
import rendertempl.render as render
import rendertempl.bindings as bindings
import pathlib
import pytest

logger = logging.getLogger(__name__)


def test_can_parse_commandline():
    options = main.parse_arguments(["-f", "wow.txt", "special.yml.j2"])
    assert options.file == pathlib.Path("wow.txt")
    assert options.template == pathlib.Path("special.yml.j2")


def test_can_print_help_when_asked():
    with pytest.raises(SystemExit):
        main.parse_arguments(["--help"])


def test_only_one_bindings_source_allowed():
    # die if both are specified
    with pytest.raises(SystemExit):
        main.parse_arguments(["-f", "wow.txt", "-d", "/tmp/wow", "template.j2"])
    # work if only one specified
    opts = main.parse_arguments(["-f", "wow.txt", "template.j2"])
    assert opts.file == pathlib.Path("wow.txt")
    opts = main.parse_arguments(["-d", "/tmp/wow", "template.j2"])
    assert opts.directory == pathlib.Path("/tmp/wow")


def test_load_and_render_complex_directory_bindings(bindings_dir, jinja_templates_dir):
    complex_bindings = bindings.load_from_directory(bindings_dir.joinpath("complex_dir_one"))
    boring_template_path = jinja_templates_dir.joinpath("interactive.j2")
    rendered = render.render_template(boring_template_path, **complex_bindings)
    logger.debug(rendered)
