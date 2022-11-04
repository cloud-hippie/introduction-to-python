import click
import random
import string

@click.group()
def cli():
    pass

@cli.command()
@click.option('--password-length', default=1, help='Number of greetings.')
@click.option("--no-numbers", is_flag=True)
@click.option("--special-chars", is_flag=True,help="Enable special characters")
def generate(password_length,no_numbers,special_chars):
    """Genetate a string with the given length"""
    output_password = ""
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers= "0123456789"
    special_char_choices="!@#$%^&*()"
    for letter in range(0, password_length):
        # Add a letter from the alphasbet above
        output_number = random.randrange(0, 10)
        if output_number % 2 == 0 and special_chars:
            master_string = letters + special_char_choices
            output_password += random.choice(master_string)
        elif no_numbers == False:
            output_password += random.choice(numbers)
    
    click.secho(f"I have generated a password: {output_password}", fg="green")


if __name__ == '__main__':
    cli()
