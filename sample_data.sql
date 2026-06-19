USE hospital_management;

-- Sample Admins
INSERT INTO admin (admin_username, admin_password) VALUES
('admin01', 111111),
('admin02', 222222);

-- Sample Doctors
INSERT INTO doctor (doctor_id, doctor_name, doctor_email, doctor_specialisation, doctor_phone, doctor_address, doctor_experience) VALUES
(201, 'Dr. Rajesh Sharma', 'rajesh.sharma@gmail.com', 'General Physician', '+91-9876543201', 'H.No. 12, MG Road, Sadar, Agra, Uttar Pradesh', 12),
(202, 'Dr. Amit Verma', 'amit.verma@gmail.com', 'ENT Specialist', '+91-9876543202', 'Flat 8B, Ashok Nagar, Sanjay Palace, Agra, Uttar Pradesh', 10),
(203, 'Dr. Neha Kapoor', 'neha.kapoor@gmail.com', 'Dermatologist', '+91-9876543203', 'H.No. 45, Gandhi Road, Civil Lines, Agra, Uttar Pradesh', 8),
(204, 'Dr. Vikram Singh', 'vikram.singh@gmail.com', 'Dentist', '+91-9876543204', 'House 21, Shanti Nagar, Sikandra, Agra, Uttar Pradesh', 15),
(205, 'Dr. Priya Mehta', 'priya.mehta@gmail.com', 'Eye Specialist', '+91-9876543205', 'Plot 9, Tulsi Marg, Shastripuram, Agra, Uttar Pradesh', 9),
(206, 'Dr. Sandeep Yadav', 'sandeep.yadav@gmail.com', 'General Physician', '+91-9876543206', 'H.No. 78, Main Market Road, Kamla Nagar, Agra, Uttar Pradesh', 7),
(207, 'Dr. Pooja Malhotra', 'pooja.malhotra@gmail.com', 'Dentist', '+91-9876543207', 'Flat 14, Rose Apartments, Dayal Bagh, Agra, Uttar Pradesh', 11),
(208, 'Dr. Arjun Reddy', 'arjun.reddy@gmail.com', 'Cardiologist', '+91-9876543208', 'House 5, Nehru Enclave, Civil Lines, Agra, Uttar Pradesh', 14),
(209, 'Dr. Kavita Nair', 'kavita.nair@gmail.com', 'Gynecologist', '+91-9876543209', 'Plot 33, Krishna Colony, Sikandra, Agra, Uttar Pradesh', 13),
(210, 'Dr. Rohit Deshmukh', 'rohit.deshmukh@gmail.com', 'Orthopedic Surgeon', '+91-9876543210', 'H.No. 66, Prem Vihar, Kamla Nagar, Agra, Uttar Pradesh', 16);

-- Sample Patients
INSERT INTO patient (patient_id, patient_name, patient_age, patient_gender, patient_phone, patient_address, patient_dob, appointment_reason) VALUES
(101, 'Aarav Sharma', 25, 'M', '9876500101', 'Sadar, Agra', '2001-03-12', 'General Checkup'),
(102, 'Priya Verma', 32, 'F', '9876500102', 'Civil Lines, Agra', '1994-07-21', 'Fever and Cold'),
(103, 'Rohan Singh', 28, 'M', '9876500103', 'Kamla Nagar, Agra', '1998-01-15', 'Skin Allergy'),
(104, 'Ananya Gupta', 21, 'F', '9876500104', 'Dayal Bagh, Agra', '2005-09-18', 'Dental Pain'),
(105, 'Vikram Yadav', 45, 'M', '9876500105', 'Sikandra, Agra', '1981-11-02', 'Eye Examination'),
(106, 'Neha Kapoor', 30, 'F', '9876500106', 'Aligarh Road, Hathras', '1996-06-10', 'Blood Pressure Check'),
(107, 'Aditya Mishra', 36, 'M', '9876500107', 'Krishna Nagar, Mathura', '1990-12-05', 'Diabetes Consultation'),
(108, 'Sneha Jain', 27, 'F', '9876500108', 'Mahavir Ganj, Aligarh', '1999-04-30', 'Back Pain'),
(109, 'Karan Patel', 40, 'M', '9876500109', 'Rambagh, Agra', '1986-08-16', 'Migraine'),
(110, 'Pooja Saxena', 24, 'F', '9876500110', 'Shastripuram, Agra', '2002-02-11', 'Routine Health Check'),
(111, 'Rahul Tiwari', 38, 'M', '9876500111', 'Sasni Gate, Aligarh', '1988-05-27', 'Chest Pain'),
(112, 'Simran Kaur', 29, 'F', '9876500112', 'Govind Nagar, Mathura', '1997-07-14', 'Throat Infection'),
(113, 'Arjun Mehta', 33, 'M', '9876500113', 'Mantola, Agra', '1993-10-22', 'Joint Pain'),
(114, 'Kavya Nair', 26, 'F', '9876500114', 'New Agra Colony, Agra', '2000-01-08', 'Tooth Extraction'),
(115, 'Manish Chauhan', 50, 'M', '9876500115', 'Aligarh Junction Area, Aligarh', '1976-09-03', 'Vision Problem'),
(116, 'Isha Agarwal', 22, 'F', '9876500116', 'Mathura Cantt, Mathura', '2004-11-19', 'Stomach Ache'),
(117, 'Sandeep Rawat', 41, 'M', '9876500117', 'Hari Parvat, Agra', '1985-04-06', 'Asthma Review'),
(118, 'Ritika Malhotra', 31, 'F', '9876500118', 'Sadar Bazar, Hathras', '1995-03-25', 'Hair Loss Treatment'),
(119, 'Harsh Vardhan', 35, 'M', '9876500119', 'Etah Chungi, Aligarh', '1991-08-09', 'Dental Cleaning'),
(120, 'Nidhi Bansal', 23, 'F', '9876500120', 'Balkeshwar, Agra', '2003-12-17', 'Eye Irritation'),
(121, 'Deepak Joshi', 47, 'M', '9876500121', 'Kamla Nagar, Agra', '1979-05-13', 'Heart Checkup'),
(122, 'Aditi Srivastava', 28, 'F', '9876500122', 'Krishna Nagar, Mathura', '1998-06-28', 'Flu Symptoms'),
(123, 'Yash Khanna', 34, 'M', '9876500123', 'Quarsi, Aligarh', '1992-01-31', 'Acne Treatment'),
(124, 'Meera Desai', 27, 'F', '9876500124', 'Sikandra, Agra', '1999-09-12', 'Root Canal'),
(125, 'Raj Malviya', 39, 'M', '9876500125', 'Dayal Bagh, Agra', '1987-02-24', 'Glasses Consultation'),
(126, 'Tanvi Chawla', 20, 'F', '9876500126', 'Civil Lines, Agra', '2006-07-07', 'High Fever'),
(127, 'Mohit Arora', 44, 'M', '9876500127', 'Raya Road, Mathura', '1982-10-15', 'Nutrition Advice'),
(128, 'Shreya Kulkarni', 25, 'F', '9876500128', 'Aligarh Road, Hathras', '2001-04-01', 'Rash Examination'),
(129, 'Abhishek Dubey', 37, 'M', '9876500129', 'Sanjay Place, Agra', '1989-06-20', 'Jaw Pain'),
(130, 'Palak Sinha', 29, 'F', '9876500130', 'Center Point, Aligarh', '1997-11-29', 'Eye Surgery Follow-up'),
(132, 'Sameer Malhotra', 50, 'M', '7683989801', '9-ram nagar colony sikandra agra', '1976-05-23', 'Knee problem');

-- Sample Appointments
INSERT INTO appointment (appointment_id, patient_id, doctor_id, appointment_date, appointment_reason, appointment_status) VALUES
(1, 101, 201, '2026-06-01', 'General Checkup', 'Completed'),
(2, 102, 201, '2026-06-02', 'Fever and Cold', 'Completed'),
(3, 103, 203, '2026-06-03', 'Skin Allergy', 'Completed'),
(4, 104, 204, '2026-06-04', 'Dental Pain', 'Cancelled'),
(5, 105, 205, '2026-06-05', 'Eye Examination', 'Scheduled'),
(6, 106, 201, '2026-06-06', 'Blood Pressure Check', 'Completed'),
(7, 107, 202, '2026-06-07', 'Diabetes Consultation', 'Scheduled'),
(8, 108, 203, '2026-06-08', 'Back Pain', 'Scheduled'),
(9, 109, 204, '2026-06-09', 'Migraine', 'Completed'),
(10, 110, 205, '2026-06-10', 'Routine Health Check', 'Scheduled'),
(11, 111, 201, '2026-06-11', 'Chest Pain', 'Cancelled'),
(12, 112, 202, '2026-06-12', 'Throat Infection', 'Scheduled'),
(13, 113, 203, '2026-06-13', 'Joint Pain', 'Completed'),
(14, 114, 204, '2026-06-14', 'Tooth Extraction', 'Scheduled'),
(15, 115, 205, '2026-06-15', 'Vision Problem', 'Scheduled'),
(16, 116, 201, '2026-06-16', 'Stomach Ache', 'Completed'),
(17, 117, 202, '2026-06-17', 'Asthma Review', 'Scheduled'),
(18, 118, 203, '2026-06-18', 'Hair Loss Treatment', 'Cancelled'),
(19, 119, 204, '2026-06-19', 'Dental Cleaning', 'Completed'),
(20, 120, 205, '2026-06-20', 'Eye Irritation', 'Scheduled'),
(21, 121, 201, '2026-06-21', 'Heart Checkup', 'Scheduled'),
(22, 122, 202, '2026-06-22', 'Flu Symptoms', 'Completed'),
(23, 123, 203, '2026-06-23', 'Acne Treatment', 'Scheduled'),
(24, 124, 204, '2026-06-24', 'Root Canal', 'Scheduled'),
(25, 125, 205, '2026-06-25', 'Glasses Consultation', 'Cancelled'),
(26, 126, 201, '2026-06-26', 'High Fever', 'Completed'),
(27, 127, 202, '2026-06-27', 'Nutrition Advice', 'Scheduled'),
(28, 128, 203, '2026-06-28', 'Rash Examination', 'Scheduled'),
(29, 129, 204, '2026-06-29', 'Jaw Pain', 'Completed'),
(30, 130, 205, '2026-06-30', 'Eye Surgery Follow-up', 'Scheduled');
