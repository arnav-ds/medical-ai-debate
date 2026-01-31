# AI Clinical Decision Support System (CDSS)

A multi-agent AI system that simulates structured clinical reasoning using three specialized virtual medical roles. By mimicking a multidisciplinary team, the system analyzes patient cases, critiques reasoning in real-time, and produces refined diagnostic insights using the Google Gemini model.

> [!IMPORTANT]
> **Disclaimer:** This project is for educational and research purposes only. It is not intended for use in clinical diagnosis or direct patient care.

---

## 🏗 System Architecture

The system follows a modular, layered architecture to ensure a clear separation of concerns between the user interface, agent logic, and the LLM provider.

* **User Interface:** A Streamlit-based web dashboard.
* **Orchestration:** A central controller managing the "hand-offs" between different AI personas.
* **Agent Logic:** Specialized prompts that define the clinical roles.
* **Provider Layer:** Interface for API communication and JSON schema enforcement.

---

## 🤖 Medical Agent Roles

The core of the system is the interaction between three distinct AI agents:

| Agent | Role | Responsibility |
| :--- | :--- | :--- |
| **Dr. Evidence** | Clinical Analyst | Identifies likely conditions, highlights key clinical findings, and proposes initial management. |
| **Dr. Skeptic** | Peer Reviewer | Acts as a "Devil's Advocate." Highlights reasoning weaknesses, suggests missing data, and proposes alternatives. |
| **Final Decision** | Lead Consultant | Integrates findings from both Evidence and Skeptic agents to produce a refined diagnosis and confidence score. |

---

## 💻 How the Code Works

### `app.py` — Frontend Interface
The entry point of the application. It manages the Streamlit UI, handles the input of patient cases, and displays the multi-step reasoning process using interactive tabs for each doctor's response.

### `conversation.py` — Orchestration Layer
This script manages the "Data Flow." It ensures that the output from Dr. Evidence is correctly fed into Dr. Skeptic, and that both outputs are summarized by the Final Agent before being sent back to the UI.

### `agents.py` — AI Personas
Contains the specific system prompts and personality definitions for the three agents. This file defines the clinical "lens" through which the LLM views the patient data.

### `llm_provider.py` — Model Interface
The bridge to the **Google Gemini API**. It handles the connection, manages API keys, and uses schema enforcement to ensure the LLM returns structured JSON data rather than raw text.

### `main.py` — API Endpoint (Optional)
A FastAPI implementation that allows the system to be accessed via REST API calls, enabling integration into other healthcare software ecosystems outside of the Streamlit UI.

---

## 🛠 Technologies Used

* **Language:** Python
* **Frontend:** Streamlit
* **Backend:** FastAPI (Optional)
* **LLM:** Google Gemini API
* **Data Handling:** Pydantic (for JSON validation)

---

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/ai-clinical-support.git](https://github.com/your-username/ai-clinical-support.git)

   | Layer         | Technology                                       |
| ------------- | ------------------------------------------------ |
| Frontend      | Streamlit                                        |
| Backend       | Python, FastAPI                                  |
| AI Runtime    | Google Gemini API                                |
| Model         | Gemini 1.5 Flash                                 |
| Agent System  | Multi-Agent Prompting (Evidence, Skeptic, Final) |
| Communication | REST-style API calls                             |
