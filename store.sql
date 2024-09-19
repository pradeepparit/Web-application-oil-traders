-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 17, 2023 at 05:01 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `store`
--

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `id` bigint(100) NOT NULL,
  `username` varchar(10) NOT NULL,
  `password` varchar(7) NOT NULL,
  `shop_name` varchar(50) NOT NULL,
  `shop_type` varchar(20) NOT NULL,
  `shop_owner_name` varchar(50) NOT NULL,
  `shop_address` varchar(50) NOT NULL,
  `shop_start_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`id`, `username`, `password`, `shop_name`, `shop_type`, `shop_owner_name`, `shop_address`, `shop_start_date`) VALUES
(1, 'Admin', 'user', 'Shree Patil Oil Traders', 'Lubricantas ', 'Mr. Patil', 'Jaysingpur', '2001-04-14 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `store_data`
--

CREATE TABLE `store_data` (
  `id` bigint(100) NOT NULL,
  `product_name` varchar(25) NOT NULL,
  `product_quantity` bigint(100) NOT NULL,
  `product_price` double NOT NULL,
  `product_arrival_date` datetime NOT NULL,
  `product_manufacture_date` datetime NOT NULL,
  `product_expiry_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `store_data`
--

INSERT INTO `store_data` (`id`, `product_name`, `product_quantity`, `product_price`, `product_arrival_date`, `product_manufacture_date`, `product_expiry_date`) VALUES
(1, 'Castrol', 29, 100, '2023-02-12 00:00:00', '2023-02-12 00:00:00', '2024-02-12 00:00:00'),
(2, 'Pennzoil Ultra Platinum', 41, 120, '2023-02-12 00:00:00', '2023-02-01 00:00:00', '2023-02-11 00:00:00'),
(3, 'star oil', 0, 130, '2023-02-12 00:00:00', '2023-01-12 00:00:00', '2023-02-14 00:00:00'),
(4, 'test', 2, 200, '2023-02-13 00:00:00', '2023-02-12 00:00:00', '2024-02-13 00:00:00'),
(5, 'test2', 2, 10, '2023-02-14 00:00:00', '2023-02-14 00:00:00', '2024-05-14 00:00:00'),
(6, 'Servo Engine oil', 0, 2700, '2023-03-07 00:00:00', '2022-02-04 00:00:00', '2024-06-04 00:00:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `store_data`
--
ALTER TABLE `store_data`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `id` bigint(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `store_data`
--
ALTER TABLE `store_data`
  MODIFY `id` bigint(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
