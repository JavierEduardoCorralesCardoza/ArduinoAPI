-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 29-11-2022 a las 12:10:37
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `corrector_de_postura`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alarma`
--

CREATE TABLE `alarma` (
  `ID_Alarma` int(11) NOT NULL,
  `Modelo_Alarma` varchar(100) NOT NULL,
  `Posicion_Alarma` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `alarma`
--

INSERT INTO `alarma` (`ID_Alarma`, `Modelo_Alarma`, `Posicion_Alarma`) VALUES
(1, 'M1', 20);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `interruptor`
--

CREATE TABLE `interruptor` (
  `ID_Interruptor` int(11) NOT NULL,
  `Modelo_Interruptor` varchar(100) NOT NULL,
  `Posicion_Interruptor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `interruptor`
--

INSERT INTO `interruptor` (`ID_Interruptor`, `Modelo_Interruptor`, `Posicion_Interruptor`) VALUES
(1, 'I1', 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `medicion`
--

CREATE TABLE `medicion` (
  `FechaYHora` datetime NOT NULL,
  `ID_Pieza_Sensor` int(11) NOT NULL,
  `Distancia` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pieza`
--

CREATE TABLE `pieza` (
  `Pieza` varchar(100) NOT NULL,
  `Medida_Pieza` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `pieza`
--

INSERT INTO `pieza` (`Pieza`, `Medida_Pieza`) VALUES
('Respaldo', 100);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pieza_de_la_silla`
--

CREATE TABLE `pieza_de_la_silla` (
  `ID_Silla_Pieza` int(11) NOT NULL,
  `ID_Silla` int(11) NOT NULL,
  `Pieza` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `pieza_de_la_silla`
--

INSERT INTO `pieza_de_la_silla` (`ID_Silla_Pieza`, `ID_Silla`, `Pieza`) VALUES
(1, 1, 'Respaldo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sensor`
--

CREATE TABLE `sensor` (
  `ID_Sensor` int(11) NOT NULL,
  `Modelo_Sensor` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `sensor`
--

INSERT INTO `sensor` (`ID_Sensor`, `Modelo_Sensor`) VALUES
(1, 'S1');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sensor_de_la_pieza`
--

CREATE TABLE `sensor_de_la_pieza` (
  `ID_Pieza_Sensor` int(11) NOT NULL,
  `Pieza` varchar(100) NOT NULL,
  `ID_Sensor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `sensor_de_la_pieza`
--

INSERT INTO `sensor_de_la_pieza` (`ID_Pieza_Sensor`, `Pieza`, `ID_Sensor`) VALUES
(1, 'Respaldo', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `silla`
--

CREATE TABLE `silla` (
  `ID_Silla` int(11) NOT NULL,
  `ID_Usuario` int(11) NOT NULL,
  `ID_Alarma` int(11) NOT NULL,
  `ID_Interruptor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `silla`
--

INSERT INTO `silla` (`ID_Silla`, `ID_Usuario`, `ID_Alarma`, `ID_Interruptor`) VALUES
(1, 18, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `ID_Usuario` int(11) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Contraseña` varchar(100) NOT NULL,
  `Edad` int(11) NOT NULL,
  `Genero` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`ID_Usuario`, `Nombre`, `Contraseña`, `Edad`, `Genero`) VALUES
(18, 'Alejandra', 'pbkdf2:sha256:30$XEUi189IHrEk8tjheFFa9nfq9mesdb$8f344dabec951a1b446a8054a4db8b3e1b282b5d7395b9120f74', 18, 'Mujer'),
(19, 'Eduardo', 'pbkdf2:sha256:30$ZPTaD6PghSLEQKNw59ZQoAmx6EboQS$a844a7d393cd4c97bdab647961452791990c162b02dc56f23274', 18, 'Hombre'),
(20, 'Javier', 'pbkdf2:sha256:30$LrvNq1LrdvZMBEM1VmhVdBUmkeh5zK$65ee272c846160a4a222a6c756a8357552c754e5d6146d5724b7', 20, 'Hombre');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alarma`
--
ALTER TABLE `alarma`
  ADD PRIMARY KEY (`ID_Alarma`),
  ADD KEY `ID_Alarma` (`ID_Alarma`);

--
-- Indices de la tabla `interruptor`
--
ALTER TABLE `interruptor`
  ADD PRIMARY KEY (`ID_Interruptor`),
  ADD KEY `ID_Interruptor` (`ID_Interruptor`);

--
-- Indices de la tabla `medicion`
--
ALTER TABLE `medicion`
  ADD PRIMARY KEY (`FechaYHora`,`ID_Pieza_Sensor`),
  ADD KEY `ID_Pieza_Sensor` (`ID_Pieza_Sensor`);

--
-- Indices de la tabla `pieza`
--
ALTER TABLE `pieza`
  ADD PRIMARY KEY (`Pieza`),
  ADD KEY `Pieza` (`Pieza`);

--
-- Indices de la tabla `pieza_de_la_silla`
--
ALTER TABLE `pieza_de_la_silla`
  ADD PRIMARY KEY (`ID_Silla_Pieza`),
  ADD KEY `ID_Silla_Pieza` (`ID_Silla_Pieza`,`ID_Silla`,`Pieza`),
  ADD KEY `ID_Silla` (`ID_Silla`),
  ADD KEY `Pieza` (`Pieza`);

--
-- Indices de la tabla `sensor`
--
ALTER TABLE `sensor`
  ADD PRIMARY KEY (`ID_Sensor`),
  ADD KEY `ID_Sensor` (`ID_Sensor`);

--
-- Indices de la tabla `sensor_de_la_pieza`
--
ALTER TABLE `sensor_de_la_pieza`
  ADD PRIMARY KEY (`ID_Pieza_Sensor`),
  ADD KEY `ID_Pieza_Sensor` (`ID_Pieza_Sensor`,`Pieza`,`ID_Sensor`),
  ADD KEY `Pieza` (`Pieza`),
  ADD KEY `ID_Sensor` (`ID_Sensor`);

--
-- Indices de la tabla `silla`
--
ALTER TABLE `silla`
  ADD PRIMARY KEY (`ID_Silla`),
  ADD KEY `ID_Alarma` (`ID_Alarma`,`ID_Interruptor`),
  ADD KEY `ID_Silla` (`ID_Silla`),
  ADD KEY `ID_Usuario` (`ID_Usuario`),
  ADD KEY `ID_Interruptor` (`ID_Interruptor`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`ID_Usuario`),
  ADD KEY `ID_Usuario` (`ID_Usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `alarma`
--
ALTER TABLE `alarma`
  MODIFY `ID_Alarma` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `interruptor`
--
ALTER TABLE `interruptor`
  MODIFY `ID_Interruptor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `pieza_de_la_silla`
--
ALTER TABLE `pieza_de_la_silla`
  MODIFY `ID_Silla_Pieza` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `sensor`
--
ALTER TABLE `sensor`
  MODIFY `ID_Sensor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `sensor_de_la_pieza`
--
ALTER TABLE `sensor_de_la_pieza`
  MODIFY `ID_Pieza_Sensor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `silla`
--
ALTER TABLE `silla`
  MODIFY `ID_Silla` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `ID_Usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `medicion`
--
ALTER TABLE `medicion`
  ADD CONSTRAINT `medicion_ibfk_1` FOREIGN KEY (`ID_Pieza_Sensor`) REFERENCES `sensor_de_la_pieza` (`ID_Pieza_Sensor`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `pieza_de_la_silla`
--
ALTER TABLE `pieza_de_la_silla`
  ADD CONSTRAINT `pieza_de_la_silla_ibfk_1` FOREIGN KEY (`ID_Silla`) REFERENCES `silla` (`ID_Silla`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `pieza_de_la_silla_ibfk_2` FOREIGN KEY (`Pieza`) REFERENCES `pieza` (`Pieza`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `sensor_de_la_pieza`
--
ALTER TABLE `sensor_de_la_pieza`
  ADD CONSTRAINT `sensor_de_la_pieza_ibfk_1` FOREIGN KEY (`Pieza`) REFERENCES `pieza` (`Pieza`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `sensor_de_la_pieza_ibfk_2` FOREIGN KEY (`ID_Sensor`) REFERENCES `sensor` (`ID_Sensor`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `silla`
--
ALTER TABLE `silla`
  ADD CONSTRAINT `silla_ibfk_1` FOREIGN KEY (`ID_Interruptor`) REFERENCES `interruptor` (`ID_Interruptor`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `silla_ibfk_2` FOREIGN KEY (`ID_Alarma`) REFERENCES `alarma` (`ID_Alarma`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `silla_ibfk_3` FOREIGN KEY (`ID_Usuario`) REFERENCES `usuario` (`ID_Usuario`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
