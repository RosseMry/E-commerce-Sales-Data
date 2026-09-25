import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns

# Set theme
sns.set_theme(style="whitegrid")

# Background colors
plt.rcParams['figure.facecolor'] = "#f8fafc"
plt.rcParams['axes.facecolor']   = "#ffffff"
plt.rcParams['axes.edgecolor']   = "#d1d5db"
plt.rcParams['grid.color']       = "#e2e8f0"

# Text colors
plt.rcParams['text.color'] = "#1e293b"
plt.rcParams['axes.labelcolor'] = "#334155"
plt.rcParams['xtick.color'] = "#334155"
plt.rcParams['ytick.color'] = "#334155"

# ============================================
# ATTRACTIVE THEME SETUP
# ============================================
sns.set_theme(style="whitegrid")

# Background colors
plt.rcParams['figure.facecolor'] = "#f8fafc"
plt.rcParams['axes.facecolor']   = "#ffffff"
plt.rcParams['axes.edgecolor']   = "#d1d5db"
plt.rcParams['grid.color']       = "#e2e8f0"

# Text colors
DARK_TEXT   = "#1e293b"
MID_TEXT    = "#334155"
LIGHT_TEXT  = "#64748b"

# Main color palette
PRIMARY     = "#2563eb"      # Blue - Electronics
SUCCESS     = "#16a34a"      # Green - High profit
WARNING     = "#ea580c"      # Orange - Medium profit
PURPLE      = "#9333ea"      # Purple - Accessories
TEAL        = "#0d9488"      # Teal - Office
RED         = "#dc2626"      # Red - Low profit/attention

# Region colors
REGION_COLORS = [PRIMARY, SUCCESS, WARNING, PURPLE]  # North, East, South, West

# Category colors
CATEGORY_COLORS = [PRIMARY, PURPLE, TEAL]  # Electronics, Accessories, Office

print("✅ Theme configured successfully!")