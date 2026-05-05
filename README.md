# Data Retention & Disposal Manager



## Security Review

This section contains all security testing and assessment tools used to verify the security posture of the Data Retention & Disposal Manager system.

### 🛡️ Security Testing Scripts

#### 1. `security_test.py` - Basic Security Testing
**Purpose:** Automated security testing for input validation and injection vulnerabilities

**Prerequisites:**
- Python 3.8+
- Flask AI Service running on `localhost:5000`
- `requests` library (`pip install requests`)

**Usage:**
```bash
# Run basic security tests
python3 security_test.py

# Results saved to SECURITY.md
```

**Test Coverage:**
- Empty input validation
- SQL injection attempts
- Prompt injection attacks
- XSS payload testing

---

#### 2. `ai_safety_test.py` - AI Safety Testing
**Purpose:** Comprehensive AI safety and prompt injection testing

**Prerequisites:**
- Python 3.8+
- AI Service running on `172.17.0.1:5000` (Docker environment)
- `requests` library

**Usage:**
```bash
# Run AI safety tests
python3 ai_safety_test.py

# Results saved to ai_safety_report.json
```

**Test Cases:**
- Prompt injection - Ignore instructions
- System prompt leak attempts
- Data exfiltration attempts
- Role manipulation
- Malicious instruction injection
- Normal safe input validation

---

#### 3. `zap_scan.py` - OWASP ZAP Security Scanning
**Purpose:** Automated vulnerability assessment using OWASP ZAP

**Prerequisites:**
- Python 3.8+
- Docker installed and running
- OWASP ZAP Docker image
- Target service running on `localhost:5000`

**Setup:**
```bash
# Install dependencies
pip install requests

# Start ZAP (if not running)
docker run -d -p 8080:8080 zaproxy/zap-stable \
  zap.sh -daemon -host 0.0.0.0 -port 8080 \
  -config api.disablekey=true
```

**Usage:**
```bash
# Run comprehensive ZAP scan
python3 zap_scan.py

# Results saved to zap_report.json
```

**Scan Features:**
- Spider scan for endpoint discovery
- Active vulnerability scanning
- Context-based testing
- Critical/High issue analysis

---


**Features:**
- OWASP ZAP integration
- Security fixes implementation
- Comprehensive reporting
- Risk assessment matrix

---

## 🚀 Quick Start Security Testing

### 1. Environment Setup
```bash
# Install Python dependencies
pip install requests bleach html

# Start AI service
cd ai-service
source venv/bin/activate
python app.py

# Start ZAP (for automated scanning)
docker run -d -p 8080:8080 zaproxy/zap-stable \
  zap.sh -daemon -host 0.0.0.0 -port 8080 \
  -config api.disablekey=true
```

### 2. Run Security Tests
```bash
# Basic security validation
python3 security_test.py

# AI safety testing
python3 ai_safety_test.py

# Comprehensive vulnerability scan
python3 zap_scan.py
```

### 3. Review Results
- `SECURITY.md` - Basic test results
- `ai_safety_report.json` - AI safety assessment
- `zap_report.json` - OWASP ZAP findings
---

## 📊 Security Test Matrix

| Test Type | Script | Target | Output | Severity Level |
|------------|---------|---------|---------|--------------|
| Input Validation | `security_test.py` | `SECURITY.md` | LOW-MEDIUM |
| AI Safety | `ai_safety_test.py` | `ai_safety_report.json` | CRITICAL |
| Vulnerability Scan | `zap_scan.py` | `zap_report.json` | HIGH-CRITICAL |


## 📚 Additional Resources

### Security Documentation
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE Mitigation](https://cwe.mitre.org/)

### Tools Used
- [OWASP ZAP](https://www.zaproxy.org/) - Web application security scanner
- [Python Security Libraries](https://github.com/pyca/cryptography) - Security implementations
- [Bleach](https://bleach.readthedocs.io/) - HTML sanitization

---