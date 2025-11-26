#!/usr/bin/env python3
"""
Minimal, safe AI-agent example for "Prioritize".

Requirements:
  pip install -r requirements.txt

Usage:
  export OPENAI_API_KEY="sk-..."
  python agent_simple.py

This script demonstrates a simple loop where the LLM suggests labels and priority.
It is intentionally small and safe.
"""
import os
import json
import openai
from typing import Dict, Any

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    print("Please set OPENAI_API_KEY environment variable.")
    exit(1)
openai.api_key = OPENAI_API_KEY

MODEL = "gpt-3.5-turbo"

SYSTEM_PROMPT = """You are a helpful assistant that receives a short task description
and should return JSON with two keys:
- labels: an array of short labels (e.g. ["work","urgent","low-effort"])
- priority: one of ["low","medium","high"]
Return ONLY JSON (no other text).
"""

def ask_model(task_description: str) -> Dict[str, Any]:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Task: {task_description}"}
    ]
    resp = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        temperature=0.2,
        max_tokens=200
    )
    text = resp["choices"][0]["message"]["content"].strip()
    try:
        data = json.loads(text)
        return data
    except Exception:
        start = text.find("{")
        end = text.rfind("}") + 1
        if start != -1 and end != -1:
            try:
                return json.loads(text[start:end])
            except Exception as e:
                return {"error": f"failed to parse JSON: {e}", "raw": text}
        return {"error": "no JSON in model response", "raw": text}

def main():
    print("Simple Prioritize prototype. Enter task descriptions. Empty line to exit.")
    while True:
        task = input("\nTask description:\n> ").strip()
        if not task:
            break
        result = ask_model(task)
        print("\nModel output:")
        print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
