from jinja2 import Environment

jinja_env = Environment()  # [...]
jinja_env.filters['quoted'] = quoted
jinja_env.filters['to_groovy_list'] = to_groovy_list


def quoted(text):
    return "'{}'".format(text)


def to_groovy_list(list):
    return '[{}]'.format(', '.join(map(quoted, list)))


#
# decorator
#

def custom_filter(func):
    jinja_env.filters[func.__name__] = func


@custom_filter
def quoted(text):
    return "'{}'".format(text)


@custom_filter
def to_groovy_list(list):
    return '[{}]'.format(', '.join(map(quoted, list)))


#
#
#

query-nexus.py \
--nexus-url 'https://nexus.local' \
--repo 'maven-releases' \
--group 'com.company.ms' \
--artifact 'my-api' \
--version '1.0.8'

#
#
#

parser = argparse.ArgumentParser('Get Swagger URL')
parser.add_argument('--nexus-url', nargs='?', default='…', help='…')
parser.add_argument('--repo', nargs='?', default='…', help='…')
parser.add_argument('--group', nargs='?', default='…', help='…')
parser.add_argument('--artifact', nargs='?', help='…')
parser.add_argument('--version', nargs='?', help='…')
parser.add_argument('--debug', action='store_true')
args = parser.parse_args()

#
#
#

@click_command
@click.option('--nexus-url', '-n', default='…', help='…')
@click.option('--repo', '-r', default='…', help='…')
@click.option('--group', '-g', default='…', help='…')
@click.option('--artifact', '-a', default='…', help='…')
@click.option('--version', '-v', default='…', help='…')
@click.option('--debug', '-d', default='…', help='…')
def retrieve_swagger_url(nexus_url, repo, group, artefact, version, debug):
    pass
