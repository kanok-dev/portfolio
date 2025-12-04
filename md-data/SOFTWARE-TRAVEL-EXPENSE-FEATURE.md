# TravelExpense Pro - Enterprise Travel & Expense Management System

> **🚀 Full Stack Web Application | Enterprise Expense Platform**

---

## 🏷️ Project Classification

| Category | Details |
|----------|---------|
| **Project Type** | ✅ **Full Stack Web Application** - Next.js 14 frontend with Express.js backend |
| **Architecture** | ✅ **Enterprise Solution** - Multi-level approval workflows |
| **Databases** | Microsoft SQL Server with Sequelize ORM |
| **Integrations** | SAP integration for accounts payable |

---

## Executive Overview

The Glico Travel Expense Management System represents a comprehensive enterprise solution designed to streamline the entire lifecycle of business travel planning and expense reimbursement. Built as a full-stack web application, this system addresses the complex needs of modern organizations where employees frequently travel for business purposes, requiring meticulous tracking, approval workflows, and financial reconciliation.

At its core, this platform transforms what traditionally has been a paper-intensive, error-prone process into a digital workflow that brings transparency, accountability, and efficiency to travel expense management. From the moment an employee plans a business trip to the final payment processing through SAP integration, every step is carefully orchestrated through this sophisticated system.

## Software Objective

### Primary Mission
The system serves as the central hub for managing all aspects of business travel expenses within the organization, eliminating manual processes and reducing the time between expense submission and reimbursement while maintaining rigorous approval controls and audit compliance.

### Core Goals

**Financial Control & Compliance**
The system enforces policy-based approval workflows that ensure every travel expense adheres to company policies and spending limits. Multi-level approval hierarchies guarantee that expenses are reviewed by appropriate authorities based on amount thresholds, employee positions, and departmental budgets. This prevents unauthorized spending and maintains financial integrity across the organization.

**Process Efficiency**
By digitizing the entire travel expense lifecycle, the system dramatically reduces processing time. Employees can submit expenses with attached receipts digitally, managers can approve from anywhere, and finance teams receive pre-validated, organized expense data ready for payment processing. What once took weeks now takes days.

**Audit Trail & Transparency**
Every action within the system is tracked and timestamped. From initial travel plan creation to final SAP payment posting, the system maintains a complete audit trail. This transparency serves both compliance requirements and provides employees with real-time visibility into their expense status.

**Integration & Automation**
The system seamlessly integrates with enterprise SAP systems for accounts payable processing, eliminating duplicate data entry and ensuring financial data consistency across platforms. Automated calculations, policy validations, and notification systems reduce manual intervention and human error.

## Technical Stack

### Frontend Architecture

**Next.js 14 Framework**
The application leverages Next.js, a production-ready React framework that provides server-side rendering, automatic code splitting, and optimized performance out of the box. This choice ensures fast page loads and excellent user experience, critical for a system used daily by employees across the organization.

**React 18.2.0**
React's component-based architecture allows for building reusable UI elements that maintain consistency across the application. The virtual DOM ensures efficient updates and smooth interactions even when handling complex data structures like multi-level expense entries.

**Material-UI v5 Design System**
The entire interface is built using Material-UI components, providing a professional, modern appearance that follows Google's Material Design principles. This ensures accessibility, responsive design, and a familiar user experience. Combined with TailwindCSS for utility-first styling, developers have the flexibility to customize designs while maintaining consistency.

**Redux State Management**
Redux manages application state centrally, ensuring that user data, form inputs, and API responses are accessible throughout the component tree. This is particularly valuable for maintaining form data across multi-step processes like travel planning and expense submission.

**Formik & Yup Validation**
Form handling is powered by Formik, which manages form state, validation, and submission logic elegantly. Yup schemas define validation rules, ensuring data integrity before submission. This combination reduces boilerplate code and provides robust client-side validation.

### Backend Infrastructure

**Express.js API Server**
The backend runs on Express.js, a minimal and flexible Node.js web application framework. It handles all API routes, authentication middleware, and business logic processing. Running on port 5002, it serves as the bridge between the frontend application and the database.

**Node.js 20 Runtime**
The application runs on Node.js 20, benefiting from the latest performance improvements and modern JavaScript features. Babel is configured to target this specific version, ensuring optimal compatibility and leveraging async/await patterns throughout the codebase.

**Sequelize ORM**
Database interactions are managed through Sequelize, a promise-based ORM that supports Microsoft SQL Server. This abstraction layer provides model definitions, associations, migrations, and query building while protecting against SQL injection through parameterized queries.

### Database & Storage

**Microsoft SQL Server**
The primary database stores all application data in a structured relational format. Running at 215.10.50.11:1390 in production, it handles complex relationships between employees, travel plans, expenses, approvals, and policies. Sequelize migrations ensure database schema versioning and controlled updates.

**File Upload Management**
Document uploads (receipts, supporting documents) are stored in the `/public/uploads/` directory with a 50MB limit per file. The system supports multiple file formats and maintains references in the database for retrieval and audit purposes.

### Authentication & Security

**JWT Token Authentication**
The system uses JSON Web Tokens for stateless authentication. Upon successful login, users receive a token valid for 30 days, stored securely and transmitted with each API request. The `isAuth` middleware validates tokens and extracts user information for authorization decisions.

**Role-Based Access Control**
A sophisticated permission system controls access to features based on user roles. The database stores roles, permissions, and their mappings, allowing fine-grained control over who can create, view, approve, or manage different types of expense records.

### Deployment & Process Management

**PM2 Process Manager**
In production environments, PM2 manages the Node.js application, providing automatic restarts, load balancing capabilities, log management, and startup scripts. The ecosystem configuration allocates 8GB of memory to handle concurrent users and large dataset processing.

**Docker Support**
The application can be containerized using Docker Compose, orchestrating the web application and database services together. This approach ensures consistent environments across development, staging, and production deployments.

## Core Features & Functionality

### 1. Travel Planning & Route Management

**Comprehensive Trip Planning**
Employees begin by creating travel plans that include trip names, dates, objectives, and destinations. The system captures the year of travel, date ranges, and associates plans with specific employees. Each plan receives a unique code (TP-formatted identifier) for easy reference.

**Multi-Destination Support**
A single travel plan can include multiple destinations through the "Plan to Visit" feature. For each destination, employees specify provinces, objectives, visit dates, travel routes, mileage, and accommodations. This granular planning ensures all travel aspects are documented upfront.

**Travel Objectives Tracking**
The system maintains master data for travel objectives and objective details, allowing standardization of travel purposes across the organization. Whether visiting customers, attending conferences, or conducting site inspections, every trip has a documented business purpose.

**Route & Mileage Documentation**
For each destination, the system tracks routes traveled and kilometers covered. This is particularly important for fleet car usage and mileage-based reimbursements, ensuring accurate calculation of travel allowances.

### 2. Expense Entry & Documentation

**Accommodation Expenses**
Employees record hotel details including hotel names, contact numbers, and costs. The system tracks accommodation expenses separately, applying appropriate tax calculations and validations based on company policies.

**Meal Allowances**
The system supports separate tracking for breakfast, lunch, and dinner allowances. These can be based on standardized per-diem rates stored in employee profiles or actual expenses with receipts. The flexibility accommodates different travel scenarios and policy requirements.

**Transportation Expenses**
Multiple transportation categories are supported:
- **Taxi & Bus**: Public transportation costs
- **Fleet Card Usage**: Company car fuel expenses with mileage tracking
- **Toll Fees**: Highway and toll road charges
- **Parking Fees**: Parking expenses during business travel

**Nature of Expense Categories**
Beyond standard categories, the system supports custom expense types through the "Nature of Expense" functionality. This includes entertainment expenses, miscellaneous costs, and other business-related spending that doesn't fit standard categories. Each expense type can be associated with specific GL accounts for accounting purposes.

**Tax & VAT Management**
The system handles complex tax scenarios through dedicated VAT and Input Tax tracking. Employees can record tax amounts on expenses, supporting both reclaimable VAT scenarios and withholding tax situations. This ensures proper tax reporting and compliance.

**Receipt & Document Attachment**
Every expense can have multiple supporting documents attached. The system accepts images and PDFs, storing them securely while maintaining database references. This digital receipt management eliminates the need for physical receipt submission and provides instant access during approvals.

### 3. Multi-Level Approval Workflow

**Intelligent Approval Routing**
The system automatically determines the required approval levels based on multiple factors:
- Employee-manager relationships defined in the organizational hierarchy
- Expense amounts compared against policy limits
- Department and cost center rules
- Job profile specifications

**Four-Level Approval Hierarchy**

**Level 1 - Direct Manager**
The immediate supervisor reviews travel plans and expenses first, verifying that the business purpose is valid and expenses are reasonable. This level catches obvious issues early in the process.

**Level 2 - Department Manager**
The department or divisional manager provides secondary approval, ensuring alignment with departmental budgets and priorities. This level adds oversight for higher-value expenses.

**Level 3 - General Manager (GM)**
Triggered automatically when expenses exceed policy-defined thresholds (`policy_remaining_amount`), GM approval adds executive oversight for significant expenditures. The system intelligently determines when this level is required based on policy configurations.

**Level 4 - Additional Approval**
For exceptional amounts or special circumstances defined in policy rules, a fourth approval level can be activated, providing additional controls for the highest-value expenses.

**Finance Processing**
After all managerial approvals, the finance team receives the expense for final verification, SAP posting, and payment processing. Finance can approve, request corrections, or reject expenses that fail final validation.

**Status Progression**
Expenses move through clear status states: Open → Submitted → Approved Level 1 → Approved Level 2 → Approved Level 3 → Approved Level 4 → Finance Approved. At any stage, rejections can occur, returning the expense to the employee with comments for correction.

**Rejection Handling**
When an expense is rejected at any level (Rejected Level 1, 2, 3, 4, or Finance), the system notifies the employee with remarks explaining the rejection reason. Employees can then modify and resubmit, starting the approval cycle again.

### 4. Policy Engine & Compliance

**Policy-Based Controls**
The system enforces expense policies that define:
- Amount limits by employee job profile
- Approval hierarchies based on expense amounts
- Valid expense types per policy
- Effective date ranges for policy applicability
- Company code, department, and cost center restrictions

**Dynamic Policy Application**
When employees submit expenses, the system evaluates applicable policies based on their profile, department, cost center, and travel dates. The appropriate policy then governs approval routing and spending limits.

**Policy Approver Configuration**
Policies define which approval levels are required. The `policy_approver` table maps policies to approver levels, allowing flexible configuration. Some policies may require only two approval levels, while others mandate all four plus finance review.

**Amount Threshold Logic**
The system compares expense amounts against policy limits. When an expense exceeds the `policy_remaining_amount` threshold, Level 3 (GM) approval is automatically added to the workflow. This ensures executives review high-value expenditures without requiring manual intervention.

### 5. Employee & User Management

**Employee Master Data**
The system maintains comprehensive employee records including:
- Employee codes and company assignments
- Personal information (name, email, phone)
- Position, department, and division
- Channel, region, and cost center assignments
- Job profiles for policy mapping
- Standard meal and allowance rates
- Vendor codes for SAP integration
- Fleet car details and registration numbers

**User Accounts & Authentication**
Separate user accounts are linked to employee records, handling login credentials and authentication. The separation allows for flexible user management where one person might have multiple accounts with different permission levels.

**Manager-Employee Relationships**
The `manager_with_employee` and `expense_manager_with_employee` tables define organizational hierarchies. These relationships drive approval routing, ensuring expenses flow to the correct managers automatically.

**Role & Permission System**
Users are assigned roles (Manager, Operation, Finance, HR, Admin) that grant specific permissions. The `role_permissions` table maps roles to capabilities like viewing all expenses, approving at specific levels, or administering master data.

### 6. Financial Integration & Reporting

**SAP A/P Integration**
Approved expenses are transmitted to SAP for accounts payable processing. The system includes SAP-specific fields like vendor codes, company codes, cost centers, and GL accounts, ensuring seamless data transfer.

**Finance Status Tracking**
Finance teams manage status progression through finance-specific states: Open, Approved, Rejected, and SAP A/P (Reverse) for corrections. This provides visibility into payment processing stages.

**Document Number Generation**
The system generates standardized document numbers (TEA2024-0001 format) for expense approvals, providing unique identifiers for tracking and reference in financial systems.

**Summary Calculations**
Expense summaries are automatically calculated, aggregating hotel, meals, allowances, transportation, and custom expenses. These totals drive approval logic and provide quick expense overviews.

**Reporting & Analytics**
The system maintains report tables (`expense_report`, `route_report`, `expense_approve_report`, `route_approve_report`) that capture approval history and status changes, enabling audit reporting and analytics.

### 7. Dashboard & Monitoring

**Executive Dashboard**
The dashboard provides visual insights into travel expense trends through chart components. Administrators and managers can view expense patterns, approval backlogs, and spending trends across departments and time periods.

**Status Monitoring**
Users can monitor the status of their submitted expenses in real-time, seeing exactly which approval level the expense is awaiting and who the pending approver is.

**Notification System**
The system sends email notifications at key workflow stages:
- Notification to approvers when expenses await their review
- Notification to employees when expenses are approved or rejected
- Notification to finance when expenses are ready for payment processing

### 8. Data Import/Export Capabilities

**Excel Import**
The system supports bulk travel plan creation through Excel file uploads. The `upload_plan_files` table tracks imported files, enabling rapid data entry for planned travel schedules.

**Excel Export**
Users can export expense data, travel plans, and reports to Excel format for offline analysis, budget planning, and external reporting requirements.

**Template Management**
Standardized templates are stored in `/public/template/` directory, ensuring consistent data formats for imports and providing users with pre-formatted Excel files for bulk uploads.

### 9. Data Security & Audit

**Edit Protection After Submission**
Once expenses are submitted for approval, the system blocks editing of financial fields. This critical security feature (Version 1.2.0) prevents fraud by ensuring approved amounts cannot be altered retroactively.

**Travel Plan Lock**
Similarly, travel plan names and details cannot be modified once submitted to Level 1 approval (Version 1.1.0), maintaining workflow integrity and preventing post-submission changes.

**Comprehensive Audit Trail**
All records include `create_by`, `update_by`, `created_at`, and `updated_at` fields, tracking who created or modified records and when. The `deleted_at` soft delete mechanism preserves historical data for audit purposes.

**Input Validation**
Both frontend and backend validation ensures data integrity. Yup schemas validate inputs client-side, while backend controllers enforce business rules and database constraints.

## Workflow Example: End-to-End Process

Let me illustrate how the system works in practice with a real-world scenario:

**Step 1: Travel Planning**
Sarah, a sales manager, needs to visit three customers in different provinces next month. She logs into the system and creates a new travel plan named "Customer Visit Q1 2025," selecting the travel dates and her employee profile. The system assigns code TP00123.

**Step 2: Route Planning**
For each customer destination, Sarah adds a "Plan to Visit" entry, specifying the province, visit dates, objectives (Customer Visit - Relationship Building), and expected routes. She estimates 450 kilometers total travel distance.

**Step 3: Expense Planning**
Sarah estimates her expenses: hotel stays, meal allowances based on her employee profile, and transportation costs. She notes she'll be using the company fleet car for travel.

**Step 4: Travel Execution**
After completing her trip, Sarah returns and enters actual expenses for each destination:
- Hotel Lotus Inn: 2,500 THB with receipt attachment
- Meals: Breakfast 150 THB, Lunch 200 THB, Dinner 300 THB per day
- Fleet card: 1,200 THB in fuel costs with mileage documentation
- Toll fees: 320 THB
- Client entertainment dinner: 2,800 THB (categorized as Nature of Expense - Entertainment)

**Step 5: Submission**
Sarah clicks submit. The system validates all required fields, calculates the total expense (8,770 THB), and creates a travel expense approval record with document number TEA2025-0456. The status changes from "Open" to "Submitted."

**Step 6: Level 1 Approval**
Sarah's direct manager receives an email notification. He logs in, reviews the expenses against the attached receipts, verifies the business purpose, and approves. The status moves to "Approved Level 1."

**Step 7: Level 2 Approval**
The department manager is notified and reviews Sarah's expense. Since it's under the policy threshold for GM approval, he provides final managerial approval. Status updates to "Approved Level 2."

**Step 8: Finance Processing**
The finance team receives the approved expense in their queue. They verify all documentation, validate SAP posting data (vendor code, cost center, GL accounts), and approve for payment. The system marks the expense as ready for SAP integration.

**Step 9: Payment**
Finance posts the expense to SAP A/P, and Sarah receives reimbursement in her next payroll cycle. The expense status is updated to reflect SAP posting completion.

Throughout this entire process, Sarah can log in at any time to see exactly where her expense is in the approval chain, who's reviewing it, and when each approval occurred. The complete audit trail is preserved for compliance purposes.

## System Highlights & Differentiators

### Intelligent Approval Automation
Unlike simpler expense systems that use fixed approval chains, this system dynamically determines approval levels based on policy rules. An expense for 500 THB might need only two approvals, while a 50,000 THB expense automatically triggers all four approval levels without manual intervention.

### Granular Expense Tracking
The system doesn't just track "transportation costs" — it separates taxi, fleet card usage, tolls, and parking into distinct categories, each with appropriate validation and tax treatment. This granularity ensures accurate accounting and better expense analytics.

### Post-Submission Protection
The recent security enhancements (Versions 1.1.0 and 1.2.0) demonstrate the system's maturity. By preventing edits after submission, it eliminates a major fraud vector while maintaining workflow integrity — a feature many commercial expense systems lack.

### Seamless Enterprise Integration
The deep SAP integration isn't an afterthought — it's built into the data model. Fields like vendor codes, company codes, plant assignments, and cost centers are first-class attributes, ensuring finance teams can post expenses to SAP without data transformation.

### Bilingual Support
With internationalization built in using react-intl, the system supports both Thai and English interfaces, accommodating diverse user bases in multinational organizations.

### Mobile-Responsive Design
Material-UI's responsive components ensure the system works on desktops, tablets, and smartphones. Managers can approve expenses from anywhere, and employees can submit receipts immediately after spending.

### Comprehensive Master Data Management
The system maintains master data for provinces, routes, objectives, expense types, work areas, and places. This standardization ensures consistent data entry and enables meaningful reporting across the organization.

## Version History & Continuous Improvement

The system is actively maintained with a formal change management process:

**Version 1.2.4 (Current)**
Latest production release with all security enhancements and Node.js 20 optimizations.

**Version 1.2.3**
Enhanced Babel configuration for Node.js 20 target, improved date handling across multiple components for better reliability and modern runtime features.

**Version 1.2.2**
Code structure refactoring for improved maintainability, package updates for security improvements, enhanced component organization.

**Version 1.2.1**
Added version display on login page for better support visibility and troubleshooting capabilities.

**Version 1.2.0**
Critical security fix preventing travel expense field editing after submission, protecting against financial fraud and maintaining audit integrity.

**Version 1.1.0**
Implemented travel plan name editing protection after Level 1 submission, ensuring approval workflow integrity.

Each version is meticulously documented in the Change.md file with detailed change descriptions, impacted files, testing verification, and impact assessments — demonstrating professional software development practices.

## Technical Excellence

### Performance Optimization
The application uses Next.js automatic code splitting, ensuring users only download code needed for the pages they access. With 8GB memory allocation in production and optimized database queries through Sequelize, the system handles hundreds of concurrent users smoothly.

### Scalability
The architecture separates frontend and backend concerns, allowing independent scaling. The Express API can be load-balanced across multiple instances using PM2's cluster mode, while the Next.js frontend benefits from static generation and incremental static regeneration for public pages.

### Code Quality
The project uses ESLint with Airbnb configuration for code consistency, Prettier for formatting, and Husky for pre-commit hooks. This ensures code quality standards are maintained across the development team.

### Development Workflow
Developers benefit from hot module replacement in development mode, automated migrations for database changes, and comprehensive NPM scripts for common tasks. The clear project structure makes onboarding new developers straightforward.

---

## Conclusion

The Glico Travel Expense Management System stands as a sophisticated enterprise application that transforms business travel expense management from a cumbersome administrative burden into a streamlined digital workflow. By combining modern web technologies with thoughtful business logic, it delivers tangible value through reduced processing times, enhanced compliance, and improved financial visibility.

The system's strength lies not just in its comprehensive feature set, but in how those features work together cohesively — from the moment an employee plans a trip through final SAP payment posting, every step is connected, validated, and traceable. This integration, combined with robust security measures and active maintenance, makes it a reliable foundation for organizational expense management.

Whether you're an employee submitting expenses, a manager reviewing approvals, a finance professional processing payments, or an administrator managing policies, this system provides the tools and visibility needed to perform your role efficiently while maintaining the controls necessary for financial governance.

*This documentation reflects the system as of Version 1.2.4, developed using modern web technologies and enterprise-grade architecture patterns to serve the travel expense management needs of organizations with complex approval workflows and stringent audit requirements.*

---

## 🏷️ Keywords

`Next.js`, `React`, `Redux`, `Node.js`, `Express.js`, `Material UI`, `TailwindCSS`, `Formik`, `Yup`, `Microsoft SQL Server`, `Sequelize`, `JWT`, `Full-Stack Development`, `Web Application`, `RESTful API`, `API Development`, `API Integration`, `SAP Integration`, `PM2`, `Docker`, `ESLint`, `Prettier`, `Husky`, `Database Management`, `Database Architecture`, `JavaScript`, `HTML5`, `CSS`, `Git`, `GitHub`, `Enterprise Solution`, `Expense Management`, `Travel Management`, `Approval Workflow`, `Financial Reporting`, `Audit Trail`, `Responsive Design`
