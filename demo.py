import json

def run_agent(data):
    print("[Agent] Parsing input...")
    print("[Agent] Generating schema...")
    print("[Agent] Creating SQL...")
    print("[Agent] Done.")
    return {"status": "success"}

if __name__ == "__main__":
    sample = {"event": "click", "user": 123}
    print(run_agent(sample))
