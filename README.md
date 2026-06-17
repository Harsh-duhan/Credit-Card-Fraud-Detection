# Credit Card Fraud Detection

This project trains a machine learning model to classify credit card transactions as legitimate or fraudulent. It uses a decision tree classifier with randomized hyperparameter search and reports accuracy, classification metrics, and a confusion matrix.

## Project Structure

```text
.
+-- Credit_card_fraud_detection.py      # Training and evaluation script
+-- Credit_card_fraud_detection.ipynb   # Notebook version of the workflow
+-- credit_card_fraud_model.pkl         # Exported trained model artifact
+-- requirements.txt                    # Python dependencies
+-- Dockerfile                          # Container build instructions
+-- .dockerignore                       # Files excluded from Docker build context
+-- .gitignore                          # Files excluded from Git/GitHub
```

## Dataset

The training script expects a file named `creditcard.csv` in the project root. This dataset is intentionally ignored by Git because it is large and should not be committed to GitHub.

Expected target column:

```text
Class
```

All other columns are used as model features.

## Run Locally

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

On Windows PowerShell:

```powershell
python -m venv .env
.\.env\Scripts\Activate.ps1
pip install -r requirements.txt
```

Place `creditcard.csv` in the project root and run:

```bash
python Credit_card_fraud_detection.py
```

## Run with Docker

Build the image:

```bash
docker build -t credit-card-fraud-detection .
```

Run the container while mounting the dataset from your local machine:

```bash
docker run --rm -v "$(pwd)/creditcard.csv:/app/creditcard.csv:ro" credit-card-fraud-detection
```

On Windows PowerShell:

```powershell
docker run --rm -v "${PWD}\creditcard.csv:/app/creditcard.csv:ro" credit-card-fraud-detection
```
