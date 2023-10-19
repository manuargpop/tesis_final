-- MySQL dump 10.13  Distrib 8.1.0, for Win64 (x86_64)
--
-- Host: localhost    Database: tesis_antropometria
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.27-MariaDB

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
-- Table structure for table `citas`
--

DROP TABLE IF EXISTS `citas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `citas` (
  `Paciente_idPaciente` int(11) NOT NULL,
  `tipo_idTipo` int(11) NOT NULL,
  `fecha` date DEFAULT NULL,
  PRIMARY KEY (`Paciente_idPaciente`,`tipo_idTipo`),
  KEY `fk_Paciente_has_tipo_tipo1_idx` (`tipo_idTipo`),
  KEY `fk_Paciente_has_tipo_Paciente_idx` (`Paciente_idPaciente`),
  CONSTRAINT `fk_Paciente_has_tipo_Paciente` FOREIGN KEY (`Paciente_idPaciente`) REFERENCES `paciente` (`idPaciente`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Paciente_has_tipo_tipo1` FOREIGN KEY (`tipo_idTipo`) REFERENCES `tipo_paciente` (`idTipo`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `citas`
--

LOCK TABLES `citas` WRITE;
/*!40000 ALTER TABLE `citas` DISABLE KEYS */;
INSERT INTO `citas` VALUES (85,1,'2023-10-18'),(86,2,'2023-10-18');
/*!40000 ALTER TABLE `citas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `informe_adulto`
--

DROP TABLE IF EXISTS `informe_adulto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `informe_adulto` (
  `idInforme_Adulto` int(11) NOT NULL AUTO_INCREMENT,
  `estatura` double DEFAULT NULL,
  `peso` double DEFAULT NULL,
  `profundidad_abdominal` double DEFAULT NULL,
  `triceps` double DEFAULT NULL,
  `subescapular` double DEFAULT NULL,
  `biceps` double DEFAULT NULL,
  `cresta` double DEFAULT NULL,
  `brazo_relajado` double DEFAULT NULL,
  `bfr` double DEFAULT NULL,
  `muneca` double DEFAULT NULL,
  `minimo_cintura` double DEFAULT NULL,
  `abdominal` double DEFAULT NULL,
  `caderas` double DEFAULT NULL,
  `Citas_Paciente_idPaciente` int(11) NOT NULL,
  `Citas_tipo_idTipo` int(11) NOT NULL,
  PRIMARY KEY (`idInforme_Adulto`),
  KEY `fk_Informe_Adulto_Citas1_idx` (`Citas_Paciente_idPaciente`,`Citas_tipo_idTipo`),
  CONSTRAINT `fk_Informe_Adulto_Citas1` FOREIGN KEY (`Citas_Paciente_idPaciente`, `Citas_tipo_idTipo`) REFERENCES `citas` (`Paciente_idPaciente`, `tipo_idTipo`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `informe_adulto`
--

LOCK TABLES `informe_adulto` WRITE;
/*!40000 ALTER TABLE `informe_adulto` DISABLE KEYS */;
INSERT INTO `informe_adulto` VALUES (29,174.45,91,21,12,15,8,28,37,39,16.9,96.3,98,104,85,1);
/*!40000 ALTER TABLE `informe_adulto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `informe_atleta`
--

DROP TABLE IF EXISTS `informe_atleta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `informe_atleta` (
  `idInforme_Atleta` int(11) NOT NULL AUTO_INCREMENT,
  `estatura` double DEFAULT NULL,
  `peso` double DEFAULT NULL,
  `profundidad_abdominal` double DEFAULT NULL,
  `envergadura` double DEFAULT NULL,
  `estatura_sentado` double DEFAULT NULL,
  `longitud_ad` double DEFAULT NULL,
  `triceps` double DEFAULT NULL,
  `subescapular` double DEFAULT NULL,
  `biceps` double DEFAULT NULL,
  `cresta` double DEFAULT NULL,
  `supraespinal` double DEFAULT NULL,
  `abdominal_atleta` double DEFAULT NULL,
  `muslo_frontal` double DEFAULT NULL,
  `pantorrilla` double DEFAULT NULL,
  `brazo_relajado` double DEFAULT NULL,
  `bfc` double DEFAULT NULL,
  `muneca_atleta` double DEFAULT NULL,
  `minimo_cintura_atleta` double DEFAULT NULL,
  `abdominal` double DEFAULT NULL,
  `caderas` double DEFAULT NULL,
  `cefalico` double DEFAULT NULL,
  `torax` double DEFAULT NULL,
  `cuello` double DEFAULT NULL,
  `mad` double DEFAULT NULL,
  `mai` double DEFAULT NULL,
  `md_1` double DEFAULT NULL,
  `mi_1` double DEFAULT NULL,
  `muslo_medio` double DEFAULT NULL,
  `p_pantorrilla` double DEFAULT NULL,
  `p_mdt` double DEFAULT NULL,
  `acromiale_radiale` double DEFAULT NULL,
  `radiale_stylion` double DEFAULT NULL,
  `midstylion_dactylion` double DEFAULT NULL,
  `altura_iliospinale` double DEFAULT NULL,
  `altura_trochanterion` double DEFAULT NULL,
  `trochanterion_tl` double DEFAULT NULL,
  `altura_tl` double DEFAULT NULL,
  `tibiale_ls_t` double DEFAULT NULL,
  `diametro_biacromial` double DEFAULT NULL,
  `diametro_biliocristal` double DEFAULT NULL,
  `largo_pie` double DEFAULT NULL,
  `torax_t` double DEFAULT NULL,
  `torax_ap` double DEFAULT NULL,
  `diametro_biepicondilar_h` double DEFAULT NULL,
  `diametro_biepicondilar_f` double DEFAULT NULL,
  `Citas_Paciente_idPaciente` int(11) NOT NULL,
  `Citas_tipo_idTipo` int(11) NOT NULL,
  PRIMARY KEY (`idInforme_Atleta`),
  KEY `fk_Informe_Atleta_Citas1_idx` (`Citas_Paciente_idPaciente`,`Citas_tipo_idTipo`),
  CONSTRAINT `fk_Informe_Atleta_Citas1` FOREIGN KEY (`Citas_Paciente_idPaciente`, `Citas_tipo_idTipo`) REFERENCES `citas` (`Paciente_idPaciente`, `tipo_idTipo`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `informe_atleta`
--

LOCK TABLES `informe_atleta` WRITE;
/*!40000 ALTER TABLE `informe_atleta` DISABLE KEYS */;
INSERT INTO `informe_atleta` VALUES (18,178.5,80,10,15,143,11.5,10.5,9.1,5,15,7.5,13,20.25,11.25,34.6,37.5,17.4,83.4,25,99.4,55.6,99,42.3,35,35,35,35,54,37,22.4,34.45,25.3,20.3,100.35,93.05,44.9,45,40.5,38,28,27.6,27.45,18,7.4,10,86,2);
/*!40000 ALTER TABLE `informe_atleta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paciente`
--

DROP TABLE IF EXISTS `paciente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paciente` (
  `idPaciente` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `documento` varchar(45) DEFAULT NULL,
  `genero` enum('Masculino','Femenino') NOT NULL,
  `pais` varchar(70) NOT NULL,
  `fnacimiento` date NOT NULL,
  `act_deporte` varchar(90) DEFAULT NULL,
  `correo` varchar(70) NOT NULL,
  `direccion` text NOT NULL,
  PRIMARY KEY (`idPaciente`),
  UNIQUE KEY `documento_UNIQUE` (`documento`)
) ENGINE=InnoDB AUTO_INCREMENT=87 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paciente`
--

LOCK TABLES `paciente` WRITE;
/*!40000 ALTER TABLE `paciente` DISABLE KEYS */;
INSERT INTO `paciente` VALUES (85,'Johnny Vargas','CI-11111111','Masculino','Afghanistan','1983-05-11','Beisbol','johnnyvargas@gmail.com','el parque'),(86,'Juan Perez','CI-1324567','Masculino','Venezuela','1983-04-05','Judo','juanperez@gmail.com','mikasa');
/*!40000 ALTER TABLE `paciente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_paciente`
--

DROP TABLE IF EXISTS `tipo_paciente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo_paciente` (
  `idTipo` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_tipo` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`idTipo`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_paciente`
--

LOCK TABLES `tipo_paciente` WRITE;
/*!40000 ALTER TABLE `tipo_paciente` DISABLE KEYS */;
INSERT INTO `tipo_paciente` VALUES (1,'Adulto'),(2,'Atleta');
/*!40000 ALTER TABLE `tipo_paciente` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-18  2:52:34
