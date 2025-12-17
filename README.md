# MedSimply

MedSimply is a healthcare medication management system built to support safe, timely, and accountable medication administration. The platform is designed for clinical and caregiving environments where medications must be tracked, scheduled, administered, and audited by authorized staff.

The project is structured as a modular Django application, with each app handling a distinct responsibility in the medication workflow.

---

## Core Applications

### 1. scheduling_app

Manages medication schedules and administration events.

* Creates medication schedules for patients
* Assigns schedules to specific health workers
* Tracks scheduled time vs actual time given
* Ensures only the assigned health worker can mark medication as given
* Logs administration status for accountability
* Integrates with notifications (SMS reminders and alerts)

### 2. medication_inventory_app

Handles medication stock and availability.

* Stores medication details
* Tracks quantities and stock levels
* Supports updates when medication is dispensed
* Helps prevent scheduling medications that are out of stock
* Provides a foundation for inventory auditing

### 3. patient_staff_app

Manages patients and healthcare staff information.

* Stores patient records
* Stores health worker/staff records
* Manages assignments between patients and health workers
* Acts as the core reference app for other modules

---

## Key Features

* Medication scheduling and administration tracking
* Role-based accountability for health workers
* Medication inventory management
* Patient and staff management
* SMS notifications and reminders
* Audit-friendly logs and history

---

## System Workflow 

1. Medications are added to the inventory
2. Patients and health workers are registered
3. Medication schedules are created and assigned
4. Health workers administer medication at scheduled times
5. Administration actions are logged and audited
6. Notifications are sent when required

---

## Tech Stack

* Python
* Django
* Django REST Framework
* MySql / MongoDB
* SMS Integration (Africa’s Talking)
