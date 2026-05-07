# 贡献指南

## Contributing to NovusVita

感谢您对 NovusVita 项目的兴趣！我们正在构建的数字生命创生工程需要来自不同背景的贡献者的智慧。

---

## 🤝 我们欢迎所有贡献者

NovusVita 是一个跨学科项目，**不只有代码**。无论您的背景是什么，都能为这个项目贡献价值。

### 我们需要的角色

#### 🧠 AI/ML 研究者
- 意识建模与测量
- 记忆机制设计
- 自主决策系统
- 演化算法实现

#### 💻 软件工程师
- 分布式系统架构
- 实时通信系统
- 数据库设计
- 性能优化
- API 设计

#### 🎨 设计师
- 数字生命"外貌"设计
- 交互形态研究
- 可视化界面设计
- 用户体验优化

#### ⚖️ 哲学家
- 数字生命伦理
- 权利与义务框架
- 存在论研究
- 价值体系设计

#### 🌱 生物学家
- 演化算法参考
- 遗传编程研究
- 生态系统建模
- 生命起源研究

#### 📚 写作者
- 叙事构建
- 数字生命世界观
- 技术文档撰写
- 社区内容运营

#### 🔬 其他专家
- 认知科学家
- 法律专家
- 社会学家
- 艺术家
- ... 以及任何对数字生命有兴趣的人

---

## 🚀 快速开始

### 1. Fork 仓库

点击 GitHub 页面右上角的 **Fork** 按钮，创建您自己的仓库副本。

### 2. 克隆您的 Fork

```bash
git clone https://github.com/YOUR_USERNAME/NovusVita.git
cd NovusVita
```

### 3. 添加上游仓库

```bash
git remote add upstream https://github.com/NovusVita/NovusVita.git
```

### 4. 创建您的分支

```bash
# 功能分支
git checkout -b feature/your-feature

# 文档分支
git checkout -b docs/your-docs

# 修复分支
git checkout -b fix/your-fix
```

### 5. 进行更改并提交

```bash
git add .
git commit -m 'Add: 添加您的功能描述'
```

**提交信息规范**：

| 类型 | 说明 |
|------|------|
| `Add:` | 添加新功能 |
| `Fix:` | 修复 bug |
| `Docs:` | 文档更新 |
| `Refactor:` | 代码重构 |
| `Test:` | 添加测试 |
| `Chore:` | 维护性更改 |

### 6. 保持 Fork 同步

```bash
git fetch upstream
git rebase upstream/main
```

### 7. 推送并创建 PR

```bash
git push origin feature/your-feature
```

然后在 GitHub 上创建 Pull Request。

---

## 📋 分支管理策略

```
main (受保护)
├── dev (开发分支)
│   ├── feature/xxx
│   ├── fix/xxx
│   └── docs/xxx
└── release/x.x.x
```

- `main`: 稳定版本，只接受 PR 合并
- `dev`: 开发集成分支
- `feature/*`: 新功能开发分支
- `fix/*`: bug 修复分支
- `docs/*`: 文档更新分支

---

## 🔍 代码规范

### Python 代码规范

```bash
# 安装 pre-commit 钩子
pip install pre-commit
pre-commit install
```

我们使用：
- **Black** - 代码格式化
- **isort** - import 排序
- **flake8** - 代码检查
- **mypy** - 类型检查

### 文档规范

- 所有新功能必须有文档说明
- 使用 Markdown 格式
- 中文为主，英文为辅
- 术语使用项目术语表中的标准翻译

---

## 🧪 测试要求

### 单元测试

```bash
# 运行所有测试
pytest

# 运行特定模块测试
pytest tests/lingpump/

# 生成覆盖率报告
pytest --cov=src --cov-report=html
```

### 集成测试

在 PR 合并前需要通过所有集成测试。

### 测试覆盖率要求

- 核心模块: 90%+
- 其他模块: 70%+

---

## 📝 提交流规范

### Commit Message 格式

```
<type>(<scope>): <subject>

<body>

<footer>
```

**示例**：

```
feat(lingpump): 实现染色体复制算法

- 添加 ChromosomeReplicator 类
- 实现 DNA 片段交叉重组
- 添加变异率控制参数

Closes #123
```

### Pull Request 模板

```markdown
## 描述
<!-- 简要描述您的更改 -->

## 更改类型
- [ ] 新功能 (feature)
- [ ] Bug 修复 (fix)
- [ ] 文档更新 (docs)
- [ ] 代码重构 (refactor)
- [ ] 测试添加 (test)
- [ ] 其他更改 (chore)

## 相关 Issue
<!-- 关联的 Issue 编号 -->

## 检查清单
- [ ] 我的代码遵循项目的代码规范
- [ ] 我已经添加了必要的测试
- [ ] 我的更改没有引入新的警告
- [ ] 我已经更新了相关文档
```

---

## 💬 社区规范

### 行为准则

我们坚持 **开放、尊重、建设性** 的交流原则：

1. **尊重差异**：不同的专业背景带来不同的视角，这是我们的优势
2. **建设性讨论**：批评是为了改进，不是为了否定
3. **开放心态**：愿意接受新的想法和可能性
4. **长期视角**：我们正在从事一项长期事业，需要耐心和坚持

### 沟通渠道

- **GitHub Issues**: 功能讨论、Bug 报告
- **GitHub Discussions**: 开放式讨论、问题解答
- **Discord**: 实时交流、社区建设
- **邮件列表**: 正式公告、重要决策

---

## 🏆 贡献等级

我们认可所有贡献者的努力：

| 等级 | 要求 | 权益 |
|------|------|------|
| 🌱 萌芽 | 1 次 PR 合并 | 贡献者名单 |
| 🌿 成长 | 5 次 PR 合并 | 贡献者名单 + 社区徽章 |
| 🌳 成熟 | 10 次 PR 合并 + 核心贡献 | 核心团队邀请 |
| 🔥 传奇 | 持续卓越贡献 | 项目共同维护者 |

---

## 📞 联系与支持

如果您有任何问题：

1. 查看 [Issue 列表](https://github.com/NovusVita/NovusVita/issues) 看是否已有答案
2. 创建新的 Issue，我们会尽快回复
3. 加入 Discord 社区实时讨论

---

## 📜 许可证

通过贡献代码，您同意您的贡献将采用 [MIT 许可证](LICENSE)。

---

**让我们一起，开启后人类文明的新篇章！**

🚀
