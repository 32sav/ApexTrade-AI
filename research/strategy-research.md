# ApexTrade AI — Strategy Research

## 1. Purpose

This document defines the initial trading strategies, research hypotheses and validation methods for ApexTrade AI.

No strategy will be considered profitable until it has been properly tested.

## 2. Supported Markets

### Forex

- XAUUSD
- EURUSD
- GBPUSD

### Deriv

- Synthetic indices supported by the selected Deriv account and API.

## 3. Initial Strategy Modules

### 3.1 Trend Following

Purpose: Identify the general market direction.

Initial indicators:

- EMA 20
- EMA 50
- EMA 200

### 3.2 Momentum Analysis

Purpose: Identify the strength of price movement.

Initial indicators:

- RSI
- MACD

### 3.3 Market Structure

Purpose: Identify changes in price direction.

Concepts:

- Higher Highs (HH)
- Higher Lows (HL)
- Lower Highs (LH)
- Lower Lows (LL)
- Break of Structure (BOS)

### 3.4 Liquidity Analysis

Purpose: Research potential liquidity sweeps around significant highs and lows.

Concepts:

- Equal highs
- Equal lows
- Previous session highs and lows
- Liquidity sweeps

### 3.5 Breakout and Retest

Purpose: Identify potential continuation after price breaks a significant level and retests it.

### 3.6 Volatility Analysis

Purpose: Measure market volatility and help determine suitable stop-loss distances.

Initial indicator:

- Average True Range (ATR)

## 4. Confluence Engine

The confluence engine will combine evidence from different strategy modules.

Provisional scoring model:

| Evidence               | Points |
| ---------------------- | -----: |
| Trend alignment        |      2 |
| Market structure       |      2 |
| Momentum               |      2 |
| Volatility suitability |      1 |
| Session suitability    |      1 |
| Total                  |      8 |

Initial research threshold: 6/8.

Important:

- The scoring system must remain configurable.
- Correlated indicators must not be counted as independent evidence.
- A low-quality setup must produce WAIT.
- Session suitability applies primarily to Forex, not synthetic indices.

## 5. Signal Types

The system will generate:

- BUY
- SELL
- WAIT

Each signal should contain:

- Instrument
- Timeframe
- Signal direction
- Confluence score
- Supporting evidence
- Entry conditions
- Stop-loss and take-profit proposal where applicable
- Signal timestamp
- Invalidation conditions

## 6. Risk Management Research

Initial demo-testing limits:

- Risk per Forex trade: 0.5%.
- Daily loss limit: 2%.
- Maximum simultaneous positions: 3.
- Maximum consecutive losses: 3.
- No martingale recovery system.
- Emergency stop must always be available.

Deriv options and Forex positions require different risk calculations.

## 7. Strategy Validation

Strategies must undergo:

1. Historical data analysis.
2. Backtesting.
3. Out-of-sample testing.
4. Walk-forward testing.
5. Demo forward testing.
6. Performance evaluation.

Evaluation metrics:

- Win rate
- Profit factor
- Expected return per trade
- Maximum drawdown
- Number of trades
- Execution costs and slippage

## 8. Development Rules

- Do not assume an indicator guarantees profitable trades.
- Avoid over-optimizing strategies against historical data.
- Record every strategy decision.
- Test each strategy independently before combining it.
- Keep strategy logic separate from broker execution.
- Live trading is prohibited until sufficient validation is completed.

## 9. Research Status

Status: Initial research hypotheses documented.

Next phase: Strategy specification and technical implementation planning.
