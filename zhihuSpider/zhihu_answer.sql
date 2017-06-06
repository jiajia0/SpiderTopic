
SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for zhihu_answer
-- ----------------------------
DROP TABLE IF EXISTS `zhihu_answer`;
CREATE TABLE `zhihu_answer` (
  `zhihu_id` bigint(20) NOT NULL,
  `url` varchar(300) NOT NULL,
  `question_id` bigint(20) NOT NULL,
  `author_id` varchar(100) DEFAULT NULL,
  `content` longtext NOT NULL,
  `parise_num` int(11) NOT NULL,
  `comments_num` int(11) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  `crawl_time` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP,
  `crawl_update_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
SET FOREIGN_KEY_CHECKS=1;
