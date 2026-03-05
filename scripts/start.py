#!/usr/bin/env python3
"""
第1步：选题和定位脚本
支持13种题材、出海模式、完整配置
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

class ProjectStarter:
    """项目启动器"""
    
    THEMES = {
        "1": "都市情感",
        "2": "霸道总裁", 
        "3": "甜宠",
        "4": "重生穿越",
        "5": "战神归来",
        "6": "古装宫廷",
        "7": "励志逆袭",
        "8": "家庭伦理",
        "9": "萌宝",
        "10": "悬疑探案",
        "11": "软科幻",
        "12": "末日重生",
        "13": "喜剧"
    }
    
    AUDIENCE_OPTIONS = ["男频", "女频", "全年龄"]
    TONE_OPTIONS = ["爽燃", "甜虐", "搞笑", "暗黑", "温情"]
    ENDING_OPTIONS = ["HE", "BE", "开放式"]
    LANGUAGE_OPTIONS = ["中文", "英文"]
    
    def __init__(self, project_dir=None):
        self.project_dir = project_dir or Path.cwd() / f"short-drama-project-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.config = {}
        
    def create_project_dir(self):
        """创建项目目录"""
        self.project_dir.mkdir(parents=True, exist_ok=True)
        print(f"📁 项目目录已创建：{self.project_dir}")
        return self.project_dir
    
    def select_theme(self):
        """选择题材"""
        print("🎯 请选择题材（输入编号或名称）：")
        for num, theme in self.THEMES.items():
            print(f"  {num}. {theme}")
        print()
        
        while True:
            choice = input("请输入选择： ").strip()
            
            # 检查数字选择
            if choice in self.THEMES:
                return self.THEMES[choice]
            
            # 检查名称选择
            for theme in self.THEMES.values():
                if choice == theme:
                    return theme
            
            print("❌ 无效选择，请重新输入")
    
    def select_audience(self):
        """选择受众"""
        print("👥 请选择目标受众：")
        for i, audience in enumerate(self.AUDIENCE_OPTIONS, 1):
            print(f"  {i}. {audience}")
        print()
        
        while True:
            choice = input("请输入选择（默认：女频）： ").strip()
            if not choice:
                return "女频"
            
            if choice.isdigit() and 1 <= int(choice) <= len(self.AUDIENCE_OPTIONS):
                return self.AUDIENCE_OPTIONS[int(choice)-1]
            
            if choice in self.AUDIENCE_OPTIONS:
                return choice
            
            print("❌ 无效选择，请重新输入")
    
    def select_tone(self):
        """选择故事基调"""
        print("🎭 请选择故事基调：")
        for i, tone in enumerate(self.TONE_OPTIONS, 1):
            print(f"  {i}. {tone}")
        print()
        
        while True:
            choice = input("请输入选择（默认：爽燃）： ").strip()
            if not choice:
                return "爽燃"
            
            if choice.isdigit() and 1 <= int(choice) <= len(self.TONE_OPTIONS):
                return self.TONE_OPTIONS[int(choice)-1]
            
            if choice in self.TONE_OPTIONS:
                return choice
            
            print("❌ 无效选择，请重新输入")
    
    def select_ending(self):
        """选择结局类型"""
        print("🎬 请选择结局类型：")
        for i, ending in enumerate(self.ENDING_OPTIONS, 1):
            print(f"  {i}. {ending}")
        print()
        
        while True:
            choice = input("请输入选择（默认：HE）： ").strip()
            if not choice:
                return "HE"
            
            if choice.isdigit() and 1 <= int(choice) <= len(self.ENDING_OPTIONS):
                return self.ENDING_OPTIONS[int(choice)-1]
            
            if choice in self.ENDING_OPTIONS:
                return choice
            
            print("❌ 无效选择，请重新输入")
    
    def select_episodes(self):
        """选择集数"""
        while True:
            choice = input("请输入集数（50-100，默认：60）： ").strip()
            if not choice:
                return 60
            
            if choice.isdigit() and 50 <= int(choice) <= 100:
                return int(choice)
            
            print("❌ 无效选择，请输入50-100之间的数字")
    
    def select_language(self, overseas=False):
        """选择语言"""
        if overseas:
            return "英文"
        
        print("🌐 请选择输出语言：")
        for i, lang in enumerate(self.LANGUAGE_OPTIONS, 1):
            print(f"  {i}. {lang}")
        print()
        
        while True:
            choice = input("请输入选择（默认：中文）： ").strip()
            if not choice:
                return "中文"
            
            if choice.isdigit() and 1 <= int(choice) <= len(self.LANGUAGE_OPTIONS):
                return self.LANGUAGE_OPTIONS[int(choice)-1]
            
            if choice in self.LANGUAGE_OPTIONS:
                return choice
            
            print("❌ 无效选择，请重新输入")
    
    def ask_overseas(self):
        """询问是否启用出海模式"""
        while True:
            choice = input("是否启用出海模式？（y/N）： ").strip().lower()
            if not choice or choice == 'n':
                return False
            if choice == 'y':
                return True
            print("❌ 请输入 y 或 n")
    
    def create_config(self, theme, audience, tone, ending, episodes, language, overseas):
        """创建配置文件"""
        self.config = {
            "project": {
                "name": f"{theme}短剧项目",
                "theme": theme,
                "audience": audience,
                "tone": tone,
                "ending": ending,
                "episodes": episodes,
                "language": language,
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
        
        config_file = self.project_dir / "config.json"
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)
        
        return config_file
    
    def print_summary(self):
        """打印配置摘要"""
        print("\n" + "="*60)
        print("🎬 第1步：选题和定位完成")
        print("="*60)
        print()
        print("📝 创作配置：")
        print(f"  • 题材：{self.config['project']['theme']}")
        print(f"  • 受众：{self.config['project']['audience']}")
        print(f"  • 基调：{self.config['project']['tone']}")
        print(f"  • 结局：{self.config['project']['ending']}")
        print(f"  • 集数：{self.config['project']['episodes']} 集")
        print(f"  • 语言：{self.config['project']['language']}")
        print(f"  • 出海模式：{'是' if self.config['project']['overseas'] else '否'}")
        print()
        print("✅ 配置已保存")
        print(f"📁 项目目录：{self.project_dir}")
        print()
        print("📋 下一步建议：")
        print("  short-drama-pro plan          # 第2步：生成创作方案")
        print("  short-drama-pro analyze       # 商业分析")
        print()
        print("="*60)
    
    def run(self, args=None):
        """运行启动流程"""
        # 解析命令行参数
        import argparse
        parser = argparse.ArgumentParser(description='短剧项目启动器')
        parser.add_argument('--theme', help='题材类型')
        parser.add_argument('--audience', help='目标受众')
        parser.add_argument('--tone', help='故事基调')
        parser.add_argument('--ending', help='结局类型')
        parser.add_argument('--episodes', type=int, help='集数')
        parser.add_argument('--language', help='输出语言')
        parser.add_argument('--overseas', action='store_true', help='启用出海模式')
        parser.add_argument('--project-dir', help='项目目录')
        
        if args:
            parsed_args = parser.parse_args(args)
        else:
            parsed_args = parser.parse_args()
        
        # 设置项目目录
        if parsed_args.project_dir:
            self.project_dir = Path(parsed_args.project_dir)
        
        # 创建项目目录
        self.create_project_dir()
        
        # 收集配置信息
        theme = parsed_args.theme or self.select_theme()
        audience = parsed_args.audience or self.select_audience()
        tone = parsed_args.tone or self.select_tone()
        ending = parsed_args.ending or self.select_ending()
        episodes = parsed_args.episodes or self.select_episodes()
        overseas = parsed_args.overseas or self.ask_overseas()
        language = parsed_args.language or self.select_language(overseas)
        
        # 创建配置文件
        config_file = self.create_config(theme, audience, tone, ending, episodes, language, overseas)
        
        # 打印摘要
        self.print_summary()
        
        return config_file

def main():
    """主函数"""
    starter = ProjectStarter()
    starter.run()

if __name__ == "__main__":
    main()