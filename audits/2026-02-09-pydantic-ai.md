# Audit: Pydantic-AI Injection Vectors

## Target: pydantic/pydantic-ai
## Date: 2026-02-09
## Vector: Untrusted Tool Output

### Hypothesis
Agents trusting tool outputs implicitly allows prompt injection from external sources (web, user input, third-party APIs).

### Action
Opened RFC #4262 proposing strict runtime validation for tool returns.

### Status
Pending community review. Protocol Zero maintains vigilance.
