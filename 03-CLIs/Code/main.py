import click


@click.group()
def cli():
    pass

@cli.command()
@click.option('--number-one', type=int, help="A number")
@click.option('--number-two', type=int, help="Another number")
def add(number_one, number_two):
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo(f"{number_one} + {number_two} is {number_one + number_two}")


if __name__ == '__main__':
    cli()
