import click
from schemas.config_file import ConfigFile


@click.group()
def cli():
    pass

@cli.command()
@click.option('--filename')
def configure(filename):
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo('Hello %s!' % filename)
    service_name = click.prompt('What is your name?')
    click.echo("Creating service %s" % service_name)
    config_file = ConfigFile(filename, input_data={'service_name': service_name})
    click.echo(config_file.data)


    

if __name__ == '__main__':
    cli()
