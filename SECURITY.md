# Public Repository Safety

[← Repository overview](README.md)

This is a documentation-only technical showcase; it does not contain the runnable assignment source or private grading assets.

## Intentionally excluded

- API keys, tokens, local `.env` configuration, credentials, request headers, and shell history
- Names, student numbers, school details, emails, usernames, home directory paths, or local machine identifiers
- Full Python agent source, teacher-provided starter/fixtures/checker, report documents and original assignment attachments
- Raw JSONL tool logs and terminal screenshots (may include file contents or device information)

Before committing future changes, review **both** file contents and Git history for sensitive strings. `.gitignore` helps prevent accidental commits but does not protect already committed data.

This repository's `scripts/render_charts.py` operates only on `data/metrics.json`, uses no credentials and makes no network requests.
