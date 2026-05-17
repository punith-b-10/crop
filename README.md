# Crop Recommendation System

Simple Flask project for recommending crops from soil and weather inputs.

## Features

- Predicts top 3 crops from farm lab inputs
- Estimates expected yield for each recommended crop
- Shows market price lookup by crop name
- Shows 30+ crop information cards
- Saves prediction history in the browser
- Uses separate HTML, CSS, JavaScript, and Python files

## Setup

```bash
pip install -r requirements.txt
python train_model.py
python app.py
```

Open this URL in the browser:

```text
http://127.0.0.1:5000
```

## Project Structure

```text
crop-recommendation-flask/
  app.py
  data.py
  train_model.py
  requirements.txt
  templates/
    index.html
  static/
    css/
      style.css
    js/
      script.js
    images/
  model/
```

Market prices are approximate sample values for project display. For real use, connect the market page to an official mandi or commodity price API.
