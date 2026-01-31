AI Clinical Decision Support System

System Overview



A multi-agent AI system that simulates structured clinical reasoning using three virtual medical roles. The system analyzes a patient case, critiques the reasoning, and produces a refined final decision using the Google Gemini model.



This project is for educational and research purposes only.



System Architecture



User

&nbsp; ↓

Streamlit Frontend (app.py)

&nbsp; ↓

Agent Orchestration (conversation.py)

&nbsp; ↓

Medical Agents (agents.py)

&nbsp; ↓

LLM Provider (llm\_provider.py)

&nbsp; ↓

Google Gemini API



How the Code Works

app.py — Frontend Interface



Handles user interaction.



Displays case input box



Sends patient case to backend logic



Shows responses from each AI doctor in tabs:



Dr Evidence



Dr Skeptic



Final Decision



conversation.py — Orchestration Layer



Controls the workflow between agents.



Flow:



Evidence agent analyzes the case



Skeptic agent critiques evidence output



Final agent integrates both



Returns structured result to the frontend.



agents.py — AI Doctor Roles



Defines the three reasoning agents.



Evidence Agent

Identifies likely condition, key findings, and initial management.



Skeptic Agent

Highlights reasoning weaknesses, missing data, and alternatives.



Final Agent

Produces refined diagnosis, immediate action, and confidence score.



Each agent sends prompts to the LLM through the provider layer.



llm\_provider.py — Model Interface



Connects the system to Google Gemini.



Responsibilities:



Sends prompts to Gemini API



Forces JSON structured responses



Extracts and validates returned data



main.py — API Endpoint (optional backend)



Provides REST endpoint if system is accessed via API instead of Streamlit UI.



Data Flow

Patient Case → Evidence Agent → Skeptic Agent → Final Agent → UI Display

Technologies Used



Streamlit

FastAPI

Google Gemini API

Python

