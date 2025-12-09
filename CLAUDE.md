# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a **portfolio showcase repository** containing screenshots and images from various completed projects. It is NOT a traditional development codebase - there are no build processes, dependencies, or code to compile.

The repository includes:
- Project screenshots organized in subdirectories by project name and technology
- Two static HTML files:
  - `index.html` - Full portfolio gallery with detailed project cards and screenshots
  - `index-short.html` - Condensed reference document for printing/PDF export
- Project documentation in `md-data/` directory

## Repository Structure

```
Potforilo/
├── index.html                              # Main portfolio gallery page (25 projects)
├── index-short.html                        # Short reference version (30+ projects)
├── CLAUDE.md                               # This file - repository guidance
├── md-data/                                # Project documentation and details
├── nurseship/                              # NurseShip healthcare platform screenshots (14 images)
├── stack-nextjs/                           # USBT Pro tournament platform screenshots
├── smartsales-csharp-jquery/               # SmartSales SFA system screenshots
├── ContentAI/                              # ContentAI SaaS platform screenshots
├── helpdesk-ai/                            # HelpDesk AI multi-agent system screenshots
├── beveragevision-ai/                      # BeverageVision computer vision screenshots
├── eorder-mobile/                          # eOrder B2B mobile app screenshots
├── merchandiser-mobile-app/                # SmartESM mobile app screenshots
├── stock-portfolio-manager-reactjs/        # DCAPort Pro portfolio manager screenshots
└── [additional project directories]/       # Other project screenshots
```

## Project Portfolio (25 Projects)

### 🏢 Enterprise SaaS & Cloud Platforms (10 projects)
1. **RouteForce Pro** - Multi-tenant distribution platform (React, Node.js, MS SQL)
2. **USBT Pro** - High-scale sports tournament platform (Next.js 14, NestJS, GraphQL)
3. **SmartSales Pro** - Sales Force Automation for Fortune 500 (NET 6, EF Core)
4. **NurseShip** - Healthcare workforce management (Next.js 15, Prisma, MySQL)
5. **SmartESM Backoffice** - Field operations management (React 18, Redux, Redis)
6. **TravelExpense Pro** - Corporate expense management with SAP integration
7. **VeriSmart Pro** - Warranty & maintenance tracking (Next.js, Prisma)
8. **SmartRedeem Pro** - B2B loyalty platform with dual-database architecture
9. **ODMS Pro** - EDI & order management (.NET Core, SQL Server)
10. **LogiFlow Pro** - E-commerce logistics platform (React 18, PostgreSQL)

### 🤖 AI & Machine Learning Solutions (4 projects)
11. **ContentAI Pro** - SaaS content generation platform (Next.js 15, tRPC, Stripe)
12. **HelpDesk AI** - Agentic customer support with LangGraph (Next.js 15, GPT-4)
13. **BeverageVision AI** - Computer vision inventory tracking (Python, PyTorch, YOLO)
14. **GoldMind AI** - Multi-model trading intelligence (GPT-4, Claude 3.5, Gemini)

### 📱 Mobile & Offline-First Applications (4 projects)
15. **eOrder Mobile** - B2B commerce application (React Native 0.76, Redux, Firebase)
16. **SmartESM Mobile** - Offline field operations (React Native, SQLite)
17. **PJP Mobile** - Field performance & coaching (React Native 0.79, MobX)
18. **FieldForce Pro** - Offline sales force automation (React Native, Realm DB)

### 💹 FinTech & Data Engineering (3 projects)
19. **QuantForge AI** - Algorithmic trading platform (Python, Scikit-learn, XGBoost)
20. **GoldTrader Elite** - Automated trading system (Node.js, MetaTrader 5, MQL5)
21. **DCAPort Pro** - Investment portfolio manager (React, PostgreSQL, Finnhub API)

### 🛠️ Specialized Tools & Consumer Apps (4 projects)
22. **NotifyHub Pro** - Multi-channel notification engine (Node.js, Firebase, LINE API)
23. **NEO Services** - Database health monitoring SaaS (React 19, MS SQL Server)
24. **MongkolPlate** - Thai numerology platform (React 19, Vite, Framer Motion)
25. **ThaiDine Finder** - Restaurant discovery platform (Next.js, Google Maps API)

## Gallery Files

### index.html (Main Portfolio Gallery)
The main portfolio gallery is a standalone, self-contained page that:
- Uses Tailwind CSS (via CDN) for styling
- Displays 25 projects in 5 categorized sections with technology badges
- Implements a modal lightbox for viewing full-size images
- Features detailed project cards with Challenge/Solution blocks and impact statements
- Includes screenshot galleries for projects with multiple images
- Responsive design: 1 column (mobile) → 2 (sm/md) columns
- Requires no build process or dependencies
- Can be opened directly in any browser

### index-short.html (Reference Document)
A condensed print-friendly reference document that:
- Lists 30+ projects in a compact format
- Designed for A4 paper printing and PDF export
- Includes technology badges and key features for each project
- Organized into categorized sections with icons
- Print-optimized with page break controls
- Features a "Print/Export PDF" button

## Working with This Repository

### Viewing the Gallery
Simply open `index.html` or `index-short.html` in a web browser. No server or build process needed.

### Adding New Projects

#### To add a project to index.html:
1. Create a new directory named: `project-name/` (lowercase with hyphens)
2. Add screenshot images to the directory (PNG, JPG, or WebP format)
3. Update `index.html` to add a new `<article class="project-card">` with:
   - Project title, subtitle, and technology badges
   - Challenge and Solution detail blocks
   - Impact pill with key metric
   - Screenshot gallery with onclick handlers for modal lightbox
   - Proper image paths relative to the HTML file (e.g., `nurseship/1-login.png`)

#### To add a project to index-short.html:
1. Add a new `<section class="project-item">` in the appropriate category
2. Include project name, technology badges, and description
3. List key features or key pages

### Screenshot Organization
- **Naming Convention**: Use descriptive names with numbers for ordering
  - Example: `1-nurseship-login.png`, `2-nurseship-dashboard.png`
- **Image Types**: PNG (preferred), JPG, or WebP formats
- **Content**: Each image should show a distinct page or feature
- **No Source Code**: This repository contains only screenshots, no actual source code

### Project Directory Examples
```
nurseship/
├── 1-nurseship-login.png
├── 2-nurseship-dashboard.png
├── 3-nurseship-shift-calendar.png
├── 4-nurseship-my-bookings.png
├── 5-nurseship-shift-swaps.png
└── [additional screenshots]
```

### Modifying the Gallery
- Both HTML files use inline styles and Tailwind CSS utility classes
- Modal lightbox functionality is handled by vanilla JavaScript at the bottom of index.html
- Image paths use relative paths (no `../` prefix needed)
- Responsive grid in index.html: 1 column (mobile) → 2 (md) → 4 (xl) for screenshot galleries
- Mobile screenshots use portrait aspect ratio (9:19.5)

### File Maintenance
When updating the portfolio:
1. **Add screenshots first** - Create directory and add images
2. **Update index.html** - Add full project card with details and screenshot gallery
3. **Update index-short.html** - Add condensed project entry
4. **Update CLAUDE.md** - Add project to the appropriate category list (this file)

## Important Notes

- This is **not a development project** - it's a collection of screenshots from completed work
- There are no package managers, build tools, or dependencies to install
- The HTML files are intentionally standalone for easy deployment
- Images are referenced using relative paths, so directory structure must be maintained
- Both HTML files should be kept in sync when adding new projects
- The `md-data/` directory contains additional project documentation and details
