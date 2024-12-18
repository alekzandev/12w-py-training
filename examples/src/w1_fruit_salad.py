import click
import logging
from click.testing import CliRunner

logging.basicConfig(level=logging.INFO)

@click.command()
@click.option('--fruits')
def salad_mixer(fruits):
    """
    Mix fruits to make a fruit salad.

    :param fruits: list of fruits
    :return: fruit_salad
    """
    if not fruits:
        logging.error('No fruits to mix!')
        return 'No Salad! :c'
    else:
        fruits = eval(fruits)
    logging.info(f'Mixing fruits: {fruits}')
    fruit_salad = ', '.join(fruits)
    logging.info(f'Fruit salad ready: {fruit_salad}')
    return fruit_salad

if __name__ == '__main__':
    print(salad_mixer())
    