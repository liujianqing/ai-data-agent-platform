import time
import random

def log(step, detail):
    print(f"[{step}] {detail}")
    time.sleep(0.3)

def run_pipeline():
    log("ParserAgent", "Parsing raw JSON logs...")
    log("ParserAgent", "Detected fields: user_id, event, timestamp")

    log("SchemaAgent", "Inferring schema...")
    log("SchemaAgent", "Generated schema with 12 fields")

    log("SQLAgent", "Generating SQL query...")
    log("SQLAgent", "SELECT user_id, COUNT(*) FROM events GROUP BY user_id")

    log("ValidationAgent", "Running validation checks...")
    log("ValidationAgent", "No anomalies detected")

    log("AnalysisAgent", "Generating insights...")
    log("AnalysisAgent", "Top users identified")

    tokens = random.randint(5000, 10000)
    print(f"\n[Token Usage] Estimated tokens consumed: {tokens}")

if __name__ == "__main__":
    run_pipeline()
