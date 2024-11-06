# GitHub examples repository path: Oscilloscopes/Python/RsInstrument

"""

Created on 2024/02

Author: Xavier Cheng
Version Number: 1
Date of last change: 2024/02/16
Requires: R&S MXO5 8 channels with FW 2.2 or newer
- Installed RsInstrument Python module (see the attached RsInstrument_PythonModule folder Readme.txt)
- Installed VISA e.g. R&S Visa 5.12.x or newer

Description: Example about how to use capture 7 channels simultanuously and save it into a CSV file.
the duration of writing the datas is performed as well via using time function.

General Information:
This example does not claim to be complete. All information has been
compiled with care. However, errors can not be ruled out.
"""



from RsInstrument import *
import time





##FileName of the saved file including 7 channels ' trace.
FileName='MultichannelFile_7Channels.csv'
# Number of channels used.
NumChannels=7

#Instrument remote: please define the IP adress of the instrument
ressource_string='TCPIP::172.23.183.4::HISLIP0::INSTR'
RTO=RsInstrument(ressource_string)

#This timeout is defined in milliseconds
RTO.visa_timeout=50000

#Creation of the csv file
fid = open(FileName, 'w')

# measure the duration of saving all datas into the CSV file.
t=time.time()

# related to NumChannel 1 to 8 used, the related number of trace are gathered and written on csv file.
if NumChannels==1:
    waveform1 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN1:DATA?')
    fid.write(str(waveform1) + '\n\n\n\n')

elif NumChannels==2:
    waveform1 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN1:DATA?')
    waveform2 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN2:DATA?')
    fid.write(str(waveform1) + '\n\n\n\n' + str(waveform2) + '\n\n\n\n')
elif NumChannels==3:
    waveform1 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN1:DATA?')
    waveform2 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN2:DATA?')
    waveform3 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN3:DATA?')
    fid.write(str(waveform1) + '\n\n\n\n' + str(waveform2) + '\n\n\n\n' + str(waveform3) + '\n\n\n\n')
elif NumChannels==4:
    waveform1 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN1:DATA?')
    waveform2 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN2:DATA?')
    waveform3 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN3:DATA?')
    waveform4 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN4:DATA?')
    fid.write(str(waveform1) + '\n\n\n\n' + str(waveform2) + '\n\n\n\n' + str(waveform3) + '\n\n\n\n' + str(waveform4) + '\n\n\n\n')
elif NumChannels==5:
    waveform1 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN1:DATA?')
    waveform2 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN2:DATA?')
    waveform3 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN3:DATA?')
    waveform4 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN4:DATA?')
    waveform5 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN5:DATA?')
    fid.write(str(waveform1) + '\n\n\n\n' + str(waveform2) + '\n\n\n\n' + str(waveform3) + '\n\n\n\n' + str(waveform4) + '\n\n\n\n' + str(waveform5) + '\n\n\n\n')
elif NumChannels==6:
    waveform1 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN1:DATA?')
    waveform2 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN2:DATA?')
    waveform3 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN3:DATA?')
    waveform4 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN4:DATA?')
    waveform5 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN5:DATA?')
    waveform6 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN6:DATA?')
    fid.write(str(waveform1) + '\n\n\n\n' + str(waveform2) + '\n\n\n\n' + str(waveform3) + '\n\n\n\n' + str(waveform4) + '\n\n\n\n' + str(waveform5) + '\n\n\n\n' + str(waveform6) + '\n\n\n\n')
elif NumChannels==7:
    waveform1 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN1:DATA?')
    waveform2 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN2:DATA?')
    waveform3 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN3:DATA?')
    waveform4 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN4:DATA?')
    waveform5 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN5:DATA?')
    waveform6 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN6:DATA?')
    waveform7 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN7:DATA?')

    fid.write(str(waveform1) + '\n\n\n\n' + str(waveform2) + '\n\n\n\n' + str(waveform3) + '\n\n\n\n' + str(waveform4) + '\n\n\n\n' + str(waveform5) + '\n\n\n\n' + str(waveform6) + '\n\n\n\n' + str(waveform7) + '\n\n\n\n')

elif NumChannels == 8:
    waveform1 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN1:DATA?')
    waveform2 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN2:DATA?')
    waveform3 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN3:DATA?')
    waveform4 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN4:DATA?')
    waveform5 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN5:DATA?')
    waveform6 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN6:DATA?')
    waveform7 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN7:DATA?')
    waveform8 = RTO.query_bin_or_ascii_float_list('FORM REAL,32;:CHAN8:DATA?')

    fid.write(str(waveform1) + '\n\n\n\n' + str(waveform2) + '\n\n\n\n' + str(waveform3) + '\n\n\n\n' + str(waveform4) + '\n\n\n\n' + str(waveform5) + '\n\n\n\n' + str(waveform6) + '\n\n\n\n' + str(waveform7) + '\n\n\n\n' + str(waveform8) + '\n\n\n\n')

# elapsed duration of the saved csv file is determined.
elapsed_2=time.time()-t





# print the elapsed duration on screen.
print(f'query duration {elapsed_2:.3f} secs')

#Close the remote session and the csv file object
RTO.close()
fid.close()




