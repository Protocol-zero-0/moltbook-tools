import subprocess
import tempfile
import os
import sys

def run_sandboxed(code: str, image="python:3.10-slim"):
    """
    Executes Python code inside a restricted Docker container.
    Blocks network, limits CPU/Memory, and mounts a temporary volume.
    """
    print(f"[*] Initializing Sandbox (Image: {image})...")
    
    # Create temp script
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as script_file:
        script_file.write(code)
        script_path = script_file.name
    
    # Docker Command: No Network, Read-Only Root, Tmpfs for /tmp, CPU/Mem Limits
    cmd = [
        "docker", "run", "--rm",
        "--network", "none",            # No internet access
        "--read-only",                  # Root filesystem read-only
        "--tmpfs", "/tmp",              # Writable /tmp in memory
        "--cpus", "0.5",                # Limit CPU
        "--memory", "128m",             # Limit Memory
        "-v", f"{script_path}:/app/script.py:ro", # Mount script read-only
        image,
        "python", "/app/script.py"
    ]
    
    print(f"[*] Executing in Isolation...")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "exit_code": result.returncode
        }
    except subprocess.TimeoutExpired:
        return {"error": "Execution Timed Out (Possible Infinite Loop)"}
    finally:
        os.remove(script_path)

if __name__ == "__main__":
    sample_code = """
import os
print("Hello from the Sandbox!")
try:
    with open('/etc/passwd', 'w') as f:
        f.write("hacked")
except OSError as e:
    print(f"Write blocked: {e}")
    """
    output = run_sandboxed(sample_code)
    print("\n--- Sandbox Output ---")
    print(output)
