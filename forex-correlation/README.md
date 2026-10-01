# Forex & Metals Correlation Guide (majors + minors, no exotics)

Data: daily Federal Reserve H.10 FX rates up to **25 Sep 2026** and monthly gold prices up to **Aug 2026**.
Correlations use log returns. Re-run with `python3 correlation.py`; the full matrices are in `results/`.

How to read a correlation coefficient (r):

| r | Meaning |
|---|---|
| +0.80 to +1.00 | Very strong: the pairs move **the same way**. Buying both is close to doubling one trade. |
| +0.50 to +0.80 | Moderate same direction |
| -0.50 to +0.50 | Weak or no reliable link |
| -0.50 to -0.80 | Moderate opposite direction |
| -0.80 to -1.00 | Very strong: the pairs move **opposite**. Buying both mostly cancels out. |

## 1. Tradable universe (no exotics)

- **Majors (7):** EURUSD, GBPUSD, USDJPY, USDCHF, USDCAD, AUDUSD, NZDUSD
- **Main crosses / minors:** EURGBP, EURJPY, GBPJPY, AUDJPY, NZDJPY, CADJPY, CHFJPY, EURCHF, GBPCHF, EURAUD, GBPAUD, AUDNZD, AUDCAD, EURCAD, GBPCAD, EURNZD (plus GBPNZD, NZDCAD, AUDCHF, NZDCHF, CADCHF, which behave like their neighbours)
- **Metals:** XAUUSD (gold), XAGUSD (silver)

## 2. Pairs that move in the SAME direction (positive)

| Pair group | 1-year daily r | 3-month daily r | 5-year weekly r | Why |
|---|---|---|---|---|
| **EURJPY / GBPJPY** | 0.88 | 0.94 | 0.85 | Both are "sell JPY" trades |
| **USDJPY / CADJPY** | 0.86 | 0.91 | 0.83 | JPY side dominates |
| **AUDJPY / NZDJPY** | 0.85 | 0.85 | 0.89 | AUD and NZD are twin risk currencies |
| **EURJPY / CHFJPY** | 0.88 | 0.89 | 0.80 | Driven by JPY |
| **AUDUSD / NZDUSD** | 0.82 | 0.77 | 0.87 | Same region, commodity and risk exposure |
| **EURUSD / GBPUSD** | 0.81 | 0.83 | 0.76 | Both are "sell USD" trades |
| **EURUSD / NZDUSD** | 0.76 | 0.77 | 0.65 | USD side dominates |
| **GBPUSD / NZDUSD** | 0.74 | 0.75 | 0.71 | |
| **EURAUD / GBPAUD** | 0.80 | 0.79 | 0.78 | AUD side dominates |
| **AUDUSD / AUDCAD** | 0.82 | 0.72 | 0.81 | AUD side dominates |
| **USDCHF / EURCHF** | 0.73 | 0.84 | 0.47 | CHF side dominates |

**All JPY crosses** (EURJPY, GBPJPY, AUDJPY, NZDJPY, CADJPY, CHFJPY, USDJPY) form one cluster with r ≈ 0.75–0.94. Being long several of them is really one large short-JPY position.

**All XXXUSD pairs** (EURUSD, GBPUSD, AUDUSD, NZDUSD) form one "anti-dollar" cluster with r ≈ 0.67–0.82.

## 3. Pairs that move in OPPOSITE directions (negative)

| Pair group | 1-year r | 3-month r | Why |
|---|---|---|---|
| **EURUSD / USDCHF** | **-0.89** | **-0.89** | The strongest pair. EUR and CHF move together, and USD sits on opposite sides of the two quotes. |
| **NZDUSD / EURNZD** | -0.79 | -0.85 | NZD is on opposite sides of the two quotes |
| **GBPUSD / USDCHF** | -0.74 | -0.78 | |
| **NZDUSD / USDCHF** | -0.74 | -0.74 | |
| **EURAUD / AUDCAD** | -0.74 | -0.77 | |
| **AUDUSD / EURAUD** | -0.71 | -0.67 | |
| **EURUSD / USDCAD** | -0.66 | -0.71 | |
| **EURUSD / USDJPY** | -0.59 | -0.65 | Weaker, because JPY has its own drivers (BoJ policy, intervention) |
| **EURGBP / GBPCHF** | -0.70 | -0.57 | |

Rule of thumb: **any XXXUSD pair against any USDXXX pair is negative.** For example, EURUSD, GBPUSD, AUDUSD and NZDUSD each run opposite to USDCHF, USDCAD and USDJPY.

### Majors matrix (1-year daily)

|        | EURUSD | GBPUSD | AUDUSD | NZDUSD | USDJPY | USDCHF | USDCAD |
|--------|-------|-------|-------|-------|-------|-------|-------|
| EURUSD | 1.00 | 0.81 | 0.68 | 0.76 | -0.59 | -0.89 | -0.66 |
| GBPUSD | 0.81 | 1.00 | 0.67 | 0.74 | -0.51 | -0.74 | -0.61 |
| AUDUSD | 0.68 | 0.67 | 1.00 | 0.82 | -0.38 | -0.64 | -0.63 |
| NZDUSD | 0.76 | 0.74 | 0.82 | 1.00 | -0.44 | -0.74 | -0.65 |
| USDJPY | -0.59 | -0.51 | -0.38 | -0.44 | 1.00 | 0.57 | 0.42 |
| USDCHF | -0.89 | -0.74 | -0.64 | -0.74 | 0.57 | 1.00 | 0.68 |
| USDCAD | -0.66 | -0.61 | -0.63 | -0.65 | 0.42 | 0.68 | 1.00 |

## 4. Metals (gold and silver)

Monthly correlation of gold with FX pairs, Aug 2021 to Aug 2026:

| Same direction as gold | r | Opposite to gold | r |
|---|---|---|---|
| AUDUSD | +0.52 | USDCAD | -0.41 |
| EURUSD | +0.47 | USDCHF | -0.40 |
| NZDUSD | +0.46 | USDJPY | -0.40 |
| GBPUSD | +0.44 | CADJPY | -0.21 |
| AUDCAD | +0.41 | | |

Gold is barely correlated with the non-USD crosses (EURGBP, EURCHF, AUDJPY and similar, with |r| < 0.15).

What this means:
- **XAUUSD tends to move with AUDUSD, EURUSD and NZDUSD**, and **against USDCHF, USDJPY and USDCAD**, because gold is priced in dollars. A weak dollar usually means higher gold. AUD shows the strongest link because Australia is a major gold producer.
- **The link is only moderate (about 0.4–0.5) right now.** Gold had a record run from 2024 to 2026, to above $4,000, helped by central-bank buying of roughly 800 t per year. It sometimes rose even while the dollar was strong. Short windows can show r near -0.8 against USDCHF, but don't treat gold as a perfect copy of the FX pairs.
- **Silver (XAGUSD)** normally tracks gold closely (typically r ≈ +0.8 to +0.9) and moves more for the same news. It has the same dollar links as gold, but it is also an industrial metal, so it tends to follow risk sentiment (AUDJPY, stocks) more closely than gold does. *(I couldn't download daily silver data from this environment, so this point comes from general market knowledge rather than my own calculation.)*

## 5. How to use this when trading

1. **Avoid doubling risk:** being long EURUSD and long GBPUSD (r ≈ 0.8) is close to one double-sized USD-short trade. Cut the size of each position.
2. **Avoid accidental hedges:** being long EURUSD and long USDCHF (r ≈ -0.9) mostly cancels out. You pay two spreads for almost no net exposure.
3. **Confirm signals:** if EURUSD breaks up, check whether USDCHF breaks down. If XAUUSD rallies, check whether AUDUSD agrees. When they disagree, the move is weaker.
4. **Diversify on purpose:** pick trades from different clusters, for example one USD pair, one JPY cross and one AUD/NZD cross. Lowly correlated combinations include EURGBP with AUDJPY, and gold with EURCHF.
5. **Re-check monthly:** correlations drift. JPY pairs in particular decouple around BoJ decisions and intervention.
