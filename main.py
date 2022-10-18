from csv import DictReader
from jinja2 import Template

def render_config():

    csv_file = "vars.csv"
    j2_template = "template.jinja2"

    try:
        with open(csv_file) as vars:
            csv_data = DictReader(vars)
            for var_data in csv_data:
                with open(j2_template) as template_data:
                    config_data = template_data.read()
                config = Template(config_data)
                print("------------")
                print(config.render(var_data))
            print("------------")
    except FileNotFoundError:
        raise Exception("File not found")


if __name__ == '__main__':
    render_config()
