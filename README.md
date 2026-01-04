# 🌍 Weekend Travel Recommendation Engine

The Weekend Getaway Ranker is a data-driven recommendation system that suggests the best weekend travel destinations from a given source city in India.
Destinations are ranked based on:

Distance from the source city
Tourist rating
Popularity score
The project uses Python and Pandas to process and rank destinations efficiently.

## 🎯 Problem Statement

Given a **source city**, recommend the **top weekend travel destinations** by considering:
- Distance (state & zone proximity)
- Google review ratings
- Popularity (number of Google reviews)
- Time required to visit
- Airport availability within 50 km

---

Objective

To build a simple data engineering pipeline that:
Takes a source city as input
Calculates distance to nearby destinations
Ranks destinations using multiple weighted factors
Returns the top recommended weekend getaways

### Feature Weights Used

| Feature | Weight |
|------|------|
| Distance Proximity | 35% |
| Google Rating | 25% |
| Airport within 50 km | 20% |
| Popularity | 10% |
| Visit Time Feasibility | 10% |

> Distance is intentionally given the highest weight to reflect **weekend travel practicality**.

---

## 🛠️ Tech Stack

- **Python**
- **Pandas**
- **Matplotlib**
- **Git & GitHub**

---

## 📂 Project Structure

travel-recommendation-engine/
│
├── travel_recommender.py
├── Top Indian Places to Visit.csv
├── requirements.txt


---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies
pip install -r requirements.txt
### 2️⃣ Run the program
python travel_recommender.py

### 3️⃣ Enter source city when prompted
Enter Source City: Kolkata

### 📊 Sample Output
Console Output
🌍 Top Weekend Destinations from Kolkata:

Name                    City        State          Zone      Rating  Popularity  VisitTime  Score
Kankalitala Temple       Bolpur      West Bengal    Eastern   4.7     0.045       0.5        0.874
Baba Baidyanath Temple   Deoghar     Jharkhand      Eastern   4.7     1.800       1.0        0.853
Hangseswari Temple       Hooghly     West Bengal    Eastern   4.6     0.120       0.5        0.848
Cooch Behar Palace       Cooch Behar West Bengal    Eastern   4.5     0.200       1.0        0.807
Hazarduari Palace        Murshidabad West Bengal    Eastern   4.5     0.180       1.5        0.798

### 📈 Visual Outputs

The program also generates:

### 1️⃣ Recommendation Score Bar Chart

Shows ranking order

Explains why one destination ranks above another

### 2️⃣ Feature Contribution Plot

Visualizes how distance, rating, airport access, and visit time contribute to the final score

Improves interpretability & explainability



Future Enhancements

Add real-time distance calculation using Google Maps API

Convert to a REST API

Add user preference-based recommendations

Visualization of rankings using charts
### 👤 Author

Rinki Ghosh
B.Tech CSE
India
