
# ApexTrade AI — System Requirements

## 1. Introduction

ApexTrade AI is a multi-market automated trading system designed to analyse financial markets and execute trades through Deriv and MetaTrader 5.

## 2. Functional Requirements

### FR-01: Market Data
- Retrieve live market prices.
- Retrieve historical price data.
- Support multiple trading instruments.
- Monitor market conditions continuously.

### FR-02: Strategy Management
- Support multiple independent trading strategies.
- Analyse trends and market structure.
- Calculate technical indicators.
- Generate BUY, SELL and WAIT signals.

### FR-03: Confluence Engine
- Combine signals from different strategies.
- Calculate a confluence score.
- Reject signals below the configured threshold.
- Record the reasons behind every decision.

### FR-04: Risk Management
- Calculate position sizes.
- Define stop-loss and take-profit levels where supported.
- Enforce daily loss limits.
- Limit simultaneous positions.
- Prevent duplicate trades.
- Provide emergency trading shutdown.

### FR-05: Trade Execution
- Connect to Deriv through its API.
- Connect to MetaTrader 5.
- Execute approved trading signals.
- Monitor open positions and contracts.
- Verify execution responses.
- Support automated and manual execution modes.

### FR-06: Monitoring
- Display trading signals.
- Display open and closed trades.
- Track account performance.
- Record trading activity.
- Provide notifications.

### FR-07: Database Management
- Store trading signals.
- Store executed trades.
- Store strategy configurations.
- Store risk events.
- Maintain system logs.

## 3. Non-Functional Requirements

### NFR-01: Security
- Protect broker authentication credentials.
- Never expose API tokens in source code.
- Restrict access to trading controls.

### NFR-02: Reliability
- Handle API disconnections.
- Prevent unintended duplicate orders.
- Log application errors.
- Verify trade execution before updating records.

### NFR-03: Performance
- Process incoming market data efficiently.
- Minimize unnecessary API requests.
- Support multiple instruments.

### NFR-04: Maintainability
- Use modular software architecture.
- Separate trading strategies from execution logic.
- Maintain readable and documented code.

### NFR-05: Scalability
- Allow additional brokers to be integrated.
- Allow new strategies to be added independently.
- Support future dashboard improvements.

## 4. Operating Constraints

- Initial execution environment: Demo accounts.
- Forex integration: MetaTrader 5.
- Deriv integration: Deriv API.
- Primary language: Python.
- Database: PostgreSQL.
- Live trading requires successful validation.

## 5. Acceptance Criteria

The system will be considered functionally ready for demo evaluation when:

1. It retrieves market data from both platforms.
2. It generates strategy signals.
3. It calculates confluence scores.
4. It rejects trades that violate risk rules.
5. It executes approved demo trades.
6. It records trading activity.
7. It supports manual intervention.
8. It recovers safely from connection failures.
