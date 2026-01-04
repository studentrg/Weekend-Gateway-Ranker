# 🌍 Weekend Travel Recommendation Engine

A **Python-based travel recommendation system** that suggests the **best weekend destinations** based on a user-selected source city.  
The system intelligently ranks destinations using **distance proximity, ratings, popularity, visit feasibility, and airport accessibility**.

---

## 🎯 Problem Statement

Given a **source city**, recommend the **top weekend travel destinations** by considering:
- Distance (state & zone proximity)
- Google review ratings
- Popularity (number of Google reviews)
- Time required to visit
- Airport availability within 50 km

---

## 🧠 Recommendation Strategy

Since the dataset does **not contain latitude/longitude**, distance is approximated using:
- **Zone-based filtering** (hard constraint)
- **State-level preference** (soft constraint)

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

### ✅ Key Highlights

✔ User-selected source city

✔ Dataset-driven (no hard-coded states)

✔ Realistic weekend travel logic

✔ Handles missing geo-coordinates intelligently

✔ Explainable scoring system

✔ Visualized recommendations

### 🎓 Academic Justification

“Due to the absence of geographical coordinates, a hierarchical proximity model using zone and state information was applied. Visit duration and airport accessibility were incorporated to improve weekend travel feasibility.”

### 🚀 Future Enhancements

Add user-adjustable weights

Include budget-based filtering

Convert into a Flask web application

Add map-based visualization

Support personalized recommendations

### 👤 Author

Ankit Mandal
B.Tech CSE
India
