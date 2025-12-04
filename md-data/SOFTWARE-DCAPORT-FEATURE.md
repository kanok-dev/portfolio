# DCAPort Pro - Smart Investment Portfolio Manager

> **🚀 Full Stack Web Application | SaaS-Ready Architecture**

---

## 🏷️ Project Classification

| Category | Details |
|----------|---------|
| **Project Type** | ✅ **Full Stack Web Application** - Complete React SPA with Node.js REST API backend |
| **Architecture** | ✅ **SaaS-Ready** - Scalable architecture for multi-user portfolio management |
| **Database** | PostgreSQL with Sequelize ORM |
| **Real-Time Data** | Finnhub API integration for live stock prices |

---

## Software Overview

**DCAPort** is a comprehensive web-based portfolio management system designed specifically for investors who follow the Dollar Cost Averaging (DCA) investment strategy. The platform empowers users to manage multiple US stock portfolios simultaneously, track their DCA purchases over time, monitor real-time performance, and make data-driven rebalancing decisions.

Unlike traditional portfolio trackers that simply log transactions, DCAPort takes a holistic approach to DCA investing. It understands that successful DCA requires discipline, consistent tracking, and periodic rebalancing to maintain target allocations. The system automatically calculates how new purchases affect portfolio balance, provides visual insights into performance trends, and alerts users when allocations drift too far from their targets.

Built with modern web technologies and a user-first philosophy, DCAPort removes the complexity and spreadsheet juggling that typically comes with managing multiple DCA portfolios. Whether you're investing $50 weekly in tech stocks or building a diversified portfolio across market sectors, DCAPort gives you the clarity and confidence to stay on track with your investment strategy.

## Core Objectives

### 1. Simplify Multi-Portfolio DCA Management
Managing multiple investment portfolios across different strategies or accounts can quickly become overwhelming. DCAPort eliminates this complexity by providing a unified interface where you can create unlimited portfolios, each with its own holdings and transaction history. Switch between portfolios instantly, and the system updates all data in real-time—no manual refreshing, no confusion about which portfolio you're viewing.

### 2. Maintain Investment Discipline
The DCA strategy works best when investors maintain consistent purchasing habits and stick to their target allocations. DCAPort helps you stay disciplined by automatically tracking every purchase, calculating how it impacts your overall allocation, and alerting you when rebalancing is needed. The built-in DCA Calculator even tells you exactly how much to invest in each stock during your next purchase cycle to maintain proper balance.

### 3. Enable Data-Driven Decision Making
Investment decisions should be based on facts, not feelings. DCAPort provides real-time stock prices via the Finnhub API, calculates precise performance metrics, and visualizes trends through interactive charts. You'll know your exact cost basis, total return, current allocations, and deviation from targets—all the data you need to make informed adjustments to your strategy.

### 4. Reduce Time Spent on Portfolio Administration
Before DCAPort, investors spent hours updating spreadsheets, manually fetching stock prices, recalculating averages, and figuring out rebalancing requirements. Now, all of this happens automatically. Log your transaction, refresh prices with one click, and instantly see updated holdings, performance charts, and rebalancing recommendations. Spend less time on administration and more time focusing on your investment goals.

## Tech Stack

### Frontend Architecture
The frontend is built as a modern Single Page Application (SPA) using React 18.3, leveraging the latest features like hooks, suspense, and concurrent rendering for optimal performance. Vite 5.4 serves as the build tool, providing lightning-fast hot module replacement during development and highly optimized production builds.

**Key Frontend Technologies:**
- **React 18.3** - Component-based UI library with modern hooks architecture
- **Vite 5.4** - Next-generation frontend build tool with instant server start
- **React Router DOM v6** - Client-side routing with nested routes and data loaders
- **Zustand 4.5** - Lightweight state management with persistence middleware
- **Tailwind CSS 3.4** - Utility-first CSS framework for rapid UI development
- **Recharts 2.12** - Composable charting library built with React components
- **Lucide React** - Beautiful, consistent icon set with tree-shaking support
- **date-fns 3.6** - Modern JavaScript date utility library
- **React Hot Toast** - Elegant notifications for user feedback

The frontend follows a feature-based architecture where components are organized by their role (pages, components, stores, services, utils). State management uses Zustand with localStorage persistence for the current portfolio selection, while all other data is fetched fresh from the backend on page load. This hybrid approach ensures data consistency while providing a smooth user experience.

### Backend Architecture
The backend is built as a RESTful API using Node.js and Express.js, providing a robust and scalable foundation for data management. Sequelize ORM handles all database interactions with PostgreSQL, defining clear models and relationships that enforce data integrity at the database level.

**Key Backend Technologies:**
- **Node.js** - JavaScript runtime built on Chrome's V8 engine
- **Express.js** - Fast, unopinionated web framework for Node.js
- **PostgreSQL** - Advanced open-source relational database
- **Sequelize 6.35** - Promise-based ORM with transaction support
- **Finnhub API** - Real-time stock market data provider
- **Helmet** - Security middleware for setting HTTP headers
- **Morgan** - HTTP request logger middleware
- **CORS** - Cross-Origin Resource Sharing middleware
- **Express Rate Limit** - Rate limiting middleware for API protection

The backend follows a layered architecture with clear separation of concerns: routes define endpoints, controllers handle business logic and validation, services interact with external APIs, and models define database schema. This structure makes the codebase maintainable, testable, and easy to extend with new features.

### Database Design
PostgreSQL serves as the relational database, chosen for its reliability, ACID compliance, and excellent support for complex queries. The schema is designed around four main tables with clear foreign key relationships and cascade delete rules to maintain referential integrity.

**Database Tables:**
- **portfolios** - Core portfolio entities with metadata (name, description, currency, active status)
- **holdings** - Stock holdings scoped to portfolios (ticker, shares, costs, prices, target allocations)
- **transactions** - DCA purchase records (date, ticker, shares, price, amount, notes)
- **performance_snapshots** - Historical performance data for trend analysis

All holdings and transactions use `portfolio_id` as a foreign key with CASCADE DELETE, ensuring that when a portfolio is deleted, all associated data is automatically removed. The holdings table uses a composite primary key of (portfolio_id, ticker) to enforce uniqueness—you can't have duplicate tickers within the same portfolio.

### External Integrations
DCAPort integrates with Finnhub, a leading financial data provider, to fetch real-time stock quotes. The integration uses the REST API with smart rate limiting (25 requests/second) to stay within free tier limits while providing fast price updates. Prices are cached in the database to minimize API calls and provide instant data retrieval.

## Feature Highlights

### 1. Multi-Portfolio Management System
Create and manage unlimited portfolios, each completely isolated from others. Perhaps you want a conservative dividend portfolio, an aggressive growth portfolio, and a sector-specific tech portfolio—DCAPort handles all of them effortlessly. Each portfolio maintains its own holdings, transactions, performance history, and target allocations.

The portfolio switcher in the header lets you instantly change context. Select a different portfolio, and every page updates automatically—the dashboard shows that portfolio's metrics, the holdings page displays those specific stocks, and the DCA log shows only relevant transactions. This complete data isolation ensures you never accidentally mix data between portfolios.

**Key Capabilities:**
- Create portfolios with custom names and descriptions
- Set currency preference (defaults to USD)
- Duplicate portfolios to test different strategies
- Soft delete (archive) portfolios without losing historical data
- View portfolio-specific statistics and summaries

### 2. Dynamic Stock Holdings Management
Gone are the days of being limited to a predefined list of stocks. DCAPort lets you add ANY valid US stock ticker to your portfolio. Whether you're investing in well-known giants like NVDA and META or exploring smaller companies, simply enter the ticker symbol and the system handles the rest.

The holdings management interface shows you everything at a glance: current shares, average cost basis, current market price, price change percentage, market value, unrealized gains/losses, and current allocation percentage. Edit any holding to update share counts or target allocations, and the system recalculates everything automatically.

**Key Capabilities:**
- Add any valid stock ticker (1-10 uppercase alphanumeric characters)
- Set target allocation percentages for rebalancing guidance
- Edit holdings to adjust shares, costs, or targets
- Delete holdings (with protection against orphaned transactions)
- Real-time price updates via Finnhub API
- Automatic calculation of cost basis using weighted averages

### 3. Comprehensive DCA Transaction Logging
Every investment journey is built one transaction at a time. The DCA Log page provides a complete chronological record of all purchases in your portfolio. Each transaction captures the date, ticker, number of shares, price per share, total amount invested, and optional notes.

What makes DCAPort special is that logging a transaction automatically updates the corresponding holding. Buy 10 shares of AAPL at $180? The system adds those shares to your AAPL holding and recalculates the weighted average cost. This eliminates the manual math that usually comes with tracking DCA purchases.

**Key Capabilities:**
- Log purchases with precise share counts and prices
- Add notes to transactions for future reference
- Edit past transactions (system recalculates holdings automatically)
- Delete incorrect transactions with holding adjustments
- View transaction statistics (total count, average amount)
- Filter and search transactions by ticker or date

### 4. Real-Time Stock Price Updates
Investment decisions require current data. DCAPort integrates with Finnhub to fetch real-time stock quotes with a single click. The price refresh button (available on Dashboard, Holdings, and Performance pages) updates all stocks in your portfolio simultaneously, showing a progress indicator as prices load.

The system implements intelligent rate limiting to respect API quotas while providing fast updates. Prices are stored in the database with timestamps, so you always know when the data was last refreshed. Price changes are calculated automatically, showing both dollar and percentage changes from the previous close.

**Key Capabilities:**
- One-click price refresh for all holdings
- Real-time progress indicator during updates
- Price change tracking (daily gain/loss)
- Percentage change calculation
- Timestamp display for data freshness
- Automatic retry on rate limit errors

### 5. Interactive Performance Dashboard
The Dashboard provides a comprehensive overview of your portfolio's health. Four key metrics greet you immediately: Portfolio Value (current market value), Total Invested (cumulative DCA purchases), Total Gain/Loss (unrealized profit/loss), and Return Percentage (overall performance).

Below the metrics, you'll find recent transaction history and portfolio breakdown charts. The interface is designed for quick scanning—you should be able to assess your portfolio's status in under 10 seconds. Color coding helps: green for positive performance, red for losses, blue for neutral information.

**Key Capabilities:**
- Real-time portfolio valuation
- Total investment tracking across all transactions
- Unrealized gain/loss calculation
- Overall return percentage
- Recent transaction preview (last 5)
- Top holdings breakdown with current vs. target allocations
- Responsive design for mobile and desktop viewing

### 6. Visual Performance Analytics
Numbers tell the story, but charts make it memorable. The Performance page transforms your transaction data into interactive visualizations using Recharts. See your portfolio value grow over time, compare invested capital vs. market value, and track gain/loss trends.

The portfolio composition pie chart shows your current allocation at a glance, making it easy to spot overweight or underweight positions. All charts are responsive and interactive—hover over data points to see exact values, and the charts automatically resize for different screen sizes.

**Key Capabilities:**
- Portfolio value trend line chart
- Invested vs. current value comparison chart
- Gain/loss trend visualization
- Portfolio composition pie chart
- Interactive tooltips with precise data
- Responsive design for all devices

### 7. Intelligent Rebalancing Calculator
The heart of DCA strategy success is maintaining target allocations over time. Market movements cause your portfolio to drift—some stocks grow faster than others, throwing off your carefully planned balance. The Rebalancing page tells you exactly where you stand and what actions to take.

The calculator uses a three-tier alert system: ✅ Good (±2% deviation), ⚠️ Watch (±2-5% deviation), and 🚨 Rebalance (>±5% deviation). For each holding, you see the current allocation, target allocation, deviation, rebalancing status, and recommended action. Stocks significantly overweight get a "Stop buying" recommendation, while underweight stocks show "Increase purchases."

**Key Capabilities:**
- Deviation analysis for all holdings
- Three-tier status indicators with visual alerts
- Specific rebalancing recommendations
- Dollar amount calculations for adjustments
- Summary of stocks needing attention
- Detailed rebalancing guidelines
- Action items for immediate attention
- Educational tips for effective rebalancing

### 8. DCA Investment Calculator
Planning your next purchase? The DCA Calculator tells you exactly how to distribute your investment amount across your holdings to maintain target allocations. Enter your DCA amount (e.g., $500), click calculate, and instantly see how much to invest in each stock.

The calculator normalizes target percentages (handling cases where targets don't sum exactly to 100%) and calculates the precise dollar amount and share count for each position. It even shows you what your new allocation percentages will be after making these purchases, complete with deviation status indicators.

**Key Capabilities:**
- Custom DCA amount input
- Proportional distribution based on target allocations
- Precise share count calculations
- "Before and after" allocation comparison
- New deviation status preview
- Recommended purchase amounts per stock
- Current stock price integration
- Quick tips and usage instructions

### 9. Complete CRUD Operations
DCAPort is fully interactive. Everything you create can be viewed, edited, updated, or deleted. Add a holding, add transactions to it, realize you entered the wrong price, edit the transaction, delete the holding later—the system handles all of this gracefully with proper validation and data integrity checks.

Modal dialogs provide focused interfaces for data entry. The Holding Modal validates ticker formats, ensures uniqueness within the portfolio, and requires all mandatory fields. The Transaction Modal links to existing holdings and recalculates averages automatically. All forms provide immediate feedback with clear error messages if something's wrong.

**Key Capabilities:**
- Create portfolios, holdings, and transactions
- Read/view all data with real-time updates
- Update any entity with proper validation
- Delete entities with confirmation dialogs
- Cascade delete protection (prevent orphaned data)
- Form validation with helpful error messages
- Toast notifications for action feedback

### 10. Seamless Portfolio Switching
The portfolio switcher dropdown in the header is more than just a navigation element—it's the command center for your multi-portfolio strategy. Click the dropdown, select a portfolio, and watch as every component updates instantly. The Dashboard recalculates metrics, Holdings shows the new stocks, DCA Log displays relevant transactions, and Performance renders new charts.

Behind the scenes, Zustand manages state transitions smoothly. When you switch portfolios, the store clears current holdings and transactions, updates the current portfolio ID, and triggers data fetching for the new context. The selected portfolio persists to localStorage, so when you return to the app later, you're right where you left off.

**Key Capabilities:**
- Instant portfolio switching from any page
- Automatic data refresh on switch
- Persistent selection across sessions
- Visual indication of current portfolio
- No page reload required
- Smooth state transitions

## Software Architecture

### Frontend Structure
```
src/
├── components/          # Reusable UI components
│   ├── Layout.jsx       # Main layout with header and navigation
│   ├── PortfolioSwitcher.jsx  # Dropdown for portfolio selection
│   ├── PortfolioModal.jsx     # Create/edit portfolio dialog
│   ├── HoldingModal.jsx       # Add/edit holdings dialog
│   └── PriceRefreshButton.jsx # Stock price update button
├── pages/               # Route-level page components
│   ├── Dashboard.jsx    # Portfolio overview and metrics
│   ├── Holdings.jsx     # Holdings table with CRUD
│   ├── DCALog.jsx       # Transaction history and logging
│   ├── Performance.jsx  # Charts and performance analytics
│   ├── Rebalancing.jsx  # Rebalancing calculator and alerts
│   ├── DCACalculator.jsx # DCA distribution calculator
│   └── Portfolios.jsx   # Portfolio management page
├── stores/              # Zustand state management
│   └── portfolioStore.js # Global portfolio state and actions
├── services/            # API clients and external services
│   ├── api.js           # REST API client functions
│   └── stockPriceService.js # Stock price fetching service
├── utils/               # Utility functions and helpers
│   └── calculations.js  # Financial calculation utilities
├── App.jsx              # Root component with routing
├── main.jsx             # Application entry point
└── index.css            # Global styles and Tailwind directives
```

### Backend Structure
```
backend/
├── models/              # Sequelize database models
│   ├── Portfolio.js     # Portfolio model and schema
│   ├── Holding.js       # Holding model and schema
│   ├── Transaction.js   # Transaction model and schema
│   ├── PerformanceSnapshot.js # Performance snapshot model
│   └── index.js         # Model relationships and associations
├── controllers/         # Request handlers and business logic
│   ├── portfolioController.js   # Portfolio CRUD operations
│   ├── holdingController.js     # Holdings CRUD operations
│   └── transactionController.js # Transaction CRUD operations
├── routes/              # API endpoint definitions
│   ├── portfolioRoutes.js    # Portfolio endpoints
│   ├── holdingRoutes.js      # Holdings endpoints
│   ├── transactionRoutes.js  # Transaction endpoints
│   └── stockPrices.js        # Stock price endpoints
├── services/            # External API services
│   ├── stockPriceService.js  # Stock price business logic
│   └── finnhubRestAPI.js     # Finnhub API client
├── config/              # Configuration files
│   └── database.js      # Sequelize database configuration
├── scripts/             # Utility scripts
│   ├── syncDatabase.js  # Database synchronization
│   ├── testConnection.js # Database connection test
│   └── migrate-to-multi-portfolio.js # Migration script
├── middleware/          # Custom Express middleware
└── server.js            # Express server entry point
```

### Data Flow Architecture

**User Action → Frontend → API → Database:**
1. User interacts with UI component (e.g., clicks "Add Transaction")
2. Component calls Zustand store action (e.g., `addTransaction()`)
3. Store action calls API service function (e.g., `transactionsAPI.create()`)
4. API service makes HTTP request to backend endpoint
5. Express route receives request and calls controller
6. Controller validates data and interacts with Sequelize models
7. Model performs database query (INSERT, UPDATE, SELECT, DELETE)
8. PostgreSQL executes query and returns result
9. Controller sends response back to frontend
10. API service returns data to store action
11. Store action updates local state
12. React components re-render with new data

**Zustand State Management Pattern:**
The application uses a single centralized store with domain-separated state slices:
- Portfolio state (portfolios array, current portfolio ID, loading/error states)
- Holdings state (holdings array, loading/error states)
- Transactions state (transactions array, loading/error states)
- Price state (price loading, error, last update timestamp)

State updates follow a consistent pattern:
1. Set loading state to true
2. Make API call
3. On success: update state with new data, set loading to false
4. On error: set error state, set loading to false

The `persist` middleware saves only the `currentPortfolioId` to localStorage, ensuring that users return to their last viewed portfolio while always fetching fresh data from the server.

### API Design Philosophy

DCAPort's REST API follows RESTful conventions with nested resource routes that reflect the data hierarchy. Portfolios are the top-level resource, with holdings and transactions nested beneath them:

```
/api/v1/portfolios                             # Portfolio collection
/api/v1/portfolios/:portfolioId/holdings       # Holdings within portfolio
/api/v1/portfolios/:portfolioId/transactions   # Transactions within portfolio
```

This structure makes the API intuitive and self-documenting. The URL path clearly shows the data relationship: holdings and transactions belong to a specific portfolio. All endpoints use appropriate HTTP methods (GET for reads, POST for creates, PUT for updates, DELETE for deletes) and return consistent JSON responses.

Error handling is standardized across all endpoints. When something goes wrong, the API returns an appropriate HTTP status code (400 for validation errors, 404 for not found, 500 for server errors) along with a descriptive error message in the response body. This makes debugging easier and provides clear feedback to users.

## Technical Achievements

### Real-Time Data Synchronization
One of DCAPort's most impressive technical features is how seamlessly it keeps data synchronized between frontend and backend. When you add a transaction, the system doesn't just update the transactions table—it also recalculates the holding's weighted average cost and share count in a database transaction. The frontend then refreshes both transactions and holdings simultaneously, ensuring perfect consistency.

### Weighted Average Cost Calculation
Accurate cost basis tracking is essential for DCA investors. DCAPort implements a mathematically precise weighted average cost calculation:

```
New Average Cost = (Old Shares × Old Avg Cost + New Shares × New Price) ÷ (Old Shares + New Shares)
```

This calculation happens automatically in the backend whenever a transaction is added or edited. The system handles edge cases gracefully, such as first purchases (when old shares = 0) and ensures that edits or deletions properly recalculate the holding's average.

### Intelligent Price Fetching Strategy
The stock price service implements several optimizations to provide fast updates while respecting API limits:

**Rate Limiting:** Requests are throttled to 25 per second (safely under Finnhub's 30/second limit) using a delay between sequential fetches.

**Progress Tracking:** The frontend receives real-time progress updates as prices load, showing "Fetching 3/11 stocks" with the current ticker being fetched.

**Duplicate Call Prevention:** The store guards against duplicate fetch calls by checking a `priceLoading` flag and a 3-second cooldown timer.

**Error Handling:** Failed price fetches don't crash the app. Instead, they return null values and display clear error messages, allowing partial updates to succeed.

**Database Caching:** Fetched prices are immediately stored in the database with timestamps, providing fast data retrieval without repeated API calls.

### Responsive Design Implementation
Every page in DCAPort adapts beautifully to different screen sizes. The design uses Tailwind's responsive utilities with a mobile-first approach:

- Dashboard cards stack vertically on mobile, spread horizontally on desktop
- Data tables show essential columns on mobile, expand to full detail on desktop
- Charts resize fluidly and adjust aspect ratios for readability
- Forms use full-width inputs on mobile, constrained widths on desktop
- Navigation collapses to a hamburger menu on small screens

The result is a consistent experience whether you're checking your portfolio on your phone during lunch or analyzing performance on a desktop at home.

### Database Transaction Safety
DCAPort uses PostgreSQL transactions to ensure data consistency during complex operations. When adding a transaction, the system:

1. Begins a database transaction
2. Inserts the new transaction record
3. Updates the holding's shares and average cost
4. Commits the transaction if both operations succeed
5. Rolls back both operations if either fails

This guarantees that your data never ends up in an inconsistent state, even if the server crashes mid-operation or network issues occur.

## User Experience Highlights

### Instant Feedback on All Actions
Every user action receives immediate visual feedback through toast notifications. Add a holding? Green success toast appears. Delete a transaction? Confirmation toast confirms the action. Encounter an error? Red error toast explains what went wrong. This constant feedback loop makes the application feel responsive and trustworthy.

### Contextual Empty States
DCAPort never shows you a blank page without explanation. If you haven't selected a portfolio, you see a helpful message with an icon guiding you to create or select one. If a portfolio has no holdings, the page explains that you should add your first stock. Empty states aren't dead ends—they're opportunities to guide users toward the next action.

### Smart Form Validation
Forms validate data intelligently without being annoying. The Holding Modal checks ticker format in real-time, showing a red border if invalid. Target percentages accept decimals and validate ranges. The Transaction Modal ensures dates are valid and prices are positive. Validation errors appear inline next to the relevant field, making it crystal clear what needs fixing.

### Loading States That Build Trust
Users never wonder if the app is working. Loading states appear for all async operations: "Loading dashboard data...", "Fetching prices...", "Saving transaction...". These messages, combined with loading spinners and progress indicators, reassure users that the system is working on their request.

### Consistent Visual Language
Colors, spacing, typography, and component patterns remain consistent throughout the application. Blue indicates primary actions, green represents success and positive metrics, red shows alerts and losses, yellow marks cautions. Cards use consistent padding and shadows. Buttons follow the same size and shape patterns. This consistency reduces cognitive load and makes navigation intuitive.

## Real-World Application

### For the Disciplined DCA Investor
DCAPort is built for investors who understand the power of consistent investing over time. If you invest $500 every two weeks across multiple stocks, DCAPort becomes your command center. Log each purchase in seconds, watch your cost basis adjust automatically, and use the rebalancing calculator to decide how to allocate your next purchase.

### For Portfolio Experimenters
Want to test different allocation strategies? Create multiple portfolios: one with 80% VOO / 20% individual stocks, another with 100% individual stock picks, and a third following a sector rotation strategy. DCAPort's multi-portfolio system lets you track and compare different approaches without mixing data.

### For Performance Trackers
Some investors obsess over performance metrics (in a healthy way). The Performance and Dashboard pages provide all the data you need: unrealized gains/losses, return percentages, allocation drift, and historical trends. Track your investment journey with precision and make data-driven adjustments.

### For The "Set It and Forget It" Investor
Not everyone wants to spend hours managing their portfolio. DCAPort respects this by making essential tasks incredibly fast. Log your weekly DCA purchase in under 30 seconds. Check rebalancing status once a month in 15 seconds. Refresh prices and review performance in under a minute. The system works for active and passive management styles.

## Future Expansion Possibilities

While DCAPort is feature-complete for its core DCA mission, the architecture supports exciting future enhancements:

**User Authentication:** Add multi-user support with JWT authentication, allowing multiple users to manage their own portfolios securely.

**Export/Import:** Enable CSV export of transactions and holdings for tax reporting, and import capability for users migrating from spreadsheets.

**Performance Snapshots:** Implement automatic daily/weekly/monthly snapshots to build historical trend data and enable time-travel analysis.

**Dividend Tracking:** Extend the transaction model to track dividends received, calculating dividend yield and total return including distributions.

**Portfolio Comparison:** Side-by-side comparison of multiple portfolios with performance metrics, allocation differences, and risk analysis.

**WebSocket Real-Time Prices:** Upgrade from REST polling to WebSocket streaming for live price updates without manual refresh.

**Mobile Apps:** React Native mobile applications for iOS and Android with native performance and offline capability.

**Tax Reporting:** Generate tax forms (1099-B equivalent) with cost basis calculations using FIFO, LIFO, or specific identification methods.

**Alerts and Notifications:** Email or push notifications when stocks deviate significantly from targets or reach price thresholds.

**Benchmark Comparison:** Compare portfolio performance against market benchmarks like S&P 500, NASDAQ, or custom indices.

## Conclusion

DCAPort represents a thoughtful approach to solving a real problem that DCA investors face: how to manage multiple portfolios with discipline and clarity. By combining modern web technologies with a deep understanding of the Dollar Cost Averaging strategy, it delivers a tool that's both powerful and approachable.

The application doesn't try to be everything to everyone. It has a clear focus: make DCA investing easier through automation, visualization, and intelligent guidance. Every feature serves this mission. Every design decision prioritizes clarity and usability. Every technical choice balances performance with maintainability.

Whether you're a seasoned investor with decades of DCA experience or a beginner just starting your investment journey, DCAPort provides the structure and insights you need to stay on track. It removes the friction from portfolio management, freeing you to focus on what really matters: building long-term wealth through consistent, disciplined investing.

---

**Technology Stack Summary:**
- Frontend: React 18.3, Vite 5.4, Tailwind CSS 3.4, Zustand 4.5, Recharts 2.12
- Backend: Node.js, Express.js, PostgreSQL, Sequelize 6.35
- External APIs: Finnhub REST API for real-time stock data
- Architecture: RESTful API, SPA with client-side routing, centralized state management

**Project Status:** ✅ Production-ready, fully functional, actively maintained

**Development Approach:** Mobile-first responsive design, component-based architecture, API-first development, database-driven consistency

---

## 🏷️ Keywords

`React`, `Vite`, `Tailwind CSS`, `Node.js`, `Express.js`, `PostgreSQL`, `Sequelize`, `Zustand`, `Recharts`, `Full-Stack Development`, `SaaS`, `Web Application`, `RESTful API`, `API Development`, `API Integration`, `Database Architecture`, `Database Management`, `Responsive Design`, `JavaScript`, `HTML5`, `CSS 3`, `Git`, `GitHub`, `Lucide React`, `Investment Platform`, `Financial Technology`, `Stock Portfolio Management`
