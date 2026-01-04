# Modular Machine Learning Pipeline using OOP (Python)

This project demonstrates how to design a **production-ready Machine Learning pipeline** using **Object-Oriented Programming (OOP)** principles in Python.

The goal of this project is not to build a complex ML model, but to show **clean architecture, scalability, and real-world ML system design**, similar to how ML pipelines are built in product-based companies.

---

## Key Highlights

- End-to-end ML pipeline using OOP
- Clear separation of responsibilities
- Dataset abstraction with Factory Pattern
- Pluggable preprocessing and evaluation layers
- Model abstraction supporting multiple algorithms
- Industry-style logging
- Easily extensible and CI/CD friendly

---

## Why This Project?

In real-world ML systems:
- Data sources change (CSV, Excel, APIs, Cloud)
- Models evolve (Linear → Tree → Neural Networks)
- Preprocessing and evaluation logic changes frequently
- Pipelines must be testable, maintainable, and scalable

This project solves these problems using **OOP design patterns** instead of writing monolithic scripts.

---

## Architecture Overview

# Modular Machine Learning Pipeline using OOP (Python)

This project demonstrates how to design a **production-ready Machine Learning pipeline** using **Object-Oriented Programming (OOP)** principles in Python. 

The goal of this project is not to build a complex ML model, but to show **clean architecture, scalability, and real-world ML system design**, similar to how ML pipelines are built in product-based companies.

---

## Key Highlights

* **End-to-end ML pipeline** using OOP principles.
* **Clear separation of responsibilities** across modules.
* **Dataset abstraction** utilizing the Factory Pattern.
* **Pluggable** preprocessing and evaluation layers.
* **Model abstraction** supporting multiple algorithms.
* **Industry-style logging** for tracking and debugging.
* **Extensible design** optimized for CI/CD environments.

---

## Why This Project?

In real-world ML systems:
* **Data sources change:** Pipelines must handle CSV, Excel, APIs, or Cloud storage.
* **Models evolve:** Systems must transition from Linear models to Tree-based or Neural Networks easily.
* **Logic updates:** Preprocessing and evaluation requirements change frequently.
* **Scalability:** Pipelines must be testable, maintainable, and modular.

This project solves these problems using **OOP design patterns** instead of writing monolithic, hard-to-maintain scripts.

---

## Architecture Overview

The **Trainer** class orchestrates the entire flow without being tightly coupled to any specific implementation.



```text
Raw Data
   ↓
Dataset (Data Ingestion)
   ↓
Preprocessor (Cleaning & Transformation)
   ↓
Model (Training & Prediction)
   ↓
Evaluator (Metrics)
   ↓
Logger (Tracking & Debugging)
```


The **Trainer** class orchestrates the entire flow without being tightly coupled to any specific implementation.

---

## 📁 Project Structure

ml_oops_pipeline/
├── src/
│   ├── data/
│   │   ├── dataset.py          # Abstract Dataset Interface
│   │   ├── csv_dataset.py      # CSV data loader
│   │   ├── excel_dataset.py    # Excel data loader
│   │   ├── api_dataset.py      # API data loader
│   │   └── data_factory.py     # Dataset factory
│   │
│   ├── preprocessing/
│   │   ├── base_preprocessor.py # Abstract Preprocessor
│   │   └── simple_preprocessor.py # Basic preprocessing logic
│   │
│   ├── models/
│   │   ├── base_model.py       # Abstract Model Interface
│   │   └── linear_model.py     # Linear regression model
│   │
│   ├── evaluation/
│   │   └── evaluator.py        # Evaluation metrics
│   │
│   ├── training/
│   │   └── trainer.py          # Pipeline controller
│   │
│   ├── logging/
│   │   └── logger.py           # Centralized logger
│   │
│   └── main.py                 # Entry point
│
├── data/
│   └── train.csv               # Sample dataset
│
├── logs/
│   └── app.log                 # Application logs
│
├── requirements.txt
├── README.md
└── .gitignore


## 🧩 OOP Concepts Used

### 1. Encapsulation
Each component (Dataset, Model, Preprocessor, Evaluator) hides its internal logic and exposes only required behavior.

### 2. Abstraction
Abstract base classes define **what** a component must do, not **how** it does it.

Example:
- `Dataset` → must implement `load()`
- `BaseModel` → must implement `train()` and `predict()`

### 3. Inheritance
Concrete implementations inherit from abstract base classes.

Example:
- `CSVDataset` → `Dataset`
- `LinearModel` → `BaseModel`

### 4. Polymorphism
The Trainer works with any dataset or model as long as it follows the expected interface.

Example:
model.train(X, y)

works for Linear, Tree-based, or Neural Network models.


### 5. Composition
The Trainer has-a Dataset, Model, Preprocessor, Evaluator, and Logger.
🏭 Dataset Factory Pattern
The DataFactory dynamically selects the appropriate dataset implementation based on input source.
Supported sources:
 - CSV files
 - Excel files
 - REST APIs

This allows the pipeline to remain unchanged when data sources change.

🧪 How the Pipeline Works
1. main.py receives a data source
2. DataFactory selects the correct dataset loader
3. Dataset loads raw data
4. Preprocessor cleans and transforms data
5. Model trains on processed data
6. Model generates predictions
7. Evaluator computes metrics
8. Logger records each step

▶️ How to Run the Project
1. Install dependencies
pip install -r requirements.txt

2. Run the pipeline
python src/main.py

Logs will be generated in:
logs/app.log

📊 Extending the Project
You can easily extend this project by:
 - Adding new datasets (S3, Database, Kafka)
 - Adding advanced preprocessing (scaling, encoding)
 - Adding new models (RandomForest, XGBoost, Neural Networks)
 - Adding new evaluation metrics (Precision, Recall, F1, AUC)
 - Deploying the model using FastAPI or batch jobs

🚀 How This Fits in Real ML Systems
In product-based companies:
 - This pipeline runs as a training job
 - Trained models are versioned and stored
 - Models are deployed as APIs or batch scoring jobs
 - CI/CD pipelines retrain and redeploy models automatically
This project mirrors that real-world design.

🧠 Interview Talking Points
 - Clean separation of concerns
 - Factory pattern for data ingestion
 - OOP-driven ML pipeline design
 - CI/CD and production readiness
 - Scalable and maintainable architecture


👤 Author
Built as a learning and interview preparation project for ML / AI Engineering roles, focusing on real-world system design, not just algorithms.