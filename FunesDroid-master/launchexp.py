import os
import sys
import shutil
import time
import argparse
from datetime import datetime
import shutil

print("Starting FunesDroid Testing...")

#launchexp.py -les [doc|bf|stai] -nevent [n] -wtime [w] -api [a]
def get_args():
    '''This function parses and return arguments passed in'''
    # Assign description to the help doc
    parser = argparse.ArgumentParser(
        description='Script that executes FunesDroid Testing')
    # Add arguments
    parser.add_argument(
        '-l', '--les', type=str, help='events that have to be execute, default value: ["doc","bf","stai"]', required=False, default=["doc","bf","stai"], nargs="+")
    parser.add_argument(
        '-n', '--nevent', type=int, help='number of repetition of the selected event, default value: [1,2,5]', required=False, default=[1,2,5], nargs="+")
    parser.add_argument(
        '-w', '--wtime', type=int, help='wait time between events, default value: [1,2,10]', required=False, default=[1,2,10], nargs="+")
    parser.add_argument(
        '-a', '--apiversion', type= int, help='api version needed for the emulator, default value: [25]', required= False, default=[25], nargs="+")
    # Array for all arguments passed to script
    args = parser.parse_args()
    # Assign args to variables
    les = args.les
    nevent = args.nevent
    wtime = args.wtime
    apiversion = args.apiversion
    # Return all variable values
    return les, nevent, wtime, apiversion


les, nevent, wtime, apiversion = get_args()

nevent=list(filter(lambda a: a != 0, nevent))
wtime=list(filter(lambda a: a != 0, wtime))
les = list(filter(lambda a: a !='',les))

os.popen("adb devices")
apkList= os.listdir('InputAPKs')


for apk in apkList:
    for t in wtime:
        for event in les:
            for number in nevent:
                print('Starting new experiment, event: '+event+', number of les:' +str(number))
                emulator= "em"+datetime.now().strftime('%Y%m%d%H%M%S')
                apiversion_string= str(apiversion[0])
                create_avd= r'echo no|C:\Users\Testing\AppData\Local\Android\sdk\tools\bin\avdmanager.bat create avd -n '+emulator+' -k "system-images;android-'+apiversion_string+';google_apis;x86"' #directory in cui sono installati gli sdk ed i loro strumenti
                start_avd= r"start cmd.exe /c C:\Users\Testing\AppData\Local\Android\Sdk\emulator\emulator.exe @"+emulator #directory in SDK contenente l'eseguibile dell'emulatore
                cmd = "python AndroLeakPR.py emulator-5554 "+event+" "+str(number)+" "+str(t)+" "+apk+" "+str(len(apkList)) #root progetto
                delete_avd = r"echo no|C:\Users\Testing\AppData\Local\Android\sdk\tools\bin\avdmanager.bat delete avd -n "+emulator #directory in cui sono installati gli sdk ed i loro strumenti
                os.system(create_avd)
                os.system(start_avd)
                os.system(cmd)
                os.popen("adb devices")
                os.popen("adb -s emulator-5554 emu kill")
                os.system(delete_avd)
                    

#Check della presenza dei file di WARNING  e le si sposta nella cartella \Results
for f in os.listdir(os.curdir):
    if os.path.isfile(f) and f.startswith("WARNING"):
        shutil.move(os.path.join(os.curdir,f),"Results")
        print('Warning: '+f+' moved in the \\Results directory.')

#Creazione archivio risultati
shutil.make_archive("Result_of_experiment", 'zip',"Results")

print("Testing Accomplished!")
