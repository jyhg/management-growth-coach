# 管理成长教练 Skill

默认语言：中文。This README is multilingual and includes concise English, 日本語, Deutsch, Français, Español, Português, and Русский sections below.

`management-growth-coach` 是一个面向管理者的 Codex skill，用于管理自查、团队成员辅导、向上汇报、跨团队协作、项目复盘、管理理论选择、多语言管理陪练和长期成长日志沉淀。

## 功能亮点

- 管理场景自查：任务交付、团队成员、向上汇报、跨团队协作、复盘、激励、授权、业务价值和纯学习场景。
- 盲点提醒：外向归因、解释过多、忽略人的压力和边界、局部 KPI 优化、过早升级、反思没有行动等。
- DISC 适配：支持 D/I/S/C 倾向下的沟通和辅导注意点，但不会把 DISC 当成固定标签。
- 多语言输出：支持中文、英文、日语、德语、法语、西班牙语、葡萄牙语、俄语。
- 管理知识库：内置古典管理、行为科学、现代管理理论、战略、运营质量、人力资源、创新变革、项目风险、沟通协作和问题解决工具。
- 长期成长机制：支持一次性快速使用、每周使用、每周两次使用、月度模式复盘和半年成长周期。
- 成长日志：每次调用可生成可追加的成长日志条目，便于持续复盘。

## 适合什么时候用

- 准备向上汇报，希望少解释、多给方案和承诺。
- 准备给团队成员做正反馈、负反馈或 1:1。
- 项目延期、跨团队不配合、资源不足，需要拆解下一步。
- 想判断一个管理问题该用什么理论、方法论或工具。
- 想把每周管理反思沉淀为可复用的管理打法。

## 快速开始

在 Codex 中直接说：

```text
用 management-growth-coach 帮我复盘一个跨部门协作问题。
```

或：

```text
帮我准备一次向上汇报，我想先给方案、承诺和闭环结果。
```

如果你没有给足上下文，skill 会先问四个问题：

1. 发生了什么？
2. 涉及哪些人？
3. 哪个结果或关系正在面临风险？
4. 下一步需要做什么决策或谈话？

## 安装

把本仓库复制到 Codex skills 目录：

```bash
cp -R management-growth-coach ~/.codex/skills/management-growth-coach
```

如果本地已经存在同名目录，建议先备份再替换：

```bash
mv ~/.codex/skills/management-growth-coach ~/.codex/skills/management-growth-coach.bak.$(date +%Y%m%d%H%M%S)
cp -R management-growth-coach ~/.codex/skills/management-growth-coach
```

安装后重启 Codex，让新 skill 生效。

## 验证

在仓库根目录运行：

```bash
python3 tests/run_tests.py
```

期望输出：

```text
13 tests passed
```

## 目录说明

- `SKILL.md`：skill 主协议，默认中文说明，保留多语言触发信息。
- `references/`：语言策略、管理知识库、管理打法、成长日志模板等。
- `tests/`：结构和 E2E 合约测试。
- `docs/`：规格、计划、研究、测试和验证记录。
- `agents/openai.yaml`：Codex UI 元信息。

## 注意事项

- 这个 skill 是管理反思和学习辅助，不替代组织制度、HR 流程、法律建议或医疗心理建议。
- DISC 只作为沟通假设，不能作为给人贴标签的依据。
- 公开分享前请清理 `references/personal_context.md` 和 `references/reflection_log.md` 中的个人、公司、项目和团队信息。
- 如果你把成长日志用于真实管理场景，建议定期检查是否有敏感信息。

## English

Management Growth Coach helps managers reflect on real situations, identify blind spots, choose useful management frameworks, prepare communication scripts, and create growth log entries. It supports management self-checks, team feedback, upward reporting, cross-team collaboration, retrospectives, delegation, motivation, and multilingual coaching.

Install by copying the repository to `~/.codex/skills/management-growth-coach`, then restart Codex. Validate with `python3 tests/run_tests.py`.

## 日本語

Management Growth Coach は、管理上の出来事を振り返り、盲点を見つけ、適切な管理フレームワークを選び、会話スクリプトと成長ログを作るための skill です。インストール後は Codex を再起動してください。

## Deutsch

Management Growth Coach unterstützt Führungskräfte bei Reflexion, Feedback, Eskalation, Zusammenarbeit, Delegation, Motivation und langfristigem Lernprotokoll. Nach der Installation Codex neu starten.

## Français

Management Growth Coach aide à analyser des situations de management, identifier les angles morts, choisir des cadres utiles, préparer des formulations et conserver un journal de progression. Redémarrez Codex après installation.

## Español

Management Growth Coach ayuda a revisar situaciones de gestión, detectar puntos ciegos, elegir marcos de management, preparar conversaciones y guardar aprendizajes. Reinicia Codex después de instalarlo.

## Português

Management Growth Coach ajuda na reflexão de gestão, feedback, colaboração entre equipes, delegação, motivação e registro de aprendizados. Reinicie o Codex após instalar.

## Русский

Management Growth Coach помогает разбирать управленческие ситуации, находить слепые зоны, выбирать подходящие управленческие инструменты, готовить формулировки и вести журнал роста. После установки перезапустите Codex.
