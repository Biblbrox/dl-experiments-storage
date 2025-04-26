# Mlflow + Minio storage for deep learning experiments

# Setup
## Local Setup
1. Fill in the `.env` file with your minio and mysql credentials (see `.env.demo`).
2. Start the services using docker-compose:
```bash
cd services
docker-compose up -d
```

## Ansible setup 
1. Install ansible:
```bash
pipx install --include-deps ansible
```

2. Fill in hosts file with your server configurations.
3. Run the ansible playbook:
```bash
ansible-playbook playbook.yml --ask-pass --ask-become-pass
```