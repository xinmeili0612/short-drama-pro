#!/usr/bin/env python3
"""
非交互式项目启动器
用于演示和测试
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

def create_project(theme="霸道总裁", episodes=60, overseas=False):
    """创建短剧项目"""
    
    # 创建项目目录
    project_dir = Path.cwd() / f"short-drama-project-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    project_dir.mkdir(parents=True, exist_ok=True)
    
    # 配置信息
    config = {
        "project": {
            "name": f"{theme}短剧项目",
            "theme": theme,
            "audience": "女频",
            "tone": "爽燃",
            "ending": "HE",
            "episodes": episodes,
            "language": "英文" if overseas else "中文",
            "overseas": overseas,
            "created_at": datetime.now().isoformat()
        },
        "workflow": {
            "step1_completed": True,
            "step2_completed": False,
            "step3_completed": False,
            "step4_completed": False,
            "step5_completed": False,
            "step6_completed": False,
            "step7_completed": False
        }
    }
    
    # 保存配置文件
    config_file = project_dir / "config.json"
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
    
    # 创建项目说明
    readme_file = project_dir / "README.md"
    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(f"""# 《{theme}》短剧项目

## 📋 项目信息
- **题材类型**：{theme}
- **集数规模**：{episodes}集
- **创作模式**：{'出海模式（英文）' if overseas else '国内模式（中文）'}
- **创建时间**：{datetime.now().strftime('%Y年%m月%d日 %H:%M')}

## 🎯 创作目标
创作一部{episodes}集的{theme}题材短剧，目标受众为女性观众，基调爽燃，结局圆满。

## 📁 文件结构
```
{project_dir.name}/
├── config.json          # 项目配置
├── README.md           # 项目说明
├── 创作方案.md         # 第2步生成
├── 角色档案.md         # 第3步生成  
├── 剧集目录.md         # 第4步生成
├── scripts/            # 剧本文件
│   ├── 第1集剧本.md
│   ├── 第2集剧本.md
│   └── ...
└── exports/            # 导出文件
    └── 完整剧本.md
```

## 🚀 下一步
1. 运行 `short-drama-pro plan` 生成创作方案
2. 运行 `short-drama-pro characters` 开发角色
3. 运行 `short-drama-pro catalog` 生成目录
4. 运行 `short-drama-pro episode 1` 生成第1集剧本

## 💰 商业化潜力
- **平台**：抖音、快手、B站等
- **受众**：女性18-35岁
- **变现**：广告分成、付费观看、IP授权
- **周期**：{episodes//15}周完成创作

---
*项目创建时间：{datetime.now().strftime('%Y年%m月%d日 %H:%M')}*
""")
    
    print("="*60)
    print("🎬 短剧项目创建成功！")
    print("="*60)
    print()
    print("📁 项目目录：", project_dir)
    print("📝 项目配置：", config_file)
    print()
    print("📋 项目信息：")
    print(f"  • 题材：{theme}")
    print(f"  • 集数：{episodes}集")
    print(f"  • 模式：{'出海模式（英文）' if overseas else '国内模式（中文）'}")
    print(f"  • 受众：女频")
    print(f"  • 基调：爽燃")
    print(f"  • 结局：HE")
    print()
    print("🚀 可用命令：")
    print("  # 生成创作方案")
    print("  short-drama-pro plan")
    print()
    print("  # 生成第1集剧本（使用旧技能）")
    print(f"  cd ~/.openclaw/workspace/skills/short-drama-script")
    print(f"  ./short-drama-script quick-generate --theme \"{theme}\" --episode 1")
    print()
    print("💡 提示：完整7步工作流正在开发中")
    print("="*60)
    
    return project_dir, config_file

def main():
    """主函数"""
    # 默认创建霸道总裁项目
    project_dir, config_file = create_project(
        theme="霸道总裁",
        episodes=60,
        overseas=False
    )
    
    # 显示配置文件内容
    print("\n📄 配置文件内容：")
    print("-"*40)
    with open(config_file, 'r', encoding='utf-8') as f:
        print(f.read())
    print("-"*40)

if __name__ == "__main__":
    main()