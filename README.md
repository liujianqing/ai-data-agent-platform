# AI Data Agent Platform 

## Overview
A multi-agent LLM system for automated data pipeline generation, schema inference, and analytics.

## Architecture
- agents/: individual agent logic
- core/: orchestrator
- services/: token + logging simulation
- data/: sample input
- logs/: runtime logs

## Run
python app.py

## Architecture
- Parser Agent
- Schema Agent
- SQL Generator Agent
- Validation Agent
- Analysis Agent

## Workflow
1. Input raw JSON logs
2. Parse and infer schema
3. Generate SQL
4. Validate results
5. Output structured analytics

## Features
- Multi-agent orchestration
- Long-chain reasoning simulation
- Token-heavy processing simulation
- Extensible architecture

## Example
Run:
```bash
python main.py
```

## Output
- Parsed schema
- Generated SQL
- Validation report

## Token Simulation
Each run simulates ~5k–10k token usage across agents.
