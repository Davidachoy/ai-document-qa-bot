#!/bin/bash
echo "🚀 Starting Doc Q&A development environment..."

echo "📦 Starting Docker services..."
docker compose up -d

echo "⏳ Waiting for services to be ready..."
sleep 5

echo "✅ Environment ready!"
echo "   - PostgreSQL: localhost:5432"
echo "   - ChromaDB: localhost:8001"
echo ""
echo "Starting apps..."
pnpm turbo run dev