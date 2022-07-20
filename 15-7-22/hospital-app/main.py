# Admin can CRUD a Staff, Doctor, Reception, Ward and two SalaryRequest operations
# Reception Staff can CRUD a Patient and Appointment, Bill
# Doctor can CRUD his Medical Tests and a Report(type == 'prescription' | 'test')
# Reception Staff can READ a Patient's Appointments and Reports
# Doctor can view all his Appointments
from admin import Admin

admin = Admin('admin1')


