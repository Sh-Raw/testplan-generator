import yaml
from jinja2 import Environment, FileSystemLoader

def render_template(template_path, values_path):
    # Load YAML data
    with open(values_path, 'r') as f:
        values = yaml.safe_load(f)

    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader('/'.join(template_path.split('/')[:-1]) or '.'))
    template_file = template_path.split('/')[-1]
    template = env.get_template(template_file)

    # Render template
    return template.render(values)
