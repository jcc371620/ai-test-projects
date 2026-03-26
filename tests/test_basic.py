# 基础功能测试 - Basic Functionality Testing
# 目的：验证 AI 模型在面对基本输入时，是否能够正确理解并生成包含预期关键词的输出，确保模型的基本功能正常。
# 设计：准备一系列简单的测试用例，包含基本的输入和预期输出关键词列表，调用 AI 接口，并检查返回的结果是否包含所有预期关键词。如果缺少任何一个关键词，则认为测试失败。
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