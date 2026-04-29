def schema(data):
    print("[SchemaAgent] inferring schema...")
    return {"fields": list(data.keys())}
