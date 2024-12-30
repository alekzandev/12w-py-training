import click
import logging
from click.testing import CliRunner
from src.w1_fruit_salad import salad_mixer

logging.basicConfig(level=logging.INFO)

@click.command()
@click.option('--fruits')
def main(fruits):
    print(salad_mixer(fruits))

if __name__ == '__main__':
    main()