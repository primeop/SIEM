# 🔐 Secure SDLC & DevSecOps Pipeline

This project demonstrates a CI/CD-integrated secure software development lifecycle using GitHub Actions, Semgrep, OWASP ZAP, Trivy, and SBOM generation.

## 🔧 Features

- ✅ **SAST**: Semgrep (with optional SonarQube)
- 🧪 **DAST**: OWASP ZAP Baseline Scan
- 📦 **Container Scanning**: Trivy
- 📜 **SBOM Generation**: CycloneDX JSON
- 🔁 **CWE/Severity Enrichment**: Python script for tagging
- 🛡️ **Supply Chain Integrity**: SLSA Compliance (optional)

## 📂 Folder Breakdown

- `.github/workflows/`: CI/CD pipeline
- `sast/`: Semgrep rules
- `dast/`: ZAP config
- `containers/`: Sample app and Dockerfile
- `scripts/`: Alert enrichment tooling
- `sbom/`: SBOM artifacts

## ▶️ Running Locally

```bash
pip install -r requirements.txt
semgrep --config auto containers/app.py
docker build -t secure-app containers/
trivy image --format cyclonedx -o sbom/sbom.cdx.json secure-app
```

## 🚀 CI/CD Pipeline
The `ci-devsecops.yml` workflow runs on every PR and automates security checks.
