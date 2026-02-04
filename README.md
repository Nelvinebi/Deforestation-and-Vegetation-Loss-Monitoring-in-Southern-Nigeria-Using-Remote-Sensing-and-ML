# 🌍 Deforestation and Vegetation Loss Monitoring in Southern Nigeria  
### Using Remote Sensing and Machine Learning (Synthetic Data Approach)

## 📌 Project Overview
Deforestation and vegetation degradation pose significant threats to biodiversity, climate regulation, and livelihoods in Southern Nigeria. However, reliable long-term environmental datasets are often limited or inaccessible.

This project presents a **fully reproducible, data-scarce-friendly framework** for monitoring deforestation and vegetation loss using **synthetic but physically realistic remote sensing data** and **machine learning techniques**. The methodology mirrors real-world satellite-based workflows (e.g., Sentinel-2, Landsat) while remaining accessible for research, training, and policy simulation.

The project demonstrates how **Environmental AI** can support early warning systems, land-use monitoring, and climate resilience planning in developing regions.

---

## 🎯 Objectives
- Simulate realistic remote sensing indicators for Southern Nigeria
- Derive vegetation indices commonly used in forest monitoring
- Apply machine learning to detect deforestation and vegetation loss
- Provide a reproducible pipeline suitable for:
  - Research and academic use
  - Capacity building and training
  - Policy and scenario analysis in data-scarce regions

---

## 🛰️ Simulated Remote Sensing Variables
The synthetic dataset represents pixel-level observations similar to satellite imagery products.

### Raw Environmental Features
- **Red Band Reflectance**
- **Near-Infrared (NIR) Band Reflectance**
- **Land Surface Temperature (K)**
- **Annual Rainfall (mm)**
- **Soil Moisture**
- **Elevation (m)**

### Derived Vegetation Indices
- **NDVI (Normalized Difference Vegetation Index)**
- **EVI (Enhanced Vegetation Index)**
- **NBR (Normalized Burn Ratio)**

### Target Variable
- **Deforestation Label**
  - `1` → Vegetation loss / deforestation
  - `0` → Stable vegetation cover

---

## 🧠 Machine Learning Concept
The dataset is designed to support:
- Supervised classification (e.g., Random Forest, XGBoost)
- Feature importance analysis
- Risk-based vegetation loss assessment

The deforestation labels are generated using a physically inspired scoring function that incorporates:
- Vegetation health (NDVI)
- Temperature stress
- Rainfall variability
- Elevation influence
- Controlled stochastic noise

---

## 📁 Repository Structure
```text
.
├── generate_deforestation_dataset.py   # Synthetic data generator
├── Southern_Nigeria_Deforestation_Synthetic_Dataset.xlsx
├── README.md
⚙️ How to Use
1️⃣ Clone the Repository
git clone https://github.com/your-username/deforestation-monitoring-southern-nigeria.git
cd deforestation-monitoring-southern-nigeria
2️⃣ Install Dependencies
pip install numpy pandas openpyxl
3️⃣ Generate the Dataset
python generate_deforestation_dataset.py
This will create:

Southern_Nigeria_Deforestation_Synthetic_Dataset.xlsx
📊 Potential Applications
National and sub-national deforestation monitoring

Environmental impact assessments

Climate resilience and land-use planning

AI/ML training for GIS and environmental science students

Prototype early warning systems for forest loss

🌱 Scalability and Extensions
This framework can be easily extended to:

Real satellite data (Sentinel-2, Landsat, MODIS)

Time-series deforestation detection

GIS-ready raster or GeoTIFF outputs

Integration with Google Earth Engine

Policy-facing risk maps and dashboards

⚠️ Disclaimer
This project uses synthetic data for demonstration and capacity-building purposes. While the data are physically realistic, they do not represent actual observations and should not be used directly for operational decision-making without validation against real satellite datasets.

👤 Author
AGBOZU EBINGIYE NELVIN
Environmental AI | Remote Sensing | Machine Learning

Focus: Climate, Sustainability, and Data-Scarce Regions

📜 License
This project is released under the MIT License.
You are free to use, modify, and distribute this work with appropriate attribution.

🤝 Acknowledgements
Inspired by global forest monitoring initiatives and the growing role of AI in environmental sustainability, climate adaptation, and ecosystem protection.
