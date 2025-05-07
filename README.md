# Supplier Performance – Mini Python Project

This short project is a simulation to show how I would analyze supplier performance using Python.  
Ability to work with business data and generate insights.(for the data are imaginary data, because I work with customer data I do not have the right to share them)


The idea is to evaluate suppliers based on different indicators (like delivery times, service level, quality issues...) and identify which ones might be at risk. I used clustering and a custom risk scoring approach to make the results more visual and actionable.

---

## 📁 What’s Inside?

The dataset includes 7 fake suppliers with the following fields:
- Number of orders
- Delivery delay (average)
- Service rate (on-time rate)
- Conformity (quality compliance)
- Delay rate
- Cost of non-conformities

I process the data, cluster the suppliers using KMeans, and calculate a global "risk score" to help decide where to focus improvement efforts.

---

## 🔧 Tools Used

- Python (Pandas, Scikit-learn)
- Matplotlib & Seaborn for visuals
- PCA (for visualization)
- KMeans (for clustering)

  <img width="559" alt="Screenshot 2025-05-07 at 16 33 06" src="https://github.com/user-attachments/assets/fcb8c51c-1dd2-4a1f-9649-f37fdc653a24" />


---

## 🧠 What It Shows

- A simple but clear supplier clustering based on behavior
- A custom scoring logic (you can adjust the weights)
- A graph to easily spot which suppliers might need attention
- An example of data storytelling from raw numbers to decision support
