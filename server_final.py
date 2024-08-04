from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime
from flask_cors import CORS 

##########################################################################################################################################################################################################################################################################################

app = Flask(__name__)
CORS(app)
# MySQL connection setup
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="suryansh2004",
    database="testdatabase")

mycursor = db.cursor()

##########################################################################################################################################################################################################################################################################################

def insert_patient(data):
        
    name = data.get('name')
    phone = data.get('phone')
    blood = data.get('blood')
    email = data.get('email')
    gender = data.get('gender')
    symptoms = data.get('symptoms')
    admit_date = data.get('admit_date')
    created = datetime.now()

    mycursor.execute("INSERT INTO patient (name, phone, blood, email, gender, symptoms, admit_date, created) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (name, phone, blood, email, gender, symptoms, admit_date, created))
    db.commit()

##########################################################################################################################################################################################################################################################################################

def insert_department(data):

    dept_head = data.get('dept_head')
    dept_name = data.get('dept_name')
    emp_count = data.get('emp_count')

    mycursor.execute("INSERT INTO department (dept_head, dept_name, emp_count) VALUES (%s, %s, %s)", (dept_head, dept_name, emp_count))
    db.commit()

##########################################################################################################################################################################################################################################################################################

def insert_doctor(data):

    dept_id = data.get('dept_id')
    doc_name = data.get('doc_name')
    phone = data.get('phone')
    email = data.get('email')
    gender = data.get('gender')
    qualification = data.get('qualification')
    specialization = data.get('specialization')

    mycursor.execute("INSERT INTO doctor (dept_id, doc_name, phone, email, gender, qualification, specialization) VALUES (%s, %s, %s, %s, %s, %s, %s)", (dept_id, doc_name, phone, email, gender, qualification, specialization))
    db.commit()

##########################################################################################################################################################################################################################################################################################

def insert_prescription(data):
    
    p_id = data.get('p_id')
    doc_id = data.get('doc_id')
    dept_id = data.get('dept_id')
    diagnosis = data.get('diagnosis')       
    medicine = data.get('medicine')
    bill = data.get('bill')
    discharge_date = data.get('discharge_date')

    mycursor.execute("INSERT INTO prescription (id, doc_id, dept_id, diagnosis, medicine, bill, discharge_date) VALUES (%s, %s, %s, %s, %s, %s, %s)", (p_id, doc_id, dept_id, diagnosis, medicine, bill, discharge_date))
    db.commit()

##########################################################################################################################################################################################################################################################################################

def delete_patient(data):

    pid = data.get('pid')
        

    mycursor.execute("DELETE FROM patient WHERE id = %s", (pid,))
    db.commit()

##########################################################################################################################################################################################################################################################################################

def delete_department(data):

    dept_id = data.get('dept_id')

    mycursor.execute("DELETE FROM department WHERE dept_id = %s", (dept_id,))
    db.commit()

##########################################################################################################################################################################################################################################################################################

def delete_doctor(data):

    doc_id = data.get('doc_id')

    mycursor.execute("DELETE FROM doctor WHERE doc_id = %s", (doc_id,))
    db.commit()

##########################################################################################################################################################################################################################################################################################

def delete_prescription(data):

    pre_id = data.get('pre_id')

    mycursor.execute("DELETE FROM prescription WHERE pre_id = %s", (pre_id,))
    db.commit()

##########################################################################################################################################################################################################################################################################################

def alter_patient(data):
     
    pid = data.get('pid')
    name1 = data.get('name')
    phone1 = data.get('phone')
    blood1 = data.get('blood')
    email1 = data.get('email')
    gender1 = data.get('gender')
    symptoms1 = data.get('symptoms')
    admit_date1 = data.get('admit_date')
    created1 = datetime.now()

    mycursor.execute("UPDATE patient SET name = %s, phone = %s, blood = %s, email = %s, gender = %s, symptoms = %s, admit_date = %s, created = %s WHERE id = %s", (name1, phone1, blood1, email1, gender1, symptoms1, admit_date1, created1, pid))
    db.commit()

##########################################################################################################################################################################################################################################################################################

def alter_department(data):

    dept_id = data.get('dept_id')
    dept_head1 = data.get('dept_head')
    dept_name1 = data.get('dept_name')
    emp_count1 = data.get('emp_count')

    mycursor.execute("UPDATE department SET dept_head = %s, dept_name = %s, emp_count = %s WHERE dept_id = %s", (dept_head1, dept_name1, emp_count1, dept_id))
    db.commit()

##########################################################################################################################################################################################################################################################################################

def alter_doctor(data):

    doc_id = data.get('doc_id')
    dept_id1 = data.get('dept_id')
    doc_name1 = data.get('doc_name')
    phone1 = data.get('phone')
    email1 = data.get('email')
    gender1 = data.get('gender')
    qualification1 = data.get('qualification')
    specialization1 = data.get('specialization')

    mycursor.execute("UPDATE doctor SET dept_id = %s, doc_name = %s, phone = %s, email = %s, gender = %s, qualification = %s, specialization = %s WHERE doc_id = %s", (dept_id1, doc_name1, phone1, email1, gender1, qualification1, specialization1, doc_id))
    db.commit()

##########################################################################################################################################################################################################################################################################################

def alter_prescription(data):

    pre_id = data.get('pre_id')
    p_id1 = data.get('p_id')
    doc_id1 = data.get('doc_id')
    dept_id1 = data.get('dept_id')
    diagnosis1 = data.get('diagnosis')
    medicine1 = data.get('medicine')
    bill1 = data.get('bill')
    discharge_date1 = data.get('discharge_date')

    mycursor.execute("UPDATE prescription SET id = %s, doc_id = %s, dept_id = %s, diagnosis = %s, medicine = %s, bill = %s, discharge_date = %s WHERE pre_id = %s", (p_id1, doc_id1, dept_id1, diagnosis1, medicine1, bill1, discharge_date1, pre_id))
    db.commit()

##########################################################################################################################################################################################################################################################################################

def patient_details(patient_id):
     
     mycursor.execute("SELECT * FROM patient WHERE id = %s", (patient_id,))
     details = mycursor.fetchone()
     return details

##########################################################################################################################################################################################################################################################################################

def doctor_details():

    mycursor.execute("SELECT doctor.*, department.dept_name FROM doctor INNER JOIN department ON doctor.dept_id = department.dept_id")
    details = mycursor.fetchall()
    return details

##########################################################################################################################################################################################################################################################################################

def department_details():

    mycursor.execute("SELECT * FROM department")
    details = mycursor.fetchall()
    return details

##########################################################################################################################################################################################################################################################################################

def prescription_details(prescription_id):

    mycursor.execute("SELECT pr.pre_id, p.name AS patient_name, d.doc_name AS doctor_name, dept.dept_name AS department_name, pr.diagnosis, pr.medicine, pr.bill, pr.discharge_date FROM prescription pr JOIN patient p ON pr.id = p.id JOIN doctor d ON pr.doc_id = d.doc_id JOIN department dept ON pr.dept_id = dept.dept_id WHERE pr.pre_id = %s", (prescription_id,))
    details = mycursor.fetchone()
    return details

##########################################################################################################################################################################################################################################################################################

def medicine_details():

    mycursor.execute("SELECT medicine, COUNT(*) AS prescription_count FROM prescription GROUP BY medicine")
    details = mycursor.fetchall()
    return details

##########################################################################################################################################################################################################################################################################################

@app.route('/')
def index():
    return "Flask server is running!"

##########################################################################################################################################################################################################################################################################################

@app.route('/insert_patient', methods=['POST'])
def insert_pat():
    data = request.form
    insert_patient(data)
    return '', 204

##########################################################################################################################################################################################################################################################################################

@app.route('/insert_department', methods=['POST'])
def insert_dept():
    data = request.form
    insert_department(data)
    return '', 204

##########################################################################################################################################################################################################################################################################################

@app.route('/insert_doctor', methods=['POST'])
def insert_doc():
    data = request.form
    insert_doctor(data)
    return '', 204

##########################################################################################################################################################################################################################################################################################

@app.route('/insert_prescription', methods=['POST'])
def insert_pre():
    data = request.form
    insert_prescription(data)
    return '', 204

##########################################################################################################################################################################################################################################################################################

@app.route('/delete_patient', methods=['POST'])
def delete_pat():
    data = request.form
    
    delete_patient(data)
    return '', 204

##########################################################################################################################################################################################################################################################################################

@app.route('/delete_department', methods=['POST'])
def delete_dept():
    data = request.form
    
    delete_department(data)
    return '', 204

##########################################################################################################################################################################################################################################################################################

@app.route('/delete_doctor', methods=['POST'])
def delete_doc():
    data = request.form
    
    delete_doctor(data)
    return '', 204

##########################################################################################################################################################################################################################################################################################

@app.route('/delete_prescription', methods=['POST'])
def delete_pre():
    data = request.form
    
    delete_prescription(data)
    return '', 204

##########################################################################################################################################################################################################################################################################################

@app.route('/alter_patient', methods=['POST'])
def alter_pat():
    data = request.form
    alter_patient(data)

    return '', 204     

##########################################################################################################################################################################################################################################################################################

@app.route('/alter_department', methods=['POST'])
def alter_dept():
    data = request.form
    alter_department(data)

    return '', 204     

##########################################################################################################################################################################################################################################################################################

@app.route('/alter_doctor', methods=['POST'])
def alter_doc():
    data = request.form
    alter_doctor(data)

    return '', 204     

##########################################################################################################################################################################################################################################################################################

@app.route('/alter_prescription', methods=['POST'])
def alter_pre():
    data = request.form
    alter_prescription(data)

    return '', 204     

##########################################################################################################################################################################################################################################################################################

@app.route('/patient_details/<int:patient_id>', methods = ['GET'])
def display_patient_details(patient_id):
    details = patient_details(patient_id)
    return jsonify(details)

##########################################################################################################################################################################################################################################################################################

@app.route('/doctor_details', methods = ['GET'])
def display_doctor_details():
    details = doctor_details()
    return jsonify(details)

##########################################################################################################################################################################################################################################################################################

@app.route('/department_details',methods = ['GET'])
def display_department_details():
    details = department_details()
    return jsonify(details)

##########################################################################################################################################################################################################################################################################################

@app.route('/prescription_details/<int:prescription_id>', methods = ['GET'])
def display_prescription_details(prescription_id):
    details = prescription_details(prescription_id)
    return jsonify(details)

##########################################################################################################################################################################################################################################################################################

@app.route('/medicine_details', methods = ['GET'])
def display_medicine_details():
    details = medicine_details()
    return jsonify(details)

##########################################################################################################################################################################################################################################################################################

if __name__ == '__main__':
    app.run(debug=True)

##########################################################################################################################################################################################################################################################################################

