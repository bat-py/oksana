-- MySQL dump 10.13  Distrib 8.0.26, for Linux (x86_64)
--
-- Host: localhost    Database: oksana
-- ------------------------------------------------------
-- Server version	8.0.26-0ubuntu0.20.04.3

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

--
-- Table structure for table `bot_messages`
--

DROP TABLE IF EXISTS `bot_messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bot_messages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `text_id` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `text` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bot_messages`
--

LOCK TABLES `bot_messages` WRITE;
/*!40000 ALTER TABLE `bot_messages` DISABLE KEYS */;
INSERT INTO `bot_messages` VALUES (1,'main_menu_balance','<b>Ваш баланс:</b> 0 RUB / 0.00 BTC / 0.00 LTC'),(2,'main_menu_city','<b>Для покупки отправьте цифру своего города из списка снизу:</b>'),(3,'list_commands','$ - Как оформить ненаход?\n# - В главное меню\n+ - Прайс\n? - Помощь'),(4,'order_bot','<b>======================================================</b>\r\nХочешь такого же бота? Пиши в Телеграм: <b>botoshop_old</b>'),(5,'main_menu_comments','<b>Отзывы покупателей</b> (отправьте 👉 9️⃣9️⃣9️⃣)\n<b>Оставить отзыв</b> (отправьте 👉 7️⃣7️⃣7️⃣)'),(6,'disput_menu','1️ ❗️Претензия о ненаходе принимаются не позже 4-ёх часов после получения адреса!❗️\r\n\r\nЕсли Вы обратились позже, чем через отведенное время - автоматом получаете отказ\r\n\r\n2️ ❗️Вы должны максимально подробно объяснить свою проблему оператору\r\n , желательно одним-двумя сообщениями, ДАЖЕ ЕСЛИ ОПЕРАТОРА НЕТ В СЕТИ ❗️\r\n\r\nПример обращения:\r\n1. Номер заказа или комментарий, адрес ТЕКСТОМ, как его выдал Вам сайт или бот(Выделить, скопировать, вставить)\r\n2. Причина ненахода (не то описание, взорвали и т.д.)\r\n3. Фото с места ( минимум две, одна с расстояния , что бы курьер мог сделать отметку)Притензии без фото не рассматриваются! Фото с места очень важно! \r\n\r\nСоставленную заявку отправлять оператору в Telegram -   \r\n@ K a t e O f f  - пиcать в поиске в телеграме БЕЗ ПРОБЕЛОВ'),(7,'help_menu','Продавец еще не задал сообщение в помощи'),(8,'now_in_stock ','<b>Сейчас в наличии:</b>'),(9,'leave_comment','Отзывы можно оставлять только после покупок'),(10,'wrong_request','Неправильный выбор, попробуйте еще раз. \r\nДля выбора варианта отправьте ЧИСЛО или СИМВОЛ слева от нужного варианта, например 2 или #'),(11,'show_more','Показать еще (отправьте 👉 9⃣9⃣9⃣)'),(12,'you_choise','<b>Вы выбрали</b>'),(13,'city','🏡 <b>Город:</b>'),(14,'choose_product','<b>Выберите товар:</b>'),(15,'product','📦 <b>Товар:</b>'),(16,'district','📋 <b>Район:</b>'),(17,'massa','📋 <b>Фасовка:</b>'),(18,'choose_payment','<b>Выберите способ оплаты:</b>'),(19,'no_in_stock','В выбранном городе закончились товары, приходите чуть позже.'),(20,'choose_fasovka','<b>Выберите фасовку:</b>'),(21,'choose_district','<b>Выберите район:</b>'),(22,'pay_with_balance','Оплата товара с баланса'),(23,'your_balance','<b>Ваш баланс:</b>\r\n0 рублей'),(24,'needed_balance','<b>Необходимый баланс:</b>'),(25,'pay','1️⃣: Оплатить'),(26,'needed_balance_continue','Для оплаты товара балансом, на Вашем счету должен быть положительный баланс, которого хватит для покупки товара.'),(30,'use_more_commission','ЧТОБЫ ОПЛАТА БЫСТРЕЕ ЗАЧИСЛИЛАСЬ, СТАВЬТЕ ВЫСОКУЮ КОМИССИЮ\r\n\r\nЧтобы получить кошелек отдельным сообщением отправьте 👉 !myltc\r\n\r\n1⃣: Проверить оплату'),(31,'warning_auto_change','В результате обмена Вы получите BTC, товар будет автоматически куплен за BTC, с Вашего BTC-баланса.'),(32,'warning_may_change_price','ВАЖНО! Оплата идентифицируется по стоимости. Диапазон колебания цены 1-50 рублей.\r\nСумма оплаты указанная для каждого из обменников ПРИБЛИЗИТЕЛЬНАЯ.\r\nТочную сумму Вы получите вместе с реквизитами на оплату.'),(33,'error_400','Unknown error occured! Details : 400'),(34,'qiwi_info','✅ ВЫДАННЫЕ РЕКВИЗИТЫ ДЕЙСТВУЮТ 1 ЧАС\r\n✅ ВЫ ПОТЕРЯЕТЕ ДЕНЬГИ, ЕСЛИ ОПЛАТИТЕ ПОЗЖЕ\r\n✅ ПЕРЕВОДИТЕ ТОЧНУЮ СУММУ. НЕВЕРНАЯ СУММА НЕ БУДЕТ ЗАЧИСЛЕНА.\r\n✅ ОПЛАТА ДОЛЖНА ПРОХОДИТЬ ОДНИМ ПЛАТЕЖОМ.\r\n✅ ОПЛАТА ПРИНИМАЕТСЯ ТОЛЬКО НА QIWI-КОШЕЛЕК.\r\n✅ ПРОБЛЕМЫ С ОПЛАТОЙ? ПИСАТЬ В TELEGRAM : getbtcbot\r\n✅ С ПРОБЛЕМНОЙ ЗАЯВКОЙ ОБРАЩАЙТЕСЬ НЕ ПОЗДНЕЕ 24 ЧАСОВ С МОМЕНТА ОПЛАТЫ.'),(35,'thirteen_page_buttons','3⃣: FastChange (CARD/TELE2) RUB\r\n4⃣: getBTC (CARD/Тинькофф Мобайл) RUB\r\n5⃣: Exchanger Charlie RUB\r\n6⃣: Exchanger Alfa RUB'),(36,'card_info','✅ ВЫДАННЫЕ РЕКВИЗИТЫ ДЕЙСТВУЮТ xxx\r\n✅ ВЫ ПОТЕРЯЕТЕ ДЕНЬГИ, ЕСЛИ ОПЛАТИТЕ ПОЗЖЕ\r\n✅ ПЕРЕВОДИТЕ ТОЧНУЮ СУММУ. НЕВЕРНАЯ СУММА НЕ БУДЕТ ЗАЧИСЛЕНА.\r\n✅ ОПЛАТА ДОЛЖНА ПРОХОДИТЬ ОДНИМ ПЛАТЕЖОМ.\r\n✅ ПРОБЛЕМЫ С ОПЛАТОЙ? ПИСАТЬ В TELEGRAM : exchangebtchelpbot\r\n✅ С ПРОБЛЕМНОЙ ЗАЯВКОЙ ОБРАЩАЙТЕСЬ НЕ ПОЗДНЕЕ 24 ЧАСОВ С МОМЕНТА ОПЛАТЫ.');
/*!40000 ALTER TABLE `bot_messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `city`
--

DROP TABLE IF EXISTS `city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `city` (
  `id` int NOT NULL,
  `city_name` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `city`
--

LOCK TABLES `city` WRITE;
/*!40000 ALTER TABLE `city` DISABLE KEYS */;
INSERT INTO `city` VALUES (1,'Красноярск'),(2,'Ачинск'),(4,'Сосновоборск'),(5,'Железногорск'),(6,'Назарово'),(8,'Березовка'),(10,'Боготол');
/*!40000 ALTER TABLE `city` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedbacks`
--

DROP TABLE IF EXISTS `feedbacks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `feedbacks` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_name` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `date` date NOT NULL,
  `feedback_text` varchar(1024) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedbacks`
--

LOCK TABLES `feedbacks` WRITE;
/*!40000 ALTER TABLE `feedbacks` DISABLE KEYS */;
INSERT INTO `feedbacks` VALUES (1,'ДжетЛи','2021-09-21','В касание'),(2,'ДжетЛи','2021-09-20','Ва33 Ач в касание , качество отличное .'),(3,' N1nt3ndo','2021-09-20','Всё ок!'),(4,'ДжетЛи','2021-09-20','Еа7 16,17 ровно Качество 5/5'),(5,'ДжетЛи','2021-09-14','4,6,7 НН спасибо большое'),(6,'СашаТуйчиев','2021-08-19','Очень порадовали камни, не пыль и крошки, прям камни! Еду снова.Лучший!'),(7,'Exbyte','2021-08-18','Координаты не точные, а так все ровно, Ача27'),(8,'N1nt3ndo','2021-08-02','Всё ништяк трёха дома'),(9,'R','2021-07-22','Топ 16 окт ровно'),(10,'R','2021-07-21','НН 37 касание'),(11,'ПокаМолодой','2021-07-20','Ачинск 0.33 в касание'),(12,'AirAr','2021-07-20','Фалина НН1 2тв ровничком'),(13,'Антоха','2021-07-13','Ачинск, 0,5 ск. искал 2 дня. Всё ровно, количество тоже стало на высоте!'),(14,'AirAr','2021-07-13','HH15 0,3 ck домашняя, всё четко , Фалина отдуши !!!!!'),(15,'Demonn124','2021-07-13','HH 20) 2ТВ Советский дома'),(16,'Demonn124','2021-07-12','НН 45) 2ТВ Советский Дома хороши ребята так держать'),(17,'LL','2021-07-12','ровнее ровного'),(18,'JangoNiger','2021-07-11','В касание.'),(19,'Demonn124','2021-07-04','НН 45) 2ТВ Советский дома красава просто'),(20,'StaffShoot_','2021-06-26','Благодарю в Касани');
/*!40000 ALTER TABLE `feedbacks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `on/off`
--

DROP TABLE IF EXISTS `on/off`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `on/off` (
  `id` int NOT NULL,
  `status` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `on/off`
--

LOCK TABLES `on/off` WRITE;
/*!40000 ALTER TABLE `on/off` DISABLE KEYS */;
INSERT INTO `on/off` VALUES (0,'off'),(1,'on');
/*!40000 ALTER TABLE `on/off` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment_methods`
--

DROP TABLE IF EXISTS `payment_methods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment_methods` (
  `method_number` int NOT NULL,
  `status` int NOT NULL,
  `method_name` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `my_wallet` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`method_number`),
  KEY `status_on_off` (`status`),
  CONSTRAINT `status_on_off` FOREIGN KEY (`status`) REFERENCES `on/off` (`id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment_methods`
--

LOCK TABLES `payment_methods` WRITE;
/*!40000 ALTER TABLE `payment_methods` DISABLE KEYS */;
INSERT INTO `payment_methods` VALUES (1,1,'Оплатить балансом',NULL),(3,1,'FastChange (CARD/TELE2) ','5536-9140-4627-3359'),(4,1,'getBTC(CARD/Тинькофф Мобайл)','5599-0050-8126-2961'),(5,1,'xchanger Charlie','5106-2110-8089-4681'),(6,1,'Exchanger Alfa','4048-4150-1038-5579'),(11,1,'LITECOIN','MFsJqCD2vh5DXVs4sBeqH1rQM7N6qWxzjJ'),(12,1,'BITCOIN','1GNMBqQ9EedvtMa7NwVz58bDsnw1orGE63'),(13,1,'Visa/MasterCard (перевод с Qiwi, Yandex-Деньги, Webmoney, Терминалы, Visa)',NULL),(14,1,'SIM-карта','+79775752135'),(15,1,'Qiwi (обменники) 15%','+79661996967,+79155268731,+79775752119');
/*!40000 ALTER TABLE `payment_methods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product` int NOT NULL,
  `massa` int NOT NULL,
  `price` int NOT NULL,
  `city` int NOT NULL,
  `districts` varchar(1024) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `price_in_city` (`city`),
  KEY `product_type_foreign_key` (`product`),
  KEY `product_massa` (`massa`),
  CONSTRAINT `price_in_city` FOREIGN KEY (`city`) REFERENCES `city` (`id`) ON DELETE CASCADE,
  CONSTRAINT `product_massa` FOREIGN KEY (`massa`) REFERENCES `products_massa` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `product_type_foreign_key` FOREIGN KEY (`product`) REFERENCES `products_types` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (6,2,2,1650,2,''),(7,10,21,3400,2,''),(14,2,2,1650,6,''),(15,10,20,3200,10,''),(22,2,1,1050,6,''),(27,2,1,1350,2,''),(28,10,24,9000,1,'22:за городом '),(29,10,20,2300,5,''),(30,10,20,2300,1,'11:Советский,14:Октябрьский'),(31,10,21,2800,5,''),(32,10,25,18000,1,'22:за городу');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_massa`
--

DROP TABLE IF EXISTS `products_massa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_massa` (
  `id` int NOT NULL,
  `massa_gr` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_massa`
--

LOCK TABLES `products_massa` WRITE;
/*!40000 ALTER TABLE `products_massa` DISABLE KEYS */;
INSERT INTO `products_massa` VALUES (1,0.33),(2,0.5),(20,2),(21,3),(24,10),(25,20),(26,30),(29,40);
/*!40000 ALTER TABLE `products_massa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products_types`
--

DROP TABLE IF EXISTS `products_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products_types` (
  `id` int NOT NULL,
  `product_name` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products_types`
--

LOCK TABLES `products_types` WRITE;
/*!40000 ALTER TABLE `products_types` DISABLE KEYS */;
INSERT INTO `products_types` VALUES (2,'Альпийские камни'),(10,'Оффлайн ТВ(САМОЕ МОЩНОЕ ТВ)');
/*!40000 ALTER TABLE `products_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_state`
--

DROP TABLE IF EXISTS `user_state`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_state` (
  `id` int NOT NULL,
  `state` varchar(512) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_state`
--

LOCK TABLES `user_state` WRITE;
/*!40000 ALTER TABLE `user_state` DISABLE KEYS */;
INSERT INTO `user_state` VALUES (-2147483648,'#'),(140067412,'+'),(156030003,'+'),(190245877,'+'),(218879657,'c1;p10'),(221224513,'c6'),(228190678,'c1'),(246289992,'c1;p10'),(251641793,'#'),(291379826,'c1;p10;f20;d11;m11'),(300676180,'c1;p10;f20;d14;m15'),(304302241,'c1'),(414057033,'c1;p10;f24'),(421556942,'c5;p10'),(437946080,'c1'),(471886563,'c1;p10;f24'),(518912638,'#'),(544790535,'#'),(571777912,'#'),(582928651,'#'),(616469434,'c5;p10'),(626305632,'c1;p10'),(655075381,'#'),(656950457,'#'),(663853104,'c1;p10'),(682812370,'c1;p10'),(707793755,'c1;p10;f24;d22;m13'),(773766324,'c1;p10'),(783248561,'c6;p10'),(783863029,'c1;p10'),(784284459,'c1;p10;f20;d11;m13'),(812381039,'+'),(819862691,'c1;p10'),(830248482,'c6;p10'),(836410892,'#'),(843580223,'+'),(868981978,'c1;p10'),(875288165,'c1;p2;f2;d11'),(875447657,'c1;p10;f20'),(918143044,'#'),(922573972,'+'),(929974626,'c1;p10'),(934889721,'c1;p10'),(948878359,'c1;p2;f1'),(970542482,'+'),(990612723,'c1;p10'),(1014643303,'c1;p10;f24'),(1022463215,'+'),(1032601477,'c1;p10'),(1057374520,'c5;p10;f20;0'),(1066214668,'c1;p10;f20'),(1076829144,'c1;p10;f21'),(1077974096,'c1;p10;f20'),(1080824438,'c1;p10'),(1084522626,'c1'),(1090204378,'c1;p10'),(1097889509,'c1'),(1109609724,'c2;p10'),(1111297468,'c1;p10'),(1120019996,'#'),(1126023407,'c1;p10'),(1181444679,'c1;p10;f24;d22;m13;p4LPU0KR'),(1193630516,'c1;p10;f20;d14;m12'),(1213117901,'#'),(1224478758,'c1;p10'),(1235307918,'#'),(1251856520,'c2;p10;f20;0;m13;p31276144'),(1258251912,'#'),(1264731133,'c1;p10'),(1269849494,'#'),(1281073447,'+'),(1304179727,'c1;p10;f24;d22'),(1308646949,'c1;p10'),(1317765344,'c1;p10;f20'),(1332491682,'c1;p10;f20'),(1354390219,'+'),(1376190601,'#'),(1386852003,'c1'),(1390474360,'#'),(1399087854,'c1;p10'),(1407271948,'c1;p10;f20;d11;m14'),(1422722132,'c1'),(1432262027,'#'),(1439449701,'c1;p2;f2;d11'),(1453471146,'c1;p10;f20'),(1476582151,'c1;p10'),(1564407751,'+'),(1564584022,'c1;p10;f20;d14;m1'),(1575847905,'c1;p10;f20'),(1583538996,'?'),(1594102672,'#'),(1600411617,'+'),(1617070828,'c1;p10;f20'),(1635743541,'c1;p10;f20'),(1699828698,'c1;p10;f20'),(1700206758,'c1;p10;f24;d22;m12'),(1704827312,'c2;p10'),(1708132946,'+'),(1722604510,'c1;p10'),(1727924881,'#'),(1737749361,'#'),(1739132238,'c1'),(1746451715,'c1'),(1746561257,'c1;p10'),(1751748528,'c10;p10'),(1754856632,'c1;p10;f20'),(1754888872,'#'),(1765317423,'c1;p10'),(1769573213,'c2;p10'),(1781117868,'c6;p10'),(1785056415,'c1;p10;f20;d14;m13;p6m4Y7A3Z2U54zC8f9d4342Grl'),(1795052889,'+'),(1802498068,'c1;p10'),(1814457932,'+'),(1822828511,'c1'),(1840070292,'c1;p10'),(1842339717,'c1;p10;f20'),(1843194874,'+'),(1844894027,'#'),(1889646052,'c1'),(1917538032,'c1;p10'),(1921160677,'c1;p10;f21;d33;m13;p39554131'),(1921165628,'c1;p2'),(1927632277,'c1'),(1929152661,'c1;p10;f24;d22;m11'),(1930870939,'c1;p10'),(1948097416,'+'),(1966366299,'c1;p10'),(1972661307,'#'),(1973400219,'c5;p10'),(1975411160,'c1;p10;f20'),(1977148710,'c1;p2'),(1988556157,'c1;p10;f24;d22;m1'),(1993062139,'c1;p10'),(2002723552,'c5;p10;f20;0'),(2009816464,'c1'),(2024227278,'c1;p10'),(2034656252,'c1'),(2040634059,'999'),(2045433900,'c1;p10;f20;d11;m11'),(2076061708,'c1;p10'),(2078419443,'c1;p10'),(2081364845,'c1'),(2095147083,'c1;p10;f20');
/*!40000 ALTER TABLE `user_state` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-04  9:40:42
