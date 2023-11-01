import can
import cantools
import time
import threading
from configurator import main
from cfg import *
from flask import Flask, render_template, jsonify
app = Flask(__name__)
bustype = bus_type
channel = 'PCAN_USBBUS1'
bitrate = bit_rate
values = None
signalName = None
bus = can.interface.Bus(bustype = bustype, channel = channel, bitrate = bitrate)
db = cantools.db.load_file(dbc_file)
signalDict = {
    848:('EVC_CHG_ACRMSVoltage_Act_V','EVC_CHG_CktTemp_Act_degC','EVC_CHG_ACRMScurrent_Act_A','EVC_CHG_ACInputSupplyStatus_St_B','EVC_CHG_CycleStatus_St_enum','EVC_CHG_Fan1DutyCycle_Act_perc','EVC_CHG_Fan2DutyCycle_Act_perc','EVC_CHG_HousingTemp_Act_degC','EVC_CHG_OperatingMode_St_enum','EVC_CHG_Status_St_enum'),
    849:('EVC_CHG_TempSensorFault_St_B','EVC_CHG_ACCurrentFault_St_enum','EVC_CHG_ACvoltSensorFault_St_B','EVC_CHG_ChargerCRCViolation_St_B','EVC_CHG_DCCurrentFault_St_enum','EVC_CHG_DCcurrSensorFault_St_B','EVC_CHG_DCVoltageFault_St_enum','EVC_CHG_DCvoltSensorFault_St_B','EVC_CHG_DeratingStatus_St_enum','EVC_CHG_Fan1Fault_St_B','EVC_CHG_Fan2Fault_St_B','EVC_CHG_FaultStatus_St_B','EVC_CHG_InternalFuseFault_St_B','EVC_CHG_MOVFault_St_B','EVC_CHG_OutRevPolarityFault_St_B','EVC_CHG_SetPointViolation_St_B','EVC_CHG_TempFault_St_B','EVC_CHG_TempSensorFault_St_B','EVC_CHG_VCUCANcommTimeout_St_B'),
    850:('EVC_CHG_DCCurrent_Act_A','EVC_CHG_DCVoltage_Act_V','EVC_CHG_InputEnergyCount_Act_kWh','EVC_CHG_MaxAvailablePower_Act_W')}
def get_data():
    global values, signalName
    while True:
        message = bus.recv()
        messageID = message.arbitration_id
        parsedDict = db.decode_message(message.arbitration_id, message.data)
        if messageID in signalDict:
            parsedDict = db.decode_message(message.arbitration_id, message.data)
            refTuple = signalDict[messageID]
            for signalName in refTuple:
                if signalName in parsedDict:
                    values = parsedDict[signalName]
                    time.sleep(0.01)  
                    
def send_data_to_html():
    global EVC_CHG_ACRMSVoltage_Act_V
    global EVC_CHG_CktTemp_Act_degC
    while True:
        if signalName == 'EVC_CHG_ACRMSVoltage_Act_V':
            EVC_CHG_ACRMSVoltage_Act_V = values
            print(EVC_CHG_ACRMSVoltage_Act_V)
        if signalName == 'EVC_CHG_CktTemp_Act_degC':
            EVC_CHG_CktTemp_Act_degC = values
            print(EVC_CHG_CktTemp_Act_degC)
        time.sleep(0.01)                   
                    
@app.route('/')
def index():
    return render_template('index1.html', status = bustype, project_status = project) 

@app.route('/data')
def main():
    return jsonify({'EVC_CHG_CktTemp_Act_degC':EVC_CHG_CktTemp_Act_degC, 
                    'EVC_CHG_ACRMSVoltage_Act_V':EVC_CHG_ACRMSVoltage_Act_V}) 

if __name__ == "__main__" :
    threading.Thread(target = lambda: app.run(host= '0.0.0.0', debug =False, port = 0)).start()   
    
t1 = threading.Thread(target=get_data)
t2 = threading.Thread(target=send_data_to_html)      
t1.start()
t2.start()  
    
