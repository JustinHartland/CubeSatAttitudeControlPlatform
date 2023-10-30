from InertialMeasurementUnit import InertialMeasurementUnit
from InvPendDatabase import InvPendDatabase
import time

#Create instance of InertialMeasurementUnit:
imuDatabase = InvPendDatabase("InvPendDatabase.db")

#Add a new trial to the database
trial_id = imuDatabase.add_trial()
print(f"Added Trial with ID: {trial_id}")

#Create instance of InvPendDatabase:
IMU1 = InertialMeasurementUnit()

#Create array to hold most recent euler angles reported by .get_euler_angles()
#[angle_x, angle_y, angle_z]
imuData = []

initialTime = time.time()

while True:
    IMU1.get_euler_angles()
    imuData = [initialTime-time.time(), *IMU1.rawAccelArray, *IMU1.rawGyroArray, IMU1.angle_x, IMU1.angle_y, IMU1.angle_z]
    imuDatabase.add_imu_data(trial_id, imuData)

    print(f"Angle X: {IMU1.angle_x} deg")

    time.sleep(0.01)