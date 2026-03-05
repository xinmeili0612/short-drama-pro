---
name: short-drama-pro
description: "专业短剧剧本创作技能，基于微信公众号文章《短剧剧本创作 Skill 正式发布！》的7步工作流开发。支持13种题材、出海模式、合规审核、专业剧本格式输出。"
---

# 专业短剧剧本创作技能

基于微信公众号文章《短剧剧本创作 Skill 正式发布！》开发的7步工作流专业短剧剧本创作工具。

## 🎯 核心功能

### 7步完整工作流
```
/开始 → /创作方案 → /角色开发 → /目录 → /分集 → /自检 → /导出
```

### 13种主流题材
1. 都市情感 2. 霸道总裁 3. 甜宠 4. 重生穿越 5. 战神归来
6. 古装宫廷 7. 励志逆袭 8. 家庭伦理 9. 萌宝 10. 悬疑探案
11. 软科幻 12. 末日重生 13. 喜剧

### 专业特色
- **专业剧本格式**：真正的文学剧本格式，不是小说
- **出海模式**：支持英文，好莱坞行业标准
- **合规审核**：内置审核检查清单
- **爽剧方法论**：内置专业参考文档
- **工作流工具**：完整的创作流程管理

## 🚀 快速开始

### 安装技能
```bash
# 复制到技能目录
cp -r short-drama-pro ~/.openclaw/workspace/skills/
```

### 开始创作
```bash
# 启动7步工作流
./short-drama-pro start

# 选择题材开始创作
./short-drama-pro start --theme "霸道总裁" --episodes 60
```

## 📋 7步工作流详解

### 第1步：/开始 - 选题和定位
```bash
# 选择题材
./short-drama-pro start --theme "霸道总裁"

# 选择叠加题材
./short-drama-pro start --theme "战神+萌宝"

# 出海模式
./short-drama-pro start --theme "都市情感" --overseas

# 完整参数
./short-drama-pro start \
  --theme "重生穿越" \
  --audience "女频" \
  --tone "爽燃" \
  --ending "HE" \
  --episodes 60 \
  --language "中文"
```

**功能**：
- 13种题材选择，支持题材叠加
- 目标受众选择（男频/女频/全年龄）
- 故事基调选择（爽燃/甜虐/搞笑/暗黑/温情）
- 结局类型选择（HE/BE/开放式）
- 集数规模设定（50-100集）
- 输出语言选择（中文/英文）
- 出海模式切换

### 第2步：/创作方案 - 故事的骨架
```bash
# 生成创作方案
./short-drama-pro plan --project "my_drama"

# 基于大纲生成方案
./short-drama-pro plan --input "outline.json"
```

**输出内容**：
- 故事核心概念
- 世界观设定
- 主要冲突线
- 节奏设计（付费卡点策略）
- 开篇黄金法则应用
- 商业化分析

### 第3步：/角色开发 - 让人物活起来
```bash
# 开发主要角色
./short-drama-pro characters --count 5

# 基于方案开发角色
./short-drama-pro characters --plan "plan.json"
```

**角色信息表**：
- 姓名、年龄、外貌
- 性格特征（公开身份 vs 真实身份）
- 核心动机和冲突点
- 爽点功能（在故事中的爽点作用）
- 人物关系图
- 成长弧线设计

### 第4步：/目录 - 完整集数规划
```bash
# 生成50-100集目录
./short-drama-pro catalog --episodes 60

# 基于角色生成目录
./short-drama-pro catalog --characters "characters.json"
```

**目录特点**：
- 一集一行，每集标注标题和核心冲突/爽点
- 重要集用 🔥 标记
- 付费卡点集用 💰 标记
- 节奏走向可视化
- 强制预览全部目录

### 第5步：/分集 - 专业剧本产出
```bash
# 生成第1集剧本
./short-drama-pro episode 1

# 批量生成多集
./short-drama-pro episodes 1 5

# 指定格式生成
./short-drama-pro episode 1 --format "professional"
```

**专业剧本格式**：
```
场景1：内景 医院手术室 日
【全景】手术室内，无影灯下，医生正在紧张手术
【近景】主角额头渗出细密汗珠
主角（冷静）：止血钳。
护士（紧张）：医生，病人血压下降！
【音乐】紧张急促的背景音乐起
```

**格式要素**：
- 场景头（内/外景、具体地点、日/夜时间）
- 景别提示（全景、中景、近景、特写）
- 动作描写和语气指示
- 音乐和音效提示
- 转场提示

### 第6步：/自检 - 质量把关
```bash
# 自检第1集
./short-drama-pro check 1

# 自检全部剧本
./short-drama-pro check all

# 合规审核
./short-drama-pro check 1 --compliance
```

**自检维度**：
1. **节奏分**：爽点密度和节奏控制
2. **冲突分**：冲突设置和解决
3. **人物分**：人物行为一致性
4. **情感分**：情感共鸣和代入感
5. **格式分**：剧本格式规范性

**合规审核清单**：
- 政治敏感内容检查
- 暴力血腥内容检查
- 色情低俗内容检查
- 价值观导向检查
- 版权风险检查

### 第7步：/导出 - 直接交付
```bash
# 导出完整项目
./short-drama-pro export --project "my_drama"

# 导出特定格式
./short-drama-pro export --format "markdown"
./short-drama-pro export --format "docx"
```

**导出内容**：
- 标准剧本结构（场次、场景、人物、台词）
- 专业拍摄备注（景别、灯光、音乐）
- 完整元信息（编剧、类型、时长、字数）
- 爽点标注和下集预告
- 角色档案和人物关系图
- 创作方案和目录

## 🌍 出海模式

### 启用出海模式
```bash
# 启动出海模式
./short-drama-pro start --overseas

# 英文剧本生成
./short-drama-pro episode 1 --language "en"
```

### 出海特色：
- **好莱坞行业标准格式**：INT./EXT.、CLOSE-UP等
- **英文台词优化**：避免中式英语
- **本地冲突机制**：符合欧美观众喜好
- **爽点本地化**：针对海外受众优化
- **文化元素库**：欧美文化参考

### 格式示例：
```
INT. HOSPITAL OPERATING ROOM - DAY

[WIDE SHOT] The operating room, under shadowless lamps, a tense surgery in progress.

[CLOSE UP] Beads of sweat form on the protagonist's forehead.

PROTAGONIST
(Calmly)
Hemostat.

NURSE
(Nervously)
Doctor, the patient's blood pressure is dropping!

[SOUND] Tense background music swells.
```

## 📊 商业化支持

### 收入参考
```bash
# 商业分析
./short-drama-pro analyze --commercial

# 收入预测
./short-drama-pro analyze --revenue
```

### 市场分析
- **平台偏好分析**：抖音、快手、B站、海外平台
- **受众分析**：年龄、性别、地域分布
- **竞争分析**：同类题材竞争情况
- **变现模式**：广告分成、付费观看、IP授权

### 投稿指导
- **平台要求**：各平台投稿格式和要求
- **审核标准**：内容审核要点
- **版权保护**：版权登记和维权
- **合同指导**：签约注意事项

## 🔧 技术架构

### 文件结构
```
short-drama-pro/
├── SKILL.md                    # 技能文档
├── _meta.json                  # 元数据
├── short-drama-pro             # 主程序
├── references/                 # 参考文档
│   ├── genre-guide.md          # 题材指南
│   ├── rhythm-design.md        # 节奏设计
│   ├── payment-strategy.md     # 付费策略
│   ├── opening-rules.md        # 开篇法则
│   ├── character-design.md     # 角色设计
│   ├── compliance-checklist.md # 合规清单
│   └── overseas-guide.md       # 出海指南
├── templates/                  # 模板文件
│   ├── script-template.md      # 剧本模板
│   ├── character-template.json # 角色模板
│   ├── plan-template.json      # 方案模板
│   └── catalog-template.md     # 目录模板
└── scripts/                    # 脚本文件
    ├── start.py                # 开始脚本
    ├── plan.py                 # 方案脚本
    ├── characters.py           # 角色脚本
    ├── catalog.py              # 目录脚本
    ├── episode.py              # 分集脚本
    ├── check.py                # 自检脚本
    └── export.py               # 导出脚本
```

### 参考文档内容
- **1500+行专业文档**：覆盖短剧创作全流程
- **实战经验提炼**：基于行业实战经验
- **方法论编码**：将"短剧的手艺"编码进文档
- **AI学习材料**：Claude创作前会先读参考材料

## ⚠️ 注意事项

### 创作要点
1. **选题要准**：选择有市场潜力的题材
2. **节奏要快**：前5秒必须抓人，每集结尾留钩子
3. **冲突要强**：设置明确的冲突和解决路径
4. **人物要活**：角色要有动机和成长
5. **格式要专**：使用专业剧本格式

### 合规要求
1. **政治敏感**：避免涉及政治敏感内容
2. **暴力血腥**：控制暴力血腥程度
3. **色情低俗**：避免色情低俗内容
4. **价值观**：符合社会主义核心价值观
5. **版权**：确保原创，避免侵权

### 商业建议
1. **市场调研**：创作前进行市场调研
2. **平台选择**：根据内容选择合适的平台
3. **版权保护**：及时进行版权登记
4. **合同审查**：仔细审查签约合同
5. **IP运营**：考虑IP的长期运营价值

## 📞 支持与反馈

### 问题反馈
- **技能问题**：技能使用中的技术问题
- **创作问题**：剧本创作中的专业问题
- **商业问题**：商业化运营中的问题
- **建议反馈**：对技能的改进建议

### 更新计划
- **v1.1**：增加更多题材模板
- **v1.2**：优化出海模式
- **v1.3**：增加AI辅助创作
- **v1.4**：集成更多平台API

### 学习资源
- **原文公众号**：钱来有道
- **作者**：冰河好帅
- **社群**：公众号底部栏加入社群
- **教程**：相关文章链接

---
*本技能基于微信公众号文章《短剧剧本创作 Skill 正式发布！》开发，遵循原文的7步工作流和专业方法论。仅供学习和创作使用。*