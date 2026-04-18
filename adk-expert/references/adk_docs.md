# Google ADK (Agent Development Kit) Reference Guide

## What is Google ADK?
Agent Development Kit (ADK) is an open-source, code-first Python toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control. It is optimized for Gemini but model and deployment agnostic.

## Installation
```bash
pip install google-adk
```

## Basic Single Agent
```python
from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="search_assistant",
    model="gemini-2.5-flash",
    instruction="You are a helpful assistant. Answer user questions using Google Search when needed.",
    description="An assistant that can search the web.",
    tools=[google_search]
)
```

## Multi-Agent Systems
Design scalable applications by composing multiple specialized agents.
```python
from google.adk.agents import LlmAgent, BaseAgent

# Define individual agents
greeter = LlmAgent(name="greeter", model="gemini-2.5-flash", instruction="You greet the user.")
task_executor = LlmAgent(name="task_executor", model="gemini-2.5-flash", instruction="You execute tasks.")

# Create parent agent and assign children via sub_agents
coordinator = LlmAgent(
    name="Coordinator",
    model="gemini-2.5-flash",
    description="I coordinate greetings and tasks.",
    sub_agents=[
        greeter, 
        task_executor
    ]
)
```

## Key Agents Types
- **LlmAgent**: Basic LLM powered agent.
- **Workflow Agents**: Includes Sequential agents, Loop agents, Parallel agents.
- **Custom Agents**: Ability to write entirely custom python agents.

## Supported Models
Gemini (Default/Optimized), Gemma, Claude, Vertex AI Hosted, Apigee AI Gateway.

## Evals & Testing
ADK comes with a built-in testing framework to evaluate agent runs.

```bash
adk eval <agent_package_dir> <eval_set.json>
```

Testing via Evals is a critical component. ADK developers must prioritize testing their agents.
