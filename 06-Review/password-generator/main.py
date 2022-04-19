import click


@click.group()
def cli():
    pass

@cli.command()
@click.option('--password-length', default=1, help='Number of greetings.')
def configure(password_lenegth):
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo(f"I got a password length of: {password_lenegth}")

if __name__ == '__main__':
    cli()
