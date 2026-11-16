# Agent Harness

A custom agent harness build from scratch

## Setup

1. Clone the repo and `cd` into it.
2. Create a virtual environment:

```
   python -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   .venv\Scripts\activate      # Windows
```

3. Install dependencies:

```
   pip install -r requirements.txt
```

4. Copy `.env.example` to `.env` and fill in your Inference API key, and other vars.

5. Create a Docker image for the agent to run code inside a sandboxed execution environment

```
   docker build -f harness/sandbox/Dockerfile -t agent-harness:0.1
```

## Running

```
   python -m harness.agent
```
