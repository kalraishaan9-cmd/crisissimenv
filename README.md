---
title: CrisisSimEnv
emoji: 🚨
colorFrom: red
colorTo: blue
sdk: docker
app_port: 7860
---

# CrisisSim: Cyber-Incident Response Environment

CrisisSim is an OpenEnv-compliant simulation designed for evaluating AI agents on real-world Cybersecurity Incident Response (IR).

## 🛡️ Task Description
The agent acts as an Incident Commander. It receives a live scenario (Observation) and must issue natural language commands (Action) to mitigate threats.

## 🚀 Setup & Usage
1. **Local Build:** `docker build -t crisissim .`
2. **Local Run:** `docker run -p 7860:7860 crisissim`
3. **Inference:** Run `python inference.py` after setting your `HF_TOKEN`.

## 📊 Action & Observation Space
- **Action:** `decision` (string) - Natural language IR commands.
- **Observation:** `scenario` (string), `threat_level` (float), `history` (list).