import click


@click.group()
def cli():
    pass

@cli.command()
@click.option('--password-length', default=1, help='Number of greetings.')
def generate(password_length):
    """Genetate a string with the given length"""
    output_password = ""
    click.echo(f"I got a password length of: {password_length}")
    
    for letter in range(0, password_length):
        output_password += "*"
    
    click.secho(f"I have generated a password: {output_password}", fg="green")


if __name__ == '__main__':
    cli()
