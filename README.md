# Mlflow + Minio storage for deep learning experiments

# Setup
## Local Setup
1. Fill in the `.env` file with your minio and mysql credentials (see `.env.demo`).
2. Start the services using docker-compose:
```bash
cd services
docker compose up -d --build
```

## PyInfra setup 
1. Install pyinfra:
```bash
uv sync
```
2. Fill in the `.env` file locally (it will be copied to a remote machine) with your minio and mysql credentials (see `.env.demo`).
3. Fill in inventory file with your server configurations.
4. Run the pyinfra deploy command:
```bash
uv run pyinfra inventory.py deploy.py
```
