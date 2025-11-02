# XGBoost Inventory Recommendation System

A data-driven inventory management solution for hotel bars that replaces reactive ordering with proactive, ML-powered recommendations.

## Problem Statement

Hotel chains face significant inefficiencies from unoptimized bar inventory:
- **Stock-outs** → Lost sales, poor guest experience, brand damage
- **Overstocking** → Capital tied up, increased holding costs, spoilage waste

This system maintains 95% service levels while minimizing inventory capital.

## Key Assumptions

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Lead Time** | 3 days | Regional supplier delivery window |
| **Service Level** | 95% | Balance between stockout cost and inventory holding cost (Z-score: 1.65) |
| **Order Increments** | 750ml | Standard bottle size for actionable recommendations |
| **Current Stock** | Latest closing balance | Assumes real-time inventory data availability |

## Model Architecture

### Why XGBoost?

The system uses **three XGBoost models per item** for uncertainty-aware forecasting:

1. **Point Forecast** (`reg:squarederror`) → Mean consumption prediction
2. **Lower Bound** (`reg:quantileerror`, α=0.1) → 10th percentile
3. **Upper Bound** (`reg:quantileerror`, α=0.9) → 90th percentile

**Key Advantages:**
- **Quantifies uncertainty** via quantile regression for statistical safety stock calculation:  
  `Safety Stock = Z × forecast_uncertainty × √lead_time`
- **Scales efficiently** across hundreds of SKU-location pairs
- **Handles complex features** (lags, rolling stats, cyclical patterns) without extensive preprocessing
- **Captures non-linear patterns** (e.g., "Fridays are busy for vodka at Location A")

### Why Not Alternatives?

- **ARIMA/Prophet**: Don't scale to hundreds of series; can't share learnings across items
- **Deep Learning (LSTMs)**: Overkill complexity for this problem; harder to interpret and deploy

## Performance

- **Metric**: Weighted Absolute Percentage Error (WAPE)
- **Result**: 35-45% on 5-fold time series CV
- **Interpretation**: Strong performance for sparse, multi-SKU inventory data
- **Business Output**: Prioritized, actionable reorder alerts

## Future Improvements

### 1. External Regressors (Priority #1)
Add demand drivers to explain variation:
- Hotel occupancy rates (from PMS)
- Local events (conferences, festivals)
- Promotions and menu features
- Weather conditions

### 2. Financial Optimization
- Integrate `item_cost` and `item_price` for revenue-based alert prioritization
- Implement Economic Order Quantity (EOQ) calculations

### 3. Lead Time Variability
Model supplier delivery uncertainty (e.g., mean = 3 days, σ = 1 day) for more robust safety stock

## Production Architecture

```
┌─────────────────┐     ┌──────────────┐     ┌─────────────────┐
│  Data Sources   │────▶│  ML Pipeline │────▶│  Alert System   │
└─────────────────┘     └──────────────┘     └─────────────────┘
   • POS System           • Feature Eng        • Power BI/Tableau
   • Inventory DB         • Daily Retrain      • Priority Ranking
   • PMS (Occupancy)      • Forecasting        • Recommended Qty
   • Event/Weather APIs   • Alert Generation   • Mobile Access
```

### Orchestration
Automated nightly execution via Airflow/AWS Step Functions:
1. Ingest consumption + inventory data
2. Engineer features & retrain models
3. Generate forecasts & alerts
4. Push to dashboard

### User Experience
Bar managers see a simple prioritized list each morning:

```
🔴 CRITICAL | Grey Goose Vodka | 0.8 days left | Order: 12 bottles (2 cases)
🟡 MEDIUM   | Jack Daniels     | 2.3 days left | Order: 6 bottles (1 case)
```

## Monitoring KPIs

**Model Health:**
- WAPE and forecast bias tracking
- Model drift detection & retraining triggers

**Business Impact:**
- ↓ Stockout rate for high-demand items
- ↑ Inventory turnover ratio
- ↓ Total inventory holding cost
- ↓ Spoilage rate (perishables)

---

**Tech Stack**: XGBoost • Python • Pandas • NumPy • Scikit-learn  
**Deployment**: Cloud-ready (AWS/GCP) • API-first design • Real-time dashboards
