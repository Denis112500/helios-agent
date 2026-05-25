# CLAUDE.md — helios-agent

## What this is
A custom Python AI agent built from scratch. Positioned as a "build-your-own-agent" educational OSS repo — the code is the tutorial. Goal: a clean, hackable agent someone can read in one sitting.

## Stack (firm)
- Python 3.10+
- GPT-4.1 via GitHub Copilot, routed through a local LiteLLM proxy
- Qwen3 (4B or 30B-A3B MoE) as planned fallback via LiteLLM config swap (deferred until tool-calling reliability is verified)
- Terminal UI with `rich`
- SQLite for conversation persistence
- NO frameworks (no LangChain, CrewAI, AutoGen, smolagents) — building from primitives is the entire point

## Build phases
- [x] Phase 0: setup (venv, .gitignore, README) ← current
- [x] Phase 1: GPT-4.1 reply via LiteLLM
- [x] Phase 2: agent loop with conversation history
- [ ] Phase 3: tool calling (read_file, list_directory)
- [ ] Phase 4: dangerous tools with confirmation (write_file, run_shell_command)
- [ ] Phase 5: rich terminal UI + SQLite persistence
- [ ] Phase 6: specialized tools (e.g. git wrapper)
- [ ] Phase 7: polish (config, logging, error handling) + final PDF doc

## Conventions
- Commit per feature, descriptive messages (Conventional Commits: `feat:`, `fix:`, `chore:`). The commits are the spine of the eventual PDF doc, so they need to read well.
- Single file (`helios.py`) until size genuinely forces a split. No premature module structure.
- No new dependencies without asking Denis. If stdlib does it, use stdlib.
- Comments only where code is non-obvious.

## Working style
- This is a LEARNING project for Denis. Do not write code Denis can't explain.
- If implementing something complex, leave a one-line comment naming the concept it demonstrates.
- Build first, write tutorial chapters after. Do NOT generate tutorial prose, chapter content, or extensive READMEs ahead of the code.
- If Denis is stuck on a concept, explain the concept — don't bypass the learning by writing the code wholesale.

## Anti-patterns
- Adding async without a real reason
- Pulling in a framework "for convenience"
- Generating large code blocks with no explanation
- Premature config files / abstraction layers
- LLM-provider-specific code (everything routes through LiteLLM)
