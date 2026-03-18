import json
from utils.api_client import call_ai

def test_basic():
    """
    基础功能测试：
    遍历 JSON 测试用例，检查 AI 回答是否包含关键词
    返回测试结果列表（方便 run_tests.py 调用）
    """
    with open("data/test_basic_cases.json", "r", encoding="utf-8") as f:
        cases = json.load(f)

    results_summary = []

    for case in cases:
        prompt = case["input"]
        expected_keywords = case["expected_keywords"]
        result = call_ai(prompt)
        passed = all(keyword in result for keyword in expected_keywords)
        results_summary.append({
            "prompt": prompt,
            "result": result,
            "passed": passed
        })
        # 打印用于 pytest 观察
        print(f"[Basic Test] Prompt: {prompt} | Passed: {passed}")

    return results_summary

# 兼容 pytest，直接用 assert 测试每条用例
def test_basic_pytest():
    results = test_basic()
    for r in results:
        assert r["passed"], f"Basic test failed: {r['prompt']}"