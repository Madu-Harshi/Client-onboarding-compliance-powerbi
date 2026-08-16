# Client Onboarding & Compliance Operations Dashboard

A Power BI portfolio project exploring client onboarding, customer segmentation, compliance risk, operational performance, and management priorities in a synthetic banking environment.

The project combines my previous experience in branch banking and customer-facing banking operations with my academic background in Software Engineering and Digital Transformation.

---

## Project Overview

Client onboarding is a critical banking process where customer experience, operational efficiency, KYC requirements, compliance controls, and risk management intersect.

This project uses Power BI to transform a synthetic banking dataset into an interactive management dashboard designed to answer operational and business questions across the client onboarding lifecycle.

The scenario is intentionally simplified for portfolio and learning purposes. It is not based on confidential, proprietary, or real customer data, and it does not attempt to reproduce a specific bank's actual processes.

The project was designed to demonstrate how banking-domain knowledge can be combined with data visualization, business analysis, and digital transformation skills to turn operational data into actionable insights.

---

## Business Context

The dashboard is designed around a simplified client onboarding and compliance operation involving:

- Customer onboarding applications
- Branch operations
- Relationship managers
- Customer segmentation
- KYC status
- Risk classification
- Application outcomes
- Processing times
- Escalations
- Compliance reviews
- Management attention areas

The analysis focuses on three perspectives:

1. **Operational performance** — What is happening across the onboarding process?
2. **Customer & portfolio characteristics** — Who are the customers and what is their risk profile?
3. **Management action** — Where should management focus attention and improvement efforts?

---

## Business Questions

The dashboard was designed to answer questions such as:

### Operational Performance

- How many applications are being handled?
- How many applications remain open?
- What is the overall approval rate?
- How long does onboarding take on average?
- Which branches handle the highest application volumes?
- How does application volume change over time?
- Where are operational pressure points emerging?

### Customer & Portfolio

- What is the composition of the customer base?
- What proportion of customers are individuals versus businesses?
- What is the customer risk profile?
- How does risk differ between customer types?
- What are the main account types?
- How is the customer base distributed across age groups and branches?

### Compliance & Risk

- How do application outcomes differ by risk level?
- Which risk segment has the highest rejection rate?
- How frequently are applications escalated?
- What are the main escalation drivers?
- What are the outcomes of compliance reviews?
- Which branches require greater management attention?

### Management Action

- Where should management focus first?
- Which escalation areas should be addressed?
- Which branches show higher operational pressure?
- Which customer segments require closer attention?
- What process areas could benefit from improvement?

---

## Dashboard Structure

The final dashboard is organized into four analytical perspectives.

### 1. Executive Overview

Provides a portfolio-wide operational snapshot.

Key elements include:

- Total Applications
- Approval Rate
- Average Processing Days
- Escalation Rate
- Open Applications
- Application Volume by Branch
- Monthly Application Volume
- Application Status
- Customer Risk Profile

This page is designed as an executive-level overview where the most important operational indicators can be understood quickly.

### 2. Customer & Portfolio Insights

Focuses on customer composition, risk exposure, and portfolio characteristics.

Key elements include:

- Total Customers
- Individual Customers
- Business Customers
- High-Risk Customers
- Average Annual Income
- Customers by Branch
- Customer Type Mix
- Risk Profile by Customer Type
- Customer Age Profile
- Customers by Account Type

This page moves from operational workload toward understanding the customer population behind the onboarding activity.

### 3. Compliance Performance

Examines compliance review workload and outcomes.

Key elements include:

- Compliance Reviews
- Approved Reviews
- Further Review
- Rejected Reviews
- Average Review Duration
- Review Outcomes by Type
- Monthly Compliance Review Volume
- Average Review Duration by Type
- Escalation Drivers

The objective is to understand where compliance workload is concentrated and which areas contribute to additional review or escalation.

### 4. Management Insights & Action

Translates operational and compliance findings into management-oriented priorities.

Key elements include:

- Open Applications
- High-Risk Customers
- Rejection Rate
- Average Processing Days
- Escalation Rate
- Application Outcomes by Risk Level
- Priority Escalation Areas
- Management Attention by Branch
- Management Priorities

The page is designed to move beyond reporting and highlight areas where management attention may be appropriate.

---

## Key Insights Demonstrated

The dashboard highlights several patterns within the synthetic dataset.

### Risk and Application Outcomes

Higher-risk applications show weaker outcomes compared with lower-risk applications.

In the final dashboard:

- Low-risk applications: 79.7% approved and 4.6% rejected
- Medium-risk applications: 72.3% approved and 9.5% rejected
- High-risk applications: 57.8% approved and 20.8% rejected

This demonstrates how segmentation can be used to identify areas requiring closer operational and compliance attention.

### Escalation Drivers

The leading escalation areas in the final dashboard are:

1. Enhanced Due Diligence (EDD)
2. KYC Documentation
3. Risk Assessment

These areas provide potential starting points for process improvement and workload analysis.

### Branch Management Attention

Branches are evaluated using operational indicators including:

- Average Processing Days
- Escalation Rate
- Management Attention

The dashboard uses these indicators to identify branches requiring higher, medium, or normal management attention.

---

## Dataset

The project uses a synthetic dataset generated specifically for this portfolio project.

The dataset contains five related tables:

- `Branches`
- `Relationship_Managers`
- `Customer_Master`
- `Client_Onboarding`
- `Compliance_Reviews`

The dataset contains 4,000 customers and 4,000 onboarding applications across 10 branches and 21 relationship managers.

No real customer, employee, or confidential banking data is used.

---

## Dataset Generation

The dataset was generated programmatically using Python, NumPy, and pandas.

A fixed random seed is used to make the generation reproducible.

The generator creates:

- 4,000 customers
- 10 branches
- 21 relationship managers
- 4,000 onboarding applications

The generated data uses controlled categories for customer type, account type, risk level, KYC status, approval status, escalation reasons, review types, and compliance outcomes.

Business rules are also validated before the final CSV files are exported.

The generator is included in the repository so that the dataset creation process can be inspected and reproduced.

---

## Data Model

The Power BI model connects the main entities through identifiers such as:

    Branches
        │
        ├── Relationship Managers
        │
        └── Customers
               │
               └── Client Onboarding
                       │
                       └── Compliance Reviews

The model was designed to allow operational, customer, and compliance information to be analyzed together while maintaining relationships between the underlying entities.

---

## Power BI Analysis

The dashboard was developed using Power BI.

Key techniques used include:

- Data modelling
- Relationships between tables
- DAX measures
- Calculated columns
- KPI cards
- Bar charts
- Stacked bar charts
- Donut charts
- Tables
- Conditional formatting
- Interactive filtering
- Sorting and categorization
- Dashboard layout design
- Business-oriented data storytelling

The emphasis was not only on creating charts, but on deciding which information is useful for a particular business audience and how it should be presented.

---

## Business-Oriented Design Approach

A major objective of this project was to avoid treating Power BI as simply a chart-building tool.

Each dashboard page was designed around a different decision-making perspective:

    Executive Overview
            ↓
    What is happening?

    Customer & Portfolio
            ↓
    Who and what are we dealing with?

    Compliance Performance
            ↓
    Where are compliance workloads and risks?

    Management Insights & Action
            ↓
    Where should attention be focused?

This approach reflects my interest in connecting operational knowledge with digital and data-driven decision-making.

---

## Why I Built This Project

My professional background includes more than a decade of experience in banking operations and branch-level customer-facing work.

My Master's studies in Software Engineering and Digital Transformation expanded this perspective toward technology, digitalization, data, and process improvement.

I created this project to explore how these areas can work together.

Rather than presenting banking experience and digital skills as separate areas, this portfolio project demonstrates how domain knowledge can help frame meaningful business questions while digital tools can be used to analyze and communicate the results.

---

## What This Project Demonstrates

This project demonstrates my ability to:

- Understand banking operational processes
- Translate business situations into analytical questions
- Structure a multi-table business dataset
- Build a Power BI data model
- Create meaningful KPIs and measures
- Analyze customer and operational segments
- Identify risk and compliance patterns
- Design management-oriented dashboards
- Present information for different audiences
- Connect data analysis with business decision-making
- Apply digital transformation concepts to an operational context

---

## Limitations & Scope

This project is a portfolio and learning exercise.

The data is synthetic and should not be interpreted as representing an actual financial institution, actual customers, or real operational performance.

The banking environment and processes have been intentionally simplified to focus on demonstrating data modelling, visualization, business analysis, and management-oriented reporting.

The project therefore demonstrates a method and analytical approach rather than a production banking solution.

---

## Data Privacy

No real customer or confidential banking data is used in this project.

All customer, branch, relationship manager, application, and compliance information is synthetic.

The dataset was created specifically for portfolio development and demonstration purposes.

---

## Repository Structure

    Client-onboarding-compliance-powerbi/
    │
    ├── dashboard/
    │   └── Client_Onboarding_Compliance_Dashboard.pdf
    │
    ├── dataset/
    │   ├── Branches.csv
    │   ├── Relationship_Managers.csv
    │   ├── Customer_Master.csv
    │   ├── Client_Onboarding.csv
    │   └── Compliance_Reviews.csv
    │
    ├── data_generation/
    │   └── powerbi_dataset_generator_FINAL.py
    │
    └── README.md

---

## Project Files

### Dashboard PDF

`dashboard/Client_Onboarding_Compliance_Dashboard.pdf`

Contains the final exported dashboard for viewing without Power BI Desktop.

### Dataset

The `dataset/` folder contains the synthetic CSV tables used for the Power BI model.

### Python Dataset Generator

`data_generation/powerbi_dataset_generator_FINAL.py`

Contains the Python logic used to generate the synthetic dataset and validate key business rules before exporting the CSV files.

---

## Tools Used

- Microsoft Power BI
- Python
- pandas
- NumPy
- GitHub

---

## Skills Demonstrated

### Banking & Business

- Branch banking operations
- Customer onboarding
- KYC and compliance concepts
- Risk awareness
- Operational performance analysis
- Customer segmentation
- Management reporting
- Process improvement thinking

### Digital & Analytical

- Power BI
- Data modelling
- DAX
- Data visualization
- KPI development
- Business intelligence
- Data storytelling
- Synthetic data generation
- Business-rule validation

### Communication

- Executive-oriented dashboard design
- Translating data into business questions
- Communicating operational findings
- Presenting management priorities

---

## Future Improvements

Possible future extensions include:

- Additional onboarding funnel analysis
- More detailed compliance workload analysis
- Trend comparisons across periods
- Branch-level drill-through analysis
- Relationship manager performance analysis
- Additional customer segmentation
- Scenario-based operational analysis
- Automated data refresh workflows
- Further Power BI interactivity

---

## Author

**Madusha Harshani**

MSc in Software Engineering & Digital Transformation

Background in banking operations and branch-level customer service.

Interested in the intersection of:

**Banking Operations · Business Analysis · Digital Transformation · Data & Business Intelligence**

---

## Note

This repository is part of my growing professional portfolio.

The purpose of the project is to demonstrate how existing domain experience can be combined with newly developed digital and analytical capabilities to approach business problems from both an operational and technology-enabled perspective.
