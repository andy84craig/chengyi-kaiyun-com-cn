# tools/site_summary.py

from collections import OrderedDict
from datetime import datetime
import json

SITE_DATA = {
    "name": "开云官方平台",
    "url": "https://www.chengyi-kaiyun.com.cn",
    "keywords": ["开云", "开云官网", "开云平台"],
    "tags": ["体育", "电竞", "娱乐", "真人"],
    "description": "开云提供体育赛事投注、电子竞技、真人娱乐等多元化服务，致力于打造安全可靠的线上娱乐平台。",
    "version": "2.4.1",
    "last_updated": "2025-03-17"
}

def extract_structured_summary(data):
    """返回结构化的站点摘要字典"""
    summary = OrderedDict()
    summary["站点名称"] = data.get("name", "未知")
    summary["官方地址"] = data.get("url", "")
    summary["核心关键词"] = data.get("keywords", [])
    summary["主要标签"] = data.get("tags", [])
    summary["简短说明"] = data.get("description", "")
    summary["数据版本"] = data.get("version", "")
    summary["更新日期"] = data.get("last_updated", "")
    return summary

def format_summary_text(summary_dict):
    """将结构化摘要转为可读文本块"""
    lines = []
    lines.append("=" * 50)
    lines.append(" 站点摘要报告")
    lines.append("=" * 50)
    for key, value in summary_dict.items():
        if isinstance(value, list):
            value_str = ", ".join(value)
        else:
            value_str = str(value)
        lines.append(f"{key}: {value_str}")
    lines.append("=" * 50)
    lines.append(f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    return "\n".join(lines)

def export_summary_to_json(summary_dict, filepath=None):
    """将摘要导出为 JSON 格式，可选写入文件"""
    json_str = json.dumps(summary_dict, ensure_ascii=False, indent=2)
    if filepath:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(json_str)
    return json_str

def display_keywords_cloud(keywords):
    """生成关键词云（简单文本表示）"""
    if not keywords:
        print("（无关键词可展示）")
        return
    max_len = max(len(kw) for kw in keywords)
    print("\n关键词云:")
    print("-" * (max_len + 4))
    for kw in keywords:
        print(f"  {kw}")
    print("-" * (max_len + 4))

def main():
    summary = extract_structured_summary(SITE_DATA)
    text = format_summary_text(summary)
    print(text)
    display_keywords_cloud(summary["核心关键词"])
    json_output = export_summary_to_json(summary)
    print("\nJSON 格式摘要:")
    print(json_output)
    print("\n（摘要处理完成）")

if __name__ == "__main__":
    main()