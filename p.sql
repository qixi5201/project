-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- 主機： localhost
-- 產生時間： 
-- 伺服器版本： 8.0.17
-- PHP 版本： 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `p`
--

-- --------------------------------------------------------

--
-- 資料表結構 `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 傾印資料表的資料 `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('4f2bb0bc3192');

-- --------------------------------------------------------

--
-- 資料表結構 `collect`
--

CREATE TABLE `collect` (
  `id` int(11) NOT NULL,
  `postid` int(11) DEFAULT NULL,
  `author` varchar(80) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- 資料表結構 `like`
--

CREATE TABLE `like` (
  `id` int(11) NOT NULL,
  `postid` int(11) DEFAULT NULL,
  `author` varchar(80) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- 資料表結構 `message`
--

CREATE TABLE `message` (
  `id` int(11) NOT NULL,
  `name` varchar(30) DEFAULT NULL,
  `body` varchar(100) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  `postid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- 資料表結構 `posts`
--

CREATE TABLE `posts` (
  `id` int(11) NOT NULL,
  `head` varchar(64) DEFAULT NULL,
  `main` varchar(64) DEFAULT NULL,
  `body` text,
  `timestamp` date DEFAULT NULL,
  `tag` varchar(64) DEFAULT NULL,
  `author` varchar(80) DEFAULT NULL,
  `like` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- 資料表結構 `saves`
--

CREATE TABLE `saves` (
  `id` int(11) NOT NULL,
  `head` varchar(64) DEFAULT NULL,
  `main` varchar(64) DEFAULT NULL,
  `body` text,
  `timestamp` date DEFAULT NULL,
  `tag` varchar(64) DEFAULT NULL,
  `author` varchar(80) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- 資料表結構 `spot`
--

CREATE TABLE `spot` (
  `id` int(11) NOT NULL,
  `head` varchar(100) DEFAULT NULL,
  `main` varchar(100) DEFAULT NULL,
  `pic` varchar(100) DEFAULT NULL,
  `tag` varchar(64) DEFAULT NULL,
  `url` varchar(64) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 傾印資料表的資料 `spot`
--

INSERT INTO `spot` (`id`, `head`, `main`, `pic`, `tag`, `url`) VALUES
(1, '木下靜涯舊居', '淡水的世外莊', 'https://drive.google.com/uc?export=view&id=1BXINXXqRWvbHAfJnBPMskk4arvN5bc-9', '景點', 'spot1_1'),
(2, '齊柏林空間', '齊柏林的視野', 'https://drive.google.com/uc?export=view&id=1wbVJDO0Ze6mvz2N-UfVTpzclfEcRY3TV', '景點', 'spot1_2'),
(3, '紅樹林自然保留區/紅樹林步道', '紅樹林生態的奧妙', 'https://drive.google.com/uc?export=view&id=14qcPLzg4Nuzf3JZq1YY1PGcjdPCNrxd9', '景點', 'spot1_3'),
(4, '淡水無極天元宮', '宮廟及櫻花', 'https://drive.google.com/uc?export=view&id=1TUzsDyVjOHOxLjKfnBG-wucP3JZwgVDG', '景點', 'spot1_4'),
(5, '滬尾藝文休閒園區', '藏身淡水的綠色秘境', 'https://drive.google.com/uc?export=view&id=1WDL39PaCGKCvcqHy9Wy-y51HiTUJc0De', '景點', 'spot1_5'),
(6, '淡水和平公園', '別具意義的紀念公園', 'https://drive.google.com/uc?export=view&id=17EAeNAW1Uerz6N2Vv57J4PgmdukZNDbw', '景點', 'spot1_6'),
(7, '雲門舞集-雲門劇場', '充滿意境的劇場', 'https://drive.google.com/uc?export=view&id=1_gIQucZbh_qRzA55xMGrxNy3G_yimDXX', '景點', 'spot1_7'),
(8, '女友の扭蛋 扭蛋專賣店', '少女心天堂', 'https://drive.google.com/uc?export=view&id=1UVBeF_CbGJSAHlnPFTDnejeWuKmWD7de', '景點', 'spot1_8'),
(9, '淡水海關碼頭', '展覽+河畔音樂會', 'https://drive.google.com/uc?export=view&id=1J4yTlXAWzJQU8QKtiDIRff3UKxbcYkt-', '景點', 'spot1_9'),
(10, '漁人碼頭&情人橋&情人塔', '休閒好去處', 'https://drive.google.com/uc?export=view&id=1FeZ23IFhO3gbfC8oUeP7QOaBycw-O2dL', '景點', 'spot1_10'),
(11, '沙崙海灘', '一同散步欣賞夕落', 'https://drive.google.com/uc?export=view&id=1LqsEhV9mf7V_U9mIi8v8xqwSe3hGNWje', '景點', 'spot1_11'),
(12, '小時候彈珠堂', '兒時回憶', 'https://drive.google.com/uc?export=view&id=1C7iv-M0Ufzfbw7gHUo7gXLgzRqCbhLFk', '景點', 'spot1_12'),
(13, '工研酢淡水廠 | 益壽多文化館', '觀光工廠', 'https://drive.google.com/uc?export=view&id=1Fw8h2N7BCsZEWN0kfUPdBZ-iDNon6EZj', '景點', 'spot1_13'),
(14, '水管公園', '淡水看落日最佳景點之一', 'https://drive.google.com/uc?export=view&id=16QZipwuc8lGrfDeqpvu4vmyCNYxjU6K2', '景點', 'spot1_14'),
(15, '小美術館 ArtBox', '藝術寶盒', 'https://drive.google.com/uc?export=view&id=1MDrdSL3kfnGs6hRbanyftk0_oPuQdpRY', '景點', 'spot1_15'),
(16, '滬尾櫻花大道', '世界最長櫻花大道', 'https://drive.google.com/uc?export=view&id=1lOv1SbkRwhyUq4EVEJcrxI6HXBN018in', '景點', 'spot1_16'),
(17, '美麗新廣場MIRANEW SQUARE', '新市鎮大商場', 'https://drive.google.com/uc?export=view&id=1SP7qQnnVoJd1cVfZrFDT0IegmQGSoWjp', '景點', 'spot1_17'),
(18, '稼日蒔光', '拍照聖地', 'https://drive.google.com/uc?export=view&id=1fV0DNMsSzpw_NKhnTmQtEIObU_GSl4sn', '景點', 'spot1_18'),
(19, '程氏古厝', '漫遊清法戰爭遺跡', 'https://drive.google.com/uc?export=view&id=1357HMrbXtwucXSWzsRYhHHCdStxU4hXl', '景點', 'spot2_1'),
(20, '殼牌倉庫', '原英商嘉士洋行倉庫', 'https://drive.google.com/uc?export=view&id=1IBOeK7kez5e0b8uTsLQy9nWSJSMvyesF', '景點', 'spot2_2'),
(21, '日本警官宿舍', '唯美日式老宅', 'https://drive.google.com/uc?export=view&id=1PeJayfv7GUMJvyKTiCV1cKxImC2cDQhS', '景點', 'spot2_3'),
(22, '多田榮吉故居', '京都木屋，私房秘境', 'https://drive.google.com/uc?export=view&id=1SfC80rEajCs4BVkjkrzgWIq4CtGiqVSp', '景點', 'spot2_4'),
(23, '前清淡水關稅務司官邸(小白宮)', '淡雅的白色拱門', 'https://drive.google.com/uc?export=view&id=1cmsuRSixCBuoNyQ7oAIQ6Vig_1Cywsyw', '景點', 'spot2_5'),
(24, '滬尾砲台', '清法戰爭後清朝最大的防禦工事', 'https://drive.google.com/uc?export=view&id=151YA9NnoUaOLubq8rezdclYpx06kVRsD', '景點', 'spot2_6'),
(25, '淡水紅毛城&園區&英國領事館', '看盡淡水滄桑歷史', 'https://drive.google.com/uc?export=view&id=1hQIA31sePg4qtHd6l_IOCw66L0lrftaE', '景點', 'spot2_7'),
(26, '一滴水紀念館', '日式禪風庭院', 'https://drive.google.com/uc?export=view&id=1vTBiPFgD6qp_-jhGaYzub63vOyfRlutm', '景點', 'spot2_8'),
(27, '淡水老街', '感受時空交錯烙印下的美好', 'https://drive.google.com/uc?export=view&id=1CaOTxhdpDV3zLyqpjGSOcT-ouBsqkCcS', '景點', 'spot2_9'),
(28, '淡水福佑宮&淡水彩繪階梯3D意象', '淡水媽祖宮保佑你', 'https://drive.google.com/uc?export=view&id=1POs48-LwGyKbEFd43pSXX6oV7iimfEtk', '景點', 'spot2_10'),
(29, '滬尾偕醫館', '馬偕紀念醫院發源地', 'https://drive.google.com/uc?export=view&id=1Hzp5xFGxqiLLAADUZN9bLUetJSCO7eiy', '景點', 'spot2_11'),
(30, '淡水禮拜堂', '帶有濃濃的懷舊風，百年古鐘與古風琴', 'https://drive.google.com/uc?export=view&id=1DDu9Ffj4pVZEZpT2R6BPeEvmphhNJZJ4', '景點', 'spot2_12'),
(31, '得忌利士洋行', '老洋行，新淡水', 'https://drive.google.com/uc?export=view&id=1ABV6sJL0fC57-6VOfJQQRZ5IiMbzC-aY', '景點', 'spot2_13'),
(32, '理學堂大書院', '牛津學堂', 'https://drive.google.com/uc?export=view&id=1Fw8h2N7BCsZEWN0kfUPdBZ-iDNon6EZj', '景點', 'spot2_14'),
(33, '鄞山寺（汀州會館）', '汀洲人的同鄉會館', 'https://drive.google.com/uc?export=view&id=1BYUAHzoY8XqdsgDD9u2FBJ09pGLVmT_D', '景點', 'spot2_15'),
(34, '淡水龍山寺', '古廟悠揚滬尾街', 'https://drive.google.com/uc?export=view&id=1uEBleQbcAW3BYb5DDBmmYLSi1QVy8boD', '景點', 'spot2_16'),
(35, '公司田溪橋遺跡', '新北市市定古蹟', 'https://drive.google.com/uc?export=view&id=1TW7SJt0OYSGML-Neo1fpkN_t8xAx5YJe', '景點', 'spot2_17'),
(36, 'Uncle Duncan', '一周只營業10小時的秘境景觀餐廳', 'https://drive.google.com/uc?export=view&id=1XfqBZO-UxW_5t0e6BfSRAUoXTcfVON28', '美食', 'spot3_1'),
(37, '福容大飯店咖啡廳', '田園咖啡廳', 'https://drive.google.com/uc?export=view&id=1ATjJXtiocFZEtq473Mq7SX37wbkYsG4_', '美食', 'spot3_2'),
(38, 'Binma Area 134', '藏身山區的絕美秘境', 'https://drive.google.com/uc?export=view&id=1F5lahba6OhKa6wBIBS63t1EXisuBD4Mh', '美食', 'spot3_3'),
(39, '紅樓咖啡館Rc1899 Café', '紅磚老宅風格咖啡廳', 'https://drive.google.com/uc?export=view&id=1AebQAXx31TpKBF2uFcbl-xY2BDazdzJD', '美食', 'spot3_4'),
(40, 'Ancre café安克黑咖啡', '淡水河畔邊咖啡廳', 'https://drive.google.com/uc?export=view&id=10Qzjg_Yox6pdFNG1EogZYwefAuHYzFKk', '美食', 'spot3_5'),
(41, '領事館咖啡', '淡水老街歐式景觀咖啡廳', 'https://drive.google.com/uc?export=view&id=1z3aIM7Ba-5oM9ldt75p23J4JHvg07dAL', '美食', 'spot3_6'),
(42, '淡水長堤咖啡館', '河景第一排賞日落', 'https://drive.google.com/uc?export=view&id=18njiRwppVLLKM93Z8it2zKrRloulNBzg', '美食', 'spot3_7'),
(43, '淡水雲門星巴克', '森林系星巴克', 'https://drive.google.com/uc?export=view&id=1uv7FvPiD4f0r8-F1jMtZCcRoFAcID9K8', '美食', 'spot3_8'),
(44, '沒有特別計畫café', '淡水隱藏版甜點店', 'https://drive.google.com/uc?export=view&id=1N8Es5mnv68ns3sVmq-aEzhoJNn_Lshq8', '美食', 'spot3_9'),
(45, '閑恬Mydeli手作美味坊', '荷蘭生活美學的巷弄甜點店', 'https://drive.google.com/uc?export=view&id=13FT0vdWU0iklvKdF0fPDdV9j50snYZH1', '美食', 'spot3_10'),
(46, '石牆仔內咖啡館', '百年古厝的玻璃木屋', 'https://drive.google.com/uc?export=view&id=1vWta8fUFYzBGxJSrcEPZ7WE0mfBiPrDw', '美食', 'spot3_11'),
(47, '嗜甜', '簡單美好的甜點店', 'https://drive.google.com/uc?export=view&id=1Z4Q8MDfGdEn7Gqq6qnu4hn-txKvyMXwx', '美食', 'spot3_12'),
(48, '天使熱愛的生活', '吹海風，看夕陽', 'https://drive.google.com/uc?export=view&id=1R3rjawOtuUjeOvMC2TNOY9dyj7ilEWJc', '美食', 'spot3_13'),
(49, '媽媽嘴咖啡(淡水樂活店)', '看風景好去處', 'https://drive.google.com/uc?export=view&id=1SEjmdMWwMT5_jqQTZ-cc_EPvQThmm0l5', '美食', 'spot3_14'),
(50, '紅毛城旁邊咖啡廳', '南法鄉村感的咖啡廳', 'https://drive.google.com/uc?export=view&id=1PMeyBgLnJ1YpgiZx42-ZSpTtQeqhwfaU', '美食', 'spot3_15'),
(51, '英國奶奶Britshake淡水', '道地的英式料理餐廳', 'https://drive.google.com/uc?export=view&id=1PAysMJdXYlp7ECr9mTpDayCAAa1L1GIF', '美食', 'spot3_16'),
(52, 'P Cafe', '老宅X精品咖啡', 'https://drive.google.com/uc?export=view&id=1GuguCMWv-TfeglKHxdVTmDYo_6G3yfZv', '美食', 'spot3_17'),
(53, 'Handshop 撼動屋(英專店)', '小清新甜點店', 'https://drive.google.com/uc?export=view&id=1RFLUB3eEjwBnHLr3ypyyc5pVyduiPtGx', '美食', 'spot3_18'),
(54, '魚見浜燒', '平價海鮮餐廳', 'https://drive.google.com/uc?export=view&id=1X8zMGzTaziZhLaXpP2y73f2Qkvx_pKnZ', '美食', 'spot4_1'),
(55, '小川鍋物', '小農蔬菜火鍋', 'https://drive.google.com/uc?export=view&id=1BsAOPTyilIUuBOmE_9i0T5fg_ryX1fq5', '美食', 'spot4_2'),
(56, '紅色穀倉', '美式景觀餐廳', 'https://drive.google.com/uc?export=view&id=1cVS1xWmx1RFW3smo4ese7QjwtpprgKHy', '美食', 'spot4_3'),
(57, 'La Villa Danshui', '在淡水夕照下用餐', 'https://drive.google.com/uc?export=view&id=1s7Z3uwsSPjkdhBZuFjVwhiqx6srhICz5', '美食', 'spot4_4'),
(58, '水灣BALI 景觀餐廳-榕堤店', '峇里島度假風餐廳', 'https://drive.google.com/uc?export=view&id=1NjZRhCKVHsbfDjOY3buYwPjKTd5gcq8z', '美食', 'spot4_5'),
(59, 'Pescador Cafe 漁夫先生', '享受平日用餐小確幸', 'https://drive.google.com/uc?export=view&id=1q2ALz-P8qVSRyZ-ekA-Ik4ReFsrA9dsV', '美食', 'spot4_6'),
(60, '黑殿飯店', '50年懷舊排骨飯', 'https://drive.google.com/uc?export=view&id=1KEsbHk5HPM2RRllMNGIecq07W1UasBp7', '美食', 'spot4_7'),
(61, '好食寨', '全素中式料理', 'https://drive.google.com/uc?export=view&id=120xTbdqVYUgEeJNVUV6JQvsk3d8OCSpU', '美食', 'spot4_8'),
(62, '墨尼尼義大利餐廳', '道地的義式料理', 'https://drive.google.com/uc?export=view&id=1mR-mz7hvDGEhrGM5Ssj6Lmhle9CQkw0i', '美食', 'spot4_9'),
(63, 'MiNi廚房', '平價又美味的義大利麵', 'https://drive.google.com/uc?export=view&id=14JQnrd3sOgqqSP0BOQAb7SSRwlHG9WbL', '美食', 'spot4_10'),
(64, '牛Bar 淡海店', '淡水商場餐廳', 'https://drive.google.com/uc?export=view&id=17cKtRvLrBX7g5jBQPVQfMe92X4Z5lQXO', '美食', 'spot4_11'),
(65, '時光樹影', '浪漫夕陽打卡新熱點', 'https://drive.google.com/uc?export=view&id=1ITLVzPpcJBZpHt3dsLiIfGu1lvZG1NE3', '美食', 'spot4_12'),
(66, '之間茶食器', '用食物和器物講故事', 'https://drive.google.com/uc?export=view&id=1R00MQtQpouVJ9-xoBwDoRYwRsbjFOI-R', '美食', 'spot4_13'),
(67, 'Pallet Bistro•木棧板餐廳', '異國料理結合當地美食', 'https://drive.google.com/uc?export=view&id=1KYKkJP9g6PbGaCXs3-xexx6gZ14SB7mg', '美食', 'spot4_14'),
(68, 'Number 7 美式餐廳', '美式鄉村風早午餐', 'https://drive.google.com/uc?export=view&id=1kq5-5VnpI4k0riGhEg_XVuYp5kye4R-4', '美食', 'spot4_15'),
(69, '星月 Hoshizuki', '日式定食餐廳', 'https://drive.google.com/uc?export=view&id=1Fw8h2N7BCsZEWN0kfUPdBZ-iDNon6EZj', '美食', 'spot4_16'),
(70, '小李川菜', '便宜又大碗', 'https://drive.google.com/uc?export=view&id=1Jn4nmulL_kQLYKln2AztjcdWMeNdy7D9', '美食', 'spot4_17'),
(71, '源味滷肉飯', '在地必嚐魯肉飯', 'https://drive.google.com/uc?export=view&id=1kWCJ28m5QMKo6Ja3YEhVXIT7qhNT_Tgl', '美食', 'spot4_18'),
(72, 'DAPUNZ 達胖滋', '現做的美式漢堡攤', 'https://drive.google.com/uc?export=view&id=1Fw8h2N7BCsZEWN0kfUPdBZ-iDNon6EZj', '美食', 'spot4_19'),
(73, '雞道樂', '雞湯系拉麵', 'https://drive.google.com/uc?export=view&id=1Wyl21ll8Kso9RsA98mo4Vv9j0dK4KBTI', '美食', 'spot4_20'),
(74, 'Otto Pasta', '隱身住宅區的平價美食', 'https://drive.google.com/uc?export=view&id=19XZE7uJDTJVKGt0g2kbrIM1vghPD9KL0', '美食', 'spot4_21'),
(75, '一個人的披薩', '美食獨享的披薩', 'https://drive.google.com/uc?export=view&id=1A-07U8PAZ5aZCNJLlTeogFxmqT7URTjk', '美食', 'spot4_22'),
(76, '魔法咖哩', '平價咖哩與豪華景觀', 'https://drive.google.com/uc?export=view&id=1gvnMqFBaWWrMQ7mIJPuArJ_Rppp8sTUn', '美食', 'spot4_23'),
(77, '越南小棧', '划算的越南美食', 'https://drive.google.com/uc?export=view&id=1xqkZTEjqIBVBRbu4lUCPjIBV-XILd8Nu', '美食', 'spot4_24'),
(78, 'Kooks 異嗑堂 (K1 Danshui 淡水廚房)', '濃濃美式氣息餐廳', 'https://drive.google.com/uc?export=view&id=1iJ-zlD3QaUYqeR90dK-Nojv2UTbrEzl_', '美食', 'spot4_25'),
(79, '米特食堂MeetEuropa', '歐風料理', 'https://drive.google.com/uc?export=view&id=14U67rxtjKIUzFEQWjC2f08fN6GyIKE-e', '美食', 'spot4_26'),
(80, '蔦燒日式居酒屋-淡水新市店', '武士居酒屋', 'https://drive.google.com/uc?export=view&id=1AJ-fXqRc7kLW3vdICjpLW1sVF0kqDEtA', '美食', 'spot4_27'),
(81, 'Come See Pizza', '可以獨享的披薩', 'https://drive.google.com/uc?export=view&id=1Fw8h2N7BCsZEWN0kfUPdBZ-iDNon6EZj', '美食', 'spot4_28'),
(82, '亨米廚房 Henmi Kitchen', '中式創意餐酒館', 'https://drive.google.com/uc?export=view&id=13Z7W1pSkuZyx9_mO9g76FUulhv0gAXm2', '美食', 'spot4_29'),
(83, '朝日夫婦', '來一碗沖繩刨冰', 'https://drive.google.com/uc?export=view&id=1YLWVBFH8beDbUNdE-zSuwN4TwzxxzhiS', '美食', 'spot5_1'),
(84, '浪花丸', '邊吃冰邊欣賞夕照', 'https://drive.google.com/uc?export=view&id=1ueLaDe3z9am5qucjKNXywy0-P5WNNN5t', '美食', 'spot5_2'),
(85, '新建成餅店', '芝麻蛋黃大餅', 'https://drive.google.com/uc?export=view&id=1vb-viUp1MNgF99T8KNuySTFEdn1336a1', '美食', 'spot5_3'),
(86, '倆樂 LiAng Le', '花生捲冰淇淋', 'https://drive.google.com/uc?export=view&id=1E77zxP0w5BsB-mTRLU3jDDkIJsApGcWM', '美食', 'spot5_4'),
(87, '賴記雞蛋糕', '古早味銅板美食', 'https://drive.google.com/uc?export=view&id=10m0smQ0AXc77xHxYkgFxa_ROFfsJukTf', '美食', 'spot5_5'),
(88, '大吉祥香豆富', '必吃麻辣鴨血臭豆腐', 'https://drive.google.com/uc?export=view&id=1h62e2PzndALOdpAbu_NNvNhrSlUh9pP_', '美食', 'spot5_6'),
(89, '胖達關東煮', '給妳幸福溫情的一餐', 'https://drive.google.com/uc?export=view&id=1R6fTduU17yz0tQpoiWJXHPifbK_oqe9O', '美食', 'spot5_7'),
(90, '源味本鋪古早味現烤蛋糕', '手工古早味蛋糕', 'https://drive.google.com/uc?export=view&id=1XbJ7JfbcotKsIOk-HPhREFixa6-BzxY_', '美食', 'spot5_8'),
(91, '淡水滬尾豆花店', '在地人最愛吃的三色豆花', 'https://drive.google.com/uc?export=view&id=13qAEMbVFVkNg7oDHayoRr_7uDibBAAc6', '美食', 'spot5_9'),
(92, '麻吉奶奶鮮奶麻糬', '手工鮮奶麻糬', 'https://drive.google.com/uc?export=view&id=1cLyXoXjKvZjxJ5uUKGQU947nP1chv91W', '美食', 'spot5_10');

-- --------------------------------------------------------

--
-- 資料表結構 `suggest`
--

CREATE TABLE `suggest` (
  `id` int(11) NOT NULL,
  `name` varchar(30) DEFAULT NULL,
  `body` varchar(100) DEFAULT NULL,
  `email` varchar(80) DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- 資料表結構 `userreister`
--

CREATE TABLE `userreister` (
  `id` int(11) NOT NULL,
  `userid` varchar(80) NOT NULL,
  `email` varchar(80) NOT NULL,
  `password` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- 資料表索引 `collect`
--
ALTER TABLE `collect`
  ADD PRIMARY KEY (`id`),
  ADD KEY `author` (`author`),
  ADD KEY `postid` (`postid`);

--
-- 資料表索引 `like`
--
ALTER TABLE `like`
  ADD PRIMARY KEY (`id`),
  ADD KEY `author` (`author`),
  ADD KEY `postid` (`postid`);

--
-- 資料表索引 `message`
--
ALTER TABLE `message`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_message_timestamp` (`timestamp`);

--
-- 資料表索引 `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`id`),
  ADD KEY `author` (`author`),
  ADD KEY `ix_posts_timestamp` (`timestamp`);

--
-- 資料表索引 `saves`
--
ALTER TABLE `saves`
  ADD PRIMARY KEY (`id`),
  ADD KEY `author` (`author`),
  ADD KEY `ix_saves_timestamp` (`timestamp`);

--
-- 資料表索引 `spot`
--
ALTER TABLE `spot`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `suggest`
--
ALTER TABLE `suggest`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_suggest_timestamp` (`timestamp`);

--
-- 資料表索引 `userreister`
--
ALTER TABLE `userreister`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `userid` (`userid`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `collect`
--
ALTER TABLE `collect`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `like`
--
ALTER TABLE `like`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `message`
--
ALTER TABLE `message`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `posts`
--
ALTER TABLE `posts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `saves`
--
ALTER TABLE `saves`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `spot`
--
ALTER TABLE `spot`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=93;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `suggest`
--
ALTER TABLE `suggest`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `userreister`
--
ALTER TABLE `userreister`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- 已傾印資料表的限制式
--

--
-- 資料表的限制式 `collect`
--
ALTER TABLE `collect`
  ADD CONSTRAINT `collect_ibfk_1` FOREIGN KEY (`author`) REFERENCES `userreister` (`userid`),
  ADD CONSTRAINT `collect_ibfk_2` FOREIGN KEY (`postid`) REFERENCES `posts` (`id`);

--
-- 資料表的限制式 `like`
--
ALTER TABLE `like`
  ADD CONSTRAINT `like_ibfk_1` FOREIGN KEY (`author`) REFERENCES `userreister` (`userid`),
  ADD CONSTRAINT `like_ibfk_2` FOREIGN KEY (`postid`) REFERENCES `posts` (`id`);

--
-- 資料表的限制式 `posts`
--
ALTER TABLE `posts`
  ADD CONSTRAINT `posts_ibfk_1` FOREIGN KEY (`author`) REFERENCES `userreister` (`userid`);

--
-- 資料表的限制式 `saves`
--
ALTER TABLE `saves`
  ADD CONSTRAINT `saves_ibfk_1` FOREIGN KEY (`author`) REFERENCES `userreister` (`userid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
