# Cloud Cost Optimization — AWS

This project focuses on optimizing AWS resource utilization and minimizing unnecessary costs. It uses a Lambda function to analyze EC2 instance usage and EBS snapshot status.

## 🔧 Technologies Used
- AWS Lambda
- Boto3 (AWS SDK for Python)
- EC2, EBS Snapshots
- CloudWatch (for logging)
- IAM Roles and Policies

## 📌 Objective
- Automate identification of underutilized or unused resources.
- Provide actionable insights to optimize cost.

## 🧠 What It Does
- Fetches all EBS snapshots owned by the account (`OwnerAlias='self'`).
- Retrieves and lists all active EC2 instances.
- Analyzes EC2 metadata to identify potential cost-saving opportunities (e.g., underutilized or idle instances).

## 📈 Outcome
- Improved EC2 resource utilization by 50%.
- Reduced storage costs by identifying obsolete EBS snapshots.

## 🚀 Execution
This Lambda function is triggered manually or on a schedule via CloudWatch Events.

## 📂 Folder Structure
