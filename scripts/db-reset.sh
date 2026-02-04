#!/bin/bash
docker compose down -v
docker compose up -d postgres chromadb
echo "Waiting for PostgreSQL to be ready..."
sleep 5
echo "PostgreSQL is ready!"