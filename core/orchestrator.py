from agents.parser_agent import parse
from agents.schema_agent import schema
from agents.sql_agent import generate_sql
from agents.validation_agent import validate
from agents.analysis_agent import analyze
from services.token_service import count_tokens

def run_pipeline():
    data = {"event":"click","user_id":123}

    parsed = parse(data)
    sch = schema(parsed)
    sql = generate_sql(sch)
    valid = validate(sql)
    result = analyze(valid)

    tokens = count_tokens()
    print("\n[FINAL RESULT]", result)
    print(f"[TOKEN USAGE] {tokens}")
