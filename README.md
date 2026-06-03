# olat-checker

> A Python script that queries and logs the current number of active users on the UZH learning management system OLAT (OpenOLAT).

## ✨ TL;DR
```bash
python olatChecker.py
```

## 🚀 Features
- **OLAT status check:** Reads the number of currently active users from the UZH OLAT system.
- **Web scraping:** Uses `requests` and `BeautifulSoup` for HTML parsing.
- **Logging:** Logs retrieved values via `olatLogger.py`.

---

## 🛠️ Installation

### Prerequisites
- Python 3.x
- `requests`, `beautifulsoup4`

### Steps
1. Clone the repository:
```bash
git clone https://github.com/HuberNicolas/olat-checker
cd olat-checker
```
2. Install dependencies:
```bash
pip install requests beautifulsoup4
```

---

## 💻 Usage

```bash
python olatChecker.py
```

---

## 📄 License

This project is licensed under the **GNU General Public License v3 (GPLv3)** – see the [LICENSE](LICENSE) file for details.

**Conditions:**
- The original copyright notice (crediting my name) must be retained in all copies or substantial portions of the software.
- Modifications and derivative works *must* also be released under the GPLv3, and the source code must be made publicly available.
