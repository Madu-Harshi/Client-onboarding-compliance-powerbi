# ============================================================
# POWER BI CLIENT ONBOARDING & COMPLIANCE DATASET GENERATOR
# ============================================================
#
# Generates five CSV tables:
#   1. Branches
#   2. Relationship_Managers
#   3. Customer_Master
#   4. Client_Onboarding
#   5. Compliance_Reviews
#
# Business rules are validated before export.
# ============================================================

import os
import random
from datetime import date, timedelta

import numpy as np
import pandas as pd


# ============================================================
# 1. REPRODUCIBILITY
# ============================================================

SEED = 42
random.seed(SEED)
np.random.seed(SEED)


# ============================================================
# 2. OUTPUT LOCATION
# ============================================================

OUTPUT_DIR = "dataset"
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ============================================================
# 3. DATASET SETTINGS
# ============================================================

NUMBER_OF_CUSTOMERS = 4000
NUMBER_OF_BRANCHES = 10
NUMBER_OF_RMS = 21
NUMBER_OF_APPLICATIONS = NUMBER_OF_CUSTOMERS

APPLICATION_START_DATE = date(2025, 1, 1)
APPLICATION_END_DATE = date(2025, 12, 31)


# ============================================================
# 4. BUSINESS RULE SETTINGS
# ============================================================

INDIVIDUAL_SHARE = 0.80
BUSINESS_SHARE = 0.20


# ============================================================
# 5. CONTROLLED VALUES
# ============================================================

CUSTOMER_TYPES = [
    "Individual",
    "Business",
]

ACCOUNT_TYPES = [
    "Savings",
    "Current",
    "Premium",
    "Business",
]

RISK_LEVELS = [
    "Low",
    "Medium",
    "High",
]

KYC_STATUSES = [
    "Completed",
    "Pending",
    "Failed",
]

APPROVAL_STATUSES = [
    "Approved",
    "Pending",
    "Rejected",
]

ESCALATION_REASONS = [
    "Enhanced Due Diligence",
    "KYC Documentation",
    "Sanctions Screening",
    "Risk Assessment",
    "Compliance Review",
]

REVIEW_TYPES = [
    "KYC",
    "AML",
    "Enhanced Due Diligence",
    "Sanctions Screening",
]

COMPLIANCE_OUTCOMES = [
    "Approved",
    "Further Review",
    "Rejected",
]


# ============================================================
# 6. NAME POOLS
# ============================================================

FIRST_NAMES = [
    "Anna", "Mikko", "Laura", "Janne", "Emma",
    "Antti", "Sanna", "Markus", "Maria", "Ville",
    "Aino", "Juho", "Emilia", "Olli", "Sara",
    "Matti", "Kaisa", "Elias", "Sofia", "Aleksi",
]

LAST_NAMES = [
    "Korhonen", "Virtanen", "Mäkinen", "Nieminen",
    "Hämäläinen", "Laine", "Heikkinen", "Koskinen",
    "Järvinen", "Lehtonen", "Salminen", "Heinonen",
    "Kallio", "Rantanen", "Saarinen",
]

REVIEWER_NAMES = [
    "Laura Nieminen",
    "Mikko Korhonen",
    "Sanna Virtanen",
    "Antti Laine",
    "Maria Heikkinen",
    "Janne Koskinen",
]


# ============================================================
# 7. HELPER FUNCTIONS
# ============================================================

def weighted_choice(options, weights):
    return random.choices(options, weights=weights, k=1)[0]


def random_date(start_date, end_date):
    days_between = (end_date - start_date).days
    return start_date + timedelta(
        days=random.randint(0, days_between)
    )


def generate_id(prefix, number, width):
    return f"{prefix}{number:0{width}d}"


# ============================================================
# 8. BRANCHES
# ============================================================

def generate_branches():

    branches = [
        {
            "Branch_ID": "B001",
            "Branch_Name": "Helsinki Central",
            "Region": "Uusimaa",
            "Branch_Type": "Metropolitan",
            "Annual_Capacity": 950,
        },
        {
            "Branch_ID": "B002",
            "Branch_Name": "Espoo",
            "Region": "Uusimaa",
            "Branch_Type": "Metropolitan",
            "Annual_Capacity": 850,
        },
        {
            "Branch_ID": "B003",
            "Branch_Name": "Tampere Central",
            "Region": "Pirkanmaa",
            "Branch_Type": "Regional",
            "Annual_Capacity": 800,
        },
        {
            "Branch_ID": "B004",
            "Branch_Name": "Turku Central",
            "Region": "Southwest Finland",
            "Branch_Type": "Regional",
            "Annual_Capacity": 750,
        },
        {
            "Branch_ID": "B005",
            "Branch_Name": "Oulu",
            "Region": "North Ostrobothnia",
            "Branch_Type": "Regional",
            "Annual_Capacity": 700,
        },
        {
            "Branch_ID": "B006",
            "Branch_Name": "Jyväskylä",
            "Region": "Central Finland",
            "Branch_Type": "Regional",
            "Annual_Capacity": 600,
        },
        {
            "Branch_ID": "B007",
            "Branch_Name": "Lahti",
            "Region": "Päijät-Häme",
            "Branch_Type": "Regional",
            "Annual_Capacity": 550,
        },
        {
            "Branch_ID": "B008",
            "Branch_Name": "Kuopio",
            "Region": "North Savo",
            "Branch_Type": "Regional",
            "Annual_Capacity": 500,
        },
        {
            "Branch_ID": "B009",
            "Branch_Name": "Lappeenranta",
            "Region": "South Karelia",
            "Branch_Type": "Local",
            "Annual_Capacity": 450,
        },
        {
            "Branch_ID": "B010",
            "Branch_Name": "Vaasa",
            "Region": "Ostrobothnia",
            "Branch_Type": "Local",
            "Annual_Capacity": 450,
        },
    ]

    df = pd.DataFrame(branches)

    assert len(df) == NUMBER_OF_BRANCHES
    assert df["Branch_ID"].is_unique

    return df


# ============================================================
# 9. RELATIONSHIP MANAGERS
# ============================================================

def generate_relationship_managers(branches):

    rm_distribution = {
        "B001": 3,
        "B002": 2,
        "B003": 2,
        "B004": 2,
        "B005": 2,
        "B006": 2,
        "B007": 2,
        "B008": 2,
        "B009": 2,
        "B010": 2,
    }

    rm_records = []
    rm_number = 1

    for branch_id, number_of_rms in rm_distribution.items():

        for _ in range(number_of_rms):

            first_name = random.choice(FIRST_NAMES)
            last_name = random.choice(LAST_NAMES)

            experience = random.randint(2, 18)

            base_capacity = 120 + (experience * 5)

            capacity = random.randint(
                max(100, base_capacity - 20),
                base_capacity + 30
            )

            rm_records.append(
                {
                    "RM_ID": generate_id("RM", rm_number, 3),
                    "RM_Name": f"{first_name} {last_name}",
                    "Branch_ID": branch_id,
                    "Experience_Years": experience,
                    "Capacity": capacity,
                    "Status": "Active",
                }
            )

            rm_number += 1

    df = pd.DataFrame(rm_records)

    assert len(df) == NUMBER_OF_RMS
    assert df["RM_ID"].is_unique
    assert set(df["Branch_ID"]).issubset(
        set(branches["Branch_ID"])
    )
    assert (df["Status"] == "Active").all()

    return df


# ============================================================
# 10. CUSTOMER MASTER
# ============================================================

def generate_customer_master(branches, relationship_managers):

    customer_records = []

    for customer_number in range(
        1,
        NUMBER_OF_CUSTOMERS + 1
    ):

        # ----------------------------------------------------
        # CUSTOMER TYPE
        # ----------------------------------------------------

        customer_type = weighted_choice(
            ["Individual", "Business"],
            [INDIVIDUAL_SHARE, BUSINESS_SHARE]
        )

        # ----------------------------------------------------
        # AGE AND INCOME
        # ----------------------------------------------------

        if customer_type == "Individual":

            age = random.randint(18, 75)

            income_band = weighted_choice(
                ["Low", "Medium", "High", "Very High"],
                [0.25, 0.45, 0.25, 0.05]
            )

            if income_band == "Low":
                annual_income = random.randint(
                    18000, 39999
                )

            elif income_band == "Medium":
                annual_income = random.randint(
                    40000, 79999
                )

            elif income_band == "High":
                annual_income = random.randint(
                    80000, 119999
                )

            else:
                annual_income = random.randint(
                    120000, 180000
                )

        else:

            age = None

            income_band = weighted_choice(
                ["Small", "Medium", "Large", "Very Large"],
                [0.30, 0.40, 0.23, 0.07]
            )

            if income_band == "Small":
                annual_income = random.randint(
                    40000, 99999
                )

            elif income_band == "Medium":
                annual_income = random.randint(
                    100000, 299999
                )

            elif income_band == "Large":
                annual_income = random.randint(
                    300000, 999999
                )

            else:
                annual_income = random.randint(
                    1000000, 5000000
                )

        # ----------------------------------------------------
        # ACCOUNT TYPE
        #
        # Business customers may have Business, Current or
        # Premium accounts. Individual customers may have
        # Savings, Current or Premium accounts.
        # ----------------------------------------------------

        if customer_type == "Individual":

            account_type = weighted_choice(
                ["Savings", "Current", "Premium"],
                [0.55, 0.30, 0.15]
            )

        else:

            account_type = weighted_choice(
                ["Business", "Current", "Premium"],
                [0.60, 0.30, 0.10]
            )

        # ----------------------------------------------------
        # RISK LEVEL
        #
        # Business customers are NEVER Low Risk.
        #
        # Individual risk is influenced by income but is not
        # determined solely by income.
        # ----------------------------------------------------

        if customer_type == "Individual":

            if annual_income < 40000:

                risk = weighted_choice(
                    ["Low", "Medium", "High"],
                    [0.75, 0.23, 0.02]
                )

            elif annual_income < 80000:

                risk = weighted_choice(
                    ["Low", "Medium", "High"],
                    [0.55, 0.38, 0.07]
                )

            elif annual_income < 120000:

                risk = weighted_choice(
                    ["Low", "Medium", "High"],
                    [0.40, 0.45, 0.15]
                )

            else:

                risk = weighted_choice(
                    ["Low", "Medium", "High"],
                    [0.30, 0.50, 0.20]
                )

        else:

            # Business = Medium or High only.
            risk = weighted_choice(
                ["Medium", "High"],
                [0.65, 0.35]
            )

        # ----------------------------------------------------
        # BRANCH
        # ----------------------------------------------------

        branch_id = random.choice(
            branches["Branch_ID"].tolist()
        )

        # ----------------------------------------------------
        # RELATIONSHIP MANAGER
        # ----------------------------------------------------

        branch_rms = relationship_managers[
            relationship_managers["Branch_ID"] == branch_id
        ]

        rm = branch_rms.sample(
            n=1,
            random_state=random.randint(1, 100000)
        ).iloc[0]

        rm_id = rm["RM_ID"]

        customer_records.append(
            {
                "Customer_ID": generate_id(
                    "C",
                    customer_number,
                    5
                ),
                "Customer_Type": customer_type,
                "Age": age,
                "Annual_Income": annual_income,
                "Account_Type": account_type,
                "Risk_Level": risk,
                "Branch_ID": branch_id,
                "RM_ID": rm_id,
            }
        )

    df = pd.DataFrame(customer_records)

    # --------------------------------------------------------
    # VALIDATION
    # --------------------------------------------------------

    assert len(df) == NUMBER_OF_CUSTOMERS
    assert df["Customer_ID"].is_unique

    assert set(df["Customer_Type"]).issubset(
        set(CUSTOMER_TYPES)
    )

    assert set(df["Risk_Level"]).issubset(
        set(RISK_LEVELS)
    )

    assert set(df["Branch_ID"]).issubset(
        set(branches["Branch_ID"])
    )

    assert set(df["RM_ID"]).issubset(
        set(relationship_managers["RM_ID"])
    )

    # Business customers must never be Low Risk.
    business_customers = df[
        df["Customer_Type"] == "Business"
    ]

    assert (
        business_customers["Risk_Level"]
        .isin(["Medium", "High"])
        .all()
    )

    assert not (
        business_customers["Risk_Level"] == "Low"
    ).any()

    business_age_check = df.loc[
        df["Customer_Type"] == "Business",
        "Age"
    ]

    assert business_age_check.isna().all()

    individual_age_check = df.loc[
        df["Customer_Type"] == "Individual",
        "Age"
    ]

    assert individual_age_check.notna().all()

    rm_branch_lookup = relationship_managers.set_index(
        "RM_ID"
    )["Branch_ID"]

    customer_rm_branches = df["RM_ID"].map(
        rm_branch_lookup
    )

    assert (
        customer_rm_branches.values
        == df["Branch_ID"].values
    ).all()

    return df


# ============================================================
# 11. CLIENT ONBOARDING
# ============================================================

def generate_client_onboarding(customer_master):

    application_records = []

    for application_number, (_, customer) in enumerate(
        customer_master.iterrows(),
        start=1
    ):

        application_id = generate_id(
            "APP",
            application_number,
            5
        )

        customer_id = customer["Customer_ID"]

        application_date = random_date(
            APPLICATION_START_DATE,
            APPLICATION_END_DATE
        )

        customer_type = customer["Customer_Type"]
        risk_level = customer["Risk_Level"]
        account_type = customer["Account_Type"]

        # ----------------------------------------------------
        # KYC
        # ----------------------------------------------------

        if risk_level == "High":
            kyc_weights = [0.82, 0.10, 0.08]

        elif risk_level == "Medium":
            kyc_weights = [0.84, 0.11, 0.05]

        else:
            kyc_weights = [0.86, 0.11, 0.03]

        kyc_status = weighted_choice(
            KYC_STATUSES,
            kyc_weights
        )

        approval_status = "Pending"
        escalation = "No"
        escalation_reason = None
        processing_days = None

        # ----------------------------------------------------
        # KYC FAILED
        # ----------------------------------------------------

        if kyc_status == "Failed":

            approval_status = "Rejected"
            escalation = "No"
            processing_days = random.randint(2, 7)

        # ----------------------------------------------------
        # KYC PENDING
        # ----------------------------------------------------

        elif kyc_status == "Pending":

            approval_status = "Pending"
            escalation = "No"
            processing_days = random.randint(1, 20)

        # ----------------------------------------------------
        # KYC COMPLETED
        # ----------------------------------------------------

        else:

            escalation_probability = 0.05

            if risk_level == "High":
                escalation_probability += 0.15

            elif risk_level == "Medium":
                escalation_probability += 0.05

            if customer_type == "Business":
                escalation_probability += 0.05

            if account_type == "Premium":
                escalation_probability += 0.03

            escalation_probability = min(
                escalation_probability,
                0.40
            )

            escalation = (
                "Yes"
                if random.random() < escalation_probability
                else "No"
            )

            # ------------------------------------------------
            # ESCALATED
            # ------------------------------------------------

            if escalation == "Yes":

                escalation_reason = weighted_choice(
                    ESCALATION_REASONS,
                    [0.30, 0.20, 0.15, 0.20, 0.15]
                )

                # Escalated cases go to Compliance Review.
                approval_status = "Pending"
                processing_days = random.randint(5, 20)

            # ------------------------------------------------
            # NOT ESCALATED
            # ------------------------------------------------

            else:

                escalation_reason = None

                if risk_level == "High":

                    approval_status = weighted_choice(
                        ["Approved", "Pending", "Rejected"],
                        [0.75, 0.10, 0.15]
                    )

                elif risk_level == "Medium":

                    approval_status = weighted_choice(
                        ["Approved", "Pending", "Rejected"],
                        [0.88, 0.08, 0.04]
                    )

                else:

                    approval_status = weighted_choice(
                        ["Approved", "Pending", "Rejected"],
                        [0.93, 0.05, 0.02]
                    )

                if approval_status == "Approved":
                    processing_days = random.randint(2, 10)

                elif approval_status == "Rejected":
                    processing_days = random.randint(2, 8)

                else:
                    processing_days = random.randint(5, 20)

        application_records.append(
            {
                "Application_ID": application_id,
                "Customer_ID": customer_id,
                "Application_Date": application_date,
                "Branch_ID": customer["Branch_ID"],
                "RM_ID": customer["RM_ID"],
                "Account_Type": account_type,
                "Customer_Type": customer_type,
                "Risk_Level": risk_level,
                "KYC_Status": kyc_status,
                "Approval_Status": approval_status,
                "Processing_Days": processing_days,
                "Escalation": escalation,
                "Escalation_Reason": escalation_reason,
            }
        )

    df = pd.DataFrame(application_records)

    # --------------------------------------------------------
    # VALIDATION
    # --------------------------------------------------------

    assert len(df) == NUMBER_OF_APPLICATIONS
    assert df["Application_ID"].is_unique
    assert df["Customer_ID"].is_unique

    assert set(df["Customer_ID"]).issubset(
        set(customer_master["Customer_ID"])
    )

    customer_lookup = customer_master.set_index("Customer_ID")

    assert (
        df["Branch_ID"].values
        == df["Customer_ID"].map(
            customer_lookup["Branch_ID"]
        ).values
    ).all()

    assert (
        df["RM_ID"].values
        == df["Customer_ID"].map(
            customer_lookup["RM_ID"]
        ).values
    ).all()

    assert (
        df["Account_Type"].values
        == df["Customer_ID"].map(
            customer_lookup["Account_Type"]
        ).values
    ).all()

    assert (
        df["Risk_Level"].values
        == df["Customer_ID"].map(
            customer_lookup["Risk_Level"]
        ).values
    ).all()

    kyc_pending = df[
        df["KYC_Status"] == "Pending"
    ]

    assert (
        kyc_pending["Approval_Status"] == "Pending"
    ).all()

    kyc_failed = df[
        df["KYC_Status"] == "Failed"
    ]

    assert (
        kyc_failed["Approval_Status"] == "Rejected"
    ).all()

    not_escalated = df[
        df["Escalation"] == "No"
    ]

    assert (
        not_escalated["Escalation_Reason"].isna()
    ).all()

    escalated = df[
        df["Escalation"] == "Yes"
    ]

    assert (
        escalated["Escalation_Reason"].notna()
    ).all()

    not_completed_kyc = df[
        df["KYC_Status"] != "Completed"
    ]

    assert (
        not_completed_kyc["Escalation"] == "No"
    ).all()

    assert (
        df["Application_Date"] >=
        APPLICATION_START_DATE
    ).all()

    assert (
        df["Application_Date"] <=
        APPLICATION_END_DATE
    ).all()

    return df


# ============================================================
# 12. COMPLIANCE REVIEWS
# ============================================================

def generate_compliance_reviews(
    client_onboarding,
    customer_master
):

    escalated_applications = client_onboarding[
        client_onboarding["Escalation"] == "Yes"
    ].copy()

    customer_risk_lookup = (
        customer_master
        .set_index("Customer_ID")["Risk_Level"]
    )

    review_records = []

    for review_number, (_, application) in enumerate(
        escalated_applications.iterrows(),
        start=1
    ):

        application_id = application["Application_ID"]
        customer_id = application["Customer_ID"]
        application_date = application["Application_Date"]

        risk_level = customer_risk_lookup.loc[
            customer_id
        ]

        review_date = (
            application_date
            + timedelta(days=random.randint(1, 7))
        )

        reviewer = random.choice(REVIEWER_NAMES)

        review_type = weighted_choice(
            REVIEW_TYPES,
            [0.30, 0.25, 0.25, 0.20]
        )

        if risk_level == "High":
            review_duration = random.randint(5, 15)

        elif risk_level == "Medium":
            review_duration = random.randint(3, 10)

        else:
            review_duration = random.randint(2, 7)

        if risk_level == "High":

            outcome = weighted_choice(
                COMPLIANCE_OUTCOMES,
                [0.55, 0.25, 0.20]
            )

        elif risk_level == "Medium":

            outcome = weighted_choice(
                COMPLIANCE_OUTCOMES,
                [0.70, 0.20, 0.10]
            )

        else:

            outcome = weighted_choice(
                COMPLIANCE_OUTCOMES,
                [0.80, 0.15, 0.05]
            )

        if outcome == "Approved":

            review_notes = (
                "Compliance review completed successfully."
            )

        elif outcome == "Further Review":

            review_notes = (
                "Additional documentation or review required."
            )

        else:

            review_notes = (
                "Compliance concerns identified during review."
            )

        review_records.append(
            {
                "Review_ID": generate_id(
                    "REV",
                    review_number,
                    5
                ),
                "Application_ID": application_id,
                "Customer_ID": customer_id,
                "Review_Date": review_date,
                "Reviewer": reviewer,
                "Review_Type": review_type,
                "Outcome": outcome,
                "Review_Duration_Days": review_duration,
                "Review_Notes": review_notes,
            }
        )

    df = pd.DataFrame(review_records)

    if df.empty:
        df = pd.DataFrame(
            columns=[
                "Review_ID",
                "Application_ID",
                "Customer_ID",
                "Review_Date",
                "Reviewer",
                "Review_Type",
                "Outcome",
                "Review_Duration_Days",
                "Review_Notes",
            ]
        )

    assert len(df) == len(escalated_applications)

    if len(df) > 0:

        assert df["Review_ID"].is_unique
        assert df["Application_ID"].is_unique

        assert set(
            df["Application_ID"]
        ) == set(
            escalated_applications["Application_ID"]
        )

        assert set(
            df["Customer_ID"]
        ).issubset(
            set(customer_master["Customer_ID"])
        )

        application_dates = (
            client_onboarding
            .set_index("Application_ID")["Application_Date"]
        )

        review_application_dates = (
            df["Application_ID"]
            .map(application_dates)
        )

        assert (
            df["Review_Date"].values
            > review_application_dates.values
        ).all()

        assert (
            df["Review_Duration_Days"] > 0
        ).all()

    return df


# ============================================================
# 13. APPLY COMPLIANCE OUTCOMES
# ============================================================

def apply_compliance_outcomes(
    client_onboarding,
    compliance_reviews
):

    outcome_to_status = {
        "Approved": "Approved",
        "Further Review": "Pending",
        "Rejected": "Rejected",
    }

    for _, review in compliance_reviews.iterrows():

        application_id = review["Application_ID"]
        outcome = review["Outcome"]

        final_status = outcome_to_status[outcome]

        client_onboarding.loc[
            client_onboarding["Application_ID"]
            == application_id,
            "Approval_Status"
        ] = final_status

    return client_onboarding


# ============================================================
# 14. FINAL CROSS-TABLE VALIDATION
# ============================================================

def validate_final_dataset(
    branches,
    relationship_managers,
    customer_master,
    client_onboarding,
    compliance_reviews
):

    assert len(branches) == NUMBER_OF_BRANCHES
    assert len(relationship_managers) == NUMBER_OF_RMS
    assert len(customer_master) == NUMBER_OF_CUSTOMERS
    assert len(client_onboarding) == NUMBER_OF_APPLICATIONS

    assert branches["Branch_ID"].is_unique
    assert relationship_managers["RM_ID"].is_unique
    assert customer_master["Customer_ID"].is_unique
    assert client_onboarding["Application_ID"].is_unique

    assert set(
        relationship_managers["Branch_ID"]
    ).issubset(
        set(branches["Branch_ID"])
    )

    assert set(
        customer_master["Branch_ID"]
    ).issubset(
        set(branches["Branch_ID"])
    )

    assert set(
        customer_master["RM_ID"]
    ).issubset(
        set(relationship_managers["RM_ID"])
    )

    assert set(
        client_onboarding["Customer_ID"]
    ).issubset(
        set(customer_master["Customer_ID"])
    )

    assert set(
        client_onboarding["Branch_ID"]
    ).issubset(
        set(branches["Branch_ID"])
    )

    assert set(
        client_onboarding["RM_ID"]
    ).issubset(
        set(relationship_managers["RM_ID"])
    )

    escalated_ids = set(
        client_onboarding.loc[
            client_onboarding["Escalation"] == "Yes",
            "Application_ID"
        ]
    )

    review_ids = set(
        compliance_reviews["Application_ID"]
    )

    assert escalated_ids == review_ids

    if len(compliance_reviews) > 0:

        assert compliance_reviews["Review_ID"].is_unique
        assert compliance_reviews["Application_ID"].is_unique

        assert set(
            compliance_reviews["Customer_ID"]
        ).issubset(
            set(customer_master["Customer_ID"])
        )

    # Business customers must never be Low Risk.
    business_customers = customer_master[
        customer_master["Customer_Type"] == "Business"
    ]

    assert not (
        business_customers["Risk_Level"] == "Low"
    ).any()

    # KYC business rules.
    kyc_pending = client_onboarding[
        client_onboarding["KYC_Status"] == "Pending"
    ]

    assert (
        kyc_pending["Approval_Status"] == "Pending"
    ).all()

    kyc_failed = client_onboarding[
        client_onboarding["KYC_Status"] == "Failed"
    ]

    assert (
        kyc_failed["Approval_Status"] == "Rejected"
    ).all()

    print("ALL CROSS-TABLE BUSINESS RULES PASSED.")


# ============================================================
# 15. EXPORT
# ============================================================

def export_tables(
    branches,
    relationship_managers,
    customer_master,
    client_onboarding,
    compliance_reviews
):

    branches.to_csv(
        os.path.join(
            OUTPUT_DIR,
            "Branches.csv"
        ),
        index=False
    )

    relationship_managers.to_csv(
        os.path.join(
            OUTPUT_DIR,
            "Relationship_Managers.csv"
        ),
        index=False
    )

    customer_master.to_csv(
        os.path.join(
            OUTPUT_DIR,
            "Customer_Master.csv"
        ),
        index=False
    )

    client_onboarding.to_csv(
        os.path.join(
            OUTPUT_DIR,
            "Client_Onboarding.csv"
        ),
        index=False
    )

    compliance_reviews.to_csv(
        os.path.join(
            OUTPUT_DIR,
            "Compliance_Reviews.csv"
        ),
        index=False
    )


# ============================================================
# 16. SUMMARY
# ============================================================

def print_summary(
    branches,
    relationship_managers,
    customer_master,
    client_onboarding,
    compliance_reviews
):

    print()
    print("=" * 60)
    print("POWER BI DATASET GENERATOR")
    print("=" * 60)

    print()
    print("DATASET COUNTS")
    print("-" * 60)
    print(f"Branches:              {len(branches)}")
    print(f"Relationship Managers: {len(relationship_managers)}")
    print(f"Customers:             {len(customer_master)}")
    print(f"Applications:          {len(client_onboarding)}")
    print(f"Compliance Reviews:    {len(compliance_reviews)}")

    print()
    print("CUSTOMER TYPE DISTRIBUTION")
    print("-" * 60)
    print(
        customer_master["Customer_Type"]
        .value_counts()
        .to_string()
    )

    print()
    print("RISK DISTRIBUTION")
    print("-" * 60)
    print(
        customer_master["Risk_Level"]
        .value_counts()
        .to_string()
    )

    print()
    print("CUSTOMER TYPE x RISK")
    print("-" * 60)
    print(
        pd.crosstab(
            customer_master["Customer_Type"],
            customer_master["Risk_Level"],
            normalize="index"
        )
        .mul(100)
        .round(1)
        .to_string()
    )

    print()
    print("ACCOUNT TYPE x CUSTOMER TYPE")
    print("-" * 60)
    print(
        pd.crosstab(
            customer_master["Customer_Type"],
            customer_master["Account_Type"],
            normalize="index"
        )
        .mul(100)
        .round(1)
        .to_string()
    )

    print()
    print("KYC STATUS DISTRIBUTION")
    print("-" * 60)
    print(
        client_onboarding["KYC_Status"]
        .value_counts()
        .to_string()
    )

    print()
    print("FINAL APPROVAL STATUS DISTRIBUTION")
    print("-" * 60)

    approval_counts = (
        client_onboarding["Approval_Status"]
        .value_counts()
    )

    approval_percentages = (
        client_onboarding["Approval_Status"]
        .value_counts(normalize=True)
        .mul(100)
        .round(1)
    )

    for status in APPROVAL_STATUSES:

        print(
            f"{status}: "
            f"{approval_counts.get(status, 0)} "
            f"({approval_percentages.get(status, 0)}%)"
        )

    print()
    print("ESCALATION DISTRIBUTION")
    print("-" * 60)
    print(
        client_onboarding["Escalation"]
        .value_counts()
        .to_string()
    )

    print()
    print("COMPLIANCE REVIEW OUTCOMES")
    print("-" * 60)

    if len(compliance_reviews) > 0:

        print(
            compliance_reviews["Outcome"]
            .value_counts()
            .to_string()
        )

    else:

        print("No compliance reviews generated.")

    print()
    print("ESCALATED APPLICATIONS AFTER REVIEW")
    print("-" * 60)

    escalated_final = client_onboarding[
        client_onboarding["Escalation"] == "Yes"
    ]

    print(
        escalated_final["Approval_Status"]
        .value_counts()
        .to_string()
    )

    print()
    print("APPLICATION SAMPLE")
    print("-" * 60)

    print(
        client_onboarding.head(10).to_string(
            index=False
        )
    )

    print()
    print("COMPLIANCE REVIEW SAMPLE")
    print("-" * 60)

    if len(compliance_reviews) > 0:

        print(
            compliance_reviews.head(10).to_string(
                index=False
            )
        )

    print()
    print("FILES CREATED")
    print("-" * 60)

    for filename in [
        "Branches.csv",
        "Relationship_Managers.csv",
        "Customer_Master.csv",
        "Client_Onboarding.csv",
        "Compliance_Reviews.csv",
    ]:

        print(
            os.path.join(
                OUTPUT_DIR,
                filename
            )
        )

    print()
    print("=" * 60)
    print("FULL PROCESS TEST COMPLETE")
    print("=" * 60)


# ============================================================
# 17. MAIN
# ============================================================

def main():

    branches = generate_branches()

    relationship_managers = (
        generate_relationship_managers(branches)
    )

    customer_master = generate_customer_master(
        branches,
        relationship_managers
    )

    client_onboarding = generate_client_onboarding(
        customer_master
    )

    compliance_reviews = generate_compliance_reviews(
        client_onboarding,
        customer_master
    )

    client_onboarding = apply_compliance_outcomes(
        client_onboarding,
        compliance_reviews
    )

    validate_final_dataset(
        branches,
        relationship_managers,
        customer_master,
        client_onboarding,
        compliance_reviews
    )

    export_tables(
        branches,
        relationship_managers,
        customer_master,
        client_onboarding,
        compliance_reviews
    )

    print_summary(
        branches,
        relationship_managers,
        customer_master,
        client_onboarding,
        compliance_reviews
    )


if __name__ == "__main__":
    main()
