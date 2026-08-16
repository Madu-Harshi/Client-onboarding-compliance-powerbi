# Client Onboarding & Compliance — Power BI Portfolio

A Power BI portfolio project exploring client onboarding, operational performance, compliance activity, customer characteristics, risk exposure and management priorities within a synthetic banking scenario.

The project combines my previous experience in branch banking and customer-facing banking operations with my academic background in Software Engineering and Digital Transformation.

---

## Project Overview

Client onboarding involves multiple interconnected activities, including customer information collection, KYC checks, risk assessment, approval decisions, escalation and compliance review.

This project was created to explore how Power BI can transform operational data into management-oriented insights.

The scenario is **synthetic** and does not contain real customer, employee, transaction or employer data.

It is informed by my previous experience in branch banking and customer-facing banking operations. Selected processes and business rules were intentionally simplified or adjusted to keep the project manageable as a portfolio project while preserving meaningful banking, onboarding and compliance concepts.

The goal was not to reproduce a real bank's internal systems or processes, but to demonstrate how domain knowledge can be combined with data analysis and digital transformation skills to build a useful management dashboard.

---

## Business Objective

The dashboard is designed to help management understand:

- Overall onboarding workload
- Processing efficiency
- Pending applications and KYC workload
- Escalation levels and drivers
- Compliance review outcomes
- Customer risk exposure
- Customer and account composition
- Branch-level operational pressure
- Areas requiring management attention

The dashboard moves from high-level operational visibility to detailed analysis and finally to management-oriented actions.

---

# Dashboard Structure

The portfolio contains five analytical pages.

---

## 1. Executive Overview

### Purpose

Provide a portfolio-wide snapshot of onboarding workload, efficiency, risk and escalation.

### Key KPIs

- Total Applications
- Open Applications
- Approval Rate
- Average Processing Days
- Escalation Rate

### Key Visuals

- Application Volume by Branch
- Monthly Application Volume
- Application Status
- Customer Risk Profile

### Questions Answered

- How much onboarding activity is being handled?
- How many applications remain open?
- What is the overall approval rate?
- How efficiently are applications being processed?
- How is workload distributed across branches?
- How is application volume changing over time?
- What is the overall customer risk profile?

---

## 2. Operational Performance

### Purpose

Analyse processing efficiency, workload pressure and operational bottlenecks.

### Key KPIs

- Average Processing Days
- Pending Applications
- Pending KYC
- Escalated Applications

### Key Visuals

- Average Processing Days by Branch
- Escalation Volume by Branch
- Applications by Processing Time
- Application Outcomes by Risk Level
- KYC Status Distribution

### Questions Answered

- Where are processing times highest?
- Which branches experience greater operational pressure?
- How much onboarding work remains pending?
- How much KYC work is still outstanding?
- How long do applications typically take?
- Does customer risk level affect application outcomes?
- What proportion of applications are approved, pending or rejected?

---

## 3. Compliance Performance

### Purpose

Examine compliance review outcomes, workload and escalation drivers.

### Key KPIs

- Compliance Reviews
- Approved Reviews
- Further Review
- Rejected Reviews
- Average Review Duration

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

### Questions Answered

- What are the outcomes of compliance reviews?
- Which review types have different outcome patterns?
- How does compliance workload change over time?
- Which review types take longer?
- What are the main drivers of escalations?
- Where could compliance process improvement have the greatest impact?

---

## 4. Customer & Portfolio Insights

### Purpose

Understand customer composition, portfolio characteristics and risk exposure.

### Key KPIs

- Total Customers
- Individual Customers
- Business Customers
- High-Risk Customers
- Average Annual Income

### Key Visuals

- Customer Type Mix
- Customer Age Profile
- Customers by Branch
- Customers by Account Type
- Risk Profile by Customer Type

### Questions Answered

- What is the customer mix?
- How large is the individual versus business customer population?
- How are customers distributed across branches?
- Which account types are most common?
- What does the customer age profile look like?
- How does risk exposure differ between customer types?
- What is the overall customer portfolio profile?

---

## 5. Management Insights & Actions

### Purpose

Translate operational and compliance analysis into management priorities.

### Key KPIs

- Average Processing Days
- Open Applications
- High-Risk Customers
- Escalation Rate
- Rejection Rate

### Key Visuals

- Application Outcomes by Risk Level
- Priority Escalation Areas
- Management Attention by Branch
- Management Priorities

### Management Priorities

The analysis highlights three broad areas for management attention:

1. **Focus on high-risk applications**

   The high-risk segment has the lowest approval rate and highest rejection rate, indicating a need for closer review and process attention.

2. **Target the main escalation sources**

   Enhanced Due Diligence (EDD), KYC documentation and risk assessment are the leading escalation drivers and therefore represent potential process-improvement opportunities.

3. **Prioritize high-attention branches**

   Branches classified as having high management attention can be reviewed for operational improvement, particularly where processing time and escalation rates are elevated.

### Questions Answered

- Which customer segments create the greatest operational or compliance concern?
- What are the main escalation areas?
- Which branches require management attention?
- Where should process improvement efforts be focused?
- How can operational data support management decisions?

---

# Dataset

The project uses a synthetic dataset containing five related tables:

```text
dataset/
│
├── Branches.csv
├── Relationship_Managers.csv
├── Customer_Master.csv
├── Client_Onboarding.csv
└── Compliance_Reviews.csv
