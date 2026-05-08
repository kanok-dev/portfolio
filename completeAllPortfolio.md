# 🏅 Senior Full-Stack & AI Engineer Portfolio
**10+ Years Experience | SaaS Architect | AI Integrator | Mobile Expert**

---

## 🤖 AI & Machine Learning Solutions (5 Projects)

### 1. HelpDesk AI - Agentic Customer Support Automation
**Role:** AI Architect & Lead Developer
**Type:** Full-Stack SaaS (Next.js + FastAPI)

* **The Challenge:** Traditional chatbots lacked context and could not handle complex routing or specific database lookups for support tickets.
* **The Solution:** Architected a **Multi-Agent System** using LangGraph to orchestrate 7 specialized agents (Triage, Search, Solution). Implemented **RAG (Retrieval-Augmented Generation)** with FAISS vector search to ground answers in company data.
* **Key Tech:** Next.js 15, Python (FastAPI), LangChain, OpenAI GPT-4, FAISS, Redis, Docker.
* **Impact:** Enabled autonomous ticket resolution and intelligent human escalation with preserved context.

### 2. GoldMind AI - Multi-Model Trading Intelligence
**Role:** Full-Stack Developer
**Type:** FinTech AI Platform

* **The Challenge:** Single-model AI predictions for gold trading often suffered from bias or hallucinations.
* **The Solution:** Built an **Ensemble AI Architecture** that cross-validates signals from GPT-4, Claude 3.5, and Gemini Pro. Developed a consensus engine to filter low-confidence trade signals.
* **Key Tech:** Node.js, Express, React, Puppeteer (News Scraping), Recharts, TA-Lib.
* **Impact:** Increased signal accuracy by aggregating multi-model sentiment and technical analysis.

### 3. BeverageVision AI - Computer Vision Inventory Tracking
**Role:** Computer Vision Engineer
**Type:** AI/ML Object Detection System

* **The Challenge:** Manual inventory counting for beverage distributors was slow and error-prone.
* **The Solution:** Developed a custom object detection pipeline using **YOLOv5/v11** to identify and count 19+ distinct beverage SKUs (cans/bottles) from mobile camera feeds.
* **Key Tech:** Python, PyTorch, YOLO, FastAPI, React, OpenCV.
* **Impact:** Automated stock-taking processes, reducing audit time by ~70% with high accuracy.

### 4. ContentAI Pro - SaaS Content Generation Platform
**Role:** Senior Full-Stack Developer
**Type:** SaaS Platform (B2B)

* **The Challenge:** Users needed a unified workspace to generate marketing copy across multiple formats (Blogs, Social, Email) without switching tools.
* **The Solution:** Built a robust SaaS platform offering **130+ AI tools**. Integrated credit-based consumption logic and Stripe subscriptions.
* **Key Tech:** Next.js 15, tRPC, Prisma, PostgreSQL, Stripe API, OpenAI API.
* **Impact:** Delivered a production-ready SaaS with secure payment gateways and scalable user management.

### 5. MezzoSync - Live Translation Platform
**Production Link:** Web/App — https://mezzo-sync.kanoks.me

**Role:** Full-Stack / Mobile Developer
**Type:** AI Realtime Translation Platform

* **The Challenge:** Users needed a smooth live translation experience across web and mobile, with realtime voice capture, transcription, translated text display, and speech playback.
* **The Solution:** Built an Expo SDK 55 + React Native web/mobile app with Soniox realtime STT, translation, and TTS over WebSocket, backed by a secure Express TypeScript token gateway.
* **Key Tech:** Expo SDK 55, React Native 0.83.4, React 19.2, Expo Router, Soniox Realtime STT/Translation/TTS, WebSocket, Express, TypeScript.
* **Impact:** Delivered a production live translation platform with secure ephemeral API token handling and cloud-ready deployment.

---

## 🏢 Enterprise SaaS & Cloud Platforms (10 Projects)

### 6. RouteForce Pro - Multi-Tenant Distribution Platform
**Role:** System Architect
**Type:** Enterprise SaaS (Multi-Tenant)

* **The Challenge:** Distributors needed a centralized system to manage inventory, sales, and logistics across multiple independent tenants securely.
* **The Solution:** Designed a **Database-per-Tenant** architecture to ensure strict data isolation. Built a complete ERP-lite suite covering Order-to-Cash, Inventory, and Promotion engines.
* **Key Tech:** React, Node.js, Microsoft SQL Server, Redis, Docker, AWS S3.
* **Impact:** Supports complex promotion logic (Mix & Match, Volume tiers) and handles thousands of daily transactions per tenant.

### 7. USBT Pro - High-Scale Sports Tournament Platform
**Production Link:** https://usbtthailand.net/

**Role:** Lead Full-Stack Engineer
**Type:** Event Management Platform

* **The Challenge:** The University Sports Board needed to handle massive traffic spikes (10,000+ users) during national tournament registrations and live scoring.
* **The Solution:** Architected a **Cloud-Native solution** using Cloudflare R2 for massive file storage and GraphQL Subscriptions for real-time score updates.
* **Key Tech:** Next.js 14, NestJS, GraphQL, MySQL, Redis, Cloudflare R2.
* **Impact:** Successfully managed 50+ sports disciplines and thousands of athletes with zero downtime during peak usage.

### 8. SmartSales Pro - Sales Force Automation (SFA)
**Role:** Senior Backend Developer
**Type:** Enterprise SFA

* **The Challenge:** Field sales teams for global FMCG brands (Nestle, Pepsi) needed to sync massive datasets (Orders, Invoices) with headquarters while offline.
* **The Solution:** Built a **Bidirectional Sync Engine** capable of handling conflict resolution and delta updates for thousands of SKUs and customers.
* **Key Tech:** .NET 6 Web API, Entity Framework Core, SQL Server, Hangfire.
* **Impact:** Trusted by Fortune 500 clients to process critical sales data securely and accurately.

### 9. NurseShip - Healthcare Workforce Management
**Role:** Full-Stack Developer
**Type:** SaaS Platform

* **The Challenge:** Hospitals struggled with complex shift scheduling, swapping, and attendance tracking for nursing staff.
* **The Solution:** Developed a modern, user-friendly platform allowing peer-to-peer shift swapping with head nurse approval workflows.
* **Key Tech:** Next.js 15, Prisma ORM, MySQL, Tailwind CSS 4, TypeScript.
* **Impact:** Reduced administrative burden on head nurses and improved staff satisfaction through flexible scheduling.

### 10. SmartESM Backoffice - Field Operations Management
**Role:** Full-Stack Lead
**Type:** Enterprise Web Application

* **The Challenge:** Managers needed real-time visibility into thousands of field sales activities (Shelf checks, Pricing) occurring simultaneously.
* **The Solution:** Built a high-performance **Backoffice Dashboard** using React and Node.js with **Redis Caching** to handle heavy read loads. Implemented dynamic route planning and planogram compliance verification tools.
* **Key Tech:** React 18, Redux, Node.js, Express, Redis, SQL Server, Docker.
* **Impact:** Enabled data-driven decision-making for retail execution, reducing out-of-stock incidents.

### 11. TravelExpense Pro - Corporate Expense Management
**Role:** Full-Stack Developer
**Type:** Internal Enterprise Tool

* **The Challenge:** The client struggled with a slow, paper-based reimbursement process that lacked integration with their SAP financial system.
* **The Solution:** Developed a digital **Multi-Level Approval Workflow** system. It handles complex logic for per-diems and mileage, automatically posting approved records to **SAP** via API.
* **Key Tech:** Next.js 14, Express.js, Microsoft SQL Server, Material UI, SAP Integration.
* **Impact:** Reduced reimbursement turnaround time from weeks to days and eliminated manual data entry errors.

### 12. VeriSmart Pro - Warranty & Maintenance Tracking
**Role:** System Architect
**Type:** SaaS Asset Management

* **The Challenge:** A device service provider needed to track warranty lifecycles and maintenance tickets across multiple distributors without data leakage.
* **The Solution:** Architected a **Multi-Tenant System** with company-based isolation. Features include automated warranty expiration alerts and service ticket workflows.
* **Key Tech:** Next.js, Prisma ORM, SQL Server, Serverless API, JWT Auth.
* **Impact:** Streamlined after-sales support operations and reduced warranty dispute cases through accurate digital tracking.

### 13. SmartRedeem Pro - B2B Loyalty Platform
**Role:** Full-Stack Developer
**Type:** Loyalty Management System

* **The Challenge:** A B2B distributor needed to incentivize retailers with points based on ERP sales data siloed in legacy databases.
* **The Solution:** Built a **Dual-Database Architecture** that syncs sales data from MSSQL (ERP) to calculate points and manages redemptions in MySQL.
* **Key Tech:** Next.js, Node.js, MySQL (Operational), MSSQL (ERP), Redux.
* **Impact:** Automated point calculation for thousands of invoices, increasing customer retention.

### 14. ODMS Pro - EDI & Order Management
**Role:** Backend Architect
**Type:** Supply Chain / EDI

* **The Challenge:** A supplier needed to integrate orders from 8 major retailers (7-Eleven, BigC, Makro), each using different EDI formats (CSV, XML, Text).
* **The Solution:** Developed a centralized **EDI Parsing Engine** that normalized disparate data formats into a unified order processing workflow.
* **Key Tech:** .NET Core, SQL Server, Entity Framework, File Parsing Libraries.
* **Impact:** Eliminated manual data entry, reducing order processing time by 90% and eliminating human error.

### 15. LogiFlow Pro - E-Commerce Logistics Platform
**Production Link:** KU Garden Frontend — https://kugarden.smart-express.biz

**Role:** Full-Stack Developer
**Type:** Logistics Management

* **The Challenge:** An e-commerce fulfillment center needed to optimize pick-pack-ship workflows and track inventory across multiple channels.
* **The Solution:** Built a warehouse management system with barcode scanning integration and real-time dashboard analytics.
* **Key Tech:** React 18, Redux Toolkit, PostgreSQL, Node.js.
* **Impact:** Streamlined warehouse operations and improved order accuracy for e-commerce shipments.

---

## 📱 Mobile & Offline-First Applications (4 Projects)

### 16. PJP Mobile - Field Performance & Coaching
**Role:** Senior Mobile Architect
**Type:** Cross-Platform Mobile App

* **The Challenge:** Sales supervisors needed a tool to track "Work-With" coaching sessions and KPI achievements in the field.
* **The Solution:** Engineered a robust React Native app using **MobX State Tree** for complex state management and **MMKV** for high-performance local storage.
* **Key Tech:** React Native 0.79, TypeScript, MobX, MMKV, Vision Camera.
* **Impact:** Digitized the coaching workflow, enabling real-time performance tracking against sales targets.

### 17. eOrder Mobile - B2B Commerce Application
**Role:** Lead Mobile Developer
**Type:** E-Commerce App

* **The Challenge:** A B2B ordering platform required a native-like experience for retailers to restock inventory with complex pricing tiers.
* **The Solution:** Built a high-performance app with **Firebase Cloud Messaging** for order updates and a multi-language (i18n) interface.
* **Key Tech:** React Native 0.76, Redux Toolkit, Firebase, i18next.
* **Impact:** Streamlined the B2B ordering process, reducing order errors and support calls.
* **Production Link:** App Store — https://apps.apple.com/th/app/eorder-app/id6468933075

### 18. SmartESM Mobile - Field Sales & Merchandising Operations
**Role:** Mobile Developer / React Native Modernization
**Type:** Cross-Platform Field Operations App

* **The Challenge:** Field sales and merchandising teams needed a mobile workflow to manage daily schedules, customer visits, pricing audits, stock checks, surveys, POSM requests, promotion checks, and shelf execution data with photo/GPS evidence.
* **The Solution:** Modernized the Smart ESM mobile app on a current **React Native 0.83.9** stack with React Navigation v7, MobX/MobX State Tree, AsyncStorage persistence, Axios API services, Vision Camera, and React Native Maps.
* **Key Tech:** React Native 0.83.9, React 19.2, React Navigation v7, MobX State Tree, AsyncStorage, Axios, Vision Camera, React Native Maps.
* **Impact:** Digitized retail execution workflows for field teams, improving visit accountability, data accuracy, and management visibility across customer outlets.
* **Production Link:** App Store — https://apps.apple.com/th/app/esm-smart-merchant/id1498603283

### 19. FieldForce Pro - Offline Sales Force Automation
**Role:** Mobile Architect
**Type:** Cross-Platform Mobile App

* **The Challenge:** Sales teams in remote areas needed to place orders and check stock without reliable internet access.
* **The Solution:** Engineered an **Offline-First Application** using **Realm Database** for robust local storage. The app handles complex pricing logic locally and syncs bi-directionally when online.
* **Key Tech:** React Native, Realm DB, Background Sync, Google Maps API.
* **Impact:** Empowered sales reps to work anywhere, increasing daily visits by eliminating network-related downtime.

---

## 💹 FinTech & Data Engineering (3 Projects)

### 20. QuantForge AI - Algorithmic Trading Platform
**Role:** ML Engineer & Backend Developer
**Type:** Quantitative Finance

* **The Challenge:** Retail traders lacked institutional-grade tools to backtest strategies against high-frequency data.
* **The Solution:** Built a Python-based ML pipeline using **Ensemble Learning** (Random Forest, XGBoost) to predict market movements with high accuracy (96% on test sets).
* **Key Tech:** Python, Scikit-learn, Pandas, Backtrader, Yahoo Finance API.
* **Impact:** Democratized access to hedge-fund style algorithmic trading strategies.

### 21. GoldTrader Elite - Automated Trading System
**Role:** Algorithmic Trader / Developer
**Type:** FinTech / Trading Bot

* **The Challenge:** Manual trading was emotional and inconsistent. The goal was to automate entry/exit based on strict technical analysis rules.
* **The Solution:** Developed a bridge between **Node.js Analysis Engine** and **MetaTrader 5 (MT5)**. The system aggregates price data, calculates indicators (RSI, MACD), and executes trades via Expert Advisors.
* **Key Tech:** Node.js, MetaTrader 5 (MQL5), Redis, Technical Analysis Libraries.
* **Impact:** Removed emotional bias from trading, executing strategies 24/7 with strict risk management protocols.

### 22. DCAPort Pro - Investment Portfolio Manager
**Role:** Full-Stack Developer
**Type:** FinTech Web App

* **The Challenge:** Investors needed a tool to track Dollar Cost Averaging (DCA) performance with real-time market data.
* **The Solution:** Built a dashboard integrating **Finnhub API** for live pricing, calculating complex metrics like realized/unrealized gains and cost basis in real-time.
* **Key Tech:** React, Node.js, PostgreSQL, Finnhub API, Recharts.
* **Impact:** Provided investors with institutional-grade portfolio analytics.

---

## 🛠️ Specialized Tools & Consumer Apps (4 Projects)

### 23. NotifyHub Pro - Multi-Channel Notification Engine
**Role:** Backend Developer
**Type:** Utility SaaS
* **Description:** A centralized notification engine managing LINE and Mobile Push channels for enterprise alerts.
* **Key Tech:** Node.js, Firebase FCM, LINE Messaging API, Cron Jobs.

### 24. NEO Services - Database Health Monitoring
**Role:** Full-Stack Developer
**Type:** DevOps / Monitoring Tool
* **Description:** A Database health monitoring SaaS that proactively alerts admins of SQL Server anomalies (gaps in invoice numbers, duplicate prices) via LINE.
* **Key Tech:** React 19, Node.js, Microsoft SQL Server, LINE API.

### 25. MongkolPlate - Thai Numerology Platform
**Role:** Frontend Developer
**Type:** Consumer Web App
* **Description:** A highly interactive web application for analyzing Thai license plate numerology using complex calculation logic.
* **Key Tech:** React 19, Vite, Framer Motion, Tailwind CSS.

### 26. ThaiDine Finder - Restaurant Discovery Platform
**Role:** Full-Stack Developer
**Type:** Consumer Web App
* **Description:** Location-based restaurant discovery tool using Google Maps & Places API with intelligent grid-based search algorithms to scan entire provinces.
* **Key Tech:** Next.js, Google Maps API, Places API, Node.js.

### Additional Production Mobile App Link

* **Inspector Baseline:** App Store — https://apps.apple.com/au/app/inspector-baseline/id6761975149
