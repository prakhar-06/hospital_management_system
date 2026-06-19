import mysql.connector as sa
p=sa.connect(host="localhost",user="root",password="")
cursor=p.cursor()
cursor.execute("create database if not exists hospital_management")
cursor.execute("use hospital_management")
p.commit()


from colorama import init, Fore
init(autoreset=True)


cursor.execute("create table if not exists patient(patient_id int primary key,"
               "patient_name varchar(20) ,patient_age int,"
               "patient_gender varchar(1),patient_phone int,patient_address varchar(150),patient_dob DATE, appointment_reason varchar(255))")

cursor.execute("create table  if not exists admin(admin_username varchar(20) primary key,"
               " admin_password int)")

def addadmin():
    admin_username = input("Enter admin username: ")
    admin_password = input("Enter admin password: ")
    query_ins = """insert into admin(admin_username,admin_password)values(%s,%s)"""
    cursor.execute(query_ins,(admin_username,admin_password))
    p.commit()
    print("Record added")

def addpatient():
    sql_select_query = """select count(*)  from patient"""
    cursor.execute(sql_select_query)
    total = cursor.fetchone()[0]
    y = str(total + 101)


    patient_id = total+101
    patient_name = input("Enter patient Name :")
    patient_age = input("Enter patient age :")
    patient_gender = input("Enter patient gender :")
    patient_phone = input("Enter patient phone :")
    patient_address = input("Enter patient address:")
    patient_dob = input("Enter patient dob :")
    appointment_reason = input("Enter appointment reason :")
    query_ins = """INSERT INTO patient  ( patient_id , patient_name , patient_age, patient_gender,
                      patient_phone , patient_address , patient_dob , appointment_reason )
                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                 """
    # print(query_ins)

    cursor.execute(query_ins,(patient_id, patient_name, patient_age, patient_gender,
                              patient_phone, patient_address, patient_dob, appointment_reason))
    p.commit()
    print( "-----------------------------Patient id is------------------------>", y)

    print("RECORDS ADDED")

def adddoctor():
    doctor_id = int(input("Enter doctor id :"))
    doctor_name = input("Enter doctor name :")
    doctor_email = input("Enter doctor email :")
    doctor_specialisation = input("Enter doctor specialisation :")
    doctor_phone = input("Enter doctor phone :")
    doctor_address = input("Enter doctor address:")
    doctor_experience = input("Enter doctor experience :")
    query_ins = """
        INSERT INTO doctor
        (doctor_id, doctor_name, doctor_email, doctor_specialisation,
         doctor_phone, doctor_address, doctor_experience)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """
    cursor.execute(query_ins,(
        doctor_id,
        doctor_name,
        doctor_email,
        doctor_specialisation,
        doctor_phone,
        doctor_address,
        doctor_experience
    ))

    p.commit()
    print("RECORDS ADDED")


cursor.execute("create table if not exists doctor(doctor_id int primary key,"
               "doctor_name varchar(20) ,doctor_email varchar(20),doctor_specialisation varchar(10),"
               "doctor_phone varchar(15),doctor_address varchar(50),doctor_experience int)")


cursor.execute("create table if not exists appointment(appointment_id int primary key,"
               "patient_id int unique, doctor_id int ,appointment_date varchar(20),"
               "appointment_reason varchar(20),appointment_status varchar(10))")

def addappointment():
     sql_select_query = """select count(*)  from appointment"""
     cursor.execute(sql_select_query)
     total = cursor.fetchone()[0]
     y = str(total+1)

     appointment_id = total+1
     patient_id = input("Enter patient id :")
     doctor_id = input("Enter doctor id :")
     appointment_date = input("Enter appointment date :")
     appointment_reason = input("Enter appointment reason :")
     appointment_status = input("Enter appointment status :")
     query_ins = """
        INSERT INTO appointment
        (appointment_id,patient_id, doctor_id, appointment_date, appointment_reason, appointment_status) 
        VALUES (%s,%s,%s,%s,%s,%s)
     """
     cursor.execute(query_ins,(appointment_id,patient_id,doctor_id,appointment_date,
                               appointment_reason,appointment_status))
     p.commit()
     print("--------------------------Appointment id for the given appointment is----------------",y)
     print("RECORDS ADDED")

p.commit()

def doctorlogin():
    doctor_id = input("Enter doctor id :")
    doctor_name = input("Enter doctor name :")
    sql_select_query = """select * from doctor where doctor_id = %s and doctor_name = %s """
    cursor.execute(sql_select_query, (doctor_id, doctor_name))
    result = cursor.fetchone()
    if result is None:
        print("Doctor not found")
    else:
        print("Doctor found")
        print("admin options")

        print("1 View my details")
        print("2 View appointment details")
        choice = int(input("Enter your choice :"))
        if choice == 1:
             doctordetails(result)

        elif choice == 2:

            sql_select_query= "SELECT COUNT(*) FROM appointment WHERE doctor_id = %s"
            cursor.execute(sql_select_query, (doctor_id,))
            total=cursor.fetchone()[0]
            print("Total number of appointments :",total)


                # Appointment details
            sql_select_query = """
                SELECT appointment_id,
                       appointment_date,
                       appointment_reason,
                       appointment_status,
                       patient_id
                FROM appointment
                WHERE doctor_id = %s
                """

            cursor.execute(sql_select_query,(doctor_id,))
            records = cursor.fetchall()
            if records is None:
                    print("Appointment not found")

            for i,row in enumerate  (records, start=1):

                    print("\n------------------RECORD" ,i, "---------------------")
                    print("Appointment ID:", row[0])
                    print("Appointment Date:", row[1])
                    print("Reason:", row[2])
                    print("Status:", row[3])
                    print("Patient ID:", row[4])
                    print("------------------------------")

def patientlogin():
    patient_id = input("Enter patient id :")
    patient_name = input("Enter patient name :")
    sql_select_query = """select * from patient where patient_id = %s and patient_name = %s """
    cursor.execute(sql_select_query, (patient_id, patient_name))
    ans = cursor.fetchone()
    if ans is None:
        print("Patient not found")
    else:
        print("Patient  status found")
        print("--------------------admin options---------------------")

        print("1. show my all details")
        print("2. view appointment details")
        print("3. exit")
        choice = int(input("enter your choice:"))
        if choice == 1:
            patientdetails(ans)
            choice=(input("want to update any of your information"))
            if choice == 'yes':
                updatepatient()
            else:

               exit()
        elif choice == 2:
            viewappointment()
            exit()
        elif choice == 3:
            print("exit")
            exit()

def viewappointment():
    appointment_id = input("Enter appointment id :")
    patient_id = input("Enter patient id :")
    sql_select_query = """select * from appointment where appointment_id = %s and patient_id = %s """
    cursor.execute(sql_select_query, (appointment_id, patient_id))
    s = cursor.fetchone()
    if s is None:
        print("Appointment not found")
    else:
        print("-----------------Appointment found------------------")


        print("Appointment ID:", s[0])
        print("patient id:", s[1])
        print("doctor id:", s[2])
        print("appointment reason:", s[3])
        print("appointment status:", s[4])
        print("------------------------------")


def func():

    print(Fore.BLUE +"----------------------WELCOME TO HOSPITAL MANAGEMENT SYSTEM-----------------------------\n")
    print("----------------------To book an appointment please login-------------------- \n")
    print("choose options:")
    print("1. NEW patient login  (online)")
    print("2. Doctor login ")
    print("3. Patient login ")
    print("4. View your appointment ")
    print("5. Admin login ")
    print("6. Exit ")

    choice=int(input("enter your choice:"))
    if choice ==  1:
         addpatient()
         print(Fore.RED + " You have registered patient successfully ,  your appointment would be book within 12hrs AFTER THE PAYMENT"
               " and you will be ""notified based on the availability of doctor......  ")
         exit()
    elif choice == 2:
        print("1. for new doctor registration ")
        print("2. doctor login ")
        choice=int(input("enter your choice:"))
        if choice == 1:
            adddoctor()
            exit()
        if choice == 2:
            doctorlogin()
            exit()
        else:
            print("not valid option")
            exit()
    elif choice == 3:
         patientlogin()
         exit()
    elif choice == 4:
         viewappointment()
         exit()
    elif choice == 5:
         print("choose option")
         print("1.admin login ")
         print("2.new admin login")
         print("3.exit ")
         choice=int(input("Enter Your Choice : "))
         if choice==1:
             adminlogin()
             exit()
         if choice==2:
             addadmin()
             exit()
         if choice==3:
             print("exit ")
             exit()
    elif choice == 6:
        print("logging out")
        print("Thanks for using the program")
    else:
        print("invalid choice")
        exit()


def doctordetails(result):
    print("\n---------DOCTOR DETAILS---------")
    print("doctor id   :", result[0])
    print("doctor name :", result[1])
    print("doctor email  :", result[2])
    print("specialisation :",result[3])
    print("phone :",result[4])
    print("doctor address:",result[5])
    print("doctor experience :",result[6])


def patientdetails(ans):
    print("\n---------PATIENT DETAILS---------")
    print("patient id :", ans[0])
    print("patient name :", ans[1])
    print("patient address :", ans[2])
    print(" patient date of birth:",ans[3])
    print("phone :",ans[4])


def appointmentdetails(s):
    print("\n---------APPOINTMENT DETAILS---------")
    print("appointment id :", s[0])
    print("patient id :", s[1])
    print("appointment date :", s[3])
    print("appointment reason :", s[4])
    print("appointment status :", s[5])


def adminlogin():
    user = input("Enter admin username :")
    pw = input("Enter admin password :")
    sql_select_query = """select * from admin where admin_username = %s and admin_password = %s """
    param=(user, pw)
    cursor.execute(sql_select_query, param)
    result = cursor.fetchone()
    if result is None:
        print("admin not found")
    else:
        print("admin login successful")
        print("1. for doctors")
        print("2. for patients")
        print("3. to book appointments")
        choice=int(input("enter your choice:"))
        if choice == 1:
            print("-------------Doctor management menu---------------")
            print("1. add doctor")
            print("2. update doctor ")
            print("3. View all doctors ")
            print("4. delete doctor")
            print("5. exit")
            choice=int(input("enter your choice:"))
            if choice == 1:
                adddoctor()
                exit()
            elif choice == 2:
                updatedoctor()
                exit()
            elif choice == 3:
                viewdoctor()
                exit()
            elif choice == 4:
                deletedoctor()
                exit()
            elif choice == 5:
                print("exit")
        elif choice == 2:
            print("-------------Patient DETAILS-------------")
            print("1. add patient")
            print("2. update patient ")
            print("3. view  patient ")
            print("4. delete patient")
            print("5. exit")
            choice=int(input("enter your choice:"))
            if choice == 1:
                addpatient()
                exit()
            elif choice == 2:
                updatepatient()
                exit()
            elif choice == 3:
                viewpatient()
                exit()
            elif choice == 4:
                deletepatient()
                exit()
            elif choice == 5:
                print("exit")
        elif choice == 3:
            print("-------------APPOINTMENT DETAILS-------------")
            print("1. Book appointment")
            print("2. cancel appointment ")
            print("3. view appointment ")
            print("4. Update or complete appointment ")
            print("5. today appointments")
            print("6. exit ")
            choice=int(input("enter your choice:"))
            if choice == 1:
                addappointment()
                exit()
            elif choice == 2:
                deleteappointment()
                exit()
            elif choice == 3:
                viewappointment()
                exit()
            elif choice == 4:
                print("1. update the appointment status as completed")
                print("2. update  the appointment date, doctor, status")
                choice=int(input("enter your choice:"))
                if choice == 1:
                    status_completed()
                    exit()
                if choice == 2:
                    updateappointment()
                    exit()
            elif choice == 5:
                today_appointments()
                exit()

            elif choice == 6:
                print("exit")

def updatedoctor():
    a = int(input("Enter doctor id for update doctor data:"))
    b=input("Enter doctor new email for update doctor data:")
    c=input("Enter doctor new phone for update doctor data:")
    d=input("Enter doctor new address for update doctor data:")
    query_update = "UPDATE doctor set doctor_email = %s , doctor_phone = %s , doctor_address= %s where doctor_id = %s"
    cursor.execute(query_update,(b,c,d,a))
    p.commit()
    print("update doctor successful")

def viewdoctor():
    cursor.execute("select* from doctor")
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    p.close()

def deletedoctor():
    a=int(input("Enter doctor id for delete doctor data:"))
    query_delete = "DELETE FROM doctor where doctor_id = %s"
    cursor.execute(query_delete,(a,))
    p.commit()
    print("delete doctor successful")

def updatepatient():
    a=int(input("Enter patient id for update patient data:"))
    b=input("Enter patient new mobile.no for update patient data:")
    c=input("Enter patient new address for update patient data:")
    query_update = "UPDATE PATIENT set patient_phone = %s, patient_address = %s where patient_id = %s"
    cursor.execute(query_update,(b,c,a))
    p.commit()

def viewpatient():
    patient_id=int(input("Enter patient id for view patient data:"))
    sql_select_query = "SELECT * FROM patient where patient_id = %s"
    cursor.execute(sql_select_query, (patient_id,))
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    p.close()


def deletepatient():
    a=int(input("Enter patient id for delete patient data:"))
    query_delete = "DELETE FROM patient where patient_id = %s"
    cursor.execute(query_delete,(a,))
    p.commit()
    print("patient deleted successful")

def deleteappointment():
    a=int(input("Enter appointment id for delete appointment data:"))
    query_delete = "DELETE FROM appointment where appointment_id = %s"
    cursor.execute(query_delete,(a,))
    p.commit()
    print("appointment deleted successful")
#
# def viewallappointment():
#     cursor.execute("select* from appointment")
#     result = cursor.fetchall()
#     for row in result:
#         print(row)
#     cursor.close()
#     p.close()
#     p.commit()

def exit():
    print("want to exit the program")
    choice=(input("enter your choice:"))
    if choice == 'yes':
        print("exit")
        print("Thanks for using this program")
    else:
        print("-------------------------------------------")
        func()


def updateappointment():
    print("what you want to update in appointment data:")
    print("1. Doctor ID")
    print("2. Appointment date")
    print("3. appointment status")
    choice=int(input("enter your choice:"))
    if choice == 1:
        appointment_id=int(input("enter appointment id for update appointment data:"))
        doctor_id = input("Enter new doctor id for update appointment data:")
        query_update = "UPDATE appointment set doctor_id = %s  where appointment_id = %s"
        cursor.execute(query_update, (doctor_id,appointment_id))
        p.commit()
        print("Appointment data updated successfulLY")
    elif choice == 2:
        appointment_id = int(input("enter appointment id for update appointment data:"))
        appointment_date = input("Enter new date for update appointment data:")
        query_update = "UPDATE appointment set doctor_id = %s  where appointment_id = %s"
        cursor.execute(query_update, (appointment_date, appointment_id))
        p.commit()
        print("Appointment data updated successfulLY")
    elif choice == 3:
        appointment_id = int(input("enter appointment id for update appointment data:"))
        appointment_status = input("Enter current status for update appointment data:")
        query_update = "UPDATE appointment set doctor_id = %s  where appointment_id = %s"
        cursor.execute(query_update, (appointment_status, appointment_id))
        p.commit()
        print("Appointment data updated successfulLY")


def today_appointments():
    from datetime import date
    y= date.today()
    appointment_date = y.strftime("%Y-%m-%d")


    sql_select_query = "SELECT COUNT(*) FROM appointment WHERE appointment_date = %s"
    cursor.execute(sql_select_query, (appointment_date,))
    total = cursor.fetchone()[0]
    print("Total number of appointments :", total)

    # Appointment details
    sql_select_query = """
        SELECT appointment_id,
               patient_id,
               appointment_date,
               appointment_reason,
               appointment_status
               
        FROM appointment
        WHERE appointment_date = %s
        """


    cursor.execute(sql_select_query, (appointment_date,))
    result = cursor.fetchall()
    if result is None:
        print("No appointment data found")
    else:
            for i, row in enumerate(result, start=1):
                print("\n------------------RECORD", i, "---------------------")
                print("Appointment ID:", row[0])
                print("patient_id:", row[1])
                print("appointment_date:", row[2])
                print("appointment_reason:", row[3])
                print("appointment_status:", row[4])
                print("------------------------------")


def status_completed():
    from datetime import date

    print( "------------------Today date-------------------->", date.today())
    today = input("enter date you want status to be completed")

    query_update = """
    UPDATE appointment
    SET appointment_status = 'Completed'
    WHERE appointment_date < %s
    AND appointment_status = 'Scheduled'
    """

    cursor.execute(query_update, (today,))

    print(cursor.rowcount, "appointments updated to Completed")

    cursor.close()


func()





