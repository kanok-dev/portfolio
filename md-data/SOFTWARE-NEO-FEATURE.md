# NEO Services - Enterprise Database Health Monitoring Platform

> **🚀 Full Stack Web Application | Database Monitoring SaaS**

---

## 🏷️ Project Classification

| Category | Details |
|----------|---------|
| **Project Type** | ✅ **Full Stack Web Application** - React 19 frontend with Node.js/Express backend |
| **Architecture** | ✅ **SaaS Platform** - Multi-database monitoring with configurable schedules |
| **Databases** | Microsoft SQL Server, PostgreSQL, Redis caching |
| **Integrations** | LINE Messaging API for instant notifications |

---

## Software Overview

NEO Services is an enterprise-grade database monitoring and health check platform built to oversee multiple Microsoft SQL Server databases simultaneously. Think of it as your vigilant database guardian that never sleeps, constantly watching over your critical business data and alerting you the moment something seems off.

The platform was born from a real-world need to manage dozens of distributed databases across different projects and clients. Rather than manually checking each database or waiting for users to report issues, NEO Services proactively monitors transaction integrity, invoice sequences, and data quality around the clock. When it finds something suspicious, like missing invoice numbers or duplicate product prices, it immediately notifies your team through LINE messaging so you can address issues before they impact your business.

What makes NEO Services particularly powerful is its flexibility. Each monitored database can have its own custom schedule, specific checks to run, and tailored notification settings. The web-based dashboard gives you a bird's-eye view of all your database health statuses in one place, with drill-down capabilities to investigate specific issues.

## Software Objectives

The primary mission of NEO Services is to eliminate database monitoring blind spots and catch data integrity issues early. We built this platform with several core objectives in mind:

**Proactive Issue Detection**: Instead of discovering problems after they've caused damage, NEO Services finds anomalies in real-time. Whether it's a gap in invoice numbering that could indicate lost transactions or duplicate pricing that might confuse your sales team, the system catches it immediately.

**Reduce Manual Overhead**: Database administrators and DevOps teams have enough on their plates without manually querying multiple databases for health checks. NEO Services automates these repetitive tasks, freeing up your technical staff to focus on more strategic work.

**Centralized Monitoring**: Managing multiple databases typically means juggling multiple tools and dashboards. NEO Services consolidates everything into a single pane of glass where you can see the health of all your databases at once.

**Instant Communication**: When issues arise, time matters. Direct LINE integration ensures your team gets notifications on the device they're already using, with rich formatted messages that include all the context needed to take action.

**Flexible Configuration**: Every business is different, and every database has unique characteristics. NEO Services lets you configure check schedules, customize validation rules, and fine-tune notification preferences for each individual database.

## Technical Stack

### Backend Architecture

The heart of NEO Services runs on **Node.js** with **Express.js** handling the API layer. We chose this stack for its excellent async capabilities, which is crucial when managing concurrent connections to multiple databases. The backend architecture follows a service-oriented pattern, separating concerns between database connectivity, health checking logic, configuration management, and notification delivery.

**Database Connectivity** leverages the `mssql` library to establish connection pools with each monitored SQL Server instance. We use connection pooling to maintain persistent, reusable database connections that minimize overhead. The system intelligently handles connection failures with automatic retry logic and graceful degradation when specific databases are temporarily unreachable.

For storing application configuration and metadata, we utilize **PostgreSQL** with **Sequelize** ORM. This gives us a robust, relational structure for managing project definitions, cron schedules, user accounts, and system settings. The choice of PostgreSQL provides ACID compliance for critical configuration data and supports complex queries when needed.

**Redis** serves as our caching layer and helps prevent duplicate notifications. When the system detects an issue, it checks Redis to see if we've already notified about that specific problem recently, avoiding notification fatigue from repeated alerts about the same issue.

Job scheduling relies on **node-cron**, which provides flexible cron expression support. Each database project can define its own schedule using standard cron syntax, allowing precise control over when health checks run.

### Frontend Experience

The user interface is built with **React 19**, taking advantage of the latest React features for optimal performance and developer experience. We use **Vite** as our build tool, which provides lightning-fast hot module replacement during development and optimized production builds.

**TailwindCSS** handles all styling through a utility-first approach, making the UI responsive and maintainable. The dashboard features real-time status updates, configuration panels, and detailed views of check results.

Authentication flows through **JWT tokens** with **bcrypt** password hashing, providing secure access control. The system implements role-based permissions, ensuring that only authorized users can modify configurations or trigger manual checks.

### Integration & Notifications

**LINE Messaging API** powers the notification system. When health checks detect issues, the system formats detailed Flex Messages with tables, summaries, and actionable information before pushing them to configured LINE user IDs. The LINE integration supports both individual push messages and multicast for team notifications.

**Winston** handles logging throughout the application, writing structured logs to both files and console with appropriate log levels. This makes troubleshooting straightforward and provides an audit trail of all system activities.

### Process Management

In production, **PM2** manages the Node.js processes, providing automatic restarts on crashes, log rotation, and monitoring capabilities. The project includes three PM2 ecosystem files for different deployment scenarios - API only, frontend only, or full stack.

## Key Features & Capabilities

### Multi-Database Health Monitoring

NEO Services can monitor virtually unlimited SQL Server databases simultaneously. Each database is configured as a "project" with its own connection string, schedule, and enabled checks. The system maintains separate connection pools for each database, ensuring that issues with one don't impact monitoring of others.

Health checks run according to the configured cron schedule for each project. When it's time to check a database, the system:
- Verifies the connection pool is healthy
- Executes the configured SQL validation queries
- Analyzes the results for anomalies
- Caches findings in Redis to prevent duplicate alerts
- Sends notifications if new issues are detected
- Updates the project's status in the dashboard

### Transaction Validation

One of the most valuable checks is transaction validation. This feature examines sales orders, invoices, and delivery documents to ensure data consistency. The service queries for:

- Documents created or updated by specific users within a timeframe
- Transactions with unusual status progressions
- Date discrepancies between creation and business dates
- User activity patterns that deviate from normal

When the system finds suspicious transactions, it aggregates them into a comprehensive report with user breakdowns, document types, and timestamps. This helps identify both technical issues (like failed updates) and potential process problems (like documents stuck in draft status).

### Invoice Number Integrity

Missing invoice numbers can indicate lost sales, technical failures, or even fraud. NEO Services specifically checks for gaps in invoice number sequences per user and per day. The system:

- Identifies the expected sequential pattern for each user's invoices
- Detects any missing numbers in the sequence
- Calculates gap sizes and ranges
- Reports the specific missing invoice numbers
- Provides context about surrounding invoices

This granular gap detection catches even small discrepancies that might otherwise go unnoticed until month-end reconciliation.

### Duplicate Product Price Detection

Pricing accuracy is critical for e-commerce and sales systems. NEO Services scans for duplicate product entries with different prices, which could confuse inventory systems or create invoicing errors. The check identifies:

- Products with multiple active price points
- Duplicate entries in price master tables
- Effective date overlaps that could cause ambiguity
- Historical changes that might indicate data quality issues

When duplicates are found, notifications include the product codes, descriptions, conflicting prices, and affected date ranges.

### Configurable Cron Scheduling

Every project can define its own monitoring schedule using standard cron expressions. Common patterns include:

- Hourly checks during business hours: `0 9-17 * * 1-5`
- Daily off-hours validation: `0 2 * * *`
- Frequent high-priority monitoring: `*/15 * * * *`

The cron controller provides API endpoints to view, update, and persist schedule changes. Schedules can be modified through the web interface and take effect immediately without requiring service restarts.

### LINE Notification System

Integration with LINE makes notifications feel natural because most teams already use LINE for business communication. The notification system formats messages beautifully with:

- **Alert Headers** highlighting the issue severity and database
- **Summary Statistics** showing counts and affected records
- **Detailed Tables** (when appropriate) listing specific problems
- **Flex Messages** with rich formatting, colors, and layout
- **Timestamp Information** with timezone-aware display

Notifications support both summary mode (just counts and high-level info) and detailed mode (including specific records). This prevents message overflow while still providing necessary detail.

The system tracks notification history in Redis, implementing deduplication logic to avoid spamming the team about the same issue repeatedly. Once an issue is notified, subsequent detections within a configurable time window are suppressed.

### Web Dashboard

The React-based dashboard provides comprehensive visibility and control:

**System Overview**: See all configured projects at a glance with status indicators showing healthy, warning, or error states. Quick stats show total databases monitored, active cron jobs, and recent check results.

**Project Management**: Add new database projects, edit connection strings, enable or disable specific health checks, and configure notification preferences. The interface validates configuration inputs and tests database connections before saving.

**Cron Configuration**: Visual cron editors help build complex schedules without memorizing cron syntax. See upcoming execution times and manually trigger checks for immediate validation.

**Real-Time Status**: Health check results stream to the dashboard in real-time. Drill into specific projects to see detailed check history, error logs, and notification records.

**User Authentication**: Role-based access control ensures sensitive operations like adding databases or modifying schedules require appropriate permissions. The system supports multiple user accounts with different permission levels.

### API Layer

A comprehensive REST API powers the frontend and enables integration with external tools:

- **GET /api/projects** - List all monitored databases with current status
- **GET /api/projects/:id** - Detailed project information and check history
- **POST /api/projects** - Register a new database to monitor
- **GET /api/cron/status** - View all scheduled jobs and their next run times
- **POST /api/cron/trigger/notifications** - Manually trigger notification processing
- **GET /health** - System health endpoint for monitoring NEO Services itself

The API implements rate limiting, CORS protection, request validation, and comprehensive error handling. All responses follow a consistent JSON structure with proper HTTP status codes.

### Database Service Layer

At the core is a sophisticated database service that manages connection pools, handles automatic reconnection, and provides clean abstractions over raw SQL queries. The service:

- Initializes connection pools on startup
- Monitors pool health and connectivity
- Implements exponential backoff for reconnection attempts
- Provides helper methods for common query patterns
- Handles transaction management and query timeout
- Logs all database interactions for troubleshooting

Connection configurations support standard SQL Server options like authentication, encryption, connection timeout, and request timeout. The service handles both SQL authentication and Windows authentication modes.

### Configuration Management

NEO Services stores all configuration in PostgreSQL using Sequelize models. This approach provides several advantages:

- **Version Control**: Track configuration changes over time
- **Backup & Recovery**: Database backups include all system configuration
- **Multi-Environment**: Separate development, staging, and production configs
- **Migration Support**: Schema changes through Sequelize migrations
- **Query Flexibility**: Complex configuration queries when needed

The configuration service exposes methods to read, write, and validate settings without exposing raw SQL. This abstraction makes the codebase more maintainable and testable.

### Security & Reliability

Security considerations are baked into the architecture:

- Passwords encrypted with bcrypt (10 rounds)
- JWT tokens with configurable expiration
- Environment variable isolation for secrets
- Helmet.js security headers on all responses
- Rate limiting on API endpoints
- Input validation on all user-provided data
- CORS restrictions to allowed origins
- SQL injection prevention through parameterized queries

Reliability features include:

- Automatic process restart via PM2
- Health check endpoints for monitoring
- Comprehensive error handling and logging
- Connection pool management with auto-recovery
- Graceful degradation when services are unavailable
- Duplicate notification prevention
- Transaction rollback on failures

## Development & Deployment

### Development Workflow

The project supports a streamlined development experience:

```bash
# Install all dependencies (backend and frontend)
yarn install:all

# Run backend API in development mode
yarn dev

# Run frontend dev server (separate terminal)
yarn client

# Or run both concurrently
yarn dev:full
```

The backend runs on port 5010 while Vite serves the frontend on port 5173. Hot module replacement ensures instant feedback when editing React components. Backend changes trigger nodemon restarts for quick iteration.

### Production Deployment

Production deployment leverages PM2 for robust process management:

```bash
# Start just the API with PM2
pm2 start ecosystem.config.js --env production

# Or use the convenient script
./start-pm2.sh api
```

The production build serves the compiled React app as static files from the Express server, eliminating the need for separate frontend hosting. Nginx can sit in front for SSL termination and load balancing if needed.

Environment-specific configuration lives in `.env` files:
- `.env.development` - Local development settings
- `.env.production` - Production configuration
- `.env.example` - Template with all available variables

## Future Roadmap

While NEO Services already delivers tremendous value, we have exciting enhancements planned:

**Database Support Expansion**: Adding PostgreSQL, MySQL, and MongoDB monitoring capabilities would make NEO Services a universal database health platform.

**Custom Check Builder**: A visual interface for building custom SQL validation queries without writing code would empower non-technical users to define domain-specific checks.

**Trend Analysis**: Historical tracking of check results over time could identify degrading performance, growing data issues, or seasonal patterns.

**Alert Routing**: More sophisticated notification rules that route different issue types to different LINE groups or integrate with email, Slack, or PagerDuty.

**Dashboard Analytics**: Visual charts and graphs showing database health trends, check success rates, and issue frequency over time.

**Mobile App**: Native mobile apps for iOS and Android would complement the LINE notifications with a dedicated monitoring interface.

**Automated Remediation**: For common issues, the system could automatically execute corrective actions rather than just notifying about problems.

## Conclusion

NEO Services represents a mature, production-ready solution for organizations serious about database reliability. It transforms reactive fire-fighting into proactive management, catches issues before they become incidents, and provides the visibility needed to maintain confidence in your data infrastructure.

Whether you're managing databases for multiple clients, operating a distributed microservices architecture, or simply want better oversight of your critical data stores, NEO Services delivers the monitoring, alerting, and management capabilities you need. The combination of flexible configuration, real-time notifications, and comprehensive health checks makes it an invaluable tool for any team responsible for database operations.

---

*Built with passion for reliable systems and maintained data integrity.*

---

## 🏷️ Keywords

`Node.js`, `Express.js`, `React`, `Vite`, `TailwindCSS`, `PostgreSQL`, `Microsoft SQL Server`, `Redis`, `Sequelize`, `Full-Stack Development`, `Web Application`, `RESTful API`, `API Development`, `API Integration`, `JWT`, `LINE Messaging API`, `node-cron`, `PM2`, `Winston`, `Database Monitoring`, `SaaS`, `JavaScript`, `TypeScript`, `HTML5`, `CSS`, `Git`, `GitHub`, `Database Management`, `Database Architecture`, `Health Monitoring`, `Automated Alerts`
