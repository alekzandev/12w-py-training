from click.testing import CliRunner
from src.w1_fruit_salad import salad_mixer

def test_salad_mixer_no_fruits():
    runner = CliRunner()
    result = runner.invoke(salad_mixer, [])
    assert result.exit_code == 0
    #assert 'apple, banana, orange' in result.output

def test_salad_mixer_with_fruits():
    runner = CliRunner()
    result = runner.invoke(salad_mixer, input='["apple", "banana", "cherry"]')
    assert result.exit_code == 0
    # assert 'apple, banana, cherry' in result.output
