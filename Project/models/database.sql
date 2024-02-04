-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 04, 2024 at 10:33 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `orion1`
--

-- --------------------------------------------------------

--
-- Table structure for table `scraped_item`
--

CREATE TABLE `scraped_item` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `target_url` varchar(255) NOT NULL,
  `scrape_timestamp` timestamp NOT NULL DEFAULT current_timestamp(),
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `scraped_item`
--

INSERT INTO `scraped_item` (`id`, `target_url`, `scrape_timestamp`, `user_id`) VALUES
(178, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-21 13:05:13', 17),
(179, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-21 13:03:28', 17),
(180, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-21 13:03:51', 17),
(181, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-21 13:05:13', 17),
(182, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 05:30:44', 18),
(183, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-21 13:21:08', 18),
(184, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-21 13:22:03', 18),
(185, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-21 13:24:27', 18),
(186, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-21 13:27:19', 18),
(187, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-21 13:27:41', 18),
(188, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-21 13:28:06', 18),
(189, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-21 14:41:52', 18),
(190, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-21 14:42:20', 18),
(191, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-21 14:49:39', 18),
(192, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 04:18:37', 18),
(193, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 04:47:02', 18),
(194, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 04:47:23', 18),
(195, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 04:49:29', 18),
(196, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 04:51:42', 18),
(197, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 04:52:00', 18),
(198, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 04:52:39', 18),
(199, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 04:52:59', 18),
(200, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 04:53:05', 18),
(201, 'https://styleconnection.co.ke/product-category/womens-clothing/dresses/', '2023-11-22 04:55:41', 18),
(202, 'https://kingscollection.co.ke/shop/ladies', '2023-11-22 05:13:30', 18),
(203, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 05:15:16', 18),
(204, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 05:29:13', 18),
(205, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 05:29:22', 18),
(206, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 05:30:44', 18),
(207, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 09:51:22', 18),
(208, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 09:51:32', 18),
(209, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 09:57:47', 18),
(210, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 09:58:30', 18),
(211, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 10:01:56', 18),
(212, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 10:02:29', 18),
(213, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 10:12:34', 18),
(214, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 10:13:04', 18),
(215, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 10:13:23', 18),
(216, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 10:16:35', 18),
(217, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 10:17:14', 18),
(218, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 10:17:52', 18),
(219, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 13:14:31', 18),
(220, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 13:15:10', 18),
(221, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 13:16:07', 18),
(222, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 13:41:05', 18),
(223, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 13:42:22', 18),
(224, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 13:45:32', 18),
(225, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-22 14:55:17', 18),
(226, 'http://localhost/orion-collections/category.php', '2023-11-23 14:24:45', 18),
(227, 'http://localhost/orion-collections/cart_view.php', '2023-11-23 15:00:09', 18),
(228, 'http://localhost/orion-collections/admin/home.php', '2023-11-23 15:04:51', 18),
(229, 'http://localhost/orion-collections/admin/users.php', '2023-11-23 15:07:12', 18),
(230, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-24 02:41:16', 18),
(231, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-24 02:47:40', 18),
(232, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-24 03:50:17', 18),
(233, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-24 03:52:31', 18),
(234, 'https://styleconnection.co.ke/product-category/womens-clothing/dresses/', '2023-11-24 04:13:02', 18),
(235, 'https://styleconnection.co.ke/product-category/womens-clothing/dresses/', '2023-11-24 04:15:36', 18),
(236, 'https://styleconnection.co.ke/product-category/womens-clothing/dresses/', '2023-11-24 04:16:11', 18),
(237, 'https://styleconnection.co.ke/product-category/womens-clothing/dresses/', '2023-11-24 04:18:51', 18),
(238, 'https://styleconnection.co.ke/product-category/womens-clothing/dresses/', '2023-11-24 04:21:03', 18),
(239, 'https://styleconnection.co.ke/product-category/womens-clothing/dresses/', '2023-11-24 04:21:05', 18),
(240, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-24 05:49:38', 18),
(241, 'http://www.kcau.ac.ke', '2023-11-24 05:53:09', 18),
(242, 'https://www.kcau.ac.ke', '2023-11-24 06:10:21', 18),
(243, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-24 06:47:41', 18),
(244, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-24 08:15:44', 18),
(245, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-24 08:19:32', 18),
(246, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-24 08:19:51', 18),
(247, 'http://localhost/orion-collections/admin/home.php', '2023-11-26 03:18:36', 18),
(248, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-26 03:19:25', 18),
(249, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-26 03:19:45', 18),
(250, 'http://localhost/orion-collections/category.php?category=kids', '2023-11-26 03:20:03', 18),
(251, 'http://localhost/orion-collections/category.php?category=kids', '2024-01-04 15:06:08', 18),
(252, 'http://localhost/orion-collections/category.php?category=kids', '2024-01-04 15:07:09', 18),
(253, 'http://localhost/orion-collections/category.php?category=kids', '2024-01-04 15:10:57', 18),
(254, 'http://localhost/orion-collections/category.php?category=kids', '2024-01-15 02:09:06', 18);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `first_name`, `last_name`, `email`, `password`) VALUES
(18, 'Eddie', 'Ogyner', 'eddyogyner@gmail.com', 'eddie');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `scraped_item`
--
ALTER TABLE `scraped_item`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `scraped_item`
--
ALTER TABLE `scraped_item`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=255;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
