import pandas as pd
import matplotlib.pyplot as plt

def recommend_places_with_visuals(source_city, top_n=5):
    # Load dataset
    df = pd.read_csv("Top Indian Places to Visit.csv")

    # Rename columns
    df = df.rename(columns={
        "Google review rating": "Rating",
        "Number of google review in lakhs": "Popularity",
        "time needed to visit in hrs": "VisitTime",
        "Airport with 50km Radius": "Airport"
    })

    # Validate source city
    source = df[df["City"].str.lower() == source_city.lower()]
    if source.empty:
        print("❌ Source city not found in dataset.")
        return

    source_state = source.iloc[0]["State"]
    source_zone = source.iloc[0]["Zone"]

    # Remove same city
    df = df[df["City"].str.lower() != source_city.lower()]

    # Keep only same zone (hard distance constraint)
    df = df[df["Zone"] == source_zone]

    # Distance score
    df["Distance_score"] = df["State"].apply(
        lambda x: 1.0 if x == source_state else 0.7
    )

    # Airport score
    df["Airport_score"] = df["Airport"].apply(
        lambda x: 1.0 if str(x).strip().lower() == "yes" else 0.0
    )

    # Normalize numeric features
    df["Rating_norm"] = (df["Rating"] - df["Rating"].min()) / (df["Rating"].max() - df["Rating"].min())
    df["Popularity_norm"] = (df["Popularity"] - df["Popularity"].min()) / (df["Popularity"].max() - df["Popularity"].min())
    df["VisitTime_norm"] = (df["VisitTime"] - df["VisitTime"].min()) / (df["VisitTime"].max() - df["VisitTime"].min())

    # Invert visit time
    df["Visit_score"] = 1 - df["VisitTime_norm"]

    # FINAL SCORE (Distance-first)
    df["Score"] = (
        0.35 * df["Distance_score"] +
        0.25 * df["Rating_norm"] +
        0.20 * df["Airport_score"] +
        0.10 * df["Popularity_norm"] +
        0.10 * df["Visit_score"]
    )

    # Top results
    top = df.sort_values("Score", ascending=False).head(top_n)

    # Console output
    print(f"\n🌍 Top Weekend Destinations from {source_city.title()}:\n")
    print(top[[
        "Name",
        "City",
        "State",
        "Zone",
        "Rating",
        "Popularity",
        "Airport",
        "VisitTime",
        "Score"
    ]])

    # -----------------------------
    # Visualization 1: Ranking
    # -----------------------------
    plt.figure()
    plt.barh(top["Name"], top["Score"])
    plt.xlabel("Recommendation Score")
    plt.title(f"Top Weekend Destinations from {source_city.title()}")
    plt.gca().invert_yaxis()
    plt.show()

    # -----------------------------
    # Visualization 2: Feature Contribution
    # -----------------------------
    plt.figure()
    plt.plot(top["Name"], top["Distance_score"], marker="o", label="Distance")
    plt.plot(top["Name"], top["Rating_norm"], marker="o", label="Rating")
    plt.plot(top["Name"], top["Airport_score"], marker="o", label="Airport Access")
    plt.plot(top["Name"], top["Visit_score"], marker="o", label="Visit Feasibility")
    plt.legend()
    plt.xticks(rotation=30)
    plt.title("Feature Contribution Comparison")
    plt.show()


# -----------------------------
# USER INPUT
# -----------------------------
if __name__ == "__main__":
    city = input("Enter Source City: ")
    recommend_places_with_visuals(city)
