# Capstone Project — Task Tracker with Postgres

## What it does
A Python app that saves tasks to a PostgreSQL database running in a separate container.

## Architecture
app (Python) --> Docker network --> db (Postgres 15)

## Services
- app: Python 3.12, connects to Postgres, inserts and reads tasks
- db: Postgres 15 with persistent volume

## How to run
docker-compose up --build

## Key concepts demonstrated
- Multi-service Docker Compose
- Inter-container networking
- Volume persistence across restarts
- Environment variable configuration
