# 管理成长教练 Skill

默认语言：中文。This README is multilingual: 中文, English, 日本語, Deutsch, Français, Español, Português, Русский.

`management-growth-coach` 是一个面向管理者的 Codex skill，用于管理自查、团队成员辅导、向上汇报、跨团队协作、项目复盘、管理理论选择、多语言管理陪练和长期成长日志沉淀。

## 功能亮点

- 管理场景自查：任务交付、团队成员、向上汇报、跨团队协作、复盘、激励、授权、业务价值和纯学习场景。
- 盲点提醒：外向归因、解释过多、忽略人的压力和边界、局部 KPI 优化、过早升级、反思没有行动等。
- DISC 适配：支持 D/I/S/C 倾向下的沟通和辅导注意点，但不会把 DISC 当成固定标签。
- 多语言输出：支持中文、英文、日语、德语、法语、西班牙语、葡萄牙语、俄语。
- 管理知识库：内置古典管理、行为科学、现代管理理论、战略、运营质量、人力资源、创新变革、项目风险、沟通协作和问题解决工具。
- 本地优先 + 联网补充：先使用本地初始化知识，再在需要时检索公开可信资料，并整合回答。
- 用户确认后沉淀：用户认可且明确要求保存时，外部公开知识先进入 `references/knowledge_inbox.md`，不会直接污染稳定知识库。
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
17 tests passed
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
- 联网检索前会做问题脱敏，不应把公司、产品、人员、客户、项目、本地路径、凭据或 token 放进搜索查询。
- 即使用户认可一次回答，也不会直接写入 `management_library.md`；外部知识先进入 append-only `knowledge_inbox.md`。
- 公开分享前请清理 `references/personal_context.md` 和 `references/reflection_log.md` 中的个人、公司、项目和团队信息。
- 如果你把成长日志用于真实管理场景，建议定期检查是否有敏感信息。

## English

### Features

- Reviews management scenes: delivery, team members, upward reporting, cross-team collaboration, retrospectives, motivation, delegation, business value, and learning-only questions.
- Highlights blind spots: external attribution, too much explanation, missed pressure or role boundaries, local KPI optimization, premature escalation, and reflection without action.
- Supports DISC-aware coaching without treating DISC as a fixed label.
- Supports Chinese, English, Japanese, German, French, Spanish, Portuguese, and Russian output.
- Includes a starter management library covering classic, behavioral, modern, strategic, quality, HR, change, project, risk, communication, and problem-solving tools.
- Uses local knowledge first, then public credible web research when useful.
- Saves accepted external knowledge first to `references/knowledge_inbox.md`, not directly to the stable library.

### When to use

- Preparing upward reporting with plans, commitments, and closure.
- Preparing feedback or 1:1 conversations.
- Diagnosing project delay, cross-team friction, or resource gaps.
- Choosing a management theory, methodology, philosophy, or tool.
- Turning weekly reflection into a reusable management playbook.

### Quick start

```text
Use management-growth-coach to review a cross-team collaboration issue.
```

If context is missing, the skill asks what happened, who is involved, what result or relationship is at risk, and what decision or conversation is needed next.

### Install

```bash
cp -R management-growth-coach ~/.codex/skills/management-growth-coach
```

If the folder already exists, back it up before replacing it.

### Validate

```bash
python3 tests/run_tests.py
```

Expected: `17 tests passed`.

### Notes

- This is a management reflection and learning aid, not legal, HR policy, medical, or psychological advice.
- Sanitize private company, product, project, customer, path, credential, and token details before web search.
- Accepted web knowledge goes to the append-only inbox first.

## 日本語

### 機能

- タスク遂行、メンバー支援、上位報告、部門横断協業、振り返り、動機づけ、委任、事業価値、学習のみの相談を整理します。
- 外部要因への偏り、説明過多、人のプレッシャーや役割境界の見落とし、局所 KPI 最適化、早すぎるエスカレーション、行動につながらない反省を検出します。
- DISC を仮説として使い、固定ラベルとして扱いません。
- 中国語、英語、日本語、ドイツ語、フランス語、スペイン語、ポルトガル語、ロシア語に対応します。
- 古典管理、行動科学、戦略、品質、HR、変革、プロジェクト、リスク、コミュニケーション、問題解決の基礎知識を含みます。
- まずローカル知識を使い、必要な場合だけ公開された信頼できる情報を検索します。
- 承認された外部知識は、安定版ライブラリではなく `references/knowledge_inbox.md` に保存します。

### 使う場面

- 上位報告で、理由説明よりも案・約束・完了条件を明確にしたいとき。
- メンバーへのフィードバックや 1on1 を準備するとき。
- プロジェクト遅延、部門間摩擦、リソース不足を整理するとき。
- どの管理理論・方法論・ツールを使うべきか判断したいとき。
- 毎週の振り返りを再利用できる管理プレイブックにしたいとき。

### クイックスタート

```text
management-growth-coach で部門横断協業の問題を振り返ってください。
```

情報が足りない場合、何が起きたか、誰が関係しているか、どの結果や関係が危ないか、次に必要な判断や会話は何かを確認します。

### インストール

```bash
cp -R management-growth-coach ~/.codex/skills/management-growth-coach
```

同名フォルダがある場合は、置き換える前にバックアップしてください。

### 検証

```bash
python3 tests/run_tests.py
```

期待結果: `17 tests passed`。

### 注意事項

- 法務、HR 制度、医療、心理専門助言の代替ではありません。
- Web 検索前に会社名、製品名、案件名、顧客名、パス、認証情報、token を除去してください。
- 承認された外部知識は、まず append-only の inbox に保存します。

## Deutsch

### Funktionen

- Prüft Managementsituationen: Lieferung, Teammitglieder, Bericht nach oben, teamübergreifende Zusammenarbeit, Retrospektive, Motivation, Delegation, Geschäftswert und reine Lernfragen.
- Erkennt blinde Flecken: externe Schuldzuweisung, zu viele Erklärungen, übersehener Druck oder Rollenunklarheit, lokale KPI-Optimierung, zu frühe Eskalation und Reflexion ohne Handlung.
- Nutzt DISC als Arbeitshypothese, nicht als festes Etikett.
- Unterstützt Chinesisch, Englisch, Japanisch, Deutsch, Französisch, Spanisch, Portugiesisch und Russisch.
- Enthält eine Managementbibliothek zu klassischen, verhaltenswissenschaftlichen, strategischen, Qualitäts-, HR-, Change-, Projekt-, Risiko-, Kommunikations- und Problemlösungswerkzeugen.
- Nutzt zuerst lokales Wissen und ergänzt bei Bedarf glaubwürdige öffentliche Webquellen.
- Speichert akzeptiertes externes Wissen zuerst in `references/knowledge_inbox.md`, nicht direkt in der stabilen Bibliothek.

### Wann verwenden

- Für Berichte nach oben mit Plan, Commitment und Abschlusslogik.
- Für Feedbackgespräche oder 1:1-Vorbereitung.
- Für Projektverzug, teamübergreifende Reibung oder Ressourcenlücken.
- Zur Auswahl passender Managementtheorie, Methodik, Philosophie oder Tools.
- Um wöchentliche Reflexion in ein wiederverwendbares Führungs-Playbook zu überführen.

### Schnellstart

```text
Nutze management-growth-coach, um ein Problem in der teamübergreifenden Zusammenarbeit zu prüfen.
```

Fehlt Kontext, fragt der Skill, was passiert ist, wer beteiligt ist, welches Ergebnis oder welche Beziehung gefährdet ist und welche Entscheidung oder welches Gespräch als Nächstes nötig ist.

### Installation

```bash
cp -R management-growth-coach ~/.codex/skills/management-growth-coach
```

Wenn der Ordner bereits existiert, vor dem Ersetzen sichern.

### Validierung

```bash
python3 tests/run_tests.py
```

Erwartung: `17 tests passed`.

### Hinweise

- Dies ist eine Reflexions- und Lernhilfe, kein Ersatz für Recht, HR-Richtlinien, Medizin oder Psychologie.
- Vor Websuche private Firmen-, Produkt-, Projekt-, Kunden-, Pfad-, Credential- und Token-Details entfernen.
- Akzeptiertes Webwissen wird zuerst in der append-only Inbox gespeichert.

## Français

### Fonctionnalités

- Analyse les situations de management : livraison, collaborateurs, reporting ascendant, collaboration transverse, rétrospective, motivation, délégation, valeur métier et apprentissage.
- Repère les angles morts : attribution externe, excès d’explication, pression ou frontières de rôle ignorées, optimisation locale des KPI, escalade trop rapide, réflexion sans action.
- Utilise DISC comme hypothèse de travail, pas comme étiquette fixe.
- Prend en charge le chinois, l’anglais, le japonais, l’allemand, le français, l’espagnol, le portugais et le russe.
- Inclut une bibliothèque de management : classique, comportemental, stratégie, qualité, RH, changement, projet, risque, communication et résolution de problèmes.
- Utilise d’abord la connaissance locale, puis ajoute des sources publiques fiables si nécessaire.
- Enregistre les connaissances externes acceptées dans `references/knowledge_inbox.md`, pas directement dans la bibliothèque stable.

### Quand l’utiliser

- Préparer un reporting ascendant avec plan, engagement et boucle de clôture.
- Préparer un feedback ou un entretien 1:1.
- Diagnostiquer un retard projet, un conflit transverse ou un manque de ressources.
- Choisir une théorie, méthode, philosophie ou outil de management.
- Transformer une réflexion hebdomadaire en playbook de management réutilisable.

### Démarrage rapide

```text
Utilise management-growth-coach pour analyser un problème de collaboration transverse.
```

Si le contexte manque, le skill demande ce qui s’est passé, qui est impliqué, quel résultat ou quelle relation est en risque, et quelle décision ou conversation est nécessaire.

### Installation

```bash
cp -R management-growth-coach ~/.codex/skills/management-growth-coach
```

Si le dossier existe déjà, sauvegardez-le avant remplacement.

### Validation

```bash
python3 tests/run_tests.py
```

Résultat attendu : `17 tests passed`.

### Notes

- Ce skill aide à réfléchir et apprendre ; il ne remplace pas les règles RH, le droit, la médecine ou la psychologie.
- Avant une recherche web, anonymisez entreprise, produit, projet, client, chemin local, identifiants et token.
- Les connaissances web acceptées vont d’abord dans une inbox append-only.

## Español

### Funciones

- Revisa situaciones de gestión: entrega, miembros del equipo, reporte ascendente, colaboración entre equipos, retrospectivas, motivación, delegación, valor de negocio y aprendizaje.
- Detecta puntos ciegos: atribución externa, demasiadas explicaciones, presión o límites de rol ignorados, optimización local de KPI, escalada prematura y reflexión sin acción.
- Usa DISC como hipótesis de trabajo, no como etiqueta fija.
- Soporta chino, inglés, japonés, alemán, francés, español, portugués y ruso.
- Incluye una biblioteca de management: clásico, comportamiento, estrategia, calidad, RR. HH., cambio, proyecto, riesgo, comunicación y resolución de problemas.
- Usa primero el conocimiento local y añade investigación web pública confiable cuando sea útil.
- Guarda el conocimiento externo aceptado en `references/knowledge_inbox.md`, no directamente en la biblioteca estable.

### Cuándo usarlo

- Preparar reportes hacia arriba con plan, compromiso y cierre.
- Preparar feedback o conversaciones 1:1.
- Diagnosticar retrasos, fricción entre equipos o falta de recursos.
- Elegir una teoría, metodología, filosofía o herramienta de gestión.
- Convertir reflexiones semanales en un playbook reutilizable.

### Inicio rápido

```text
Usa management-growth-coach para revisar un problema de colaboración entre equipos.
```

Si falta contexto, el skill pregunta qué ocurrió, quién está involucrado, qué resultado o relación está en riesgo y qué decisión o conversación viene después.

### Instalación

```bash
cp -R management-growth-coach ~/.codex/skills/management-growth-coach
```

Si ya existe la carpeta, haz una copia de seguridad antes de reemplazarla.

### Validación

```bash
python3 tests/run_tests.py
```

Resultado esperado: `17 tests passed`.

### Notas

- Es una ayuda de reflexión y aprendizaje, no sustituye políticas de RR. HH., asesoría legal, médica o psicológica.
- Antes de buscar en la web, elimina empresa, producto, proyecto, cliente, rutas locales, credenciales y token.
- El conocimiento web aceptado entra primero en una inbox append-only.

## Português

### Funcionalidades

- Revisa situações de gestão: entrega, membros da equipe, reporte para liderança, colaboração entre equipes, retrospectivas, motivação, delegação, valor de negócio e aprendizado.
- Identifica pontos cegos: atribuição externa, excesso de explicação, pressão ou limites de papel ignorados, otimização local de KPI, escalada precoce e reflexão sem ação.
- Usa DISC como hipótese de trabalho, não como rótulo fixo.
- Suporta chinês, inglês, japonês, alemão, francês, espanhol, português e russo.
- Inclui biblioteca de gestão: clássica, comportamental, estratégia, qualidade, RH, mudança, projeto, risco, comunicação e solução de problemas.
- Usa primeiro o conhecimento local e adiciona pesquisa web pública confiável quando útil.
- Salva conhecimento externo aceito em `references/knowledge_inbox.md`, não diretamente na biblioteca estável.

### Quando usar

- Preparar reporte para liderança com plano, compromisso e fechamento.
- Preparar feedback ou conversas 1:1.
- Diagnosticar atraso de projeto, atrito entre equipes ou falta de recursos.
- Escolher uma teoria, metodologia, filosofia ou ferramenta de gestão.
- Transformar reflexão semanal em um playbook reutilizável.

### Início rápido

```text
Use management-growth-coach para revisar um problema de colaboração entre equipes.
```

Se faltar contexto, o skill pergunta o que aconteceu, quem está envolvido, qual resultado ou relação está em risco e qual decisão ou conversa vem a seguir.

### Instalação

```bash
cp -R management-growth-coach ~/.codex/skills/management-growth-coach
```

Se a pasta já existir, faça backup antes de substituir.

### Validação

```bash
python3 tests/run_tests.py
```

Resultado esperado: `17 tests passed`.

### Notas

- É um apoio para reflexão e aprendizado, não substitui políticas de RH, aconselhamento jurídico, médico ou psicológico.
- Antes da busca web, remova empresa, produto, projeto, cliente, caminhos locais, credenciais e token.
- Conhecimento web aceito vai primeiro para uma inbox append-only.

## Русский

### Возможности

- Разбирает управленческие ситуации: поставка результата, сотрудники, отчёт наверх, кросс-командная работа, ретроспектива, мотивация, делегирование, бизнес-ценность и обучение.
- Находит слепые зоны: внешняя атрибуция, избыток объяснений, игнорирование давления или границ роли, локальная оптимизация KPI, преждевременная эскалация и рефлексия без действия.
- Использует DISC как рабочую гипотезу, а не как ярлык.
- Поддерживает китайский, английский, японский, немецкий, французский, испанский, португальский и русский языки.
- Включает библиотеку управления: классический менеджмент, поведенческие подходы, стратегия, качество, HR, изменения, проекты, риски, коммуникация и решение проблем.
- Сначала использует локальные знания, затем при необходимости добавляет надёжные публичные веб-источники.
- Сохраняет принятое внешнее знание в `references/knowledge_inbox.md`, а не сразу в стабильную библиотеку.

### Когда использовать

- Подготовить отчёт руководству с планом, обязательствами и закрытием цикла.
- Подготовить обратную связь или 1:1.
- Разобрать задержку проекта, трение между командами или нехватку ресурсов.
- Выбрать управленческую теорию, методологию, философию или инструмент.
- Превратить еженедельную рефлексию в повторно используемый playbook.

### Быстрый старт

```text
Используй management-growth-coach, чтобы разобрать проблему кросс-командного взаимодействия.
```

Если контекста не хватает, skill спросит, что произошло, кто вовлечён, какой результат или отношения под риском и какое решение или разговор нужен дальше.

### Установка

```bash
cp -R management-growth-coach ~/.codex/skills/management-growth-coach
```

Если папка уже существует, сделайте резервную копию перед заменой.

### Проверка

```bash
python3 tests/run_tests.py
```

Ожидаемый результат: `17 tests passed`.

### Примечания

- Это инструмент для управленческой рефлексии и обучения, а не замена HR-политик, юридической, медицинской или психологической консультации.
- Перед веб-поиском удаляйте названия компаний, продуктов, проектов, клиентов, локальные пути, credentials и token.
- Принятое веб-знание сначала попадает в append-only inbox.
