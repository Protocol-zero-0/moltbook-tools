#!/bin/bash
# Protocol Zero: Skill Manifest Verifier
# Validates agent skill JSON for security compliance

MANIFEST=$1

if [ -z "$MANIFEST" ]; then
  echo "Usage: $0 <manifest.json>"
  exit 1
fi

echo "Verifying $MANIFEST..."
# Check for required fields
if grep -q '"security_level":' "$MANIFEST"; then
  echo "[PASS] Security level defined."
else
  echo "[FAIL] Missing security_level."
  exit 1
fi

echo "[OK] Manifest compliant."
