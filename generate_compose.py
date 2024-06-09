#!/usr/bin/env python3

import os
import click
import logging

from typing import List

# from vigor.compose import Compose
from vigor.utils import get_immediate_subdirectories


class Compose(CommandRunner):
    def run(self, *args) -> str:
        params = ["docker", "compose"]
        params.extend(args)

        process = super().run(*params, capture_output=True)
        return process.stdout

    def help(self) -> str:
        params = ["--help"]

        return self.run(*params)

    def generate_compose_file(self, files: List[str], env: str=None) -> str:
        params = ["config"]

        if env:
            params.append("--env-file")
            params.append(env)

        for file in files:
            params.append("--file")
            params.append(file)

        return self.run(*params)


# Some global stuff I don't know how to not abstract
root_dir = os.path.dirname(os.path.abspath(__file__))
services = get_immediate_subdirectories(full_path=root_dir, ignore=[".git"], absolute_path=False)


@click.command()
@click.option("--service", type=click.Choice(services),
    help="Services to generate compose file for.", required=True, multiple=True)
def generate_config(services):
    """
    Generates aggregated docker-compose.yml for services.
    """
    files = []
    for service in services:
        files.append(os.path.join(root_dir, service, "docker-compose.yml"))

    aggregated_env = aggregate_env_file(services=services)

    aggregated_compose = os.path.join(root_dir, "docker-compose.yml")
    with open(aggregated_compose, "w") as compose_file:
        compose = Compose()
        compose_config = compose.generate_compose_file(files=files, env=aggregated_env)
        compose_file.write(compose_config)
        logging.info(f"Aggregated docker-compose.yml file created at {aggregated_compose}")


def aggregate_env_file(services: List) -> str:
    """
    Aggregates all found .env files into one for aggregated docker-compose.yml file.

    Args:
        services (List): List of services to check for.

    Returns:
        str: Path to the new .env file
    """
    env_files = []
    for service in services:
        absolute_path = os.path.join(root_dir, service)
        for item in os.scandir(absolute_path):
            if item.is_file and item.name.endswith(".env"):
                env_files.append(item.path)

    # Only proceed if there's any files
    if not env_files:
        return

    aggregate_config = {}
    for file in env_files:
        with open(file, "r") as read_file:
            for line in read_file:
                split = line.split("=")
                aggregate_config[split[0]] = split[1]

    aggregate_filename = os.path.join(root_dir, ".env")
    with open(aggregate_filename, "w") as write_file:
        for key, value in aggregate_config.items():
            write_file.write(f"{key}={value}")

    return aggregate_filename


if __name__ == "__main__":
    generate_config()
