# eOrder Mobile - Enterprise B2B/B2C Commerce Platform

> **🚀 Full Stack Mobile Application | Cross-Platform Solution**

---

## 🏷️ Project Classification

| Category | Details |
|----------|---------|
| **Project Type** | ✅ **Full Stack Mobile Application** - React Native cross-platform (iOS & Android) |
| **Architecture** | ✅ **SaaS-Ready** - Enterprise-grade with offline-first architecture |
| **Backend Integration** | RESTful API with Firebase Cloud Messaging |
| **Multi-Language** | Thai, English, Japanese, Lao with i18n support |

---

## eOrdering React Native Application

**eOrdering** is a comprehensive enterprise-grade mobile ordering and asset management platform built with cutting-edge React Native 0.76+ technology. This cross-platform solution delivers seamless B2B/B2C e-commerce experiences with advanced inventory tracking, multi-language support (Thai, English, Japanese, Lao), and real-time notifications, designed for scalability and performance in production environments.

## Commercial Features

### Business-Critical Capabilities
- **Enterprise Authentication & Security**: JWT-based authentication with automatic token refresh, secure session management, and role-based access control
- **Advanced Product Catalog Management**: Multi-category product browsing, real-time inventory updates, product search and filtering, detailed product specifications
- **Intelligent Shopping Cart**: Persistent cart state, quantity management, price calculations, promotional code support, multi-item checkout
- **Complete Order Lifecycle Management**: Order placement, real-time order tracking, order history with detailed views, order status updates, reorder functionality
- **Asset Management & Tracking**: QR code-based asset verification, asset check-in/check-out, asset location tracking, asset history and reporting
- **Push Notification System**: Firebase Cloud Messaging integration, local and remote notifications, notification preferences, in-app notification center
- **Multi-language Internationalization**: Full i18n support for Thai, English, Japanese, and Lao languages with RTL support preparation
- **User Profile & Account Management**: Profile editing, password management, preferences settings, order preferences
- **Responsive UI/UX Design**: Modern Material Design principles, custom theming, adaptive layouts for tablets and phones

### Technical Differentiators
- **Cross-Platform Native Performance**: Single codebase for iOS and Android with native performance
- **Offline-First Architecture**: AsyncStorage persistence, offline cart management, sync capabilities
- **Real-time Data Synchronization**: Live inventory updates, order status changes, notification delivery
- **Scalable Backend Integration**: RESTful API integration with centralized configuration
- **Production-Ready Build Pipeline**: Automated builds, code quality checks, comprehensive testing

## Technology Stack

### Frontend Technologies
- **React Native 0.76+**: Latest stable version with New Architecture support for enhanced performance
- **TypeScript**: Type-safe development with full IntelliSense support
- **React Navigation v7**: Advanced navigation with stack, tab, and drawer navigators
- **Redux Toolkit**: Modern state management with feature-based slice architecture
- **React Native Paper**: Material Design component library with theming
- **React Native Elements**: Additional UI components for rich user experiences

### Backend Integration
- **RESTful API**: Comprehensive API integration with eOrdering backend services
- **Firebase Cloud Messaging**: Push notification delivery and management
- **JWT Authentication**: Secure token-based authentication with refresh mechanism
- **AsyncStorage**: Persistent local data storage for offline support

### Development Tools & Quality Assurance
- **ESLint**: Code quality and consistency enforcement
- **Jest**: Unit and integration testing framework
- **TypeScript Compiler**: Static type checking and code validation
- **Metro Bundler**: Fast, scalable JavaScript bundler
- **Git**: Version control with feature branch workflow

### Internationalization & Localization
- **i18next**: Complete i18n framework with dynamic language switching
- **Language Support**: Thai (default), English, Japanese, Lao
- **Locale Management**: Organized translation files with namespace support

### Build & Deployment
- **Xcode 16.3+**: iOS app compilation and distribution
- **Android Studio 2024.3+**: Android app building and deployment
- **Gradle**: Android build automation
- **CocoaPods**: iOS dependency management via Bundler
- **Fastlane-Ready**: Prepared for CI/CD automation

### Third-Party Integrations
- **Firebase**: Cloud Messaging, Analytics foundation
- **Vector Icons**: Comprehensive icon library support
- **QR Code Scanner**: Native QR/barcode scanning capabilities
- **Image Handling**: Optimized image loading and caching

## Common Development Commands

```bash
# Development
yarn start              # Start Metro bundler
yarn android           # Run on Android (targets emulator/device)
yarn ios              # Run on iOS simulator (iPhone 16 Pro Max)

# Code Quality
yarn lint             # Run ESLint
yarn test             # Run Jest tests

# iOS Dependencies (from ios/ directory)
cd ios && bundle install && bundle exec pod install && cd ..

# Production Builds
# Android: yarn android --variant=release
# iOS: Build through Xcode after setting Release scheme
```

## Architecture Overview

### Core Application Structure
- **Navigation**: React Navigation v7 with native stack and bottom tab navigation
- **State Management**: Redux Toolkit with feature-based slices (login, cart, products, notifications, etc.)
- **Internationalization**: i18next with Thai as default language, supporting EN/TH/JP/LA
- **UI Framework**: React Native Paper with custom theming, React Native Elements
- **Notifications**: Firebase Cloud Messaging with proper permission handling
- **Storage**: AsyncStorage for persistent data

### Key Directories
- `src/navigation/`: Navigation configuration (StackNavigator.jsx, BottomTabNavigator)
- `src/redux/`: Redux store and feature slices
- `src/screens/`: Screen components organized by feature
- `src/components/`: Reusable UI components
- `src/services/`: API service layers and HTTP clients
- `src/utils/`: Utility functions, storage, navigation helpers
- `src/config/`: API configuration and environment settings
- `src/assets/`: Images, fonts, locale files, and static data

### API Integration
- Base API: `https://uat.spbt.smart-ms2.com/api.eordering` (UAT environment)
- Notification API: `https://uat.api.notification.smart-ms2.com`
- Main services: Authentication, Products, Orders, Asset Checks, Notifications
- API configuration centralized in `src/config/apiConfig.js`

### Core Features
- **Authentication**: Login/Register with JWT tokens and refresh token mechanism
- **Product Ordering**: Category-based product browsing, cart management, checkout
- **Asset Management**: Asset check functionality with QR code scanning
- **Order Management**: Order history, tracking, and details
- **Notifications**: Firebase push notifications with local and remote handling
- **Multi-language Support**: Complete i18n implementation
- **Profile Management**: User profile editing and settings

### State Management Structure
- `loginSlice`: User authentication and session management
- `cartSlice`: Shopping cart items and checkout process
- `productsSlice`: Product catalog and category data
- `assetChecksSlice`: Asset checking functionality
- `notificationSlice`: Notification state and preferences
- `loadingSlice`: Global loading states
- `searchSlice`: Search functionality
- `appVersionSlice`: App version management

### Navigation Architecture
- Stack Navigator as root navigation
- Bottom Tab Navigator for main app sections (Home, Asset Check, My Order, Notifications, Profile)
- Deep linking support configured
- Navigation service for programmatic navigation

### Development Notes
- Uses React Native 0.76 with New Architecture support
- TypeScript configuration extends @react-native/typescript-config
- Metro bundler with standard React Native configuration
- ESLint extends @react-native configuration
- Firebase app initialization handled in App.tsx
- Permission requests for notifications handled per platform
- iOS requires iPhone 16 Pro Max simulator configuration
- Android uses standard emulator/device setup

### Environment Requirements
- Node.js v20.19.1
- Yarn v1.22.22
- Xcode 16.3+ (iOS development)
- Android Studio 2024.3+ (Android development)
- Ruby v3.4.3 (for CocoaPods via Bundler)
- Java Development Kit 17

---

## 🏷️ Keywords

`React Native`, `TypeScript`, `Redux Toolkit`, `React Navigation`, `Firebase`, `Mobile App Development`, `iOS Development`, `Android App Development`, `Cross-Platform`, `Full-Stack Development`, `RESTful API`, `API Integration`, `AsyncStorage`, `SQLite`, `Push Notifications`, `i18n`, `Internationalization`, `QR Code`, `E-Commerce`, `B2B`, `B2C`, `Mobile App Development`, `Hybrid App Development`, `JavaScript`, `Node.js`, `Git`, `GitHub`, `Redux`, `Firebase Cloud Messaging`, `JWT`