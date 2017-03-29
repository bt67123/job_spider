# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.5.49)
# Database: lagou
# Generation Time: 2017-03-29 16:09:57 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table job_counts
# ------------------------------------------------------------

DROP TABLE IF EXISTS `job_counts`;

CREATE TABLE `job_counts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `keyword` varchar(50) DEFAULT NULL,
  `total` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table jobs
# ------------------------------------------------------------

DROP TABLE IF EXISTS `jobs`;

CREATE TABLE `jobs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `positionId` int(11) NOT NULL,
  `positionName` varchar(50) DEFAULT NULL,
  `salary` varchar(50) DEFAULT NULL,
  `education` varchar(10) DEFAULT NULL,
  `financeStage` varchar(20) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  `companyFullName` varchar(50) DEFAULT NULL,
  `companyShortName` varchar(50) DEFAULT NULL,
  `companyLabelList` varchar(100) DEFAULT NULL,
  `companySize` varchar(20) DEFAULT NULL,
  `companyLogo` varchar(200) DEFAULT NULL,
  `district` varchar(20) DEFAULT NULL,
  `companyId` int(11) DEFAULT NULL,
  `industryField` varchar(50) DEFAULT NULL,
  `positionLables` varchar(100) DEFAULT NULL,
  `workYear` varchar(20) DEFAULT NULL,
  `lastLogin` varchar(30) DEFAULT NULL,
  `jobNature` varchar(20) DEFAULT NULL,
  `businessZones` varchar(50) DEFAULT NULL,
  `firstType` varchar(20) DEFAULT NULL,
  `secondType` varchar(20) DEFAULT NULL,
  `positionAdvantage` varchar(100) DEFAULT NULL,
  `publisherId` int(11) DEFAULT NULL,
  `gradeDescription` varchar(50) DEFAULT NULL,
  `createTime` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
