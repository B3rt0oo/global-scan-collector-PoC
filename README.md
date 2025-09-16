# Global Scan Collector PoC

**A Proof of Concept FastAPI application for collecting IDS alerts and storing them in PostgreSQL.**  

This project demonstrates a lightweight collector that receives alerts from intrusion detection systems (IDS) and logs them into a database for further analysis. Perfect for testing, prototyping, or educational purposes.

---

## Features

- **FastAPI-based API** for receiving JSON-formatted IDS alerts  
- **PostgreSQL integration** for persistent storage  
- **Bearer token authentication** for secure access  
- **Docker-ready** for easy deployment and testing  
- Safe for public repositories — sensitive data handled via `.env`  

---

## Quick Start

### 1. Clone the repository

```bash
git clone git@github.com:B3rt0oo/global-scan-collector.git
cd global-scan-collector/collector
