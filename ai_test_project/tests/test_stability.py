import json
from utils.api_client import call_ai

def test_stability(repeat=3):
    """
    稳定性测试：
    读取 JSON 中的多个 prompt，对每个 prompt 调用 repeat 次 AI 接口
    并记录每次输出，判断是否一致
    """
    with open("data/test_stability_cases.json", "r", encoding="utf-8") as f:
        cases = json.load(f)

    results = []
    for case in cases:
        prompt = case["input"]
        outputs = []
        for i in range(repeat):
            output = call_ai(prompt)
            outputs.append(output)
        passed = len(set(outputs)) == 1  # 是否所有输出一致
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