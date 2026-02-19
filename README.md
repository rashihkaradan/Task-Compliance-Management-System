<<<<<<< HEAD

# Internal Operations Task & Compliance Management System

A custom Frappe application developed as a final internship project to manage internal organizational tasks with approval workflow, SLA monitoring, execution tracking, and compliance reporting.

---

## 📌 Project Overview

This system manages the full lifecycle of internal operational tasks within an organization.
It enforces Maker–Checker approvals, tracks execution work logs, monitors SLA deadlines, and provides compliance reporting and dashboards.

The solution is implemented as a custom Frappe app named **status**.

---

## 🚀 Key Features

* Internal Task creation and tracking
* Maker–Checker approval workflow
* Role-based access control
* Execution work log tracking
* SLA due date calculation
* Automatic SLA breach detection
* System notifications
* Compliance reports
* Task dashboard

---

## 👥 User Roles

### Requester (Maker)

* Create and edit tasks in Draft/Rejected
* Submit tasks for approval
* View task progress
* Cannot approve or execute

### Reviewer (Checker)

* Review submitted tasks
* Approve or reject tasks
* Add rejection remarks
* Cannot modify task content

### Executor (Operations Team)

* View approved tasks
* Log work execution
* Update execution status
* Cannot approve/reject

### Compliance Manager

* View tasks and audit data
* Monitor SLA breaches
* Read-only access

### System Administrator

* Full system configuration
* Roles, workflow, permissions

---

## 🔄 Workflow Lifecycle

Draft → Pending Review → Approved → In Execution → Completed → Closed
↘ Rejected ↗

---

## 🧱 DocTypes

### Internal Task (Parent)

Stores task details, SLA dates, status, assignment, and approval data.

### Task Work Log (Child)

Stores execution logs including:

* Executor
* Start/End time
* Duration
* Work description

---

## ⏱ SLA Management

SLA due date is calculated automatically based on priority:

| Priority | SLA      |
| -------- | -------- |
| Critical | Same day |
| High     | +1 day   |
| Medium   | +3 days  |
| Low      | +5 days  |

SLA breach is flagged automatically when overdue.

---

## 📊 Reports

The system provides the following reports:

* Task Status Summary
* Tasks by Department
* Tasks by Executor
* SLA Breached Tasks

---

## 📈 Dashboard

Workspace: **Task Compliance Dashboard**

Charts included:

* Tasks by Status
* Tasks by Department
* Tasks by Executor
* SLA Breached Tasks

---

## 🔔 Notifications

Automatic alerts are sent for:

* Task pending review
* Task approval
* Task rejection
* SLA breach

---

## 🛠 Installation

1. Get app:

```
bench get-app status <repo_url>
```

2. Install on site:

```
bench --site yoursite install-app status
```

3. Run migrations:

```
bench migrate
bench restart
```

---

## ▶️ Usage

1. Create users and assign roles
2. Create Internal Task
3. Submit for review
4. Reviewer approves/rejects
5. Executor logs work
6. Task completes and closes

---

## 📚 Technologies Used

* Frappe Framework v15
* ERPNext v15
* Python
* MariaDB

---

## 📄 License

This project was developed for internship evaluation purposes.

---

## 👨‍💻 Author

**Rashih Karadan**
Frappe Developer Intern

=======
>>>>>>>

