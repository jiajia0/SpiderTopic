SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for zhihu_question
-- ----------------------------
DROP TABLE IF EXISTS `zhihu_question`;
CREATE TABLE `zhihu_question` (
  `zhihu_id` int(11) NOT NULL,
  `topics` varchar(255) DEFAULT NULL,
  `url` varchar(300) NOT NULL,
  `title` varchar(200) NOT NULL,
  `content` longtext NOT NULL,
  `create_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `update_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `answer_num` int(11) NOT NULL,
  `comments_num` int(11) NOT NULL,
  `watch_user_num` int(11) NOT NULL,
  `click_num` int(11) NOT NULL,
  `crawl_time` datetime NOT NULL ON UPDATE CURRENT_TIMESTAMP,
  `crawl_update_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`zhihu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
SET FOREIGN_KEY_CHECKS=1;
