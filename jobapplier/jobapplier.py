import click
from naukri.naukri import NaukriController
from omegaconf import OmegaConf
from config import BaseConfig
@click.group()
def cli():
    """CLI tool for job application."""

@cli.command("search")
@click.option('--title', '-t', help='Job title to search for')
@click.option('--location', '-l', default='Any', help='Job location (default: Any)')
def search(title, location):
    """Search for job listings."""
    click.echo(f"Searching for {title} jobs in {location}...")
    # Implement job search logic here

# Add more commands as needed...

@cli.command("apply")
@click.option('--config', '-c', default='config/config.yml', help='Config file')
@click.option('--site', '-s', help='Job Site')
@click.option('--limit', '-l', default=30, help='Set no of job to be applied')
def apply(config, site, limit):
    config = load_config(config)
    """Search for job listings."""
    if site == 'naukri':
        naukri_cnt = NaukriController(config, limit)
        naukri_cnt.apply()
    # click.echo(f"Searching for {title} jobs in {location}...")
    # Implement job search logic here
def load_config(config_file):
    configs = []
    configs.append(OmegaConf.structured(BaseConfig))
    configs.append(OmegaConf.load(config_file))
    config = OmegaConf.merge(*configs)
    return config
