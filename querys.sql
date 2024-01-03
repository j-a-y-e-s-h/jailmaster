/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Table structure for table `prisoners`
CREATE DATABASE IF NOT EXISTS jms;
USE jms;
DROP TABLE IF EXISTS `prisoners`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prisoners` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `sections` varchar(50) DEFAULT NULL,
  `other_details` varchar(50) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

-- Dumping data for table `prisoners`
LOCK TABLES `prisoners` WRITE;
/*!40000 ALTER TABLE `prisoners` DISABLE KEYS */;
INSERT INTO `prisoners` VALUES (1,'Death shot','Rajastan',404,'sharp shooter','2023-11-1 08:51:19'),(2,'Harley Quinn','Delhi',402,'kill 102','2023-11-1 05:19:02'),(3,'Bloodsport','Mumbai',102, 'One child','2023-11-1 06:58:23');
/*!40000 ALTER TABLE `prisoners` ENABLE KEYS */;
UNLOCK TABLES;

-- Table structure for table `login`
DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `login` (
  `username` varchar(15) NOT NULL,
  `password` varchar(10) NOT NULL,
--   `sec_que` varchar(100) NULL,
--   `sec_ans` varchar(30) NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

-- Dumping data for table `login`
LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES ('1','1','2023-11-1 01:34:25');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

-- Table structure for table `prison_allocate`
DROP TABLE IF EXISTS `prison_allocate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prison_allocate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `p_id` int(11) DEFAULT NULL,
  `p_a_date` datetime DEFAULT NULL,
  `allocate` datetime DEFAULT NULL,
  `released` datetime DEFAULT NULL,
  `Supplies` varchar(50) DEFAULT NULL,
  `p_c_a_id` int(11) DEFAULT NULL,
  `p_c_a_type` char(1) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `FK_prisoners` (`p_id`),
  KEY `FK_prison_allocate` (`p_c_a_id`),
  CONSTRAINT `FK_prisoners` FOREIGN KEY (`p_id`) REFERENCES `prisoners` (`id`) ON DELETE CASCADE,
  CONSTRAINT `FK_prison_cell` FOREIGN KEY (`p_c_a_id`) REFERENCES `prison_cell` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

-- Dumping data for table `prison_allocate`
LOCK TABLES `prison_allocate` WRITE;
/*!40000 ALTER TABLE `prison_allocate` DISABLE KEYS */;
INSERT INTO `prison_allocate` VALUES (1,1,null,'2022-11-01 00:00:00','2023-11-01 00:00:00',0,3,'T','2022-11-01 07:05:05'),
 (2,2,null,'2023-10-17 05:33:05',NULL,NULL,1,'G','2023-10-17 05:33:05');
/*!40000 ALTER TABLE `prison_allocate` ENABLE KEYS */;
UNLOCK TABLES;

-- Table structure for table `prison_cell`
DROP TABLE IF EXISTS `prison_cell`;
CREATE TABLE `prison_cell` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `prison_no` int(11) DEFAULT NULL,
  `charges` int(11) DEFAULT NULL,
  `prison_type` char(1) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `prison_no` (`prison_no`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table `prison_cell`
LOCK TABLES `prison_cell` WRITE;
/*!40000 ALTER TABLE `prison_cell` DISABLE KEYS */;
INSERT INTO `prison_cell` VALUES (1,1,5000,'T','2023-10-15 07:05:03'),(3,2,100,'G','2023-10-16 10:38:49'),(4,10,100,'G','2023-10-17 05:15:29');
/*!40000 ALTER TABLE `prison_cell` ENABLE KEYS */;
UNLOCK TABLES;

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;