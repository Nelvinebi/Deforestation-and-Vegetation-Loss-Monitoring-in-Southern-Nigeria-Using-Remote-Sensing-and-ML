
"""
Deforestation and Vegetation Loss Monitoring in Southern Nigeria
Synthetic Remote Sensing Dataset Generator

This script generates physically realistic synthetic remote sensing data
and exports it to an Excel file for ML and GIS workflows.
"""

import numpy as np
import pandas as pd

def generate_dataset(n_samples=3000, output_file="Southern_Nigeria_Deforestation_Synthetic_Dataset.xlsx"):
    np.random.seed(42)

    data = pd.DataFrame({
        "red_band": np.random.uniform(0.05, 0.4, n_samples),
        "nir_band": np.random.uniform(0.2, 0.8, n_samples),
        "land_surface_temperature_K": np.random.normal(305, 5, n_samples),
        "annual_rainfall_mm": np.random.normal(1800, 300, n_samples),
        "elevation_m": np.random.uniform(0, 500, n_samples),
        "soil_moisture": np.random.uniform(0.1, 0.5, n_samples)
    })

    # Vegetation indices
    data["NDVI"] = (data["nir_band"] - data["red_band"]) / (
        data["nir_band"] + data["red_band"]
    )

    data["EVI"] = 2.5 * (data["nir_band"] - data["red_band"]) / (
        data["nir_band"] + 6 * data["red_band"] + 1
    )

    data["NBR"] = (data["nir_band"] - data["land_surface_temperature_K"] / 350) / (
        data["nir_band"] + data["land_surface_temperature_K"] / 350
    )

    # Simulated deforestation label
    deforestation_score = (
        -2.5 * data["NDVI"]
        + 0.04 * (data["land_surface_temperature_K"] - 300)
        - 0.0004 * data["annual_rainfall_mm"]
        + 0.002 * data["elevation_m"]
        + np.random.normal(0, 0.4, n_samples)
    )

    data["deforestation_label"] = (
        deforestation_score > np.percentile(deforestation_score, 65)
    ).astype(int)

    data.to_excel(output_file, index=False)
    print(f"Dataset saved to: {output_file}")

if __name__ == "__main__":
    generate_dataset()
