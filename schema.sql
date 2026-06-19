CREATE DATABASE IF NOT EXISTS hospital_management;
USE hospital_management;

CREATE TABLE IF NOT EXISTS patient (
    patient_id INT PRIMARY KEY,
    patient_name VARCHAR(20),
    patient_age INT,
    patient_gender VARCHAR(1),
    patient_phone INT,
    patient_address VARCHAR(150),
    patient_dob DATE,
    appointment_reason VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS doctor (
    doctor_id INT PRIMARY KEY,
    doctor_name VARCHAR(20),
    doctor_email VARCHAR(20),
    doctor_specialisation VARCHAR(10),
    doctor_phone VARCHAR(15),
    doctor_address VARCHAR(50),
    doctor_experience INT
);

CREATE TABLE IF NOT EXISTS admin (
    admin_username VARCHAR(20) PRIMARY KEY,
    admin_password INT
);

CREATE TABLE IF NOT EXISTS appointment (
    appointment_id INT PRIMARY KEY,
    patient_id INT UNIQUE,
    doctor_id INT,
    appointment_date VARCHAR(20),
    appointment_reason VARCHAR(20),
    appointment_status VARCHAR(10),
    FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctor(doctor_id)
);
