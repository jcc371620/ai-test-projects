import json
from utils.api_client import call_ai

def test_basic():
    with open("data/test_basic.json", "r", encoding="utf-8") as f:
        cases = json.load(f)

    results = []
    for case in cases:
        prompt = case["input"]
        expected = case.get("expected_keywords", [])
        output = call_ai(prompt)
        passed = all(k in output for k in expected)
        results.append({
            "prompt": prompt,
            "result": output,
            "passed": passed
        })
        print(f"[Basic] Prompt: {prompt} | Passed: {passed} | Output: {output}")

    return results

def test_basic_pytest():
    results = test_basic()
    for r in results:
        assert r["passed"], f"Basic test failed: {r['prompt']}"