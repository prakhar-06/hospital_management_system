# 🏥 Hospital Management System

A console-based Hospital Management System built in **Python** with a **MySQL** backend. This project simulates real-world hospital operations — patient registration, doctor management, and appointment scheduling — with role-based access for Admins, Doctors, and Patients.

This is my first complete Python project after 6 months of learning, built to apply core concepts of databases, CRUD operations, and structured program design to a real-world use case.

## 📌 Overview

Small clinics and Tier-2 city hospitals often rely on manual registers or unanswered phone calls for appointment booking, leading to lost records, double bookings, and no easy access to patient history. This system digitizes that entire workflow — patients can register and book online instead of depending on phone calls, admins get full record control, and doctors get instant access to their schedules.

## ✨ Features

### 👨‍💼 Admin
- Secure login system
- Add, update, view, and delete doctor records
- Add, update, view, and delete patient records
- Book, update, cancel, and view appointments
- View today's appointments in one click
- Mark appointments as "Completed" automatically based on date

### 🩺 Doctor
- Doctor login using ID + name verification
- View personal profile details
- View all appointments assigned to them, with full patient/date/status breakdown

### 🧑‍⚕️ Patient
- Self-registration (no admin needed)
- Login to view personal details
- Update contact information directly
- View appointment status and history

### 📅 Appointment Management
- Unique appointment IDs generated automatically
- Status tracking: Scheduled → Completed
- Date-based filtering for daily appointment overview
- Prevents duplicate/false bookings via relational constraints

## 🛠️ Tech Stack & Libraries

| Library | Purpose |
|---|---|
| `mysql-connector-python` | Connects Python to MySQL and handles all database operations (insert, update, delete, fetch) |
| `colorama` | Adds colored terminal output for better readability and a more polished CLI experience |
| `datetime` | Handles date logic — comparing today's date with appointment dates to auto-update statuses |

## 🗄️ Database Design

The system uses a relational MySQL database (`hospital_management`) with four core tables:
- **patient** — stores patient demographic and appointment-reason data
- **doctor** — stores doctor profile and specialization data
- **admin** — stores admin login credentials
- **appointment** — links patients and doctors via foreign keys, tracking date, reason, and status

## ⚙️ How to Run

1. Install dependencies:
   ```bash
   pip install mysql-connector-python colorama
