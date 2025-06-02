import json

with open('semgrep-results.json') as f:
    results = json.load(f)

for finding in results['results']:
    print(f"[{finding['check_id']}] {finding['extra']['message']}")
    print(f"CWE: {finding['extra'].get('cwe')}, Severity: {finding['extra']['severity']}")
