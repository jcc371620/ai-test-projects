import json
from utils.api_client import call_ai

def test_stability(repeat=3):
    with open("data/test_stability.json", "r", encoding="utf-8") as f:
        cases = json.load(f)

    results = []
    for case in cases:
        prompt = case["input"]
        outputs = []
        for _ in range(repeat):
            outputs.append(call_ai(prompt))
        passed = len(set(outputs)) == 1
        results.append({
            "prompt": prompt,
            "repeat": repeat,
            "outputs": outputs,
            "passed": passed
        })
        print(f"[Stability] Prompt: {prompt} | Passed: {passed} | Outputs: {outputs}")
    return results

def test_stability_pytest():
    results = test_stability()
    for r in results:
        assert r["passed"], f"Stability test failed: {r['prompt']}"