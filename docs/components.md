# Components, Tools, and Action Format

[← Repository overview](../README.md)

## Unified model-provider contract

The completed Python controller used a common `chat(messages)` interface with three channels:

| Channel | Purpose | Evidence level |
|---|---|---|
| Demo | Scripted, deterministic actions for loop tests | Channel tested |
| Ollama | Local model via its chat HTTP API | Connectivity and structured output tested |
| Online DeepSeek API | Online JSON-formatted model actions | Used in successful complete matrix runs and A/B verification |

The channel is selected using `--model demo`, `--model ollama`, or `--model online`. Provider credentials are **not** present here.

## One proposed action per turn

An *illustrative* structured response (not extracted from any private log):

```json
{
  "think": "Inspect the requirements before proposing code.",
  "tool": "read_file",
  "args": {"path": "README.md"}
}
```

Every returned action goes through JSON parsing and registered-tool argument validation.

## Registered tools

| Tool | Arguments | Function | Guardrail |
|---|---|---|---|
| `read_file` | `path` | Return text from a UTF-8 file | Errors returned to agent |
| `write_file` | `path`, `content` | Save a UTF-8 file | Path/content preview + human approval |
| `run_bash` | `cmd` | Run a shell command | 20-second timeout, output limited to 2,000 characters |
| `finish` | `summary` | End the loop | Natural exit and final status |

The registry checks missing required fields, wrong types, extra fields, and unknown tools. The `finish` action is a controller action rather than a filesystem or shell tool.

## Human approval before writes

The controller displays the proposed write destination and the first ten lines. In interactive mode, a `y` response permits the write and an `n` response blocks it. The decision is recorded in the per-turn audit log as `approved: true` or `approved: false`.

## JSONL audit schema

Each turn has fields:

```json
{
  "turn": 3,
  "tool": "run_bash",
  "args": {"cmd": "python check_matrix.py"},
  "ok": true,
  "summary": "Checker was executed.",
  "approved": null
}
```

*Illustrative schema record. This is not a copied runtime log.* Real `summary` text, arguments, and turn numbers depend on the actual run.

The full lab source, private checker, and execution logs are not published in this portfolio.
