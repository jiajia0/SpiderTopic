 - 利用scrapy爬取[伯乐在线](http://www.jobbole.com/)下的文章内容，并且存入本地的mysql数据库中。

 - 创建spider数据库，并创建相关结构表：
```
SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for jobboleblog
-- ----------------------------
DROP TABLE IF EXISTS `jobboleblog`;
CREATE TABLE `jobboleblog` (
  `title` varchar(200) NOT NULL,
  `create_date` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `url` varchar(300) NOT NULL,
  `url_object_id` varchar(50) NOT NULL,
  `front_image_url` varchar(300) DEFAULT NULL,
  `front_image_path` varchar(300) CHARACTER SET utf8mb4 DEFAULT NULL,
  `comment_nums` int(11) NOT NULL DEFAULT '0',
  `fav_nums` int(11) NOT NULL DEFAULT '0',
  `praise_nums` int(11) NOT NULL DEFAULT '0',
  `tags` varchar(100) DEFAULT NULL,
  `content` longtext CHARACTER SET utf8mb4 NOT NULL,
  PRIMARY KEY (`url_object_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
SET FOREIGN_KEY_CHECKS=1;
```

 - 修改settings下的相关数据库配置，即可运行main函数进行爬取保存。