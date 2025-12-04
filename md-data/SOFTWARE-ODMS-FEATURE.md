# ODMS Pro - Order & Delivery Management System

> **🚀 Full Stack Web Application | Enterprise EDI Platform**

---

## 🏷️ Project Classification

| Category | Details |
|----------|---------|
| **Project Type** | ✅ **Full Stack Web Application** - ASP.NET Core MVC with Entity Framework |
| **Architecture** | ✅ **Enterprise Solution** - Multi-retailer EDI processing pipelines |
| **Databases** | SQL Server with comprehensive schema |
| **Integrations** | 8 major Thai retailers (7-Eleven, Makro, BigC, etc.) |

---

## Executive Summary

ODMS is an enterprise-grade web application designed to streamline order management and proof-of-delivery operations for suppliers working with major Thai retail chains. The system serves as a centralized hub for processing Electronic Data Interchange (EDI) documents, managing delivery workflows, and maintaining comprehensive records across multiple retail partners.

Built with ASP.NET Core and Entity Framework, ODMS addresses the complexities of multi-retailer operations by providing dedicated processing pipelines for each partner while maintaining a unified user experience. The platform currently supports eight major retailers including 7-Eleven, Makro, BigC, CP Retail, The Mall, MaxValue, Tops, and Villa Market.

---

## Software Objectives

The primary objectives driving ODMS development reflect real-world challenges faced by suppliers in the fast-moving consumer goods industry:

**Operational Efficiency**: Replace manual EDI file processing with automated workflows that reduce human error and processing time. What previously took hours of manual data entry now happens in minutes with built-in validation and error reporting.

**Multi-Partner Complexity Management**: Each retail chain has unique EDI formats, business rules, and approval workflows. ODMS abstracts these differences behind a consistent interface while maintaining the flexibility needed for partner-specific requirements.

**Delivery Visibility**: Track the entire delivery lifecycle from order creation through proof of delivery, with supporting documentation and status updates accessible to all stakeholders.

**Data Integrity**: Maintain accurate master data mappings between supplier product codes and retailer-specific codes, ensuring orders flow smoothly without translation errors.

**Audit Compliance**: Preserve complete transaction histories with approval chains, status changes, and document archives to support both internal audits and retailer requirements.

---

## Technical Architecture

### Tech Stack Overview

**Runtime & Framework**
- .NET Core 3.1 (ASP.NET Core MVC)
- Entity Framework Core 3.1 with SQL Server
- Session-based authentication with role management

**Data Processing**
- CsvHelper for CSV/TSV parsing
- NPOI for Excel report generation
- EFCore.BulkExtensions for high-performance bulk operations

**Frontend**
- Razor Views with server-side rendering
- jQuery DataTables with server-side processing
- Bootstrap for responsive UI

**Integration**
- RESTful APIs with CORS support for E-Ordering integration
- File-based EDI import/export with configurable FTP paths
- SMTP email notifications for approval workflows

### Solution Structure

The codebase is organized into logical service layers:

**EDIService** - Core domain layer containing all entity models, database contexts, and repository interfaces for POD and EDI operations. This includes partner-specific customer and material mapping tables, EDI document models, and business enumerations.

**EOrderingService** - Separate domain layer for e-commerce integration, maintaining order, product, and customer entities synchronized with external ordering platforms.

**LogFilesService** - Centralized logging utilities for tracking import/export operations and troubleshooting data issues.

**sis.pod.website** - Main ASP.NET Core web application containing controllers, views, services, and configuration. This is the user-facing layer where all business workflows are orchestrated.

---

## Core Features & Capabilities

### 1. Proof of Delivery Management

The POD module handles the complete delivery lifecycle from SAP integration through final delivery confirmation:

**Delivery Import**: Accept tab-delimited delivery files containing order details, billing information, and shipping data. The system validates against master data and flags discrepancies before committing to the database.

**Document Attachment**: Users can attach multiple supporting documents (delivery receipts, photos, signatures) to each delivery order, creating a complete digital paper trail.

**Status Tracking**: Monitor delivery status through predefined stages (Open, Delivered, Rejected) with reason codes explaining any exceptions or partial deliveries.

**Delivery Reporting**: Generate Excel reports with customizable filters showing delivery performance, outstanding orders, and achievement metrics by customer or time period.

### 2. Multi-Retailer EDI Processing

Each retail partner has a dedicated processing pipeline, but common functionality includes:

**EDI File Import**: Parse partner-specific text or CSV files containing purchase orders. The system maps retailer product codes to SAP material codes, validates customer information, and calculates pricing and totals.

**Intelligent Validation**: Cross-reference imported data against customer master files and material mappings. Any discrepancies generate detailed error logs highlighting missing mappings or invalid data.

**Edit PO Workflow**: After initial import, users can upload edited purchase orders (typically CSV format) to update quantities, delivery dates, or add promotional items. The system replaces existing PO data while maintaining audit history.

**Export Capabilities**: Generate retailer-specific export files in required formats (text files, Excel spreadsheets) ready for upload to partner systems or SAP integration.

**Error Management**: When imports fail validation, the system generates downloadable error reports showing exactly which rows failed and why, enabling quick corrections.

### 3. Partner-Specific Implementations

While sharing common architecture, each retailer integration has unique characteristics:

**7-Eleven (Primary Partner)**: Handles high-volume fixed-format text files with complex product hierarchies. Supports FOC (free of charge) items, reference PO updates, and warehouse quantity tracking.

**Makro**: Processes tab-delimited files with emphasis on bulk order quantities and distribution center routing.

**BigC**: Manages multiple vendor codes with special handling for LINDT2 supplier segment, including separate data tables for tracking.

**CP Retail**: Integrates purchase orders across CP All's convenience store network with branch-level granularity.

**Agent (E-Ordering)**: The most sophisticated workflow featuring multi-level approval chains. Orders flow through two approval stages with email notifications at each step. Approvers receive links to review orders and can approve, reject, or request modifications. The system maintains a complete approval audit trail.

**Tops, Villa, MaxValue, The Mall**: Each has dedicated import parsers, customer/material mappings, and export formats matching retailer specifications.

### 4. Inventory Management

**Stock Closing Balance Import**: Bulk import of stock levels across multiple warehouses and plants. The system uses EF Core bulk operations to efficiently replace thousands of records, ensuring current stock visibility.

**Plant-Based Organization**: Stock data is segmented by plant and location codes, allowing different supplier organizations (like TG and GFT subsidiaries) to maintain independent inventory views.

### 5. Master Data Management

Maintaining accurate master data is critical for EDI operations:

**Customer Master**: Store retailer-specific customer codes, branch information, SAP mappings, and approval email addresses. Separate tables for each retail partner accommodate their unique customer structures.

**Material Mapping**: Cross-reference tables linking supplier SAP material codes to retailer product codes. Each partner has dedicated mapping tables because the same product may have different codes at different retailers.

**User-Customer Mapping**: Associate system users with specific customer codes, enabling sales representatives to see only their assigned accounts.

### 6. Approval Workflow Engine

The Agent EDI workflow demonstrates the system's approval capabilities:

**Multi-Level Approvals**: Orders meeting minimum quantity thresholds trigger two-tier approval. Level 1 approvers review and forward to Level 2, who provide final authorization.

**Email Notifications**: At each approval stage, the system sends email notifications with embedded approval links. Recipients can approve/reject directly from email without logging in.

**Status Transitions**: The workflow enforces valid status transitions (Pending → Approval_1 → Approval_2 or rejection at any stage), preventing out-of-sequence approvals.

**Transaction History**: Every approval action is logged in the Transaction_Approved table, capturing who acted, when, what decision was made, and who was notified.

### 7. Role-Based Access Control

Simple but effective role segmentation:

**TG Group**: Users see data filtered to TG sales organization (1001/0 plant), supplier code 72668.

**GFT Group**: Users see data filtered to GFT sales organization (1005 plant), supplier code 73160.

**Admin**: Full visibility across all organizations without filtering.

Session variables maintain user context throughout their workflow, ensuring data isolation.

### 8. Dashboard & Analytics

**Real-Time Metrics**: Dashboard shows current open orders, delivered orders, total POs, and achievement percentage calculated as (delivered / total) * 100.

**Multi-Source Aggregation**: Combines statistics from multiple EDI sources (7-Eleven, Makro, etc.) and delivery orders for comprehensive visibility.

**Role-Specific Views**: Metrics automatically filter based on user's sales organization, showing only relevant data.

### 9. API Integration

**E-Ordering API**: RESTful endpoints enable external e-commerce platforms to submit orders programmatically. CORS policies allow specific origins to call APIs securely.

**Order Import Endpoint**: Accepts order IDs from E-Ordering system, retrieves order details, maps products, and creates EDI Agent records ready for approval workflow.

**Data Synchronization**: Maintains linkage between E-Ordering order IDs and internal EDI records for traceability.

---

## Key Highlights & Differentiators

**Partner-Specific Customization at Scale**: Rather than forcing retailers into a one-size-fits-all model, ODMS embraces their unique requirements while sharing common infrastructure. This reduces integration friction and speeds up onboarding of new retail partners.

**Built for High-Volume Operations**: Bulk insert/delete capabilities handle thousands of records efficiently. The 7-Eleven integration regularly processes files with hundreds of SKUs across multiple POs without performance degradation.

**Fail-Safe Import with Detailed Diagnostics**: When EDI imports encounter errors, the system doesn't just fail—it generates Excel error reports showing exactly which products lack mappings, which customers aren't found, and what data is malformed. This accelerates issue resolution from days to hours.

**Email-Driven Approvals**: Approvers don't need to log in daily to check for pending orders. They receive emails with action links, review order details, and approve/reject in one click. This dramatically improves approval cycle time.

**Comprehensive Audit Trails**: Every import, export, approval, and status change is logged. If a retailer questions an order six months later, complete history is readily available.

**Dual Database Architecture**: Separating POD/EDI operations from E-Ordering data provides clean boundaries and allows independent scaling/optimization of each domain.

**Configurable File Paths**: Different environments (UAT, production) and different partners can use different FTP directories without code changes—just configuration updates.

---

## Use Case Scenarios

**Daily EDI Processing**: Each morning, the operations team downloads EDI files from retailer FTP sites. They log into ODMS, navigate to the appropriate retailer controller (e.g., Edi7Eleven), and upload the file. Within seconds, the system validates data, creates purchase orders, and shows success/error counts. Error reports are downloaded, issues are corrected in master data, and files are re-imported. Clean POs are then exported in SAP-compatible format for fulfillment processing.

**Delivery Confirmation**: Drivers complete deliveries and submit signed receipts. Back-office staff log into ODMS, navigate to Upload File → Import Delivery, and upload the delivery data file. They attach scanned receipts to the corresponding delivery orders. Retailers can now see delivery status and supporting documents on demand.

**Approval Workflow**: A large order comes through E-Ordering integration. The system detects it exceeds approval thresholds and sets status to Pending. The first approver receives an email, clicks the link, reviews quantities and delivery dates, and clicks Approve. The second approver immediately receives their notification, reviews, and approves. The order status changes to Approval_2, triggering fulfillment. All actions are logged with timestamps and approver names.

**Stock Reconciliation**: Weekly, the warehouse team exports current stock positions from their WMS. They upload the tab-delimited file via the Stock Import function. ODMS deletes the previous week's balances and bulk-inserts the new data. Sales teams can now see current available-to-promise quantities when planning orders.

**Material Mapping Maintenance**: A new product launches across all retail partners. The master data team adds the SAP material code and maps it to each retailer's specific product code in the appropriate Material_Mapping tables. When EDI files arrive referencing those retailer codes, ODMS automatically translates to SAP codes for fulfillment.

---

## Business Benefits

**Reduced Order Processing Time**: What previously required manual data entry into SAP now happens automatically, freeing staff to focus on exceptions rather than routine data entry.

**Improved Order Accuracy**: Automated validation against master data catches errors before they reach fulfillment, reducing costly delivery mistakes.

**Enhanced Retailer Relationships**: Faster order processing, better delivery visibility, and comprehensive documentation strengthen partner confidence.

**Scalability for Growth**: Adding new retail partners follows established patterns—create customer/material mappings, configure file paths, add dedicated repository. The architecture supports organic growth.

**Compliance & Traceability**: Complete audit trails satisfy both internal controls and external compliance requirements (tax audits, retailer reconciliations).

**Operational Visibility**: Managers see real-time dashboard metrics showing order volumes, delivery performance, and bottlenecks across all channels.

---

## Future Enhancement Opportunities

While ODMS already delivers substantial value, several areas offer potential for further development:

**Runtime Modernization**: Upgrading from .NET Core 3.1 (which reached end-of-life) to .NET 6+ or .NET 8 would provide performance improvements, enhanced security, and access to latest framework features.

**Automated Scheduling**: Implementing background jobs for scheduled EDI file pickup, processing, and archiving would reduce manual intervention.

**Advanced Analytics**: Building power BI dashboards with historical trending, forecasting, and exception alerting would provide deeper business insights.

**Mobile Interface**: A responsive mobile app would allow field sales teams to check order status and delivery teams to update delivery status on the go.

**API Expansion**: Exposing more functionality via APIs would enable integration with additional systems (CRM, planning tools, customer portals).

**Machine Learning**: Pattern recognition for predicting approval outcomes, detecting anomalous orders, or forecasting demand could add predictive capabilities.

---

## Conclusion

ODMS represents a mature, production-proven solution addressing real operational challenges in multi-retailer order management. The system successfully balances the need for standardization with the reality of partner-specific requirements, providing a reliable foundation for high-volume EDI processing.

The architecture demonstrates thoughtful separation of concerns, with clear domain boundaries and reusable components. While built on established technologies (ASP.NET Core, Entity Framework, SQL Server), the implementation shows attention to performance, data integrity, and user experience.

For suppliers managing relationships with multiple Thai retail chains, ODMS eliminates much of the manual effort and error-prone processes inherent in EDI operations. The system has proven its value through sustained production use, processing thousands of orders daily while maintaining data accuracy and audit compliance.

---

**Document Version**: 1.0  
**Last Updated**: December 2025  
**System Version**: 1.0.4  
**Technology Foundation**: .NET Core 3.1, ASP.NET Core MVC, Entity Framework Core, SQL Server

---

## 🏷️ Keywords

`ASP.NET`, `ASP.NET MVC`, `.NET Core`, `Entity Framework`, `Microsoft SQL Server`, `C#`, `Full-Stack Development`, `Web Application`, `RESTful API`, `API Development`, `API Integration`, `jQuery DataTables`, `Bootstrap`, `NPOI`, `CsvHelper`, `SMTP`, `EDI Processing`, `Order Management`, `Proof of Delivery`, `Multi-Retailer`, `Database Management`, `Database Architecture`, `HTML5`, `CSS`, `JavaScript`, `Git`, `GitHub`, `Supply Chain`, `Retail Integration`, `B2B`, `Enterprise Solution`
