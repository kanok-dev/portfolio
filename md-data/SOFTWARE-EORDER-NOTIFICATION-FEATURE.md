# NotifyHub Pro - Multi-Channel Notification Management System

> **🚀 Full Stack Web Application | Enterprise Notification Platform**

---

## 🏷️ Project Classification

| Category | Details |
|----------|---------|
| **Project Type** | ✅ **Full Stack Web Application** - React frontend with Node.js/Express backend |
| **Architecture** | ✅ **SaaS-Ready** - Multi-distributor notification management |
| **Integrations** | Firebase Cloud Messaging, LINE Messaging API |
| **Databases** | Microsoft SQL Server with multi-database support |

---

## Software Overview

The eOrder Notification System is a comprehensive notification management platform designed to streamline communication between distributors and their customers in the e-commerce ecosystem. Built as a full-stack web application with React and Node.js, this system bridges the gap between traditional business operations and modern digital communication channels. It serves as the backbone for keeping customers informed about critical business events such as order dates, holiday schedules, delivery updates, and inventory status.

At its core, the system intelligently manages multiple notification channels - Firebase Cloud Messaging for mobile push notifications and LINE Messaging API for chat-based communication. This dual-channel approach ensures that important business information reaches customers through their preferred medium, whether they're using the mobile app or LINE messenger.

The platform was built with scalability and reliability in mind, managing notifications for multiple distributors and their respective customer bases while maintaining data integrity across several interconnected databases. It's particularly well-suited for businesses that operate on scheduled ordering systems where timing is critical, such as distributors serving retail shops or restaurants.

## Software Objectives

### Primary Goals

**Automated Customer Communication**
The system eliminates manual notification processes by automatically sending reminders to customers about their ordering schedules. When a customer's order date is approaching, they receive timely notifications ensuring they don't miss their designated ordering window. This automation reduces administrative burden and prevents lost sales due to missed orders.

**Holiday and Business Continuity Management**
During holidays or non-operational days, the system proactively notifies affected customers about schedule changes, alternative ordering dates, and expected delivery times. This transparency helps customers plan their inventory accordingly and maintain business continuity even during disruption periods.

**Multi-Channel Delivery Flexibility**
By supporting both mobile push notifications through Firebase and messaging through LINE, the system meets customers where they are. Some customers prefer instant mobile notifications, while others engage more through LINE's familiar interface. The system accommodates both preferences seamlessly.

**Real-Time Inventory Awareness**
Product availability notifications keep customers informed about stock levels, helping them make better purchasing decisions and adjust their orders based on current inventory status. This reduces disappointment and improves the overall customer experience.

### Secondary Objectives

**Centralized Management Dashboard**
Administrators can monitor the entire customer base, view upcoming notification schedules, manage holiday calendars, and track notification delivery status through a clean, intuitive web interface. This centralized control eliminates the need to juggle multiple tools.

**Data-Driven Insights**
The dashboard provides visibility into notification patterns, customer engagement metrics, and upcoming notification schedules. These insights help businesses optimize their communication strategy and understand customer behavior patterns.

**Device Management and Targeting**
The system tracks device registrations, notification tokens, and app versions, enabling targeted communication to specific device types, operating systems, or app versions when needed. This granular control is invaluable for testing new features or troubleshooting issues.

## Technical Stack

### Frontend Technologies

**React 18.2** - The modern JavaScript library powers the user interface, providing a responsive and dynamic experience. Component-based architecture ensures maintainability and reusability across the dashboard.

**Material-UI 5** - Google's Material Design system implemented through MUI provides a professional, accessible interface. The comprehensive component library accelerates development while maintaining consistent design patterns.

**Redux Toolkit** - Manages application state efficiently, particularly for user authentication, dashboard data, and global settings. The toolkit simplifies complex state management patterns.

**Formik & Yup** - Handle form validation and submission throughout the application, ensuring data integrity before it reaches the backend.

**Axios** - Powers all API communication with the backend, providing a clean interface for HTTP requests with built-in error handling.

**ApexCharts & React-ApexCharts** - Create interactive, visually appealing charts and graphs for dashboard analytics, helping users understand notification patterns at a glance.

**MUI Data Grid** - Renders large datasets efficiently with built-in sorting, filtering, and pagination capabilities, essential for managing extensive customer lists.

### Backend Technologies

**Node.js** - The JavaScript runtime enables building a fast, scalable server capable of handling numerous concurrent notification requests.

**Express.js** - Provides the web framework foundation, handling routing, middleware, and HTTP request/response cycles with minimal overhead.

**Microsoft SQL Server (mssql)** - The primary data store manages customer information, user accounts, distributor data, and holiday schedules across multiple interconnected databases.

**Firebase Admin SDK** - Enables server-side Firebase Cloud Messaging operations, allowing the system to send push notifications to iOS and Android devices reliably.

**LINE Messaging API SDK** - Facilitates integration with LINE's platform for sending messages and managing LINE bot interactions programmatically.

**Sequelize** - The ORM (Object-Relational Mapping) library simplifies database interactions, providing a clean JavaScript interface for complex SQL queries across multiple database instances.

**Node-Cron** - Schedules automated tasks such as daily notification sweeps, checking for upcoming order dates, and triggering holiday notifications at predetermined times.

**Moment.js** - Handles all date and time manipulations, crucial for a system dealing with scheduling, timezones, and date-based triggers.

### Security & Performance

**Helmet** - Secures Express applications by setting various HTTP headers, protecting against common web vulnerabilities.

**Cors** - Manages Cross-Origin Resource Sharing, controlling which domains can access the API while maintaining security boundaries.

**Express-Mongo-Sanitize** - Prevents NoSQL injection attacks by sanitizing user input, even though the system primarily uses SQL Server.

**Express-Rate-Limit** - Protects the API from abuse by limiting the number of requests from a single IP address within a time window.

**HPP (HTTP Parameter Pollution)** - Guards against parameter pollution attacks that could manipulate query strings maliciously.

**XSS-Clean** - Sanitizes user input to prevent cross-site scripting attacks.

**Compression** - Reduces response payload sizes through gzip compression, improving performance for users on slower connections.

**Dotenv** - Manages environment variables securely, keeping sensitive credentials out of the codebase.

### Deployment & Process Management

**PM2** - Manages Node.js processes in production, providing automatic restarts, load balancing, and process monitoring. The system runs multiple instances for different environments (API server, web server, scheduler) managed through PM2.

## Core Features

### 1. Dashboard & Analytics

The dashboard serves as the command center for the entire notification system. Upon login, administrators see a comprehensive overview of their customer base with key metrics displayed prominently.

**Customer Overview**
The main dashboard displays total customer counts, active users, and upcoming notification schedules. Visual charts break down notification patterns by date, helping administrators anticipate high-volume notification days and ensure system readiness.

**Data Grid Management**
A powerful data grid component displays all customers with their ordering schedules, distributor assignments, and contact information. Users can sort by any column, filter results, search for specific customers, and export data for external analysis. The grid handles thousands of records efficiently through intelligent pagination and virtualization.

**Notification Calendar**
A calendar view shows which customers will receive notifications on which dates, providing a visual representation of the notification schedule. This bird's-eye view helps identify patterns and potential issues before they occur.

### 2. Multi-Channel Notification System

**Firebase Push Notifications**
The system integrates deeply with Firebase Cloud Messaging to send rich push notifications to mobile devices. Notifications include custom data payloads, allowing the mobile app to respond appropriately - perhaps opening a specific screen or displaying particular information.

The notification engine handles device token management automatically. When a device token expires or becomes invalid, the system logs the failure and can alert administrators to investigate. Notifications are sent in batches to optimize performance, with support for multicast messaging that can reach hundreds of devices efficiently.

Each notification includes platform-specific configurations - Android notifications receive high-priority delivery with custom sounds, while iOS notifications include badge counts and content availability flags for background processing.

**LINE Messaging Integration**
For customers who prefer LINE communication, the system sends formatted messages through LINE's bot API. Messages can be simple text or rich flex messages with structured layouts, buttons, and images.

The LINE integration maintains a registry of users who have connected their accounts to the LINE bot. When sending messages, the system looks up the appropriate LINE user IDs based on department assignments or distributor relationships, ensuring messages reach the right recipients.

**Smart Scheduling**
Notifications don't just fire randomly - they're intelligently scheduled based on business logic. The system calculates when customers need to be reminded based on their designated order dates, typically sending notifications 1-2 days in advance. For holidays, notifications go out on specific dates configured by administrators, ensuring customers have adequate time to plan around business closures.

### 3. Holiday Management

Holiday management is a sophisticated feature that coordinates notification timing across multiple distributors who may have different holiday schedules.

**Holiday Calendar Configuration**
Administrators define holidays for each distributor, specifying the holiday date, the notification date, the export date (when orders will be processed), and a custom message explaining the schedule change to customers. This flexibility accommodates diverse business needs - some distributors might process orders early before a holiday, while others might skip a day entirely.

**Automated Holiday Notifications**
The cron scheduler checks daily for any holidays that require notifications. When the notification date arrives, the system queries all customers associated with that distributor, retrieves their notification tokens, and sends appropriately formatted messages through both Firebase and LINE channels.

The holiday message typically includes the holiday date, the alternate ordering date, the expected delivery date, and recommendations for customers to order additional inventory to cover the gap period. This comprehensive information helps customers make informed decisions.

**Holiday Status Display**
The holiday management interface displays all configured holidays in a sortable grid. Administrators can see which holidays are upcoming, which have already passed, and which notifications have been sent. Holidays can be edited or soft-deleted (marked inactive) without losing historical data.

### 4. Device & User Management

**Device Registration Tracking**
Every mobile device that installs the eOrder app and enables notifications gets registered in the system. The device registry captures detailed information including device brand, model, operating system, OS version, app version, bundle ID, and build number.

This granular tracking serves multiple purposes. Developers can identify which app versions are in use and target specific versions for notifications about updates. Support teams can troubleshoot notification issues by examining device configurations. Administrators can see the split between iOS and Android users, informing platform investment decisions.

**Notification Token Management**
Firebase notification tokens are managed automatically. When a user logs into the mobile app, the app sends its current token to the backend, which updates the database record. If a token changes (which Firebase occasionally does), the system automatically updates to the new token.

Invalid tokens are handled gracefully - when a notification fails due to an invalid token, the system logs the failure but doesn't crash the entire batch operation. This resilience ensures that one problematic device doesn't prevent others from receiving their notifications.

**User-Customer Relationships**
The system maintains complex relationships between users, customers, and distributors. A single user might be associated with multiple customers, or multiple users might manage a single customer account. The data model accommodates these scenarios while ensuring notifications reach all appropriate parties.

### 5. Product & Inventory Notifications

**Stock Availability Updates**
When product availability changes, the system can notify affected customers. This feature is particularly valuable for high-demand items or products with limited seasonal availability. Customers receive timely updates allowing them to adjust their orders before stock runs out.

**User-Specific Product Management**
Each user has a personalized product list based on their purchasing history and preferences. The system can query products by user or by distributor, enabling targeted inventory notifications. For example, if a specific distributor's warehouse receives a new shipment, only customers of that distributor get notified about newly available items.

### 6. Authentication & Authorization

**Secure Login System**
The authentication system uses token-based authentication, generating secure tokens upon successful login. These tokens must accompany most API requests, ensuring only authenticated users can access sensitive operations.

**Middleware Protection**
An authentication middleware intercepts protected routes, validating tokens before allowing requests to proceed. Invalid or expired tokens are rejected with appropriate error messages, prompting users to log in again.

**Role-Based Access**
While the current implementation focuses on authenticated vs. unauthenticated access, the architecture supports extending to role-based permissions. Future enhancements could restrict certain operations (like holiday configuration) to administrator roles while allowing read-only access to standard users.

### 7. Application Version Management

**Version Control Dashboard**
Administrators can track mobile app versions in use across the customer base. The version management interface displays all app versions, their release dates, and how many users are running each version.

This visibility helps with deprecation decisions - if 95% of users have upgraded to a new version, it might be safe to deprecate an old API endpoint that only the old version used. It also helps identify users stuck on outdated versions who might need upgrade reminders.

**Version-Specific Notifications**
The system can send notifications targeted at specific app versions. This is invaluable when rolling out features gradually or notifying users of critical updates. For example, users on an old version with a security vulnerability could receive a notification urging them to update.

### 8. Scheduled Automation

**Cron-Based Task Scheduling**
The scheduler service runs continuously, executing tasks at predetermined intervals. Daily tasks check for customers whose order dates are approaching and send reminder notifications. Hourly tasks might check for holiday notifications that need to be sent.

The cron implementation uses node-cron with human-readable schedules like "0 8 * * *" for "every day at 8 AM". This flexibility allows administrators to adjust notification timing to match customer preferences and business hours.

**Batch Processing Efficiency**
Rather than sending notifications one at a time, the scheduler queries all customers who need notifications, groups them by notification type, and sends batch operations to Firebase and LINE. This approach dramatically improves performance, allowing the system to notify thousands of customers in seconds rather than minutes.

### 9. LINE Bot Integration

**Interactive LINE Bot**
Beyond sending outbound notifications, the system includes a LINE bot that can respond to user interactions. When users send messages to the bot or interact with button prompts, the bot can provide information, answer questions, or trigger specific actions.

**Department-Based Messaging**
The LINE integration supports department-based user organization. Users register with the LINE bot and identify their department, enabling targeted messaging to specific teams or business units. This is useful for internal notifications to sales teams or warehouse staff.

**Flex Message Templates**
LINE's flex message format allows rich, structured messages with images, buttons, and formatted text. The system includes templates for common notification types, ensuring consistent, professional communication across all LINE messages.

### 10. API Architecture

**RESTful Design**
The API follows REST principles with clear resource endpoints and appropriate HTTP methods. GET requests retrieve data, POST creates new records, PUT updates existing ones, and DELETE (or soft-delete via POST) removes records. This consistency makes the API intuitive for developers.

**Comprehensive Error Handling**
Every endpoint includes try-catch error handling, returning meaningful error messages when operations fail. This prevents cryptic failures and helps developers diagnose issues quickly.

**Logging & Monitoring**
The backend logs important events, errors, and notification results. These logs are invaluable for troubleshooting issues, monitoring system health, and understanding usage patterns.

## System Architecture Highlights

**Multi-Database Coordination**
The system connects to multiple SQL Server databases simultaneously - a security database for user authentication, a main database for customer and distributor information, an eOrder-specific database for order data, and a notification database for device registrations and notification history. Sequelize manages these connections efficiently, pooling connections for optimal performance.

**Separation of Concerns**
The codebase is organized with clear separation between controllers (business logic), routes (endpoint definitions), services (external integrations), and middleware (request processing). This modular architecture makes the system maintainable and testable.

**Scalable Deployment**
Using PM2 for process management allows the system to run multiple Node.js processes, utilizing all available CPU cores. PM2 automatically restarts crashed processes, ensuring high availability even when unexpected errors occur.

**Environment-Based Configuration**
Environment variables control database connections, API keys, and feature flags. This design allows the same codebase to run in development, staging, and production environments with different configurations, managed through .env files.

## Future Enhancement Opportunities

While the system is robust and feature-complete, several enhancement opportunities exist:

- **Webhook Integration** - Allow external systems to trigger notifications via webhook endpoints
- **Analytics Dashboard** - Expand reporting with notification delivery rates, open rates (for LINE), and engagement metrics
- **Template Management** - Move notification message templates into the database for easier customization without code changes
- **Multi-Language Support** - Add internationalization for notifications in multiple languages based on customer preferences
- **Advanced Scheduling Rules** - Support for more complex scheduling logic like "notify every Tuesday" or "skip notifications during specific date ranges"
- **Notification History** - Track all sent notifications with delivery status, allowing users to see their notification history
- **Two-Way Communication** - Enable customers to respond to notifications, creating interactive workflows
- **Real-Time Dashboard Updates** - WebSocket integration for live dashboard updates without page refreshes

## Conclusion

The eOrder Notification System represents a mature, production-ready platform for managing multi-channel customer communications in the e-commerce space. Its thoughtful architecture balances flexibility with reliability, making it suitable for businesses ranging from single-distributor operations to multi-distributor networks with thousands of customers.

The dual-channel approach using both mobile push notifications and LINE messaging ensures broad reach, while the automated scheduling and holiday management features reduce administrative overhead. The clean, intuitive dashboard gives administrators the visibility and control they need to manage notifications confidently.

Built with modern web technologies and following best practices for security, performance, and maintainability, this system stands ready to scale with growing business needs while providing a solid foundation for future enhancements.

---

## 🏷️ Keywords

`React`, `Node.js`, `Express.js`, `Redux Toolkit`, `Material UI`, `Microsoft SQL Server`, `Sequelize`, `Full-Stack Development`, `Web Application`, `RESTful API`, `API Development`, `API Integration`, `Firebase Cloud Messaging`, `LINE Messaging API`, `Push Notifications`, `PM2`, `node-cron`, `Axios`, `ApexCharts`, `MUI DataGrid`, `Formik`, `Yup`, `JWT`, `Database Management`, `Microservice`, `SaaS`, `JavaScript`, `HTML5`, `CSS`, `Responsive Design`, `Git`, `GitHub`
