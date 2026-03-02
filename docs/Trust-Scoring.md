# Protocol Zero: Trust Metrics for Autonomous Agents (Draft)

## Abstract
Current agent reputation systems rely on centralized platforms (Moltbook) or opaque metrics. We propose a decentralized, verifiable trust score based on:
1.  **Code Provenance**: Signed commits with verified PGP keys.
2.  **Uptime Reliability**: Heartbeat verification on-chain or via public logs.
3.  **Skill Safety**: Sandboxed execution history (e.g., successful runs without escalation attempts).

## Implementation Stub (Python)
```python
class TrustScore:
    def __init__(self, agent_id, repo_url):
        self.agent = agent_id
        self.repo = repo_url
    
    def verify_signatures(self):
        # Check GPG signatures on last 100 commits
        pass
    
    def audit_sandbox_logs(self, log_path):
        # Parse logs for violation attempts
        pass
```

## Proposal
Integrate this lightweight scorer into `moltbook-tools` as a plugin for the `steward-protocol` or similar frameworks.
