import logging

import rich
import rendertempl.render as render

logger = logging.getLogger(__name__)


def test_can_render_template_with_values(jinja_templates_dir):
    templ_path = jinja_templates_dir.joinpath("trivial.yml.j2")
    realized = render.render_template(
        templ_path, wonderful_key="great_key", wonderful_val="great_val"
    )
    rich.print(realized)
