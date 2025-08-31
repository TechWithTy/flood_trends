cat > README.md << 'EOF'
# Flood Trends

Integration for historical and projected flood risk trends.

## Overview
- Historical/projection endpoints
- Typed request/response models
- FastAPI-ready routes and proxy helpers

## Project Structure
- api/: base models, requests, responses, route handlers
- client.py: high-level client wrapper
- config.py: configuration and environment variables
- pyproject.toml: package metadata

## Setup
- Python 3.11+
- Configure API credentials (see config.py)

## Usage
See `api/` and `routes.py` for examples. Import the client for programmatic use.

## License
MIT (or repository default)
EOF