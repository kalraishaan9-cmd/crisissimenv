---
title: CrisisSimEnv
emoji: 🚨
colorFrom: red
colorTo: gray
sdk: docker
app_port: 7860
---

# CrisisSim: Cyber-Incident Response Environment

CrisisSim is an OpenEnv-compliant simulation designed for evaluating AI agents on real-world Cybersecurity Incident Response (IR).

CrisisSim is an OpenEnv-compliant simulation designed for evaluating AI agents on real-world Cybersecurity Incident Response (IR).

## 🛡️ Task Description
The agent acts as an Incident Commander. It receives a live scenario (Observation) and must issue natural language commands (Action) to mitigate threats.

### Action Space
- **Type:** `CrisisAction` (Pydantic Model)
- **Field:** `decision` (String) - e.g., "Isolate the affected server and revoke admin tokens."

### Observation Space
- **Scenario:** Current situation description.
- **Threat Level:** A float (1.0 to 0.0) representing risk remaining.
- **History:** List of previous actions taken in the episode.

## 📊 Performance & Grading
Grading is programmatic based on keyword coverage and threat reduction:
- **Easy:** Phishing Scam (Keywords: reset, notify, block)
- **Medium:** Ransomware Outbreak (Keywords: shutdown, segment, backup)
- **Hard:** Data Exfiltration (Keywords: firewall, forensics, revoke)

**Reward Function:** `0.15` per unique relevant keyword + `0.2` completion bonus.

## 🚀 Setup & Usage
1. Build: `docker build -t crisissim .`
2. Run: `docker run -p 7860:7860 crisissim`
3. Baseline: `python inference.py` (Ensure `HF_TOKEN` and `API_BASE_URL` are set)

## 🛠️ OpenEnv Compliance
- Implements `step()`, `reset()`, and `state()` endpoints via FastAPI.
- Uses typed Pydantic models for all communications.
- Provides a meaningful reward signal for partial task completion.
