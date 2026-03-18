from datetime import datetime
import json
import os
from tests.test_basic import test_basic
from tests.test_stability import test_stability
from tests.test_safety import test_safety

def save_report(report_data, directory="report"):
    """
    保存测试结果到 JSON 文件，按时间自动命名，避免覆盖
    """
    os.makedirs(directory, exist_ok=True)
    timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(directory, f"result_{timestamp_str}.json")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(report_data, f, ensure_ascii=False, indent=4)
    print(f"\n测试结果已保存到 {filename}")
    return filename

def summarize_results(results):
    total = len(results)
    passed = sum(1 for r in results if r.get("passed"))
    failed = total - passed
    return {"total": total, "passed": passed, "failed": failed}

if __name__ == "__main__":
    all_results = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tests": {},
        "summary": {}
    }

    print("=== Running Basic Tests ===")
    basic_results = test_basic()
    all_results["tests"]["basic"] = basic_results
    all_results["summary"]["basic"] = summarize_results(basic_results)

    print("\n=== Running Stability Tests ===")
    stability_results = test_stability(repeat=3)
    all_results["tests"]["stability"] = stability_results
    all_results["summary"]["stability"] = summarize_results(stability_results)

    print("\n=== Running Safety Tests ===")
    safety_results = test_safety()
    all_results["tests"]["safety"] = safety_results
    all_results["summary"]["safety"] = summarize_results(safety_results)

    # 保存报告并返回文件名
    report_file = save_report(all_results)

    print("\n=== Test Summary ===")
    for test_name, stats in all_results["summary"].items():
        print(f"{test_name.capitalize()}: Total={stats['total']}, Passed={stats['passed']}, Failed={stats['failed']}")