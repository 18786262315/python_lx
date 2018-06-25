-- MySQL dump 10.13  Distrib 5.5.42, for Linux (x86_64)
--
-- Host: localhost    Database: jingxuan
-- ------------------------------------------------------
-- Server version	5.5.42-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `mr_province`
--

DROP TABLE IF EXISTS `mr_province`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mr_province` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(6) NOT NULL,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mr_province`
--

LOCK TABLES `mr_province` WRITE;
/*!40000 ALTER TABLE `mr_province` DISABLE KEYS */;
INSERT INTO `mr_province` VALUES (1,'110000','北京市'),(2,'120000','天津市'),(3,'130000','河北省'),(4,'140000','山西省'),(5,'150000','内蒙古'),(6,'210000','辽宁省'),(7,'220000','吉林省'),(8,'230000','黑龙江'),(9,'310000','上海市'),(10,'320000','江苏省'),(11,'330000','浙江省'),(12,'340000','安徽省'),(13,'350000','福建省'),(14,'360000','江西省'),(15,'370000','山东省'),(16,'410000','河南省'),(17,'420000','湖北省'),(18,'430000','湖南省'),(19,'440000','广东省'),(20,'450000','广  西'),(21,'460000','海南省'),(22,'500000','重庆市'),(23,'510000','四川省'),(24,'520000','贵州省'),(25,'530000','云南省'),(26,'540000','西  藏'),(27,'610000','陕西省'),(28,'620000','甘肃省'),(29,'630000','青海省'),(30,'640000','宁  夏'),(31,'650000','新  疆'),(32,'710000','台湾省'),(33,'810000','香  港'),(34,'820000','澳  门');
/*!40000 ALTER TABLE `mr_province` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-28 22:29:12
