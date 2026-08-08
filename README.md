# Agentic Travel Planner

An AI-powered travel planning app. You enter your trip details — starting location, destination, number of days, group size, budget, and any special preferences — and the app generates a full day-by-day itinerary with cost estimates, transportation suggestions, accommodation recommendations, and budget optimization tips.

## How it works

- **Frontend (`fe/`)**: A Streamlit app collects trip details from the user and sends them to the backend.
- **Backend (`be/`)**: A FastAPI server receives the trip details, builds a structured prompt, and sends it to Groq's `llama-3.1-8b-instant` model via LangChain to generate the travel plan.

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI, Uvicorn
- **LLM**: Groq (`llama-3.1-8b-instant`) via `langchain-groq`
- **Environment management**: `python-dotenv`

## Project Structure

```
Agentic_Travel_Planner/
├── be/
│   └── main.py          # FastAPI backend, /plan_trip endpoint
├── fe/
│   └── app.py            # Streamlit frontend
├── .env                   # GROQ_API_KEY (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Kadingela-Ramya/Agentic-Travel-Planner.git
cd Agentic-Travel-Planner
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1   # Windows PowerShell
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your environment variables

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
```

Get a free Groq API key at [console.groq.com](https://console.groq.com).

### 5. Run the backend

```bash
cd be
uvicorn main:f_obj --reload
```

The backend runs at `http://127.0.0.1:8000`.

### 6. Run the frontend

In a separate terminal (with the same virtual environment activated):

```bash
cd fe
streamlit run app.py
```

## Usage

1. Open the Streamlit app in your browser.
2. Enter your starting location, destination, number of trip days, group size, and total budget.
3. Add any special preferences (e.g. "party, temples, local food").
4. Click **BuildTravellingPlan** to generate your itinerary.

## Notes

- The model does not invent exact prices when reliable data isn't available — costs are labeled as estimates.
- If the requested budget is unrealistic for the trip, the app will flag it and suggest cost-saving alternatives rather than silently ignoring the constraint.

