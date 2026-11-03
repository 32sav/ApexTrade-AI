# ApexTrade AI — System Architecture

## 1. Architecture Overview

ApexTrade AI uses a modular architecture consisting of a frontend, backend, trading intelligence engine, broker integration layer and database.

The architecture separates trading decisions from broker-specific execution.

## 2. System Components

### 2.1 Frontend Layer

Technology: React

Responsibilities:

- Display trading dashboard.
- Show market charts and trading signals.
- Display account performance.
- Configure strategies and risk settings.
- Provide manual trade controls.
- Provide emergency shutdown controls.

### 2.2 Backend Layer

Technology: Python and FastAPI

Responsibilities:

- Coordinate system components.
- Expose API endpoints.
- Manage application configuration.
- Communicate with the frontend.
- Handle authentication and authorization.

### 2.3 Market Data Engine

Responsibilities:

- Retrieve live prices.
- Retrieve historical candles.
- Normalize market data.
- Monitor market conditions.
- Provide data to strategy modules.

### 2.4 Strategy Engine

Responsibilities:

- Run independent trading strategies.
- Calculate technical indicators.
- Analyse price action.
- Generate BUY, SELL and WAIT signals.

Initial strategy modules:

- Trend following.
- Momentum.
- Market structure.
- Liquidity analysis.
- Breakout and retest.

### 2.5 Confluence Engine

Responsibilities:

- Receive strategy outputs.
- Evaluate signal agreement.
- Calculate confluence scores.
- Apply minimum signal thresholds.
- Generate final trading decisions.

### 2.6 Risk Management Engine

Responsibilities:

- Calculate position sizes.
- Validate stop-loss and take-profit parameters.
- Enforce account risk limits.
- Monitor daily losses.
- Reject unsafe trades.

### 2.7 Execution Manager

Responsibilities:

- Receive approved trading decisions.
- Route orders to the appropriate broker adapter.
- Verify execution responses.
- Monitor open positions and contracts.
- Handle execution errors.

### 2.8 Broker Integration Layer

Deriv Adapter:

- Connect through Deriv WebSocket API.
- Subscribe to market data.
- Request contract proposals.
- Execute supported contracts.
- Monitor contract outcomes.

MetaTrader 5 Adapter:

- Connect through the MT5 Python package.
- Retrieve Forex market data.
- Submit trading orders.
- Monitor positions and account information.

### 2.9 Database Layer

Technology: PostgreSQL

Stores:

- User information.
- Broker account references.
- Instruments.
- Strategy configurations.
- Trading signals.
- Executed trades.
- Risk events.
- System logs.

## 3. Data Flow

1. Broker adapters retrieve market data.
2. Market data engine normalizes incoming data.
3. Strategy modules analyse market conditions.
4. Confluence engine evaluates strategy signals.
5. Risk engine validates the proposed trade.
6. Execution manager routes approved trades.
7. Broker adapter submits the order.
8. Execution results are recorded in PostgreSQL.
9. Dashboard displays updated information.

## 4. Design Principles

- Modularity: Components operate independently.
- Separation of concerns: Trading decisions are separated from execution.
- Security: Credentials are protected.
- Reliability: Errors and disconnections are handled safely.
- Extensibility: Additional brokers and strategies can be integrated.
- Observability: Trading decisions and system events are logged.

## 5. Execution Safety

- Demo trading is the default operating mode.
- Manual override must always be available.
- Risk checks must run before order submission.
- Duplicate orders must be prevented.
- Emergency shutdown must block new orders.
- Open positions must be reconciled after connection recovery.
