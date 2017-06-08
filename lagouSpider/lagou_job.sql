

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for lagou_job
-- ----------------------------
DROP TABLE IF EXISTS `lagou_job`;
CREATE TABLE `lagou_job` (
  `url` varchar(300) NOT NULL COMMENT '原始url',
  `url_object_id` varchar(50) NOT NULL COMMENT 'url的md5转存',
  `title` varchar(100) NOT NULL COMMENT '职位名称',
  `salary_min` varchar(5) DEFAULT NULL COMMENT '最小薪资',
  `salary_max` varchar(5) DEFAULT NULL COMMENT '最大薪资',
  `work_years` varchar(11) DEFAULT NULL COMMENT '最小工作年限',
  `degree_need` varchar(30) DEFAULT NULL COMMENT '学历要求',
  `job_type` varchar(20) DEFAULT NULL COMMENT '职位类型全职还是兼职',
  `publish_time` varchar(20) DEFAULT NULL COMMENT '发布职位时间',
  `tags` varchar(100) DEFAULT NULL COMMENT '职位标签',
  `job_advantage` varchar(1000) DEFAULT NULL COMMENT '职位诱惑',
  `job_desc` longtext COMMENT '职位描述',
  `job_addr` varchar(50) DEFAULT NULL COMMENT '工作地点',
  `company_url` varchar(300) DEFAULT NULL COMMENT '公司url',
  `company_name` varchar(100) DEFAULT NULL COMMENT '公司名称',
  `crawl_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `crawl_update_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `job_city` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`url_object_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
SET FOREIGN_KEY_CHECKS=1;
