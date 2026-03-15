from gevent.testing.travis import commands
from pyinfra import host, inventory
from pyinfra.operations import apt, server, git, files, docker

HOME_DIR = f"/home/{host.data.ssh_user}"
REPO_DIR = f"{HOME_DIR}/dl-experiments-storage"

apt.packages(
    name="Install Docker and Docker Compose",
    packages=["docker.io", "docker-compose-v2"],
    update=True,
    _sudo=True,
)

server.user(
    name="Add user to docker group",
    user=host.data.ssh_user,
    groups=["sudo", "docker"],
    _sudo=True,
)

git.repo(
    name="Clone git repository",
    src="https://github.com/Biblbrox/dl-experiments-storage.git",
    dest=REPO_DIR,
    branch="dev",
)

files.put(
    name="Upload .env file",
    src="services/.env",
    dest=f"{REPO_DIR}/services/.env",
    mode="644",
)

server.shell(
    name="Stop docker compose service if exists",
    commands=["docker kill $(docker ps -q)"],
    _continue_on_error=True,
    _ignore_errors=True,
)

server.shell(
    name="Run docker compose service",
    commands=[f"cd {REPO_DIR}/services && docker compose up -d"],
)
