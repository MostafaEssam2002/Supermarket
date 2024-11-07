
CREATE TABLE `admin` (
  `id` int(5) NOT NULL,
  `name` varchar(40) DEFAULT NULL,
  `adminpass` varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `admin` (`id`, `name`, `adminpass`) VALUES
(1, 'mostafa essam', 'd3d9446802a44259755d38e6d163e820');

CREATE TABLE `employees` (
  `employee_id` int(11) NOT NULL,
  `employee_name` varchar(100) DEFAULT NULL,
  `employee_password` varchar(32) DEFAULT NULL,
  `employee_phone` varchar(100) DEFAULT NULL,
  `address` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `employees` (`employee_id`, `employee_name`, `employee_password`, `employee_phone`, `address`) VALUES
(1, 'mostafa essam', '25f9e794323b453885f5181f1b624d0b', '01118606952', 'menofia'),
(2, 'ammar yasser', '202cb962ac59075b964b07152d234b70', '01148546554', 'tala'),
(3, 'amr kadah', 'd3d9446802a44259755d38e6d163e820', '01148181776', 'giza'),
(4, 'ebrahem hegazy', '25f9e794323b453885f5181f1b624d0b', '01148090156', 'london'),
(5, 'hassan saad', '25f9e794323b453885f5181f1b624d0b', '01045879663', 'tanta'),
(6, 'amr saeed', '25f9e794323b453885f5181f1b624d0b', '01056787645456', 'mama'),
(7, 'hazem saad', '71640f63d0ba6bb560be81f51ca61e64', '01048797512', 'sadat'),
(8, 'nagey', 'd18490031c62dd491eef57525fef80a1', '897465312', 'maki'),
(9, 'mostafa essam', 'd3d9446802a44259755d38e6d163e820', '01118606952', 'menofia'),
(10, 'yaser samy', 'e35cf7b66449df565f93c607d5a81d09', '01149625779', 'suiz'),
(11, 'mostafa essam', 'd3d9446802a44259755d38e6d163e820', '011148900685', 'menodia');

CREATE TABLE `inventory` (
  `id` int(11) NOT NULL,
  `item` varchar(200) DEFAULT NULL,
  `quantity` int(20) DEFAULT NULL,
  `price` int(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `inventory` (`id`, `item`, `quantity`, `price`) VALUES
(1, 'Bread', 100, 500),
(2, 'Cake', 100, 2000),
(3, 'Chips', 10, 1000),
(4, 'Chocolate', 100, 2000),
(5, 'Candy', 100, 1000),
(6, 'Banana', 100, 2000),
(7, 'Appele', 100, 500),
(8, 'Orange', 100, 5000),
(9, 'Strawberry', 100, 1500),
(10, 'Mango', 100, 500),
(11, 'Cola', 100, 1000),
(12, 'Milk', 100, 2000),
(13, 'Tea', 100, 1000),
(14, 'Purified water', 100, 500),
(15, 'Beef', 100, 2500),
(16, 'Pizza', 100, 2000),
(17, 'Beaf', 100, 5000),
(18, 'Pork', 100, 5000),
(19, 'Checken Wings', 100, 3000),
(20, 'Sauce', 100, 1000),
(21, 'Vinegar', 100, 2000),
(23, 'Checken', 200, 4000),
(24, 'Pasta', 100, 1000),
(25, 'Carrot', 40, 150),
(26, 'Onion', 30, 1000),
(28, 'garlec', 124, 222),
(29, 'sudaen', 865, 4040),
(30, 'olive', 450, 200),
(31, 'mostarda', 40, 100);

ALTER TABLE `admin` ADD PRIMARY KEY (`id`);
ALTER TABLE `employees`  ADD PRIMARY KEY (`employee_id`);
ALTER TABLE `inventory`  ADD PRIMARY KEY (`id`);
COMMIT;
