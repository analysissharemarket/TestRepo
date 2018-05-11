import datetime;
import os;
import csv;
import time;
import requests;
import zipfile;
from shutil import rmtree
import sys
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


##########################################################################
#                                                                        #
# Below Code is to Download Bhav Copy from NSE Site First it Create      #
# Dynamic Name According to site                                         #                   
#                                                                        #
##########################################################################
now = datetime.datetime.now()
checkHoliday = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
holiday=False
if checkHoliday == '2018-3-30' :
    holiday=True
elif checkHoliday == '2018-5-1' :
    holiday=True
elif checkHoliday == '2018-8-15' :
    holiday=True
elif checkHoliday == '2018-8-22' :
    holiday=True
elif checkHoliday == '2018-9-13' :
    holiday=True
elif checkHoliday == '2018-9-20' :
    holiday=True
elif checkHoliday == '2018-10-2' :
    holiday=True
elif checkHoliday == '2018-10-18' :
    holiday=True
elif checkHoliday == '2018-11-7' :
    holiday=True
elif checkHoliday == '2018-11-8' :
    holiday=True
elif checkHoliday == '2018-11-23' :
    holiday=True
elif checkHoliday == '2018-12-25' :
    holiday=True
if holiday == True :
    exit();

#############################################################################   
#
# Download Delivery Percentage Bhav Copy
#
#############################################################################
now = datetime.datetime.now()
delivery_percent_bhav_copy_name = "DELV_PER_FULL_BHAV_COPY_";
if  now.day < 10 : 
                delivery_percent_bhav_copy_name = delivery_percent_bhav_copy_name +"0" 
delivery_percent_bhav_copy_name=delivery_percent_bhav_copy_name +"_"+str(now.day)+now.strftime("%b").upper() + str(now.year) + ".csv"
delivery_percent_bhav_copy_url = "https://www.nseindia.com/products/content/sec_bhavdata_full.csv"
r = requests.get(delivery_percent_bhav_copy_url)
with open(delivery_percent_bhav_copy_name,'wb') as f:
    f.write(r.content)
print (" bhavcopy_url ",  delivery_percent_bhav_copy_url)

#############################################################################   
#
# Removing Unwanted Blan Space in Column e.g ' DATE , SERIES
#
#############################################################################
comand="sh removingUnwantedPaddingFUllBhav.sh "+delivery_percent_bhav_copy_name
os.system(comand)


stringToReplace="";
stringToReplaceWith="";
with open(delivery_percent_bhav_copy_name, newline='\n') as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ',')
    for row in reader:
        print(row['SYMBOL'],row['DATE1'])
        stringToReplace=row['DATE1']
        struct_time = time.strptime(stringToReplace, "%d-%b-%Y")
        new_date=str(struct_time.tm_year)+"-"
        if struct_time.tm_mon < 10  :
                    new_date=new_date+"0"
        new_date=new_date+str(struct_time.tm_mon)+"-"
        if struct_time.tm_mday < 10  :
                    new_date=new_date+"0"
        new_date=new_date+str(struct_time.tm_mday)
        stringToReplaceWith=new_date
        print(row['SYMBOL'],row['SERIES'],new_date)
        break;

##########################################################################
#                                                                        #
# Below Code is to replace date from format 01-Aug-2017 t0  2017-08-01   #
#                                                                        #
##########################################################################
with open(delivery_percent_bhav_copy_name, 'r') as file :
    filedata = file.read()
# Replace the target string
filedata = filedata.replace(stringToReplace, stringToReplaceWith)
# Write the file out again
with open(delivery_percent_bhav_copy_name, 'w') as file:
    file.write(filedata)




##########################################################################
#                                                                        #
# Below Code is to Download Bhav Copy from NSE Site First it Create      #
# Dynamic Name According to site                                         #                   
#                                                                        #
##########################################################################
bhav_copy_folder_name = "cm"
bhavcopy_url = "https://www.nseindia.com/content/historical/EQUITIES/"
now = datetime.datetime.now()
bhavcopy_url = bhavcopy_url + str(now.year) + "/" + now.strftime("%b").upper() + "/"
if  now.day < 10 : 
                bhav_copy_folder_name = bhav_copy_folder_name +"0" 
     
bhav_copy_folder_name = bhav_copy_folder_name + str(now.day) + now.strftime("%b").upper() + str(now.year)
bhavcopy_url = bhavcopy_url + bhav_copy_folder_name +"bhav.csv.zip"
r = requests.get(bhavcopy_url)
with open(bhav_copy_folder_name+"bhav.csv.zip",'wb') as f:
    f.write(r.content)
print (" bhavcopy_url ",  bhavcopy_url)  
zip_ref = zipfile.ZipFile(bhav_copy_folder_name+"bhav.csv.zip", 'r')
zip_ref.extractall(bhav_copy_folder_name)
zip_ref.close()
stringToReplace="";
stringToReplaceWith="";
bhav_copy_name=bhav_copy_folder_name+"/"+bhav_copy_folder_name+'bhav.csv'
with open(bhav_copy_name, newline='\n') as csvfile:
    reader = csv.DictReader(csvfile, delimiter = ',')
    for row in reader:
        stringToReplace=row['TIMESTAMP']
        struct_time = time.strptime(row['TIMESTAMP'], "%d-%b-%Y")
        new_date=str(struct_time.tm_year)+"-"
        if struct_time.tm_mon < 10  :
                    new_date=new_date+"0"
        new_date=new_date+str(struct_time.tm_mon)+"-"
        if struct_time.tm_mday < 10  :
                    new_date=new_date+"0"
        new_date=new_date+str(struct_time.tm_mday)
        stringToReplaceWith=new_date
        print(row['SYMBOL'],row['SERIES'],new_date)
        break;


##########################################################################
#                                                                        #
# Below Code is to replace date from format 01-Aug-2017 t0  2017-08-01   #
#                                                                        #
##########################################################################
with open(bhav_copy_name, 'r') as file :
    filedata = file.read()
# Replace the target string
filedata = filedata.replace(stringToReplace, stringToReplaceWith)
# Write the file out again
with open(bhav_copy_name, 'w') as file:
    file.write(filedata)
##########################################################################
#                                                                        #
# Below Code Call A  Bash script to load csv file in mysql tabele Tra-   #
# Saction                                                                #
##########################################################################
comand="cp "+delivery_percent_bhav_copy_name+" ~/"
os.system(comand)
comand="cp "+bhav_copy_name+" ~/"
os.system(comand)
comand="sh loadData.sh ~/"+bhav_copy_folder_name+'bhav.csv'+" "+delivery_percent_bhav_copy_name
os.system(comand)

##########################################################################
#                                                                        #
# Below Code Call A  Bash script to load csv file in mysql tabele Tra-   #
# Saction                                                                #
##########################################################################

stringToappend=''    
#with open('/tmp/dateDataFile.csv', 'r') as f:
with open('/tmp/dateDataFileNumDays.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        stringToappend=stringToappend+row[0]+",,"
#print (stringToappend)

listofSymbol=[]
mapOfSymbolAndDate={}
with open('/tmp/symbolDataFile.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        mapOfSymbolAndDate[row[0]]=stringToappend
        listofSymbol.append(row[0])
#print (listofSymbol)

#for key, value in mapOfSymbolAndDate.iteritems():
#    print "%s,%s" % (key, value)
with open('/tmp/transaction.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        nameString=row[0];
        closeValue=row[5];
        dateString=row[10];
        #print "%s %s" % (nameString, dateString)
        valueF=mapOfSymbolAndDate.get(nameString)
        indexValue=valueF.find(dateString)
        valueF=valueF[:(indexValue+11)]+closeValue+valueF[(indexValue+11):]
        mapOfSymbolAndDate[nameString]=valueF
        #print valueF
        #break;

with open('/tmp/out.csv', 'w') as fout:
    writer = csv.writer(fout)
    for key, value in mapOfSymbolAndDate.items():
        stringToappend=key+","+value
        writer.writerow([u''.join(stringToappend).encode('utf8').strip()])

comand="sh removingUnwantedPadding.sh /tmp/out.csv"
os.system(comand)

with open('/tmp/out.csv', 'r') as f,open('/tmp/tempFinal.csv', 'w') as fout:
    reader = csv.reader(f)
    writer = csv.writer(fout)
    lineNum = 0
    for row in reader:
        totalDays=len(row)
        tempStr=""
        header='SYMBOL'
        for counter in range(0,totalDays):
            if lineNum == 0 and counter%2 != 0:
                header=header+","+row[counter]
            if counter%2 == 0 :
                tempStr=tempStr+row[counter]+","
        #print tempStr
        if lineNum == 0:
            writer.writerow([u''.join(header).encode('utf8').strip()])
            lineNum = 1;
        writer.writerow([u''.join(tempStr).encode('utf8').strip()])   
comand="sh removingUnwantedPadding.sh /tmp/tempFinal.csv"
os.system(comand)

with open('/tmp/tempFinal.csv', 'r') as f,open('/tmp/Final.csv', 'w') as fout:
    reader = csv.reader(f)
    writer = csv.writer(fout)
    tempInt = 0
    for row in reader:
        myOtherString = ','.join(str(elm) for elm in row)
        #print myOtherString
        stringToappend=myOtherString+','
        sumofVal = 0
        if tempInt > 0:
            counter = len(row)-2
            curVal = row[counter]
            prevVal = row[counter - 1]
            while counter > 1:
                if (str(curVal) != '') and (str(prevVal) != ''):
                    curVal = float(curVal)
                    prevVal = float(prevVal)
                    diffVal = round(((curVal - prevVal)*100)/prevVal,3)
                    stringToappend=stringToappend+str(diffVal)+','
                    if (diffVal >= 0):
                        sumofVal = sumofVal + 1
                    else :
                        sumofVal = sumofVal - 1
                else:
                    stringToappend=stringToappend+','
                counter = counter - 1
                curVal = row[counter]
                prevVal = row[counter - 1]
        stringToappend=stringToappend+','+str(sumofVal)
        writer.writerow([u''.join(stringToappend).encode('utf8').strip()])
        tempInt = tempInt + 1
        
comand="sh removingUnwantedPadding.sh /tmp/Final.csv"
os.system(comand)
##########################################################################
#                                                                        #
# Below Code Sending Attachment                                          #
#                                                                        #
##########################################################################
COMMASPACE = ', '
sender = 'analysis.sharemarket@gmail.com'
gmail_password = ''
#recipients = ['EMAIL ADDRESSES HERE SEPARATED BY COMMAS']
recipients = ['er.amit8696@gmail.com','nsnitinsinglaca@gmail.com','dhimannitish88@gmail.com']
# Create the enclosing (outer) message
outer = MIMEMultipart()
outer['Subject'] = 'File ' + 'Final.csv'
outer['To'] = COMMASPACE.join(recipients)
outer['From'] = sender
outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'
fileattachment='/tmp/Final.csv'
# List of attachments
attachments = [fileattachment]
# Add the attachments to the message
for file in attachments:
        try:
            with open(file, 'rb') as fp:
                msg=MIMEBase('application', "octet-stream")
                msg.set_payload(fp.read())
                encoders.encode_base64(msg)
                msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
                outer.attach(msg)
        except:
                print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
                raise
                print("Unable to send the email. Error: ")
composed = outer.as_string()

    # Send the email
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as s:
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(sender, gmail_password)
        s.sendmail(sender, recipients, composed)
        s.close()
        print("Email sent!")
except:
    print("Unable to send the email. Error: ", sys.exc_info()[0])
    print("Unable to send the email. Error: ")
    raise
    print("Unable to send the email. Error: ")
os.remove("/tmp/Final.csv")
os.remove("/tmp/out.csv")
os.remove("/tmp/tempFinal.csv")
os.remove(bhav_copy_folder_name+"bhav.csv.zip")
rmtree(bhav_copy_folder_name)
#SELECT * FROM `transaction` order by symbol , timestamp DESC
#DELETE FROM `transaction` where timestamp='2018-04-12'
