-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: onlineshopping
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `administrator`
--

DROP TABLE IF EXISTS `administrator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrator` (
  `admno` int NOT NULL AUTO_INCREMENT,
  `admaccount` varchar(12) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `telnum` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`admno`),
  KEY `fk1_idx` (`admaccount`),
  CONSTRAINT `admfk1` FOREIGN KEY (`admaccount`) REFERENCES `users` (`account`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrator`
--

LOCK TABLES `administrator` WRITE;
/*!40000 ALTER TABLE `administrator` DISABLE KEYS */;
INSERT INTO `administrator` VALUES (1,'333331','15951833699'),(2,'333332','15312020827');
/*!40000 ALTER TABLE `administrator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `aftersales`
--

DROP TABLE IF EXISTS `aftersales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aftersales` (
  `aftno` int NOT NULL,
  `ono` int NOT NULL,
  `sender` varchar(20) NOT NULL,
  `content` varchar(100) NOT NULL,
  PRIMARY KEY (`aftno`,`ono`),
  KEY `fk1_idx` (`ono`),
  KEY `fk2_idx` (`sender`),
  CONSTRAINT `aftfk1` FOREIGN KEY (`ono`) REFERENCES `orders` (`ono`),
  CONSTRAINT `aftfk2` FOREIGN KEY (`sender`) REFERENCES `users` (`account`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aftersales`
--

LOCK TABLES `aftersales` WRITE;
/*!40000 ALTER TABLE `aftersales` DISABLE KEYS */;
INSERT INTO `aftersales` VALUES (1,1,'111112','发顺丰'),(1,2,'111111','你好'),(1,12,'111111','111'),(2,1,'222222','好的'),(2,2,'111111','泡芙一点都不好吃'),(2,12,'222221','5453'),(3,1,'111112','谢谢'),(3,2,'222221','真的吗'),(4,2,'222221','我不信');
/*!40000 ALTER TABLE `aftersales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `collection`
--

DROP TABLE IF EXISTS `collection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `collection` (
  `cno` int NOT NULL,
  `gno` int NOT NULL,
  PRIMARY KEY (`cno`,`gno`),
  KEY `cfk2_idx` (`gno`),
  CONSTRAINT `cfk1` FOREIGN KEY (`cno`) REFERENCES `customer` (`cno`),
  CONSTRAINT `cfk2` FOREIGN KEY (`gno`) REFERENCES `goods` (`gno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collection`
--

LOCK TABLES `collection` WRITE;
/*!40000 ALTER TABLE `collection` DISABLE KEYS */;
INSERT INTO `collection` VALUES (1,2),(1,3),(2,4),(3,4),(1,5),(1,10);
/*!40000 ALTER TABLE `collection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `cno` int NOT NULL AUTO_INCREMENT,
  `caccount` varchar(12) NOT NULL,
  `name` varchar(10) NOT NULL DEFAULT '还没有取名',
  `telnum` varchar(11) DEFAULT NULL,
  `address` varchar(45) DEFAULT NULL,
  `bank` varchar(15) DEFAULT NULL,
  `bcnum` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`cno`),
  UNIQUE KEY `cno_UNIQUE` (`cno`),
  KEY `cfk1_idx` (`caccount`),
  CONSTRAINT `custfk1` FOREIGN KEY (`caccount`) REFERENCES `users` (`account`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'111111','路人甲','13851239561','奎尔萨拉斯1','中国银行5','7945'),(2,'111112','赵一','13951687532','天辉遗迹','中国银行','4643435'),(3,'111113','王五','15936885172','华工北二201','农业银行','123456'),(4,'316456','还没有取名',NULL,NULL,NULL,NULL),(5,'123123','还没有取名',NULL,NULL,NULL,NULL),(6,'456789','还没有取名',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `extraaftersales`
--

DROP TABLE IF EXISTS `extraaftersales`;
/*!50001 DROP VIEW IF EXISTS `extraaftersales`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `extraaftersales` AS SELECT 
 1 AS `aftno`,
 1 AS `ono`,
 1 AS `sender`,
 1 AS `content`,
 1 AS `cno`,
 1 AS `sno`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `extragoods`
--

DROP TABLE IF EXISTS `extragoods`;
/*!50001 DROP VIEW IF EXISTS `extragoods`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `extragoods` AS SELECT 
 1 AS `商品编号`,
 1 AS `商品名称`,
 1 AS `商品状态`,
 1 AS `商品库存量`,
 1 AS `商品介绍`,
 1 AS `商家编号`,
 1 AS `商品价格`,
 1 AS `商家名称`,
 1 AS `商品类别`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `extraorder`
--

DROP TABLE IF EXISTS `extraorder`;
/*!50001 DROP VIEW IF EXISTS `extraorder`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `extraorder` AS SELECT 
 1 AS `商家编号`,
 1 AS `订单编号`,
 1 AS `顾客编号`,
 1 AS `顾客姓名`,
 1 AS `顾客联系方式`,
 1 AS `收货地址`,
 1 AS `商品编号`,
 1 AS `商品名称`,
 1 AS `商品数量`,
 1 AS `订单总价`,
 1 AS `订单状态`,
 1 AS `下单时间`,
 1 AS `订单评价`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `extraorder2`
--

DROP TABLE IF EXISTS `extraorder2`;
/*!50001 DROP VIEW IF EXISTS `extraorder2`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `extraorder2` AS SELECT 
 1 AS `顾客编号`,
 1 AS `订单编号`,
 1 AS `商品名`,
 1 AS `商品编号`,
 1 AS `商品单价`,
 1 AS `商品数量`,
 1 AS `订单总价`,
 1 AS `订单状态`,
 1 AS `订单生成时间`,
 1 AS `收货地址`,
 1 AS `评价`,
 1 AS `商家编号`,
 1 AS `商家名`,
 1 AS `商家电话`,
 1 AS `管理员电话`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `goods`
--

DROP TABLE IF EXISTS `goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `goods` (
  `gno` int NOT NULL AUTO_INCREMENT,
  `sno` int NOT NULL,
  `gcno` int DEFAULT NULL,
  `name` varchar(10) NOT NULL,
  `amount` int NOT NULL,
  `introduction` varchar(100) DEFAULT NULL,
  `price` double NOT NULL,
  `state` varchar(45) NOT NULL DEFAULT '下架',
  PRIMARY KEY (`gno`),
  KEY `gfk1_idx` (`sno`),
  KEY `gfk2_idx` (`gcno`),
  CONSTRAINT `gfk1` FOREIGN KEY (`sno`) REFERENCES `seller` (`sno`),
  CONSTRAINT `gfk2` FOREIGN KEY (`gcno`) REFERENCES `goodscategory` (`gcno`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods`
--

LOCK TABLES `goods` WRITE;
/*!40000 ALTER TABLE `goods` DISABLE KEYS */;
INSERT INTO `goods` VALUES (1,1,1,'泡芙',996,'好吃的泡芙',25,'在售'),(2,1,1,'蛋挞',20,'好吃的蛋挞',5,'在售'),(3,1,1,'麻薯',100,'好吃的麻薯',15,'下架'),(4,2,2,'鼠标垫',99,'普普通通的鼠标垫',30,'在售'),(5,2,3,'蓝牙耳机',18,'普普通通的蓝牙耳机',180,'在售'),(6,2,3,'笔记本电脑',0,'甩卖啦',1000,'在售'),(8,1,1,'桃酥',50,'好吃的桃酥',5,'下架'),(9,4,3,'手机',10,'大米手机',1500,'在售'),(10,3,1,'水牛奶',100,'营养牛奶',80,'在售');
/*!40000 ALTER TABLE `goods` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `goods_BEFORE_UPDATE` BEFORE UPDATE ON `goods` FOR EACH ROW BEGIN
declare msg char(20);
if new.amount<0
then
set msg='not enough goods';
signal sqlstate 'HY000' set message_text=msg;
elseif new.price<=0
then
set msg='price wrong';
signal sqlstate 'HY000' set message_text=msg;
end if;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `goodscategory`
--

DROP TABLE IF EXISTS `goodscategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `goodscategory` (
  `gcno` int NOT NULL AUTO_INCREMENT,
  `categoryname` varchar(30) NOT NULL,
  PRIMARY KEY (`gcno`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goodscategory`
--

LOCK TABLES `goodscategory` WRITE;
/*!40000 ALTER TABLE `goodscategory` DISABLE KEYS */;
INSERT INTO `goodscategory` VALUES (1,'食品'),(2,'日用品'),(3,'电子商品'),(4,'奢侈品'),(5,'其他'),(9,'try1');
/*!40000 ALTER TABLE `goodscategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `goodsgcno`
--

DROP TABLE IF EXISTS `goodsgcno`;
/*!50001 DROP VIEW IF EXISTS `goodsgcno`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `goodsgcno` AS SELECT 
 1 AS `gno`,
 1 AS `sno`,
 1 AS `gcno`,
 1 AS `name`,
 1 AS `amount`,
 1 AS `introduction`,
 1 AS `price`,
 1 AS `state`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `goodsgno`
--

DROP TABLE IF EXISTS `goodsgno`;
/*!50001 DROP VIEW IF EXISTS `goodsgno`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `goodsgno` AS SELECT 
 1 AS `gno`,
 1 AS `sno`,
 1 AS `gcno`,
 1 AS `name`,
 1 AS `amount`,
 1 AS `introduction`,
 1 AS `price`,
 1 AS `state`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `goodssno`
--

DROP TABLE IF EXISTS `goodssno`;
/*!50001 DROP VIEW IF EXISTS `goodssno`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `goodssno` AS SELECT 
 1 AS `gno`,
 1 AS `sno`,
 1 AS `gcno`,
 1 AS `name`,
 1 AS `amount`,
 1 AS `introduction`,
 1 AS `price`,
 1 AS `state`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `ordaftersales`
--

DROP TABLE IF EXISTS `ordaftersales`;
/*!50001 DROP VIEW IF EXISTS `ordaftersales`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `ordaftersales` AS SELECT 
 1 AS `aftno`,
 1 AS `ono`,
 1 AS `sender`,
 1 AS `content`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `ono` int NOT NULL AUTO_INCREMENT,
  `cno` int NOT NULL,
  `gno` int NOT NULL,
  `amount` int NOT NULL,
  `state` enum('待发货','待收货','已收货') NOT NULL,
  `time` varchar(50) NOT NULL,
  `remark` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ono`),
  UNIQUE KEY `ono_UNIQUE` (`ono`),
  KEY `ofk1_idx` (`cno`),
  KEY `ofk2_idx` (`gno`),
  CONSTRAINT `ofk1` FOREIGN KEY (`cno`) REFERENCES `customer` (`cno`),
  CONSTRAINT `ofk2` FOREIGN KEY (`gno`) REFERENCES `goods` (`gno`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,2,4,1,'已收货','2021.8.21.09.15',NULL),(2,1,1,10,'已收货','2021.8.23.21.59','321'),(3,2,3,5,'待发货','22.44.13',NULL),(6,1,1,33,'待发货','17:27:09',NULL),(12,1,1,10,'待收货','13:39:11',NULL);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `orders_AFTER_INSERT` AFTER INSERT ON `orders` FOR EACH ROW BEGIN
update goods set goods.amount=goods.amount-new.amount where goods.gno=new.gno;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `seller`
--

DROP TABLE IF EXISTS `seller`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seller` (
  `sno` int NOT NULL AUTO_INCREMENT,
  `saccount` varchar(12) NOT NULL,
  `admno` int NOT NULL DEFAULT '1',
  `name` varchar(10) NOT NULL DEFAULT '还没起名的商家',
  `introduction` varchar(100) DEFAULT NULL,
  `telnum` varchar(11) DEFAULT NULL,
  `bank` varchar(15) DEFAULT NULL,
  `bcnum` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`sno`),
  KEY `sfk1_idx` (`admno`),
  KEY `sfk2_idx` (`saccount`),
  CONSTRAINT `sfk1` FOREIGN KEY (`admno`) REFERENCES `administrator` (`admno`),
  CONSTRAINT `sfk2` FOREIGN KEY (`saccount`) REFERENCES `users` (`account`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seller`
--

LOCK TABLES `seller` WRITE;
/*!40000 ALTER TABLE `seller` DISABLE KEYS */;
INSERT INTO `seller` VALUES (1,'222221',1,'泸溪海','好吃的甜点','13526857939','中国银行','1249'),(2,'222222',2,'散步者','高端漫步者','15962437891','中国银行','542'),(3,'222223',2,'很牛','专卖牛奶','18945621379','工商银行','5464'),(4,'222224',1,'大米','电子产品','14689256789','农业银行','456');
/*!40000 ALTER TABLE `seller` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `account` varchar(12) NOT NULL,
  `password` varchar(15) NOT NULL,
  `identity` enum('顾客','商家','管理员') NOT NULL,
  PRIMARY KEY (`account`),
  UNIQUE KEY `account_UNIQUE` (`account`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('111111','123456','顾客'),('111112','123456','顾客'),('111113','123456','顾客'),('123123','123123','顾客'),('222221','123456','商家'),('222222','123456','商家'),('222223','123456','商家'),('222224','123456','商家'),('316456','123456','顾客'),('333331','123456','管理员'),('333332','123456','管理员'),('456789','123123','顾客');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `users_AFTER_INSERT` AFTER INSERT ON `users` FOR EACH ROW BEGIN
if new.identity='顾客'
THEN
 insert into customer(caccount) values(new.account);
elseif new.identity='商家'
THEN
 insert into seller(saccount)  values(new.account); 
else 
insert into administrator(admaccount)  values(new.account);
END if;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Dumping events for database 'onlineshopping'
--

--
-- Dumping routines for database 'onlineshopping'
--
/*!50003 DROP PROCEDURE IF EXISTS `ordertable` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `ordertable`(IN tname varchar(64),IN colname varchar(64))
BEGIN
SET @sqlcmd = CONCAT('select * from ', tname, ' order by ', colname);
PREPARE stmt FROM @sqlcmd;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Final view structure for view `extraaftersales`
--

/*!50001 DROP VIEW IF EXISTS `extraaftersales`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `extraaftersales` AS select `aftersales`.`aftno` AS `aftno`,`aftersales`.`ono` AS `ono`,`aftersales`.`sender` AS `sender`,`aftersales`.`content` AS `content`,`customer`.`cno` AS `cno`,`seller`.`sno` AS `sno` from ((((`aftersales` join `orders`) join `customer`) join `goods`) join `seller`) where ((`aftersales`.`ono` = `orders`.`ono`) and (`orders`.`cno` = `customer`.`cno`) and (`orders`.`gno` = `goods`.`gno`) and (`goods`.`sno` = `seller`.`sno`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `extragoods`
--

/*!50001 DROP VIEW IF EXISTS `extragoods`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `extragoods` AS select `goods`.`gno` AS `商品编号`,`goods`.`name` AS `商品名称`,`goods`.`state` AS `商品状态`,`goods`.`amount` AS `商品库存量`,`goods`.`introduction` AS `商品介绍`,`seller`.`sno` AS `商家编号`,`goods`.`price` AS `商品价格`,`seller`.`name` AS `商家名称`,`goodscategory`.`categoryname` AS `商品类别` from ((`goods` join `seller`) join `goodscategory`) where ((`goods`.`sno` = `seller`.`sno`) and (`goods`.`gcno` = `goodscategory`.`gcno`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `extraorder`
--

/*!50001 DROP VIEW IF EXISTS `extraorder`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `extraorder` AS select `extragoods`.`商家编号` AS `商家编号`,`orders`.`ono` AS `订单编号`,`orders`.`cno` AS `顾客编号`,`customer`.`name` AS `顾客姓名`,`customer`.`telnum` AS `顾客联系方式`,`customer`.`address` AS `收货地址`,`orders`.`gno` AS `商品编号`,`extragoods`.`商品名称` AS `商品名称`,`orders`.`amount` AS `商品数量`,(`orders`.`amount` * `extragoods`.`商品价格`) AS `订单总价`,`orders`.`state` AS `订单状态`,`orders`.`time` AS `下单时间`,`orders`.`remark` AS `订单评价` from ((`orders` join `customer`) join `extragoods`) where ((`orders`.`cno` = `customer`.`cno`) and (`extragoods`.`商品编号` = `orders`.`gno`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `extraorder2`
--

/*!50001 DROP VIEW IF EXISTS `extraorder2`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `extraorder2` AS select `customer`.`cno` AS `顾客编号`,`orders`.`ono` AS `订单编号`,`goods`.`name` AS `商品名`,`goods`.`gno` AS `商品编号`,`goods`.`price` AS `商品单价`,`orders`.`amount` AS `商品数量`,(`orders`.`amount` * `goods`.`price`) AS `订单总价`,`orders`.`state` AS `订单状态`,`orders`.`time` AS `订单生成时间`,`customer`.`address` AS `收货地址`,`orders`.`remark` AS `评价`,`seller`.`sno` AS `商家编号`,`seller`.`name` AS `商家名`,`seller`.`telnum` AS `商家电话`,`administrator`.`telnum` AS `管理员电话` from ((((`orders` join `goods`) join `seller`) join `administrator`) join `customer`) where ((`orders`.`gno` = `goods`.`gno`) and (`goods`.`sno` = `seller`.`sno`) and (`seller`.`admno` = `administrator`.`admno`) and (`orders`.`cno` = `customer`.`cno`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `goodsgcno`
--

/*!50001 DROP VIEW IF EXISTS `goodsgcno`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `goodsgcno` AS select `goods`.`gno` AS `gno`,`goods`.`sno` AS `sno`,`goods`.`gcno` AS `gcno`,`goods`.`name` AS `name`,`goods`.`amount` AS `amount`,`goods`.`introduction` AS `introduction`,`goods`.`price` AS `price`,`goods`.`state` AS `state` from `goods` order by `goods`.`gcno` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `goodsgno`
--

/*!50001 DROP VIEW IF EXISTS `goodsgno`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `goodsgno` AS select `goods`.`gno` AS `gno`,`goods`.`sno` AS `sno`,`goods`.`gcno` AS `gcno`,`goods`.`name` AS `name`,`goods`.`amount` AS `amount`,`goods`.`introduction` AS `introduction`,`goods`.`price` AS `price`,`goods`.`state` AS `state` from `goods` order by `goods`.`gno` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `goodssno`
--

/*!50001 DROP VIEW IF EXISTS `goodssno`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `goodssno` AS select `goods`.`gno` AS `gno`,`goods`.`sno` AS `sno`,`goods`.`gcno` AS `gcno`,`goods`.`name` AS `name`,`goods`.`amount` AS `amount`,`goods`.`introduction` AS `introduction`,`goods`.`price` AS `price`,`goods`.`state` AS `state` from `goods` order by `goods`.`sno` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `ordaftersales`
--

/*!50001 DROP VIEW IF EXISTS `ordaftersales`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `ordaftersales` AS select `aftersales`.`aftno` AS `aftno`,`aftersales`.`ono` AS `ono`,`aftersales`.`sender` AS `sender`,`aftersales`.`content` AS `content` from `aftersales` order by `aftersales`.`ono` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-08-31 14:13:50
