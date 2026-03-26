# 测试稳定性 - Stability Testing
# 目的：验证 AI 模型在面对相同输入时，是否能够生成一致的输出，确保模型的稳定性和可靠性。
# 设计：准备一系列测试用例，针对每个用例调用 AI 接口多次（如 3 次），并检查返回的结果是否一致。如果同一输入产生了不同的输出，则认为测试失败。
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