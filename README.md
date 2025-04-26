# Mlflow + Minio storage for deep learning experiments

# Setup
## Local Setup
1. Fill in the `.env` file with your minio and mysql credentials (see `.env.demo`).
2. Start the services using docker-compose:
```bash
cd services
docker compose up -d --build
```

## Ansible setup 
1. Install ansible:
```bash
pipx install --include-deps ansible
```
2. Fill in the `.env` file locally (it will be copied to a remote machine) with your minio and mysql credentials (see `.env.demo`).
3. Fill in hosts file with your server configurations.
4. Run the ansible playbook:
```bash
ansible-playbook playbook.yml --ask-pass --ask-become-pass
```