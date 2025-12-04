# PJP Mobile - Field Sales Performance & Coaching Platform

> **🚀 Full Stack Mobile Application | Sales Force Automation**

---

## 🏷️ Project Classification

| Category | Details |
|----------|---------|
| **Project Type** | ✅ **Full Stack Mobile Application** - React Native 0.79 cross-platform (iOS & Android) |
| **Architecture** | ✅ **SaaS-Ready** - Multi-role hierarchy with offline capabilities |
| **State Management** | MobX State Tree with MMKV persistence |
| **Features** | GPS tracking, photo documentation, survey modules |

---

## Executive Summary

PJP (Personal Job Performance) is a comprehensive mobile application designed for field sales teams to manage their daily activities, track store visits, conduct performance reviews, and monitor sales objectives. Built with React Native, this cross-platform solution serves as a digital companion for field sales representatives, enabling them to execute their work plans efficiently while maintaining real-time synchronization with backend systems.

The application bridges the gap between field operations and sales management by providing tools for scheduling, reporting, and performance tracking. It empowers sales teams to document store visits, complete questionnaires, capture photographic evidence, and conduct one-on-one coaching sessions—all from a single, unified mobile interface.

---

## Software Overview

### Purpose and Mission

PJP Mobile addresses the critical challenge faced by field sales organizations: maintaining visibility and accountability across distributed sales teams. Traditional paper-based workflows and disconnected systems often lead to delayed reporting, incomplete documentation, and missed coaching opportunities. This application transforms field sales operations by digitizing the entire workflow from planning to execution to review.

The platform serves multiple user roles within the sales hierarchy, from field representatives conducting store visits to supervisors managing team performance. By centralizing data collection and providing real-time insights, PJP enables data-driven decision-making and continuous performance improvement.

### Target Users

- **Field Sales Representatives**: Execute daily work plans, visit stores, complete assessments
- **Sales Supervisors**: Conduct coaching sessions (Work With), review team performance
- **Sales Managers**: Monitor team KPIs, approve schedules, track regional performance
- **Area Managers**: Oversee multiple territories, analyze trends, manage resources

### Platform Support

- **iOS**: Native support via React Native 0.79.3
- **Android**: Native support via React Native 0.79.3
- **Languages**: English and Thai with i18next internationalization
- **Offline Capability**: Persistent local storage via MMKV

---

## Core Objectives

### 1. Streamline Field Operations
Enable sales representatives to efficiently plan, execute, and document their daily activities without administrative overhead. The app reduces paperwork and manual data entry by providing intuitive digital forms and automated workflows.

### 2. Enhance Coaching Effectiveness
Facilitate meaningful one-on-one coaching sessions between supervisors and sales representatives through structured review processes and action tracking. The "Work With" functionality ensures coaching is documented and followed up systematically.

### 3. Improve Store Coverage
Maximize store visit efficiency through intelligent planning calendars, location verification, and real-time status tracking. Representatives can see at a glance which stores need visits and prioritize accordingly.

### 4. Drive Performance Accountability
Provide transparent performance metrics aligned with sales objectives (KPIs). Both representatives and managers can track progress toward targets, identify gaps, and take corrective action promptly.

### 5. Ensure Data Accuracy
Capture verified field data through GPS validation, photo documentation, and structured questionnaires. This eliminates reporting discrepancies and provides audit trails for compliance.

---

## Technical Architecture

### Technology Stack

#### Frontend Framework
- **React Native 0.79.3**: Cross-platform mobile framework leveraging native components
- **React 19.0.0**: Modern JavaScript library with latest concurrent features
- **TypeScript 5.0.4**: Strongly-typed development ensuring code reliability

#### Navigation & UI
- **React Navigation 6.x**: Type-safe screen navigation with native stack implementation
- **React Native Paper 5.12.5**: Material Design component library
- **React Native Vector Icons 10.2.0**: Comprehensive icon set (Material Community Icons)
- **React Native Safe Area Context 5.4.1**: Proper handling of device notches and safe zones

#### State Management
- **MobX State Tree 6.0.1**: Predictable state container with time-travel debugging
- **MobX React Lite 4.0.7**: Lightweight React bindings for reactive UI updates
- **React Native MMKV 3.1.0**: High-performance key-value storage for persistence

#### Data & API Layer
- **Axios 1.7.7**: HTTP client with interceptors for authentication and error handling
- **AbortController Pattern**: Request cancellation for improved performance
- **Centralized Error Handling**: Unified error management across API calls

#### Form Management
- **Formik 2.4.6**: Robust form handling with validation
- **Yup 1.4.0**: Schema-based validation engine
- **React Native Keyboard Aware ScrollView**: Auto-scrolling for input fields

#### Date & Time
- **Day.js 1.11.13**: Lightweight date manipulation library
- **React Native Calendars 1.1307.0**: Interactive calendar components with custom marking

#### Camera & Media
- **React Native Vision Camera 4.6.4**: High-performance camera with modern architecture
- **React Native Image Marker 1.2.6**: Image watermarking for photo documentation
- **React Native Image Resizer 3.0.11**: Image optimization before upload

#### Geolocation
- **React Native Geolocation Service 5.3.1**: Accurate GPS positioning with background support
- **Location Validation**: Verify field representatives are at store locations

#### Charts & Visualization
- **React Native Chart Kit 6.12.0**: Performance charts and dashboard visualizations
- **React Native SVG 15.9.0**: Scalable vector graphics support
- **Shopify React Native Skia 2.0.2**: High-performance 2D graphics

#### Device Integration
- **React Native Device Info 14.0.1**: Device metadata and capabilities
- **React Native Permissions 5.1.0**: Runtime permission management
- **React Native FS 2.20.0**: File system access for document handling
- **React Native Blob Util 0.22.2**: Binary data handling for uploads

#### Development & Quality
- **ESLint**: Code linting with React Native preset
- **Jest 29.6.3**: Testing framework with React Native support
- **Patch Package 8.0.0**: Custom patches for third-party dependencies
- **Prettier 2.8.8**: Consistent code formatting

---

## Feature Catalog

### 1. Authentication & Security

#### User Login
- Credential-based authentication with username/password
- Secure token storage using MMKV encrypted storage
- Automatic token refresh and session management
- Biometric authentication readiness (infrastructure in place)

#### Session Management
- Persistent login state across app restarts
- Automatic logout on authentication failure (401 responses)
- Token validation before sensitive operations
- Secure credential storage with encryption

#### Security Features
- Authorization headers automatically injected via Axios interceptors
- Request-level authentication tokens
- Logout clears all user data and tokens
- No plain-text credential storage

---

### 2. Dashboard & Performance Analytics

#### My Performance Overview
The dashboard serves as the command center for sales representatives, providing a comprehensive view of their performance across multiple dimensions:

##### Monthly Coaching Summary
- Current month coaching activity metrics
- Reference categories with actual counts
- Visual indicators of coaching completion rates
- Historical comparison capabilities

##### Work Status Tracking
- Real-time view of scheduled activities
- Date-based organization of work plans
- Activity type indicators (WW, FW, ONE)
- Customer/salesman associations
- Completion status with visual check marks
- Location verification status

##### KPI Summary Table (Month-to-Date)
- Target vs. Actual performance comparison
- Achievement percentage calculations
- Multiple KPI categories tracked simultaneously
- Color-coded performance indicators
- Sortable and filterable views

##### 3-Step Performance Metrics
Specialized tracking for the "แช่, เช็ค, ช็อป" (Soak, Check, Shop) methodology:
- Individual step targets and actuals
- Consolidated achievement percentages
- Step-by-step progress visualization
- Trend analysis over time

##### Store Audit Summary
- Audit completion tracking
- Quality compliance metrics
- Target vs. actual audit counts
- Achievement percentages
- Priority store identification

##### Monthly Summary Table
Comprehensive monthly activity overview including:
- Number of Work With (WW) days executed
- Number of Field Work (FW) days completed
- Customer Representatives (CR) contacted
- Market Representatives (MR) connected
- Total store connections (overall)
- WW-specific store connections
- FW-specific store connections
- Horizontal scrolling for dense data presentation

#### Dashboard Interactions
- **Pull-to-Refresh**: Updates all dashboard sections simultaneously
- **Loading States**: Skeleton screens during initial data fetch
- **Empty States**: User-friendly messages when data is unavailable
- **Data Caching**: Reduces redundant API calls for better performance

---

### 3. Work Planning & Scheduling

#### Dual Calendar System

##### Schedule Plan View
The planning calendar allows representatives to create and manage their future work schedule:

- **Monthly Calendar Interface**: Visual month-at-a-time planning
- **Activity Type Selection**: Choose between WW, FW, or ONE activities
- **Multi-Day Planning**: Schedule multiple activities across weeks
- **Color-Coded Dots**: Visual indicators for different activity types
  - Work With (WW) activities
  - Field Work (FW) activities
  - One-on-One (ONE) coaching sessions
- **Date Restrictions**: Cannot schedule activities in the past
- **Edit Capability**: Modify existing schedule entries
- **Submit & Approve Workflow**: Formal schedule submission for manager approval
- **Month Navigation**: Chevron-based navigation between months

##### Work Plan View
The execution calendar shows approved work plans ready for execution:

- **Daily Activity Breakdown**: Tap any date to see scheduled activities
- **Pre-populated Plans**: Activities approved by management
- **Execution Tracking**: See which activities are completed
- **Location Verification**: Visual indicators for location compliance
- **Status Icons**: Check marks for visited activities
- **Activity Details**: Customer/salesman names and activity types
- **View-Only Past Dates**: Historical activities are read-only
- **Current Date Execution**: Today's activities are actionable

#### Calendar Features

##### Visual Indicators
- **Color-Coded Dots**: Each activity type has a distinct color
- **Multiple Activities**: Single day can show multiple colored dots
- **Selected State**: Highlighted dates with activities
- **Disabled Dates**: Greyed-out dates outside current month
- **Month Headers**: Clear month/year labeling

##### Navigation
- **Swipe Gestures**: Swipe between months
- **Arrow Navigation**: Tap chevrons to change months
- **Today Button**: Quick jump to current date
- **Month Change Events**: Data automatically refreshes

##### Responsive Design
- **Dynamic Day Sizing**: Adapts to different screen sizes
- **Tablet Optimization**: Scales appropriately for larger screens
- **Safe Area Awareness**: Respects device notches and home indicators

---

### 4. Store Visit Workflow

#### Store List Management

##### Location-Based Store Discovery
- **GPS Integration**: Real-time location tracking
- **Distance Calculation**: Shows proximity to each store
- **Location Permission Handling**: Graceful fallback if GPS denied
- **Background Location**: Maintains position while using other features

##### Store Status Indicators
- **White (Open)**: Store not yet visited, ready for visit
- **Yellow (Out of Area)**: Visited but outside geofence boundary
- **Green (In Area)**: Successfully visited within location boundaries
- **Visual Color Coding**: Quick recognition of visit status

##### Store Search & Filter
- **Real-time Search**: Filter by customer name or code
- **Search Highlighting**: Matched text highlighted in results
- **Instant Results**: No delay in search responsiveness
- **Clear Search**: Quick button to reset search

##### Store List Display
- **Card-Based Layout**: Each store in distinct card
- **Store Information Display**:
  - Customer code and name
  - Store address
  - Visit status icon
  - Location verification status
  - Distance from current position
  - Activity type association
- **Pull-to-Refresh**: Update store list and locations
- **Infinite Scroll**: Lazy loading for large store lists
- **Empty States**: Friendly messaging when no stores match

#### Store Detail View

##### Information Tab
Comprehensive store profile including:
- **Customer Demographics**: Code, name, contact information
- **Address Details**: Full address with map integration possibility
- **Store Classification**: Type, tier, route assignment
- **Contact Persons**: Decision makers and staff
- **Operating Hours**: Store schedule information
- **Visit History**: Previous visit dates and outcomes

##### Performance Tab
Historical performance metrics:
- **Sales Trends**: Monthly/quarterly sales data
- **Product Mix**: Category-wise sales breakdown
- **Growth Indicators**: Year-over-year comparisons
- **Target Achievement**: Store-specific KPI tracking
- **Visual Charts**: Graphical performance representation
- **Date Range Selection**: Filter performance by period

---

### 5. Field Work Execution

#### Photo Capture & Documentation

##### Advanced Camera Interface
- **Native Camera Integration**: React Native Vision Camera for high performance
- **Real-time Preview**: Live viewfinder with focus and exposure controls
- **Flash Control**: Toggle flash for different lighting conditions
- **Multiple Photo Support**: Capture multiple angles/subjects per visit
- **Photo Review**: Preview before accepting image
- **Retake Option**: Discard and recapture if needed

##### Image Processing
- **Automatic Watermarking**: Timestamp and GPS coordinates embedded
- **Image Compression**: Optimized file sizes for efficient upload
- **Orientation Correction**: Automatic EXIF-based rotation
- **Quality Preservation**: Balance between size and clarity

##### Photo Management
- **Gallery View**: Thumbnail grid of captured photos
- **Delete Capability**: Remove unwanted images before submission
- **Upload Queue**: Batch upload of multiple images
- **Progress Tracking**: Visual feedback during upload
- **Retry Logic**: Automatic retry on network failures

#### Geolocation Verification

##### GPS Validation
- **Geofence Checking**: Verify user within acceptable radius of store
- **Configurable Tolerance**: Adjustable distance threshold per store
- **Visual Feedback**: Color-coded indicators (green/yellow)
- **Location Override**: Manual verification for edge cases
- **GPS Accuracy Display**: Show location precision level

##### Location Status Types
- **In Area (Green)**: Within geofence, full compliance
- **Out of Area (Yellow)**: Outside boundary but visit acknowledged
- **No GPS**: Location services unavailable
- **High Accuracy Required**: Prompts user to improve GPS signal

---

### 6. Questionnaire System

#### Dynamic Form Generation

##### Question Types
The questionnaire system supports three distinct question formats:

**Radio Button (Single Choice)**
- Single answer selection from predefined choices
- Mutually exclusive options
- Visual radio button indicators
- Required/optional field configuration
- Optional remark field for additional context

**Checkbox (Multiple Choice)**
- Multiple simultaneous selections allowed
- Independent choice toggles
- Visual checkbox indicators
- Minimum/maximum selection constraints
- Optional remark field per question

**Text Input (Free Form)**
- Multi-line text area for detailed responses
- Character count tracking
- Keyboard-aware scrolling
- Required field validation
- Auto-save draft functionality

##### Question Attributes
- **Sequential Ordering**: Questions numbered and ordered consistently
- **Required Indicators**: Visual asterisk (*) for mandatory questions
- **Descriptions**: Optional help text below question title
- **Conditional Logic**: Show/hide based on previous answers
- **Section Grouping**: Related questions organized into collapsible sections

#### Questionnaire Sections

##### Collapsible Groups
- **Section Headers**: Bold titles with expand/collapse chevrons
- **Descriptions**: Section-level context and instructions
- **Animation**: Smooth expand/collapse transitions
- **State Persistence**: Remembers expanded/collapsed state during session
- **Navigation**: Jump between sections easily

##### Answer Management

**Real-time Validation**
- **Required Field Checking**: Red indicators for missing required answers
- **Format Validation**: Text pattern validation for specific formats
- **Character Limits**: Enforce minimum/maximum text lengths
- **Choice Validation**: Ensure valid option selections

**Data Persistence**
- **Auto-save Drafts**: Periodic save of incomplete questionnaires
- **Resume Capability**: Return to partially completed forms
- **Local Storage**: Offline answer retention
- **Sync on Connect**: Upload when network available

**Error Handling**
- **Visual Error Indicators**: Red number badges for questions with errors
- **Error Messages**: Specific guidance on what's missing or invalid
- **Scroll to Error**: Auto-scroll to first incomplete required field
- **Submission Blocking**: Prevent incomplete submissions

#### Questionnaire Submission

##### Pre-submission Checks
- **Completeness Validation**: Verify all required fields answered
- **Format Validation**: Check answer formats meet requirements
- **Warning Prompts**: Alert user to potential issues before submit
- **Review Summary**: Show overview of answers before final submit

##### Submission Process
- **Loading Indicators**: Visual feedback during save operation
- **Network Handling**: Graceful handling of connectivity issues
- **Retry Logic**: Automatic retry on transient failures
- **Confirmation Dialog**: Success message with timestamp

##### Post-submission
- **Visit Status Update**: Automatically mark visit as completed
- **Navigation**: Return to store list or work plan
- **Data Refresh**: Update related screens with new data
- **Offline Queue**: Queue submissions when offline for later sync

---

### 7. Work With (WW) Activities

#### Salesman Performance Management

##### Activity Overview
Work With represents joint field visits where supervisors accompany sales representatives to:
- Observe in-field performance
- Provide real-time coaching
- Demonstrate best practices
- Build team relationships
- Validate compliance

##### Salesman Selection
- **Salesman Directory**: Browse assigned team members
- **Search Functionality**: Find salesman by name or code
- **Availability Indicators**: Show who's scheduled for the day
- **Profile Access**: View salesman details and history
- **Quick Selection**: Recently worked-with salesmen highlighted

##### Joint Visit Execution

**Store Selection Together**
- Supervisor and salesman collaborate on store selection
- Shared visibility into planned stores
- Real-time coordination of visit sequence
- Dynamic route optimization based on location

**Observation & Coaching**
- Structured observation checklists
- Real-time note-taking during visit
- Photo documentation of coaching moments
- Performance scoring on multiple dimensions

**Performance Tracking**
- **Activity Metrics**: Stores visited, time spent per store
- **Quality Scores**: Evaluation of visit quality
- **Skill Assessments**: Rate specific sales techniques
- **Improvement Areas**: Document coaching opportunities

##### Visit Documentation

**Coaching Notes**
- Free-form text for observations
- Structured fields for specific competencies
- Positive reinforcement documentation
- Development area identification

**Action Items**
- Specific behavioral improvements to work on
- Skill development recommendations
- Follow-up coaching topics
- Timeline for improvement

---

### 8. Review & Discussion Workflow

#### Review Priority Discussion

##### Monthly Discussion Framework
Structured framework for reviewing sales performance and setting priorities:

**Discussion Categories**
- Organized into sequential discussion groups
- Each group contains related topics
- Expandable/collapsible sections for focused review
- Visual numbering for systematic progression

**Last Month Review**
- Previous month's targets and actuals
- Achievement percentages
- Priority actions from prior month
- Outcome assessment of previous priorities

**Current Month Planning**
- New month targets
- Adjusted strategies based on learnings
- Priority action identification
- Resource allocation decisions

##### Priority Setting
**Priority Flags**
- Toggle priority status for discussion items
- Visual indicators (checkboxes, stars)
- Priority count summary
- Filtering by priority status

**Action Planning**
- Free-text action field for each priority
- Specific, measurable action descriptions
- Owner assignment (implicit by user)
- Timeline associations

##### Discussion Capture
- **Structured Data Entry**: Predefined fields ensure completeness
- **Historical Comparison**: Side-by-side last month vs current month
- **Progress Tracking**: Visual indicators of improvement/decline
- **Document Conversation**: Capture key discussion points

##### Submission & Approval
- **Save Draft**: Interim save without finalizing
- **Submit for Review**: Lock discussion and route for approval
- **Manager Approval Flow**: Supervisors approve discussion outcomes
- **Audit Trail**: Track who modified what and when

#### WW/FW Review Tracking

##### Visit Answer Review
Systematic review of questionnaires completed during Work With and Field Work visits:

**Grouped by Visit**
- Organized by date and customer
- Clear separation between different store visits
- Visit metadata displayed (date, store, activity type)
- Quick navigation between visits

**Answer Display**
- **Answers Section**: Display selected choices from questionnaires
- **Remarks Section**: Show text responses and notes
- **Question Context**: Original question displayed for reference
- **Response Timestamp**: When answer was recorded

##### Review Status Management

**Checkbox Review System**
- Each answer has individual review checkbox
- Checkbox indicates supervisor has reviewed and acknowledged
- Visual distinction between reviewed and unreviewed items
- Review status persists and syncs to server

**Review States**
- **Not Reviewed (Unchecked)**: Default state, needs attention
- **Reviewed (Checked)**: Supervisor has acknowledged and verified
- **Bulk Actions**: Select all for quick review
- **Review History**: Track when and by whom review occurred

##### Use Cases

**Quality Assurance**
Supervisors verify that field representatives:
- Completed questionnaires accurately
- Followed proper procedures
- Documented findings thoroughly
- Identified correct improvement actions

**Coaching Opportunities**
During review, supervisors can:
- Identify patterns in responses
- Spot training needs
- Recognize best practices
- Schedule follow-up discussions

**Compliance Validation**
Ensure all required elements documented:
- All stores visited completed questionnaires
- Required photos captured and uploaded
- Action items recorded
- Geolocation verified

##### Review Submission
- **Save Progress**: Mark reviewed items incrementally
- **Submit Review**: Finalize review and lock changes
- **Feedback Loop**: Comments can trigger re-submission
- **Completion Tracking**: Dashboard shows review completion rate

---

### 9. One-on-One (1 On 1) Sessions

#### Review & Discussion Confirmation

##### Session Purpose
Formal one-on-one meetings between supervisors and sales representatives focused on:
- Performance review and feedback
- Career development discussions
- Goal setting and alignment
- Issue resolution
- Recognition and motivation

##### Pre-session Preparation
**Salesman Selection**
- Choose team member for session
- View upcoming scheduled sessions
- Reschedule if needed
- Session history access

**Data Gathering**
- Automatic compilation of performance metrics
- Recent activity summary
- Outstanding action items
- Previous session notes

##### Discussion Workflow

**Priority Review**
- Review of priority items from last session
- Status updates on committed actions
- Discussion of barriers encountered
- Celebration of completed priorities

**Current Performance**
- KPI review (targets vs. actuals)
- Trend analysis
- Comparative performance (vs. team, vs. region)
- Strengths and development areas

**Goal Setting**
- Establish new priorities for upcoming period
- SMART goal definition
- Resource needs identification
- Success criteria definition

##### Documentation

**Session Notes**
- Structured note-taking interface
- Key discussion points
- Agreed-upon actions
- Development plans
- Recognition items

**Action Items**
- Specific action commitments
- Owner assignment
- Due dates
- Success measures
- Follow-up schedule

**Review Confirmation**
- Both parties acknowledge discussion
- Digital signature or confirmation
- Immutable record created
- Synced to central system

##### Follow-up Tracking
- **Action Status**: Track completion of committed actions
- **Next Session Scheduling**: Automatic scheduling of follow-up
- **Reminder Notifications**: Alerts for upcoming due dates
- **Progress Updates**: Interim check-in capability

---

### 10. Settings & Configuration

#### Language Preferences

##### Bilingual Support
- **English**: Default language for international users
- **Thai**: Localized for Thai market users
- **Instant Switching**: Change language without app restart
- **Persistent Preference**: Language choice saved to user profile
- **Complete Coverage**: All UI text and messages localized

##### Translation Quality
- Native speaker translations for accuracy
- Context-aware translations for business terms
- Consistent terminology across screens
- Regular updates for new features

#### Profile Management

##### User Information Display
- Username and full name
- Role and position
- Team assignment
- Manager hierarchy
- Contact information

##### Profile Actions
- **Change Password**: Secure password update flow
- **Update Profile Photo**: Avatar image upload
- **Contact Preferences**: Email, phone, notification settings
- **Privacy Controls**: Data sharing preferences

#### Application Settings

##### Version Information
- Current app version display
- Build number for technical support
- Last update timestamp
- Check for updates functionality

##### About Section
- Company information
- Support contact details
- Terms of service access
- Privacy policy link
- License information

##### Advanced Settings
- **Cache Management**: Clear local data cache
- **Debug Mode**: Enable diagnostic logging (for support)
- **Data Usage**: Show storage and network consumption
- **Permissions Review**: Manage app permissions

#### Logout Process
- **Confirm Dialog**: Prevent accidental logout
- **Data Sync Check**: Warn if unsynced data exists
- **Secure Cleanup**: Clear tokens and sensitive data
- **Session Termination**: Invalidate server session
- **Return to Login**: Smooth transition to login screen

---

## User Interface Design

### Design Principles

#### Material Design Foundation
The application follows Google's Material Design guidelines, providing:
- **Familiar Interactions**: Standard Android/iOS patterns
- **Tactile Surfaces**: Elevated cards and layered surfaces
- **Meaningful Motion**: Purposeful transitions and animations
- **Adaptive Layouts**: Responsive to different screen sizes

#### Visual Hierarchy
- **Primary Actions**: Prominent buttons in accent color
- **Secondary Actions**: Outlined or text buttons
- **Status Indicators**: Color-coded for quick recognition
- **Typography Scale**: Clear heading and body text distinction

#### Color System

**Primary Palette**
- Primary Color: Used for app bars, key actions, active states
- Primary Light: Hover states, selected items
- Primary Dark: Active press states, shadows

**Functional Colors**
- **Success (Green)**: Completed actions, positive indicators
- **Warning (Yellow)**: Caution states, out-of-bounds locations
- **Error (Red)**: Validation errors, failed operations
- **Info (Blue)**: Informational messages, neutral states

**Text Colors**
- Primary Text: High-contrast for body content
- Secondary Text: Reduced contrast for metadata
- Disabled Text: Low contrast for inactive elements

#### Component Design

##### Cards
- **Elevation**: Subtle shadows for depth perception
- **Padding**: Generous internal spacing for readability
- **Dividers**: Subtle lines separating sections
- **Actions**: Right-aligned action buttons

##### Lists
- **Item Height**: Touch-friendly 56-72dp minimum
- **Leading Icons**: Visual category identification
- **Supporting Text**: Metadata below primary content
- **Trailing Actions**: Icons or chevrons for navigation

##### Forms
- **Outlined Inputs**: Clear field boundaries
- **Floating Labels**: Space-efficient labeling
- **Error States**: Red underlines with helper text
- **Character Counts**: Live feedback on text inputs

##### Navigation
- **Material Bottom Tabs**: Primary navigation pattern
- **Stack Navigation**: Hierarchical screen flow
- **Breadcrumbs**: Context awareness in deep screens
- **Swipe Gestures**: Natural back navigation

### Responsive Design

#### Screen Adaptations
- **Phone Portrait**: Optimized for one-handed use
- **Phone Landscape**: Expanded content area utilization
- **Tablet Portrait**: Multi-column layouts where appropriate
- **Tablet Landscape**: Side-by-side master-detail views

#### Safe Area Handling
- Automatic inset detection for notched devices
- Bottom navigation respects home indicator
- Content avoids camera cutouts
- Landscape orientation accounts for side bezels

### Accessibility Features

#### Visual Accessibility
- **Contrast Ratios**: WCAG AA compliance minimum
- **Text Scaling**: Respects system font size preferences
- **Color Independence**: Information not conveyed by color alone
- **Focus Indicators**: Clear keyboard navigation

#### Interaction Accessibility
- **Touch Targets**: Minimum 44x44pt tap areas
- **Spacing**: Adequate separation between interactive elements
- **Error Recovery**: Clear error messages with corrective guidance
- **Undo Actions**: Ability to reverse destructive operations

---

## Data Management

### State Architecture

#### MobX State Tree Implementation
The application uses MobX State Tree for predictable, observable state management:

**State Modules**
- **UserState**: Authentication status, user profile, token management
- **ConfigState**: Application configuration, feature flags, environment settings
- **SettingState**: User preferences, language selection, app settings
- **APIDataState**: Cached API responses, data invalidation strategies

**State Persistence**
- MMKV storage for fast read/write operations
- Automatic serialization and deserialization
- Selective persistence (sensitive data excluded)
- Migration strategies for version upgrades

#### Reactive Updates
- **Observer Pattern**: Components automatically re-render on state changes
- **Computed Values**: Derived data recalculated efficiently
- **Action Tracking**: All state modifications go through actions
- **Snapshot History**: Time-travel debugging capabilities

### API Integration

#### HTTP Client Configuration
Centralized Axios configuration with:
- **Base URL Management**: Environment-specific endpoints
- **Request Interceptors**: Automatic auth header injection
- **Response Interceptors**: Consistent error handling
- **Timeout Configuration**: Prevent hanging requests
- **Retry Logic**: Automatic retry on network failures

#### Request Cancellation
- **AbortController Pattern**: Cancel in-flight requests
- **Component Cleanup**: Cancel on component unmount
- **Navigation Cancel**: Abort when navigating away
- **Memory Leak Prevention**: Avoid state updates after unmount

#### Error Handling Strategy

**HTTP Status Handling**
- **200-299 Success**: Normal data processing
- **400 Bad Request**: Validation error display to user
- **401 Unauthorized**: Automatic logout and redirect to login
- **403 Forbidden**: Permission denied message
- **404 Not Found**: Resource not available handling
- **500 Server Error**: Generic error with retry option
- **Network Errors**: Offline detection and queueing

**Error Presentation**
- User-friendly error messages
- Technical details hidden by default
- Action suggestions (retry, contact support)
- Error codes for support diagnostics

### Data Caching

#### Cache Strategy
- **API Response Caching**: 15-minute TTL for dashboard data
- **Image Caching**: Automatic disk caching of photos
- **Selective Invalidation**: Clear specific cache keys on updates
- **Memory Management**: Automatic cache eviction on low memory

#### Offline Support
- **Local Data Persistence**: Core data available offline
- **Queue Management**: Queue API calls when offline
- **Sync on Reconnect**: Automatic upload when network restored
- **Conflict Resolution**: Last-write-wins strategy with timestamps

---

## Performance Optimization

### Rendering Optimization

#### React Optimization
- **Memoization**: useMemo and useCallback for expensive computations
- **Component Memoization**: React.memo for pure components
- **Lazy Loading**: Deferred component loading for faster startup
- **List Virtualization**: FlatList for efficient long lists

#### State Updates
- **Batched Updates**: Multiple state changes in single render
- **Selective Re-renders**: Observer pattern updates only affected components
- **Immutable Updates**: Proper state immutability for change detection
- **Throttling**: Debounce rapid user inputs

### Network Optimization

#### Request Optimization
- **Request Deduplication**: Prevent duplicate simultaneous requests
- **Pagination**: Load data in chunks for large datasets
- **Incremental Loading**: Initial render with minimal data
- **Background Sync**: Non-blocking data updates

#### Payload Optimization
- **Image Compression**: Reduce photo sizes before upload
- **Selective Fields**: Request only needed data fields
- **Batch Operations**: Combine multiple operations in single request
- **Delta Updates**: Send only changed data

### Asset Optimization

#### Image Handling
- **WebP Format Support**: Smaller file sizes with quality
- **Multiple Resolutions**: Appropriate image size per device
- **Lazy Loading**: Load images as they enter viewport
- **Placeholder Images**: Show placeholders during load

#### Bundle Optimization
- **Code Splitting**: Separate bundles for different features
- **Tree Shaking**: Remove unused code
- **Minification**: Reduce JavaScript bundle size
- **Compression**: Gzip assets for faster download

---

## Security & Privacy

### Authentication Security

#### Token Management
- **Secure Storage**: MMKV with encryption for token storage
- **Token Expiration**: Automatic logout on token expiry
- **Refresh Tokens**: Seamless token renewal without re-login
- **Token Validation**: Verify token integrity before sensitive operations

#### Credential Handling
- **No Plain Text Storage**: Credentials never stored unencrypted
- **Secure Transmission**: HTTPS for all API communication
- **Password Requirements**: Enforce strong password policies
- **Failed Login Protection**: Rate limiting on login attempts

### Data Privacy

#### Personal Data Protection
- **Minimal Data Collection**: Only collect necessary information
- **Data Encryption**: Sensitive data encrypted at rest
- **Secure Transmission**: TLS 1.2+ for all network traffic
- **Data Retention**: Automatic cleanup of old data

#### Location Privacy
- **Purpose Disclosure**: Clear explanation of GPS usage
- **Permission Request**: Runtime permission with context
- **Optional Location**: Graceful degradation if denied
- **Location Accuracy**: Only request precision needed

### App Security

#### Code Security
- **Obfuscation**: JavaScript code minification and obfuscation
- **Root Detection**: Warn on rooted/jailbroken devices
- **SSL Pinning**: Prevent man-in-middle attacks
- **Secure Dependencies**: Regular security updates

#### Data Security
- **Input Validation**: Sanitize all user inputs
- **SQL Injection Prevention**: Parameterized queries
- **XSS Prevention**: Escape user-generated content
- **CSRF Protection**: Token-based request validation

---

## Integration Points

### Backend API Integration

#### Endpoint Categories

**Authentication Services**
- `POST /auth/login`: User authentication
- `GET /auth/profile`: User profile retrieval
- `POST /auth/logout`: Session termination
- `POST /auth/refresh`: Token renewal

**Configuration Services**
- `GET /config/app`: Application configuration
- `GET /config/features`: Feature flags
- `GET /config/version`: Version check

**Dashboard Services**
- `GET /dashboard/coaching-summary`: Monthly coaching metrics
- `GET /dashboard/work-status`: Work activity status
- `GET /dashboard/kpi-summary`: KPI performance data
- `GET /dashboard/3-step-summary`: 3-step methodology metrics
- `GET /dashboard/store-audit`: Audit completion data
- `GET /dashboard/monthly-summary`: Comprehensive monthly stats

**Schedule & Work Plan Services**
- `GET /schedule-plan`: Retrieve monthly schedule
- `POST /schedule-plan`: Create/update schedule
- `POST /schedule-plan/approve`: Submit for approval
- `GET /work-plan`: Retrieve approved work plans
- `GET /work-plan/date`: Get specific date activities

**Customer & Store Services**
- `GET /customers`: List customers
- `GET /customers/:id`: Customer detail
- `GET /customers/search`: Search customers
- `POST /customers/location`: Update customer location

**Questionnaire Services**
- `GET /questionnaire`: Get questionnaire for visit
- `POST /questionnaire/answer`: Submit answers

**Review Services**
- `GET /review/priority`: Priority discussion data
- `POST /review/priority/save`: Save discussion
- `GET /review/ww-fw`: WW/FW review items
- `POST /review/ww-fw/save`: Submit review status

**Salesman Services**
- `GET /salesman`: List salesmen
- `GET /salesman/:id`: Salesman detail
- `GET /salesman/performance`: Performance data

**Upload Services**
- `POST /upload/photo`: Photo upload
- `POST /upload/batch`: Batch file upload

#### API Contract
- **Request Format**: JSON with Content-Type header
- **Response Format**: Consistent JSON structure
- **Error Format**: Standardized error objects
- **Date Format**: ISO 8601 timestamps
- **Pagination**: Cursor-based pagination

### Third-Party Services

#### Geolocation Services
- Native iOS/Android location services
- Background location updates
- Geocoding for address resolution
- Reverse geocoding for location lookup

#### Camera Services
- Native camera access via Vision Camera
- Photo library access for selections
- Image compression and optimization
- EXIF metadata extraction

#### File System
- Document directory access
- Temporary file management
- Cache directory utilization
- External storage (Android)

---

## Deployment & Distribution

### Build Configuration

#### iOS Build
- **Xcode Project**: `ios/pjp.xcodeproj`
- **Bundle Identifier**: `com.verismart.pjp`
- **Deployment Target**: iOS 13.4+
- **CocoaPods**: Dependency management via Podfile
- **Provisioning**: App Store distribution profile required

#### Android Build
- **Gradle Configuration**: `android/app/build.gradle`
- **Package Name**: `com.verismart.pjp`
- **Min SDK Version**: Android 6.0 (API 23)
- **Target SDK Version**: Android 14 (API 34)
- **Signing**: Keystore required for release builds

### Release Process

#### Version Management
- **Semantic Versioning**: MAJOR.MINOR.PATCH format
- **Build Numbers**: Auto-incremented per build
- **Release Notes**: Maintained per version
- **Changelog**: User-facing change documentation

#### App Store Distribution
- **iOS App Store**: Apple Developer Program account required
- **Google Play Store**: Google Play Console access needed
- **Beta Testing**: TestFlight (iOS) and Internal Testing (Android)
- **Staged Rollouts**: Gradual user percentage increases

---

## Future Roadmap

### Planned Enhancements

#### Advanced Analytics
- **Predictive Analytics**: AI-driven performance predictions
- **Trend Analysis**: Automated insight generation
- **Benchmarking**: Peer comparison capabilities
- **Custom Dashboards**: User-configurable dashboard widgets

#### Collaboration Features
- **Team Chat**: In-app messaging for coordination
- **Shared Notes**: Collaborative note-taking
- **Activity Feed**: Social-style activity updates
- **Mentions**: Tag colleagues in notes and discussions

#### Offline Enhancements
- **Full Offline Mode**: Complete functionality without network
- **Smart Sync**: Optimized sync algorithms
- **Conflict Resolution UI**: Manual conflict handling
- **Offline Indicators**: Clear offline state communication

#### Integration Expansion
- **Calendar Integration**: Sync with device calendar
- **Email Integration**: Send reports via email
- **CRM Integration**: Bidirectional CRM sync
- **BI Tool Export**: Export to analytics platforms

---

## Technical Requirements

### Device Requirements

#### iOS Devices
- **Minimum Version**: iOS 13.4+
- **Recommended**: iOS 15.0+
- **Devices**: iPhone 6s and newer
- **Storage**: 100MB minimum available space
- **Camera**: Rear camera required for photo features
- **GPS**: Location services required

#### Android Devices
- **Minimum Version**: Android 6.0 (API 23)
- **Recommended**: Android 11.0+
- **Storage**: 100MB minimum available space
- **Camera**: Rear camera required for photo features
- **GPS**: Location services required
- **RAM**: 2GB minimum recommended

### Network Requirements
- **Connectivity**: Internet connection required for most features
- **Bandwidth**: 3G minimum, 4G/LTE recommended
- **Latency**: < 500ms preferred for responsive UI
- **Offline Capability**: Limited features available offline

### Permission Requirements

#### iOS Permissions
- **Camera**: Photo capture functionality
- **Location When In Use**: Store visit verification
- **Photo Library**: Saving captured photos

#### Android Permissions
- **Camera**: Photo capture functionality
- **Fine Location**: Precise GPS positioning
- **Coarse Location**: Approximate positioning fallback
- **Storage**: Photo saving and file access
- **Network State**: Connectivity detection

---

## Glossary of Terms

**CR (Customer Representative)**: Sales representatives who visit retail stores

**FW (Field Work)**: Individual store visits conducted independently by sales representatives

**KPI (Key Performance Indicator)**: Measurable values demonstrating effectiveness of sales activities

**MR (Market Representative)**: Regional sales representatives managing specific territories

**PJP (Personal Job Performance)**: The application and methodology for field sales management

**WW (Work With)**: Joint field visits where supervisors accompany sales representatives

**3-Step (แช่, เช็ค, ช็อป)**: Specific sales methodology (Soak, Check, Shop)

**1 On 1**: Formal one-on-one coaching sessions between supervisors and team members

**Geofence**: Virtual geographic boundary used to verify visit locations

**Visit Status**: Current state of store visit (Open, In Progress, Completed)

**Location Status**: GPS verification result (In Area, Out of Area, No GPS)

**Schedule Plan**: Future work schedule created by sales representative

**Work Plan**: Approved schedule of activities ready for execution

**Store Audit**: Systematic evaluation of store compliance and quality

**Achievement**: Percentage of target accomplished (Actual/Target × 100)

---

## Support & Maintenance

### Technical Support
For technical assistance, please contact:
- **Email**: support@verismart.com
- **Issue Tracker**: GitHub Issues (for development team)
- **Documentation**: Internal wiki and CLAUDE.md

### Version History
Current Version: 0.0.1
- Initial release with core functionality
- iOS and Android platform support
- Bilingual support (English/Thai)

### Known Issues
See PATCH_MANAGEMENT.md for current compatibility patches and known limitations.

---

**Document Version**: 1.0
**Last Updated**: 2025-12-04
**Author**: PJP Development Team
**Status**: Living Document

---

## 🏷️ Keywords

`React Native`, `TypeScript`, `MobX State Tree`, `React Navigation`, `MMKV`, `Axios`, `Formik`, `Yup`, `Mobile App Development`, `iOS Development`, `Android App Development`, `Cross-Platform`, `Full-Stack Development`, `RESTful API`, `API Integration`, `GPS Tracking`, `Google Maps API`, `Camera Integration`, `React Native Vision Camera`, `Day.js`, `React Native Calendars`, `Chart Kit`, `Firebase`, `Push Notifications`, `Offline-First`, `Sales Force Automation`, `Field Sales`, `CRM`, `Performance Management`, `JavaScript`, `Git`, `GitHub`, `Redux`, `Hybrid App Development`, `Mobile Platforms`, `User Interface Design`
