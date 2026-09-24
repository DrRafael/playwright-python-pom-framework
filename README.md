# Playwright & Python Page Object Model (POM) Framework

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-1.40%2B-green.svg)](https://playwright.dev/python/)
[![Pytest](https://img.shields.io/badge/Pytest-8.0%2B-red.svg)](https://docs.pytest.org/)

A scalable and maintainable end-to-end (E2E) UI test automation framework built with **Python**, **Playwright (Sync API)**, and **Pytest**, implementing the **Page Object Model (POM)** design pattern.

---

## 🚀 Key Features

* **Page Object Model (POM)**: Complete separation of test logic from page-specific element locators and actions for high maintainability.
* **Base Page Abstraction**: Encapsulated common web interactions (`BasePage`) to promote code reusability.
* **Custom Pytest Fixtures**: Modular fixture setup in `conftest.py` managing Page Object lifecycle across tests.
* **Auto-Waiting & Smart Locators**: Native Playwright explicit assertions (`expect`) avoiding fragile hardcoded sleeps.

---

## 🛠️ Tech Stack

* **Language**: Python 3.10+
* **Automation Library**: Playwright (Python Sync API)
* **Test Runner**: Pytest
* **Design Pattern**: Page Object Model (POM)

---

## 📁 Repository Structure

```text
playwright-python-pom-framework/
│
├── pages/                   # Page Object Model components
│   ├── base_page.py         # Base class with reusable driver actions
│   └── login_page.py        # Page object encapsulation for Login flow
│
├── tests/                   # Automated test suites
│   └── test_login_flow.py   # E2E test cases using POM fixtures
│
├── conftest.py              # Pytest fixtures and environment setup
├── .gitignore               # Excluded caches and local configurations
└── requirements.txt         # Project dependencies
