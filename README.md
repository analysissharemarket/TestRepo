# TestRepo

Add Line  secure-file-priv = ""
in file /etc/mysql/my.cnf 
in case of ubuntu installation

!includedir /etc/mysql/conf.d/
!includedir /etc/mysql/mysql.conf.d/
[mysqld]
secure-file-priv = ""

create database shareDb

create table 

nse_security_full_bhavcopy 

+-------------+-----------------------+------+-----+---------+-------+
| Field       | Type                  | Null | Key | Default | Extra |
+-------------+-----------------------+------+-----+---------+-------+
| SYMBOL      | varchar(15)           | NO   |     | NULL    |       |
| SERIES      | char(2)               | NO   |     | NULL    |       |
| DATE1       | date                  | NO   |     | NULL    |       |
| prevclose   | decimal(8,2) unsigned | NO   |     | NULL    |       |
| open        | decimal(8,2) unsigned | NO   |     | NULL    |       |
| high        | decimal(8,2) unsigned | NO   |     | NULL    |       |
| low         | decimal(8,2) unsigned | NO   |     | NULL    |       |
| last        | decimal(8,2) unsigned | NO   |     | NULL    |       |
| close       | decimal(8,2) unsigned | NO   |     | NULL    |       |
| avrggprice  | decimal(8,2) unsigned | NO   |     | NULL    |       |
| tottrdqty   | bigint(20) unsigned   | NO   |     | NULL    |       |
| turnovrlacs | bigint(20) unsigned   | NO   |     | NULL    |       |
| nooftrade   | bigint(20) unsigned   | NO   |     | NULL    |       |
| delvqty     | int(11)               | NO   |     | NULL    |       |
| delvper     | int(11)               | NO   |     | NULL    |       |
+-------------+-----------------------+------+-----+---------+-------+

CREATE TABLE `nse_security_full_bhavcopy` (
  `SYMBOL` varchar(15) NOT NULL,
  `SERIES` char(2) NOT NULL,
  `DATE1` date NOT NULL,
  `prevclose` decimal(8,2) unsigned NOT NULL,
  `open` decimal(8,2) unsigned NOT NULL,
  `high` decimal(8,2) unsigned NOT NULL,
  `low` decimal(8,2) unsigned NOT NULL,
  `last` decimal(8,2) unsigned NOT NULL,
  `close` decimal(8,2) unsigned NOT NULL,
  `avrggprice` decimal(8,2) unsigned NOT NULL,
  `tottrdqty` bigint(20) unsigned NOT NULL,
  `turnovrlacs` bigint(20) unsigned NOT NULL,
  `nooftrade` bigint(20) unsigned NOT NULL,
  `delvqty` int(11) NOT NULL,
  `delvper` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

2) transaction 

+-------------+-------------+------+-----+---------+-------+
| Field       | Type        | Null | Key | Default | Extra |
+-------------+-------------+------+-----+---------+-------+
| SYMBOL      | varchar(30) | NO   |     | NULL    |       |
| SERIES      | varchar(4)  | NO   |     | NULL    |       |
| OPEN        | double      | NO   |     | NULL    |       |
| HIGH        | double      | NO   |     | NULL    |       |
| LOW         | double      | NO   |     | NULL    |       |
| CLOSE       | double      | NO   |     | NULL    |       |
| LAST        | double      | NO   |     | NULL    |       |
| PREVCLOSE   | double      | NO   |     | NULL    |       |
| TOTTRDQTY   | bigint(20)  | NO   |     | NULL    |       |
| TOTTRDVAL   | double      | NO   |     | NULL    |       |
| TIMESTAMP   | date        | NO   |     | NULL    |       |
| TOTALTRADES | bigint(20)  | NO   |     | NULL    |       |
| ISIN        | varchar(30) | NO   |     | NULL    |       |
+-------------+-------------+------+-----+---------+-------+

 CREATE TABLE `transaction` (
  `SYMBOL` varchar(30) NOT NULL,
  `SERIES` varchar(4) NOT NULL,
  `OPEN` double NOT NULL,
  `HIGH` double NOT NULL,
  `LOW` double NOT NULL,
  `CLOSE` double NOT NULL,
  `LAST` double NOT NULL,
  `PREVCLOSE` double NOT NULL,
  `TOTTRDQTY` bigint(20) NOT NULL,
  `TOTTRDVAL` double NOT NULL,
  `TIMESTAMP` date NOT NULL,
  `TOTALTRADES` bigint(20) NOT NULL,
  `ISIN` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
