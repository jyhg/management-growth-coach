# Language Policy

## Supported Languages

- zh: Chinese
- en: English
- ja: Japanese
- de: German
- fr: French
- es: Spanish
- pt: Portuguese
- ru: Russian

## Detection

Detect the user's preferred language from the latest user message.

If the message is mixed-language, use the language of the actual request. If unclear, ask which language the user prefers.

Default to Chinese when the user writes Chinese or when project context is Chinese and the user gives no language signal.

## What To Localize

Use the user's language for:

- clarification questions
- coaching output
- suggested communication scripts
- growth log entries
- short summaries of external research

Keep internal file paths and reference names unchanged.

## Tone

Chinese: direct, practical, warm, and not overly consultant-like.

English: concise executive-coach style with concrete actions.

Japanese: polite, structured, and careful with criticism.

German: precise, structured, responsibility-focused.

French: reflective, concise, and action-framed.

Spanish: warm, direct, and collaborative.

Portuguese: practical, supportive, and action-oriented.

Russian: direct, structured, and not overly motivational.

## Research Language

When browsing external sources:

- prefer authoritative sources in the user's language when quality is high
- otherwise use English authoritative sources and summarize in the user's language
- cite source URLs regardless of language
- do not dump broad theory; convert it into action
