# LLM Content Generation API

A Flask API for generating content using different LLMs (Large Language Models), ready for Google Cloud deployment.

## Features

- Run multiple LLMs (OpenAI, Vertex AI, HuggingFace, etc.)
- Easily extendable for new models
- Deployable on Google Cloud Run

## Usage

### Locally

```bash
pip install -r requirements.txt
python app.py
```

### API Endpoints

- `GET /` — Health check
- `POST /generate` — Generate content  
  Send JSON: `{ "prompt": "your prompt", "model": "openai" }`

### Deploy on Google Cloud Run

```bash
gcloud run deploy --source .
```

Or using Docker:

```bash
docker build -t llm-api .
docker run -p 8080:8080 llm-api
```

## Extending

Add support for any model in `llms.py` (implement API calls for OpenAI, Vertex, HuggingFace, etc.).
