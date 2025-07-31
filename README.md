# AI-Driven Green Credit Score System

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## Description

This project is an AI-Driven Green Credit Score System that leverages artificial intelligence to assess and score individuals or organizations based on their environmental, social, and governance (ESG) practices. The system aims to promote sustainable initiatives by providing a transparent, data-driven "green" credit score.

## Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Getting Started](#getting-started)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [Contact](#contact)

## Features

- **AI-Based Green Credit Scoring:** Advanced models for calculating ESG-based credit scores.
- **Data Visualization Dashboard:** Interactive dashboard for monitoring and analyzing scores.
- **API Service:** FastAPI backend for model inference and system integration.
- **Extensible Pipeline:** Easily add new data sources and scoring metrics.

## Technology Stack

- **Python** (100%)
- **FastAPI** for backend APIs
- **Streamlit** for dashboards and visualization
- **Uvicorn** as ASGI server
- **Scikit-learn, Pandas, NumPy** for data science and ML
- **PyCharm** (recommended) as the development environment

## Getting Started

### Prerequisites

- Python 3.8+
- [PyCharm](https://www.jetbrains.com/pycharm/) (recommended for running and managing the project)
- pip (Python package manager)

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/astrogenius9/AI-Driven-Green-Credit-Score-System.git
    cd AI-Driven-Green-Credit-Score-System
    ```

2. **(Recommended) Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Deployment

We recommend using **PyCharm** for easy configuration and running of multiple scripts. However, you can also use the command line.

### 1. Start the FastAPI backend

```sh
uvicorn app.main:app --reload
```

This will start the API server locally at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### 2. Launch the Streamlit Dashboard

```sh
streamlit run dashboard/dashboard.py
```

This will launch the interactive dashboard in your browser.

### 3. (Optional) Generate Synthetic Data

If you need to generate or refresh demo data, run:

```sh
python generate_data.py
```

### 4. (Optional) Train and Predict Models

If you wish to retrain the models or perform predictions:

```sh
python train_and_predict.py
```

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request. For major changes, open an issue first to discuss your ideas.

### Contributors
This project was made by the following: 

- Aditya Chalapathy ([LinkedIn](YOUR_ARYAN_GOSAVI_LINKEDIN_URL_HERE))
- Aryan Gosavi ([LinkedIn](YOUR_ARYAN_GOSAVI_LINKEDIN_URL_HERE))
- Krish Bharadwaj ([LinkedIn](YOUR_KRISH_BHARADWAJ_LINKEDIN_URL_HERE))

## Contact

Repository created by [astrogenius9](https://github.com/astrogenius9). 

Aditya Chalapathy ([LinkedIn](YOUR_ARYAN_GOSAVI_LINKEDIN_URL_HERE))

Project Link: [https://github.com/astrogenius9/AI-Driven-Green-Credit-Score-System](https://github.com/astrogenius9/AI-Driven-Green-Credit-Score-System).


