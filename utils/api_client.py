import os
from openai import OpenAI
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("请在 .env 文件中设置 OPENAI_API_KEY")

# 创建客户端
client = OpenAI(api_key=API_KEY)

def call_ai(prompt, model="gpt-4o-mini"):
    """
    调用 OpenAI API 返回文本（最新版 SDK 正确写法）
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

# 测试
if __name__ == "__main__":
    print(call_ai("你好"))