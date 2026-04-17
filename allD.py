# =========================
# IMPORT LIBRARIES
# =========================
import pandas as pd
import matplotlib.pyplot as plt
import re

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("company_dataset.csv", nrows=101)

# Clean column names
df.columns = df.columns.str.strip().str.lower()

print("Before cleaning:")
print(df.head())


# =========================
# DATA CLEANING
# =========================

# ---- Clean ratings ----
df['ratings'] = pd.to_numeric(df['ratings'], errors='coerce')

# ---- Clean review_count (convert "59.9k" → 59900) ----
def clean_reviews(x):
    x = str(x)
    x = x.replace("(", "").replace(")", "").replace("Reviews", "").strip()
    
    if 'k' in x:
        return float(x.replace('k', '')) * 1000
    return float(x)

df['review_count'] = df['review_count'].apply(clean_reviews)

# ---- Clean years ("55 years old" → 55) ----
df['years'] = df['years'].str.extract(r'(\d+)').astype(float)

# ---- Clean employees ("1 Lakh+" → 100000) ----
def clean_employees(x):
    x = str(x)
    if "Lakh" in x:
        return 100000
    return None

df['employees'] = df['employees'].apply(clean_employees)

# Drop NaN AFTER cleaning
df = df.dropna()

print("\nAfter cleaning:")
print(df.head())


# =========================
# PIE CHART
# =========================
plt.figure()
plt.pie(df['employees'], labels=df['name'], autopct='%1.1f%%')
plt.title("Employees Distribution")
plt.show()


# =========================
# FUNNEL (Ratings)
# =========================
df_sorted = df.sort_values(by='ratings', ascending=False)

plt.figure()
plt.barh(df_sorted['name'], df_sorted['ratings'])
plt.gca().invert_yaxis()
plt.title("Ratings Funnel")
plt.xlabel("Ratings")
plt.show()


# =========================
# BAR CHART (Years)
# =========================
plt.figure()
plt.bar(df['name'], df['years'])
plt.xticks(rotation=45)
plt.title("Company vs Years")
plt.show()


# =========================
# LINE CHART (ctype)
# =========================
df['ctype_code'] = df['ctype'].astype('category').cat.codes

plt.figure()
plt.plot(df['name'], df['ctype_code'], marker='o')
plt.xticks(rotation=45)
plt.title("Company vs CType")
plt.show()


# =========================
# HISTOGRAM (Review Count)
# =========================
plt.figure()
plt.hist(df['review_count'], bins=10)
plt.title("Review Count Distribution")
plt.show()