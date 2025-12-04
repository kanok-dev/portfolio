# ThaiDine Finder - Location-Based Restaurant Discovery Platform

> **🚀 Full Stack Web Application | SaaS-Ready Architecture**

---

## 🏷️ Project Classification

| Category | Details |
|----------|---------|
| **Project Type** | ✅ **Full Stack Web Application** - React 18 frontend with Node.js/Express backend |
| **Architecture** | ✅ **SaaS-Ready** - JWT authentication, stateless design for horizontal scaling |
| **APIs** | Google Places API, Google Geocoding API |
| **Features** | Grid-based search algorithm, Excel export |

---

## Software Overview

Thai Restaurant Finder is a comprehensive web application designed specifically for discovering restaurants across Thailand using Google Places API integration. The platform enables users to conduct location-based searches by province, district, or sub-district, delivering detailed restaurant information within specified regions. Built with a modern full-stack architecture, this system demonstrates scalable design principles suitable for both standalone applications and SaaS deployment models.

The application leverages Google's powerful geocoding and places APIs to transform Thai administrative divisions into precise geographical coordinates, then systematically scans these areas using an intelligent grid-based algorithm. This approach ensures comprehensive coverage of even the largest provinces while managing API rate limits and optimizing search efficiency.

## Project Classification

**Type:** Full-Stack Web Application with SaaS Potential

This project exemplifies a complete full-stack solution combining both frontend and backend technologies into a cohesive system. The architecture separates concerns cleanly between client and server, making it particularly well-suited for evolution into a Software-as-a-Service platform. The existing authentication layer, API-driven design, and modular component structure provide a solid foundation for multi-tenant deployment scenarios.

**SaaS Readiness Indicators:**
- JWT-based authentication system already implemented
- RESTful API architecture with clear endpoint separation
- Stateless backend design enabling horizontal scaling
- Client-server separation allowing independent deployment
- Data export functionality catering to business users
- Rate limiting awareness built into core logic

With moderate enhancements—such as database integration for user management, subscription tiers, usage tracking, and multi-tenancy support—this application could readily transform into a commercial SaaS offering for businesses seeking local restaurant intelligence, market research firms, or food delivery platforms.

## Software Objectives

### Primary Goals

**1. Comprehensive Geographic Coverage**
The system aims to provide exhaustive restaurant discovery across Thailand's administrative regions. By accepting queries at province, district, or sub-district levels, users can narrow their searches from broad provincial scans to highly focused neighborhood-level investigations. This granular control makes the platform valuable for various use cases—from national market analysis to hyperlocal business intelligence.

**2. Intelligent Search Optimization**
Rather than relying on single-point searches that might miss establishments, the application employs a sophisticated grid-based scanning methodology. The software calculates geographical bounds for the specified region, divides it into manageable grid cells (currently 5km squares), and systematically searches each grid center. This technique ensures restaurants aren't overlooked due to proximity limitations in the Google Places API.

**3. Data Accessibility and Export**
Understanding that raw data has limited value without proper presentation, the system provides both interactive visualization through paginated tables and practical export capabilities. Users can download comprehensive datasets in Excel format, facilitating further analysis, integration with business intelligence tools, or sharing with stakeholders who require offline access.

**4. Secure Access Control**
The platform implements JWT-based authentication to protect API resources and ensure only authorized users can execute searches. This security layer not only prevents unauthorized access but also creates a framework for future user management, usage tracking, and potential monetization strategies.

## Technical Stack

### Backend Architecture

**Runtime Environment**
- **Node.js with Express.js** - The server leverages Express framework running on Node.js, providing a lightweight yet powerful foundation for building RESTful APIs. The asynchronous nature of Node.js proves particularly beneficial when orchestrating multiple concurrent Google API requests during grid-based searches.

**Core Dependencies**
- **axios (^1.7.9)** - Handles all HTTP communications with Google's external APIs, providing promise-based request handling with automatic JSON transformation.
- **bcrypt (^5.1.1)** - Implements secure password hashing using industry-standard cryptographic algorithms, protecting user credentials even in the event of database compromise.
- **jsonwebtoken (^9.0.2)** - Manages JWT token generation and verification, enabling stateless authentication that scales well across distributed systems.
- **cors (^2.8.5)** - Configures Cross-Origin Resource Sharing policies, allowing the React frontend to communicate with the backend server during development and production.
- **dotenv (^16.4.7)** - Facilitates environment-based configuration management, keeping sensitive credentials like API keys and JWT secrets out of version control.
- **nodemon (^3.1.9)** - Provides development-time automatic server restart on file changes, accelerating the development feedback loop.

**External API Integration**
- **Google Places API (Nearby Search)** - Retrieves restaurant listings within specified radii of grid center points.
- **Google Geocoding API** - Converts Thai administrative region names into precise latitude/longitude bounds.

### Frontend Architecture

**Framework**
- **React 18.2.0** - Modern functional component architecture with hooks for state management and side effects. The declarative nature of React makes the UI predictable and maintainable.
- **React Scripts 5.0.1** - Provides zero-configuration build tooling through Create React App, handling webpack configuration, Babel transpilation, and development server setup.

**UI Component Library**
- **Material-UI (MUI) v6.3.0** - Comprehensive React component library implementing Google's Material Design principles. Includes:
  - `@mui/material` - Core components like TextField, Button, Table, Paper, Grid
  - `@mui/icons-material` - Icon set for visual enhancements (SaveAlt, etc.)
  - `@emotion/react` and `@emotion/styled` - CSS-in-JS styling solution powering MUI's theming

**Specialized Libraries**
- **@react-google-maps/api (^2.13.0)** - React wrapper for Google Maps JavaScript API, though currently underutilized in the existing codebase, suggesting planned map visualization features.
- **axios (^1.5.0)** - Manages client-side HTTP requests to the backend API.
- **react-paginate (^8.2.0)** - Provides pagination controls for managing large restaurant result sets.
- **xlsx (^0.18.5)** - Client-side Excel file generation enabling users to export search results for offline analysis.

**Development Tools**
- **ESLint** - Code quality and style enforcement configured through react-app preset.
- **Web Vitals (^3.3.1)** - Performance monitoring library tracking Core Web Vitals metrics.

## Core Features

### 1. User Authentication System

**Login Flow**
The application implements a secure authentication workflow starting with a dedicated login interface. Users provide email and password credentials, which the backend validates against stored user records (currently in-memory, designed for database integration). Upon successful authentication, the server generates a JWT token containing the user's email claim and a one-hour expiration timestamp.

**Token Management**
The frontend stores the received JWT token in component state and includes it in subsequent API requests via the Authorization header using Bearer token format. This stateless approach allows the backend to verify request authenticity without maintaining session state, enabling easier horizontal scaling.

**Security Considerations**
Passwords undergo bcrypt hashing with a salt factor of 10 before storage. The JWT secret key is externalized through environment variables, preventing exposure in source code. The current implementation includes commented-out password verification logic in [app.js:86-90](app.js#L86-L90), suggesting development-stage authentication bypass for testing purposes.

### 2. Geographic Search by Administrative Division

**Thai Address Hierarchy**
The search form accepts three optional parameters mapping to Thailand's administrative structure:
- **Province (จังหวัด)** - First-level administrative division
- **District (อำเภอ)** - Second-level subdivision
- **Sub-district (ตำบล)** - Third-level subdivision

Users can specify any combination of these fields, allowing searches ranging from entire provinces down to specific neighborhoods. The system constructs appropriate geocoding queries by combining these parameters with the country name "ประเทศไทย" (Thailand).

**Geocoding Process**
The `getAreaBounds` function in [app.js:102-157](app.js#L102-L157) orchestrates the geocoding workflow:
1. Constructs a formatted address string from provided parameters
2. Sends a request to Google Geocoding API
3. Extracts geographical bounds (northeast/southwest corners) from the response
4. Falls back to viewport bounds if geometry bounds are unavailable
5. Returns a four-element array: `[latN, lngE, latS, lngW]`

This bounding box defines the search area for subsequent restaurant queries.

### 3. Intelligent Grid-Based Scanning

**Grid Calculation Algorithm**
To overcome the radius limitations of Google Places API (maximum 50km), the application divides large search areas into smaller grids. The `calculateGridCount` function in [app.js:163-175](app.js#L163-L175) performs this division:

1. Calculates the latitudinal span of the bounding box in kilometers
2. Computes the longitudinal span accounting for latitude-dependent distortion (using cosine correction)
3. Divides each dimension by the configured grid size (currently 5km)
4. Rounds up to ensure complete coverage

**Grid Center Generation**
The `calculateGridCenters` function in [app.js:178-194](app.js#L178-L194) generates search points within each grid cell by calculating the center coordinates. This systematic approach ensures overlapping coverage areas, minimizing the chance of missing restaurants that fall between grid boundaries.

**Example:** A province like Chiang Mai might be divided into a 20×15 grid, resulting in 300 separate search points, each with a 50km radius, ensuring comprehensive coverage even for large provinces.

### 4. Restaurant Data Aggregation

**Places API Integration**
The `getRestaurantsByGrid` function in [app.js:202-251](app.js#L202-L251) executes the actual restaurant searches:

1. Iterates through each grid center point
2. Constructs a Nearby Search API request with:
   - Location: Grid center coordinates
   - Radius: 50,000 meters (maximum allowed)
   - Type: "restaurant" (filters to food establishments)
3. Collects results from initial response
4. Checks for pagination tokens and retrieves additional pages after 2-second delay (Google requirement)
5. Implements 1-second delays between grid searches to respect rate limits

**Deduplication**
Since grid radii overlap intentionally, the same restaurant may appear in multiple search results. The system maintains a Set of place_ids and filters duplicates before returning the final dataset, ensuring each restaurant appears exactly once in results.

**API Usage Tracking**
The application counts every API request made during a search operation and returns this metric to the frontend. This transparency helps users understand the resource consumption of their queries—particularly important given Google Places API's pay-per-request pricing model.

### 5. Results Presentation and Management

**Paginated Table Display**
The `RestaurantTable` component in [client/src/components/RestaurantTable.js](client/src/components/RestaurantTable.js) presents search results in a clean, navigable format:

- Displays 10 restaurants per page by default
- Shows restaurant name, vicinity (address), primary type, and map link
- Implements Material-UI Pagination component for navigation
- Displays total restaurant count prominently

**Interactive Map Links**
Each restaurant entry includes a "ดูบนแผนที่" (View on Map) button that opens Google Maps in a new tab with the exact coordinates, enabling users to visualize locations, read reviews, and access directions immediately.

**Excel Export Functionality**
The export feature leverages the SheetJS library to generate XLSX files client-side:

1. Transforms restaurant objects into flat records with Thai column headers
2. Includes computed Google Maps search URLs as clickable links in the spreadsheet
3. Triggers browser download of the generated file named "restaurants.xlsx"

This functionality proves invaluable for business users who need to analyze data in Excel, create reports, or share findings with non-technical stakeholders.

### 6. Responsive Material Design Interface

**Component Architecture**
The frontend employs a component-based structure with clear separation of concerns:

- **App.js** - Root component managing global state (authentication, search results, loading states)
- **Header.js** - Application branding and navigation
- **Footer.js** - Copyright and supplementary information
- **LoginForm.js** - Authentication interface with email/password fields
- **SearchForm.js** - Geographic search parameters input
- **RestaurantTable.js** - Results display with pagination and export

**Material-UI Integration**
The consistent use of Material-UI components ensures a polished, professional appearance:
- Grid system for responsive layouts adapting to mobile and desktop
- Paper elevation for depth and visual hierarchy
- Typography variants maintaining consistent font scaling
- Color-coded buttons (primary for actions, secondary for exports)
- Loading indicators during asynchronous operations
- Alert components for error messaging

**User Experience Enhancements**
- Disabled submit until at least one search parameter is provided
- Loading spinner during search operations
- Error messages displayed prominently when searches fail
- Conditional rendering preventing empty table displays
- Auto-focus on email field when login form appears

## Key Highlights and Differentiators

### 1. Thailand-Specific Optimization
Unlike generic restaurant search tools, this application is purpose-built for Thailand's administrative geography. The system understands Thai address formatting conventions and constructs geocoding queries in Thai language, improving accuracy when working with Google's APIs. This localization extends to the entire user interface, which presents forms, labels, and messages in Thai, reducing friction for local users.

### 2. Complete Coverage Strategy
The grid-based scanning methodology represents a sophisticated approach to geographical search that many simpler applications overlook. By systematically covering entire regions rather than relying on single-point searches, the system can confidently claim to find "all" restaurants in an area, not just those closest to an arbitrary center point. This completeness makes the platform particularly valuable for market research, competitive analysis, and comprehensive business intelligence.

### 3. API Efficiency Awareness
The implementation demonstrates thoughtful consideration of external API costs and limitations. Features like request counting, deliberate rate limiting through delays, and strategic deduplication show that the developers understand the commercial realities of building applications on metered APIs. This cost-consciousness would prove essential in any SaaS deployment scenario.

### 4. Data Portability
By including robust Excel export functionality, the application acknowledges that users often need to work with data outside the web interface. This export capability bridges the gap between real-time search and traditional business analysis workflows, making the platform more versatile and valuable to enterprise users.

### 5. Separation of Concerns
The clear delineation between frontend (client directory) and backend (root-level app.js) reflects modern best practices in web development. This separation enables:
- Independent scaling of client and server components
- Different deployment strategies (static hosting for frontend, containerized backend)
- Team specialization (frontend developers can work without understanding backend logic)
- Technology evolution (could swap React for another framework without touching backend)

### 6. Authentication-Ready Architecture
While the current user database is in-memory and basic, the authentication infrastructure is properly designed with industry-standard patterns (JWT tokens, bcrypt hashing, middleware-based protection). This foundation could be extended to a production-grade system with minimal architectural changes—primarily swapping the in-memory array for database queries.

## Future Enhancement Opportunities

### For Standalone Application
- **Database Integration:** Replace in-memory user storage with PostgreSQL or MongoDB for persistence
- **Map Visualization:** Utilize the already-imported @react-google-maps/api to display restaurant locations on an interactive map
- **Advanced Filtering:** Add filters for ratings, price levels, opening hours, and specific cuisine types
- **Saved Searches:** Allow authenticated users to save favorite search configurations for quick re-execution
- **Historical Data:** Store search results to track restaurant openings/closings over time

### For SaaS Transformation
- **Multi-Tenancy:** Implement organization/workspace concepts allowing businesses to manage team access
- **Subscription Tiers:** Create pricing plans based on search volume, export capabilities, or advanced features
- **Usage Analytics:** Provide customers with dashboards showing their search patterns and API consumption
- **API Access:** Offer programmatic access to the search engine for integration with customer systems
- **White-Label Options:** Enable partners to rebrand the interface for their specific markets
- **Extended Geography:** Expand beyond Thailand to support restaurant discovery in other Southeast Asian countries

## Technical Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     CLIENT (React App)                      │
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────────┐  │
│  │  LoginForm   │  │  SearchForm  │  │ RestaurantTable │  │
│  └──────┬───────┘  └──────┬───────┘  └────────┬────────┘  │
│         │                 │                    │            │
│         └─────────────────┼────────────────────┘            │
│                           │                                 │
│                      ┌────▼─────┐                          │
│                      │  App.js  │                          │
│                      │ (State)  │                          │
│                      └────┬─────┘                          │
│                           │                                 │
│                      Axios HTTP                             │
└───────────────────────────┼─────────────────────────────────┘
                            │
                    ┌───────▼────────┐
                    │  CORS Layer    │
                    └───────┬────────┘
                            │
┌───────────────────────────▼─────────────────────────────────┐
│                  SERVER (Express.js)                        │
│                                                             │
│  ┌──────────────────┐  ┌─────────────────────────────┐    │
│  │ /login           │  │ /all-restaurants            │    │
│  │ /register        │  │ (JWT Protected)             │    │
│  └──────────────────┘  └───────────┬─────────────────┘    │
│                                     │                       │
│                        ┌────────────▼──────────────┐       │
│                        │ Geographic Processing     │       │
│                        │ - getAreaBounds()         │       │
│                        │ - calculateGridCount()    │       │
│                        │ - calculateGridCenters()  │       │
│                        └────────────┬──────────────┘       │
│                                     │                       │
│                        ┌────────────▼──────────────┐       │
│                        │ getRestaurantsByGrid()    │       │
│                        │ - Loop through centers    │       │
│                        │ - Rate limiting           │       │
│                        │ - Deduplication          │       │
│                        └────────────┬──────────────┘       │
└─────────────────────────────────────┼───────────────────────┘
                                      │
                          ┌───────────▼────────────┐
                          │   Google APIs          │
                          │ - Geocoding API        │
                          │ - Places Nearby Search │
                          └────────────────────────┘
```

## Conclusion

Thai Restaurant Finder represents a well-architected solution to the challenge of comprehensive restaurant discovery within Thailand's diverse geographical landscape. The application demonstrates thoughtful engineering decisions—from grid-based search optimization to JWT authentication—that reveal both practical business sense and technical competence.

The project stands at an interesting crossroads: fully functional as a standalone tool for immediate use, yet structured in a way that welcomes evolution into a commercial SaaS platform. The existing authentication layer, API-driven design, and clean separation between frontend and backend provide exactly the foundation needed for multi-tenant deployment.

For developers, this codebase offers valuable lessons in integrating external APIs thoughtfully, managing rate limits gracefully, and building user interfaces that balance simplicity with functionality. For business stakeholders, it demonstrates a viable approach to extracting value from Google's rich location data ecosystem while maintaining awareness of cost implications.

Whether deployed as an internal tool for market research, adapted as a customer-facing service for restaurant discovery, or evolved into a full SaaS platform serving multiple business clients, Thai Restaurant Finder provides a solid starting point backed by modern web development practices and clear architectural vision.

---

## Commercial Project Name

**PlaceScout Thailand™** - *Intelligent Restaurant Discovery Platform*

Alternative commercial names:
- **RestaurantRadar Thailand** - Comprehensive F&B Location Intelligence
- **ThaiDine Analytics** - Geographic Restaurant Discovery Suite
- **FoodMap Explorer** - Thailand's Complete Restaurant Database
- **VenueVista Thailand** - Smart Location-Based Business Intelligence

---

**Document Version:** 1.0
**Last Updated:** December 4, 2025
**Commercial Project Name:** PlaceScout Thailand™
**Technical Project Name:** Thai Restaurant Finder
**Project Repository:** my-google-places-api

**Keywords:** Full-Stack Development, Web Application, React, Node.js, ExpressJS, Material UI, JavaScript, HTML5, CSS 3, CSS, RESTful API, API Integration, API Development, SaaS, Web Development, Responsive Design, JSON, HTTP, Google Maps API, Redux, TypeScript, Web Design, User Interface Design, Website Optimization, Software Debugging, Bug Fix, Google Analytics, Git, GitHub, npm, Database Design, SQL, restaurant discovery, Thailand location intelligence, Google Places API integration, geographic search, business intelligence platform, F&B analytics, location-based services, grid-based search algorithm, restaurant database, market research tool, competitive analysis, geospatial data, JWT authentication, data export Excel, Thai administrative geography, province district subdistrict search, venue mapping, hospitality industry, food service locator, place intelligence, API optimization, rate limiting, geocoding, nearby search, multi-tenant architecture, scalable web platform, subscription software, business analytics, real-time search, comprehensive coverage, deduplication algorithm, pagination system, Website Customization, App Development, Chatbot Development, Artificial Intelligence, Search Engine Optimization
