sudo rm -rf  /tmp/dateDataFile.csv
sudo rm -rf  /tmp/dateDataFileNumDays.csv
sudo rm -rf  /tmp/transaction.csv
sudo rm -rf /tmp/symbolDataFile.csv
sudo chown mysql:mysql ~/*.csv
#sudo chmod 777 ~/*.csv
mysql -e " LOAD DATA LOCAL INFILE '$1' INTO TABLE transaction FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES" -uroot -hlocalhost -proot123 shareDb
mysql -e " LOAD DATA LOCAL INFILE '$2' INTO TABLE nse_security_full_bhavcopy FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES" -uroot -hlocalhost -proot123 shareDb
rm -rf $1
mysql -e " SELECT distinct(timestamp) FROM transaction WHERE SERIES='EQ' ORDER BY TIMESTAMP INTO OUTFILE '/tmp/dateDataFile.csv'	FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' " -uroot -hlocalhost -proot123 shareDb
numOfDays=20
fromDate=`tail -n $numOfDays /tmp/dateDataFile.csv | head -1`
mysql -e " SELECT distinct(timestamp) FROM transaction WHERE SERIES='EQ' AND TIMESTAMP >= '$fromDate' ORDER BY TIMESTAMP INTO OUTFILE '/tmp/dateDataFileNumDays.csv'	FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' " -uroot -hlocalhost -proot123 shareDb
mysql -e " SELECT * FROM transaction WHERE SERIES='EQ' AND TIMESTAMP >= '$fromDate' ORDER BY SYMBOL, TIMESTAMP INTO OUTFILE '/tmp/transaction.csv'	FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' " -uroot -hlocalhost -proot123 shareDb
mysql -e " SELECT distinct(SYMBOL) FROM transaction WHERE SERIES='EQ' AND TIMESTAMP >= '$fromDate' ORDER BY SYMBOL INTO OUTFILE '/tmp/symbolDataFile.csv'	FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' " -uroot -hlocalhost -proot123 shareDb
sudo chmod 777 /tmp/dateDataFile.csv
sudo chmod 777 /tmp/dateDataFileNumDays.csv
sudo chmod 777 /tmp/transaction.csv
sudo chmod 777 /tmp/symbolDataFile.csv
