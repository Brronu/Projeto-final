-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 05-Jun-2023 às 21:56
-- Versão do servidor: 10.4.27-MariaDB
-- versão do PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `cinema_db`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `filmes`
--
-- Criação: 31-Maio-2023 às 23:15
-- Última actualização: 05-Jun-2023 às 19:17
--

CREATE TABLE `filmes` (
  `codigo` int(11) NOT NULL,
  `titulo` varchar(100) NOT NULL,
  `genero` varchar(20) NOT NULL,
  `duracao` int(11) NOT NULL,
  `classificacao_indicativa` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- RELACIONAMENTOS PARA TABELAS `filmes`:
--

--
-- Extraindo dados da tabela `filmes`
--

INSERT INTO `filmes` (`codigo`, `titulo`, `genero`, `duracao`, `classificacao_indicativa`) VALUES
(213, 'Capital America', 'Ficção', 3, 18),
(252, 'lll', 'ççç', 4, 18),
(585, 'Thor', 'Ficção', 3, 18),
(785, 'aaa', 'zzz', 5, 78),
(999, 'Homen de ferro', 'Ficção', 3, 18),
(1356, 'aaa', 'Ficção', 1, 15),
(555555, 'kkkkkk', 'hhh', 25, 12);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `filmes`
--
ALTER TABLE `filmes`
  ADD PRIMARY KEY (`codigo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
