# 🧮 Fuzzy Logic Product Discount Calculator

## Overview 🎯

Welcome to the Fuzzy Logic Product Discount Calculator! This Python-based system intelligently determines product discounts using fuzzy logic principles, taking into account sales performance.

## Features ✨

- **Intelligent Discount Calculation**: Utilizes fuzzy logic for nuanced decision-making
- **Multiple Input Variables**: Considers both sales performance and customer loyalty
- **Jupyter Notebook Support**: Includes experimental notebooks for testing and visualization
- **Easy Integration**: Simple REST API interface
- **Customizable Rules**: Flexible fuzzy rule base that can be modified

## Technical Stack 🛠️

- Python 3.8+
- scikit-fuzzy
- NumPy
- Jupyter Notebook
- FastAPI (for API endpoints)

## Installation 📦

```bash
# Clone the repository
git clone https://github.com/Wilimaxs/fuzzy-discount-calculator.git

# Install dependencies
pip install -r requirements.txt
```

## Quick Start 🚀

1. Start the API server:

```bash
uvicorn app.main:app --reload
```

2. Send a POST request to calculate discount:

```bash
curl -X POST "http://localhost:8000/calculate-discount" \
     -H "Content-Type: application/json" \
     -d '{"sold": 0, "loyalty": 0}'
```

## API Specification 📝

### Calculate Discount Endpoint

**Endpoint:** `/calculate-discount`

#### Request Format

```json
{
  "sold": 0, // Number of items sold (0-100)
  "loyalty": 0 // Customer loyalty score (0-100)
}
```

#### Response Format

```json
{
  "discount": "NO_DISCOUNT" // Possible values: NO_DISCOUNT, SMALL, MEDIUM, LARGE
}
```

## Fuzzy Logic Implementation 🧠

The system uses three main components:

1. **Input Variables**:

   - Sales Performance (0-100)
   - Customer Loyalty (0-100)

2. **Output Variable**:

   - Discount Level (NO_DISCOUNT, SMALL, MEDIUM, LARGE)

3. **Fuzzy Rules**:
   - If sales are low and loyalty is low → NO_DISCOUNT
   - If sales are medium or loyalty is high → SMALL
   - If sales are high and loyalty is medium → MEDIUM
   - If sales are high and loyalty is high → LARGE

## Usage Examples 💡

### Python Code Example

```python
from discount_calculator import FuzzyDiscountCalculator

# Initialize calculator
calculator = FuzzyDiscountCalculator()

# Calculate discount
result = calculator.calculate_discount(sold=75, loyalty=80)
print(f"Recommended discount: {result}")
```

### API Request Example

```python
import requests

url = "http://localhost:8000/calculate-discount"
data = {
    "sold": 75,
    "loyalty": 80
}

response = requests.post(url, json=data)
print(response.json())
```

## Testing 🧪

Run the test suite:

```bash
pytest tests/
```

## Support 📧

For support or questions, please contact us at:

- Email: wildan27370@gmail.com
- GitHub Issues: [Create an issue](https://github.com/yourusername/fuzzy-discount-calculator/issues)

---

Made with ❤️ by NexuraPay
