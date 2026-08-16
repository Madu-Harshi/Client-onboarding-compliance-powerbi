# Client Onboarding & Compliance — Power BI Portfolio

A Power BI portfolio project exploring client onboarding, operational performance, compliance activity, customer characteristics, risk exposure and management priorities within a synthetic banking scenario.

The project combines my previous experience in branch banking and customer-facing banking operations with my academic background in Software Engineering and Digital Transformation.

---

## Project Overview

Client onboarding involves multiple interconnected activities, including customer information collection, KYC checks, risk assessment, approval decisions, escalation and compliance review.

This project explores how Power BI can be used to transform operational data into management-oriented insights.

The scenario is synthetic and does not contain real customer, employee, transaction or employer data.

The project is informed by my previous experience in branch banking and customer-facing banking operations. Selected processes and business rules were intentionally simplified or adjusted to keep the project manageable as a portfolio project while preserving meaningful banking, onboarding and compliance concepts.

The objective was not to reproduce a specific bank's internal systems or procedures. Instead, the project demonstrates how banking domain knowledge can be combined with digital transformation and analytical skills to design a business-focused reporting solution.

---

## Business Objective

The dashboard is designed to provide visibility into:

- Overall onboarding workload
- Processing efficiency
- Pending applications and KYC workload
- Escalation levels and drivers
- Compliance review outcomes
- Customer risk exposure
- Customer and account composition
- Branch-level operational pressure
- Management priorities

The five-page dashboard follows a progression from high-level visibility to detailed analysis and finally to management-oriented action.

---

# Dashboard Structure

The portfolio contains five analytical pages:

1. Executive Overview
2. Operational Performance
3. Compliance Performance
4. Customer & Portfolio Insights
5. Management Insights & Actions

---

## 1. Executive Overview

### Subtitle

Portfolio-wide workload, efficiency, risk & escalation snapshot

### Purpose

Provide a high-level view of the overall client onboarding operation.

### Key KPIs

- Total Applications: 4,000
- Open Applications: 702
- Approval Rate: 89.1%
- Average Processing Days: 7.4
- Escalation Rate: 9.8%

### Key Visuals

- Application Volume by Branch
- Monthly Application Volume
- Application Status
- Customer Risk Profile

### Key Questions

- How much onboarding activity is being handled?
- How many applications remain open?
- What is the overall approval rate?
- How efficiently are applications being processed?
- How is workload distributed across branches?
- How does application volume change over time?
- What is the overall customer risk profile?

---

## 2. Operational Performance

### Subtitle

Processing efficiency, workload pressure & operational bottlenecks

### Purpose

Examine processing efficiency, workload pressure and operational bottlenecks within the onboarding process.

### Key KPIs

- Average Processing Days: 7.4
- Pending Applications: 702
- Pending KYC: 422
- Escalated Applications: 393

### Key Visuals

- Average Processing Days by Branch
- Escalation Volume by Branch
- Applications by Processing Time
- Application Outcomes by Risk Level
- KYC Status Distribution

### Selected Findings

Average processing time varies across the ten branches, ranging from 6.7 days to 7.4 days.

Escalation volume also varies across branches, with Jyväskylä showing the highest volume at 56 and Lappeenranta the lowest at 25.

The application outcome analysis shows a clear relationship between risk level and rejection rate:

- Low Risk: 4.6% rejection rate
- Medium Risk: 9.5% rejection rate
- High Risk: 20.8% rejection rate

KYC status is distributed across:

- Completed: 85.0%
- Pending: 10.6%
- Failed: 4.5%

### Key Questions

- Where are processing times highest?
- Which branches experience greater escalation pressure?
- How much onboarding work remains pending?
- How much KYC work is still outstanding?
- How long do applications typically take?
- How do application outcomes differ by risk level?
- What proportion of KYC cases are completed, pending or failed?

---

## 3. Compliance Performance

### Subtitle

Review outcomes, compliance workload & escalation drivers

### Purpose

Examine compliance review outcomes, workload patterns, review duration and escalation drivers.

### Key KPIs

- Compliance Reviews: 393
- Approved Reviews: 260
- Further Review: 83
- Rejected Reviews: 50
- Average Review Duration: 7.23 days

### Key Visuals

- Review Outcomes by Type
- Monthly Compliance Review Volume
- Average Review Duration by Type
- Escalation Drivers

### Review Types

- KYC
- AML
- Enhanced Due Diligence (EDD)
- Sanctions

### Selected Findings

Review outcomes vary across review types.

The dashboard shows the following approval percentages:

- KYC: 73.5%
- AML: 58.9%
- EDD: 65.6%
- Sanctions: 63.2%

Average review duration varies between:

- KYC: 7.5 days
- EDD: 7.3 days
- AML: 7.2 days
- Sanctions: 6.7 days

The leading escalation drivers shown in the dashboard are:

- EDD: 117
- KYC Docs: 84
- Risk Assessment: 81
- Compliance Review: 56
- Sanctions: 55

### Key Questions

- What are the outcomes of compliance reviews?
- How do review outcomes differ by review type?
- How does compliance workload change over time?
- Which review types take longer?
- What are the main escalation drivers?
- Where could process improvement opportunities exist?

---

## 4. Customer & Portfolio Insights

### Subtitle

Customer composition, risk exposure & portfolio characteristics

### Purpose

Understand customer composition, portfolio characteristics, branch distribution, account types and customer risk exposure.

### Key KPIs

- Total Customers: 4,000
- Individual Customers: 3,156
- Business Customers: 844
- High-Risk Customers: 562
- Average Annual Income: €143.8K

### Key Visuals

- Customer Type Mix
- Customer Age Profile
- Customers by Branch
- Customers by Account Type
- Risk Profile by Customer Type

### Selected Findings

The customer portfolio consists of:

- Individual Customers: 78.9%
- Business Customers: 21.1%

Customers are distributed across ten branches, with Tampere Central having the highest customer count at 347 and Vaasa the lowest at 292.

Account types are distributed as:

- Savings: 1,737
- Current: 1,172
- Premium: 575
- Business: 516

The dashboard also compares risk exposure between business and individual customers and provides an age-group profile across the customer portfolio.

### Key Questions

- What is the customer mix?
- How large is the individual versus business customer population?
- How are customers distributed across branches?
- Which account types are most common?
- What does the customer age profile look like?
- How does risk exposure differ between customer types?
- What are the main characteristics of the customer portfolio?

---

## 5. Management Insights & Actions

### Subtitle

Operational risks, pressure points & management priorities

### Purpose

Translate the findings from the previous analytical pages into management-oriented priorities.

### Key KPIs

- Average Processing Days: 7.4
- Open Applications: 702
- High-Risk Customers: 562
- Rejection Rate: 9.0%
- Escalation Rate: 9.8%

### Key Visuals

- Application Outcomes by Risk Level
- Priority Escalation Areas
- Management Attention by Branch
- Management Priorities

### Priority Escalation Areas

The dashboard focuses on the three leading escalation areas:

1. EDD — 117
2. KYC Docs — 84
3. Risk Assessment — 81

This focuses management attention on the largest escalation sources rather than presenting all escalation categories equally.

### Application Outcomes by Risk Level

The dashboard highlights a clear difference in outcomes by risk level:

- Low Risk: 79.7% approved, 15.7% pending, 4.6% rejected
- Medium Risk: 72.3% approved, 18.2% pending, 9.5% rejected
- High Risk: 57.8% approved, 21.4% pending, 20.8% rejected

The high-risk segment therefore has the lowest approval rate and highest rejection rate.

### Management Attention by Branch

Branches are classified according to average processing days and escalation rate.

The dashboard identifies:

High attention:

- Espoo
- Helsinki Central
- Jyväskylä

Medium attention:

- Kuopio
- Lahti
- Lappeenranta
- Oulu

Normal attention:

- Tampere Central
- Turku Central
- Vaasa

### Management Priorities

The dashboard highlights three broad management priorities:

1. Focus on high-risk applications

   The high-risk segment has the lowest approval rate and highest rejection rate, indicating an area requiring closer operational and compliance attention.

2. Target the main escalation sources

   EDD, KYC documentation and risk assessment are the leading escalation areas and therefore represent potential process-improvement opportunities.

3. Prioritize high-attention branches

   Branches classified as High should be reviewed for operational improvement, particularly in relation to processing time and escalation rates.

### Key Questions

- Which risk segment requires the greatest attention?
- What are the leading escalation areas?
- Which branches require management attention?
- Where should process improvement efforts be focused?
- How can operational data support management decisions?

---

# Dataset

The project uses a synthetic dataset consisting of five related CSV tables:

- Branches.csv
- Relationship_Managers.csv
- Customer_Master.csv
- Client_Onboarding.csv
- Compliance_Reviews.csv

The dataset generation script defines:

- 4,000 customers
- 10 branches
- 21 relationship managers
- 4,000 onboarding applications
- Application dates covering 2025
- Controlled customer types
- Controlled account types
- Risk levels
- KYC statuses
- Approval statuses
- Escalation reasons
- Compliance review types
- Compliance review outcomes

---

# Data Model

The project uses a relational structure rather than a single flat dataset.

The main entities are:

Branches

Relationship Managers

Customer Master

Client Onboarding

Compliance Reviews

The tables are connected through identifiers such as:

- Branch_ID
- RM_ID
- Customer_ID
- Application_ID

This structure allows the dashboard to analyse relationships between branches, customers, onboarding activity and compliance reviews.

---

# Synthetic Data Generation

The dataset was generated programmatically using Python.

The generator uses:

- Python
- pandas
- NumPy
- Randomised data generation
- Controlled business rules
- Validation checks
- Reproducible random seed

A fixed seed is used so that the generated dataset can be reproduced consistently.

The generator creates the five CSV tables and includes validation checks before export.

Examples of validation include:

- Unique identifiers
- Valid branch relationships
- Valid relationship-manager relationships
- Valid customer/application relationships
- Escalated applications linked to compliance reviews
- KYC status and approval-status consistency
- Cross-table relationship consistency
- Business-customer risk constraints

The generator is included in the repository to make the synthetic dataset transparent and reproducible.

---

# Business Logic

The scenario uses simplified banking and compliance business rules.

The overall concept is:

Application received

→ KYC processing

→ Application decision

→ Escalation where required

→ Compliance review

→ Final outcome

Risk level is also incorporated into the scenario so that higher-risk customers receive greater compliance attention.

For example, the dataset generator explicitly validates that:

- KYC-pending applications have a Pending approval status
- KYC-failed applications have a Rejected approval status
- Escalated applications have corresponding compliance review records
- Business customers are not assigned Low Risk

These rules are intentionally simplified for portfolio purposes.

They should not be interpreted as representing the exact procedures, policies or systems of any particular bank.

---

# Power BI Analysis

The dashboard demonstrates the use of Power BI for business-oriented analysis and storytelling.

Key capabilities demonstrated include:

- Data modelling
- Table relationships
- DAX measures
- KPI development
- Interactive filtering
- Data visualisation
- Dashboard layout
- Customer segmentation
- Risk analysis
- Operational analysis
- Compliance analysis
- Management reporting
- Business storytelling

The project focuses on starting with business questions and using data to support analysis and management decisions.

---

# Key Insights Demonstrated

The dashboard demonstrates several analytical patterns within the synthetic scenario.

### Operational

- 4,000 onboarding applications are analysed.
- 702 applications remain open.
- Average processing time is 7.4 days.
- Processing time varies across branches.
- Escalation volume varies across branches.
- 422 applications have pending KYC status.

### Risk

- High-risk applications have a 20.8% rejection rate.
- Medium-risk applications have a 9.5% rejection rate.
- Low-risk applications have a 4.6% rejection rate.
- High-risk applications have the lowest approval rate.
- High-risk customers account for 562 customers in the portfolio.

### Compliance

- 393 compliance reviews are analysed.
- 260 reviews are approved.
- 83 reviews result in Further Review.
- 50 reviews are rejected.
- Average review duration is 7.23 days.
- EDD, KYC documentation and risk assessment are the leading escalation areas.

### Customer Portfolio

- 4,000 customers are analysed.
- 78.9% are individual customers.
- 21.1% are business customers.
- Savings is the largest account category.
- Customer distribution varies across branches.
- Customer risk exposure differs between business and individual customers.

All figures are generated from synthetic data and are intended to demonstrate analytical reasoning rather than represent real banking performance.

---

# Skills Demonstrated

## Banking & Business Domain

- Branch banking operations
- Client onboarding
- Customer-facing banking operations
- KYC / AML concepts
- Compliance processes
- Risk assessment
- Customer segmentation
- Operational performance analysis
- Management reporting
- Process improvement thinking

## Digital & Analytical

- Power BI
- DAX
- Data modelling
- KPI design
- Data visualisation
- Dashboard design
- Business storytelling
- Synthetic data modelling
- Python-based dataset generation
- Data validation

## Digital Transformation Perspective

The project demonstrates how existing banking domain knowledge can be translated into a data-driven management solution.

Rather than treating the project purely as a technical dashboard exercise, the analysis starts from business questions and operational problems, then uses data modelling, measures and visualisation to support decision-making.

---

# Portfolio Context

This project forms part of my broader professional portfolio.

My background combines:

- More than a decade of banking operations experience
- Branch banking and customer-facing experience
- Experience with banking operations and compliance-related activities
- Operational coordination and reporting
- A Master's degree in Software Engineering & Digital Transformation

This project represents one way I am building on that foundation by applying digital and analytical approaches to banking-related business problems.

The portfolio is intended to demonstrate not only technical tool usage, but also the ability to understand a business context, structure information, identify relevant questions and communicate insights to decision-makers.

---
## Repository Contents

```text
Client-onboarding-compliance-powerbi/

├── README.md

├── dashboard/
│   └── Client_Onboarding_Compliance_Dashboard.pdf

├── dataset/
│   ├── Branches.csv
│   ├── Relationship_Managers.csv
│   ├── Customer_Master.csv
│   ├── Client_Onboarding.csv
│   └── Compliance_Reviews.csv

└── data_generation/
    └── powerbi_dataset_generator.py

---

# Disclaimer

This project is entirely for educational and portfolio purposes.

All customer, employee, branch, application and compliance data are synthetic.

The project does not use confidential customer information, proprietary banking data or internal employer systems.

The scenario is informed by banking domain knowledge, but selected processes, data structures and business rules have been simplified or adjusted for portfolio scope.

The dashboard should therefore not be interpreted as a representation of any specific bank's actual processes, policies, performance or systems.

---

# Project Outcome

The project demonstrates how banking domain knowledge, digital transformation thinking and Power BI can be combined to create a management-oriented analytical solution.

The focus is not only on building visualisations, but on moving from:

Visibility → Analysis → Insight → Management Action
