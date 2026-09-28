<div align="justify">
🧪 Test Automation & Quality Assurance — She Guides Me

This repository contains the test strategy, automated test suites, test cases, and quality assurance framework for [She Guides Me](https://sheguidesme.com/).

---
</div>
Test Case Table = https://docs.google.com/spreadsheets/d/1D_Qpq1WAo70c8AcGFLRc6jTxUWQxuU-HFTEfOzjltE4/edit?usp=sharing

<div align="justify">
📌 Project Overview

**Target Application:** [https://sheguidesme.com/](https://sheguidesme.com/)  
**Objective:** Ensure high quality, cross-browser compatibility, web performance, and functional accuracy for the platform across key user journeys.

---
</div>
🛠️ Tech Stack & Test Tools

* **End-to-End (E2E) Testing:** Playwright / Cypress / Selenium *(Update based on your stack)*
* **API Testing:** Postman / REST Assured
* **Performance & Load Testing:** Lighthouse / k6 / Apache JMeter
* **Accessibility (a11y) Testing:** Axe-core / WAVE
* **Version Control:** Git & GitHub / GitLab CI/CD

---

📂 Repository Structure

```text
├── .github/workflows/     # CI/CD pipeline configurations
├── tests/
│   ├── e2e/               # UI and End-to-End functional tests
│   ├── api/               # API endpoint tests
│   ├── accessibility/     # Accessibility audits (a11y)
│   └── performance/       # Lighthouse / k6 performance scripts
├── test-data/             # Mock data and test fixtures
├── reports/               # Auto-generated test execution reports
├── .gitignore
├── package.json           # Node dependencies & test scripts
└── README.md
