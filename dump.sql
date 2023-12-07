-- MariaDB dump 10.19  Distrib 10.11.4-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: gitstore_db
-- ------------------------------------------------------
-- Server version	10.11.4-MariaDB-1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES
(2,'Hoodies'),
(3,'Mugs'),
(1,'T-shirts');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `color` varchar(20) NOT NULL,
  `size` varchar(30) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `category_id` int(11) NOT NULL,
  `stock` int(11) NOT NULL,
  `discount` int(11) NOT NULL,
  `description` text NOT NULL,
  `image_1` varchar(150) NOT NULL,
  `image_2` varchar(150) NOT NULL,
  `image_3` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES
(8,'hoody_1','red','2X',100.00,2,5,0,'hoody','9ef61c0f5b1cff819021.jpg','b6061977cf626a3a1b48.jpg','c8adffc061fc519fcef5.jpg'),
(9,'hoody_2','black','3X',200.00,2,0,10,'hoody','2d121783c5879e1c6eb0.jpg','b56e6a88f7e86322f4d3.jpg','79841e6ccf9b4ba92561.jpg'),
(10,'hoody_3','white','3X',250.00,2,6,15,'hoody','07cc5e1751196fb8ea0a.jpg','83bb56e487d5ba2762af.jpg','34e15d92282df5ec70ee.jpg'),
(11,'hoody_4','blue','X',200.00,2,10,5,'hoody','6ec9d429b2364b2d2440.jpg','0e94d957ee86342f6b4e.jpg','a22d44b9f51b26be8a91.jpg'),
(12,'hoody_5','red','L',300.00,2,3,0,'hoody','65a2528ceda05400d8b8.jpg','1363ae1ea4ab4ef3a9c6.jpg','9414a63a7cd4e3445f69.jpg'),
(13,'hoody_6','gray','2X',250.00,2,0,0,'hoody','233ef766210e0b1456f1.jpg','5410cb51cbee3cecc318.jpg','be964a9b3b4fe9c85f61.jpg'),
(14,'hoody_7','red','3X',250.00,2,5,0,'hoody','b223eaf3173283ca0111.jpg','e3687b27e67c890e957c.jpg','d8ce928a926751e87e41.jpg'),
(15,'hoody_8','red','L',250.00,2,300,0,'hoody','78891a4c4d5349be8418.jpg','71878fcd5e074430bed8.jpg','10644ccb15723fd0d594.jpg'),
(17,'mug_1','red','none',100.00,3,5,0,'mug','346e493443417dbff183.jpg','da462256f2b0e1cf31f5.jpg','0f0913a2c37935eaf5fa.jpg'),
(18,'mug_2','white','none',100.00,3,0,0,'mugs','d8273ebec057269e80a4.jpg','14531f00ad778bca30e9.jpg','aed70a874e6e9f7ee36c.jpg'),
(19,'mug_3','black','none',150.00,3,6,10,'mug','95a19a03c278ffb18e79.jpg','c2e0c41db48fdc91c1fe.jpg','22bf4fe9dc49cf9313e6.jpg'),
(20,'T-shirt_1','black, red','L, X, 2X',100.00,1,3,0,'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','d142d5e987d45ebfb071.jpg','722e826280f1e9af7835.jpg','239683ee2c5b5e14af50.jpg'),
(21,'T-shirt_2','black','2X',250.00,1,5,4,'t-shirt','266455a0e124113af551.jpg','036c365bd134b76e3dfb.jpg','7c3ec9e1877a72791bfb.jpg'),
(22,'T-shirt_3','red','3X',200.00,1,3,2,'t-shirt','3e5ab2029e2f28d15e4b.jpg','fa5fa86dd2fd9ff2d79a.jpg','11f7f4b42c60b8f049f4.jpg'),
(23,'mug4','red','big',120.00,3,5,0,'mug','58db4514d5628e4f570e.jpg','e0b43b0c62d041a824a9.jpg','ea96249687929afd194a.jpg');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `firstname` varchar(20) NOT NULL,
  `lastname` varchar(20) DEFAULT NULL,
  `email` varchar(120) NOT NULL,
  `password` varchar(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES
(1,'mahmoudelwazeer','Mahmoud','Elwazeer','elwazeermahmoud48@gmail.com','$2b$12$wpUj2ucoNBDDB0w7aloQveSH539/qpBHiDrlfga3mLzpBmVUaxwlO'),
(2,'mahmoudelwadzeer','Mahmoud','dcd','elwazeermahmoud48@gmail.comsadsa','$2b$12$cKmC07W2VESXiw7aHCHrb.WGgnFTzum8k0Xva/V1N8f4AobLLkeke'),
(3,'admin','admin','admin','admin@admin.com','$2b$12$92WGNkNyCZ9RVzPf8szxQuv5gU3iHce2/UIeF3yr929dYIaWpA2fm');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-07 20:32:03
