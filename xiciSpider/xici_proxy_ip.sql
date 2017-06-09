

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for cixi_proxy_ip
-- ----------------------------
DROP TABLE IF EXISTS `xici_proxy_ip`;
CREATE TABLE `cixi_proxy_ip` (
  `ip` varchar(20) NOT NULL,
  `port` varchar(255) NOT NULL,
  `speed` float DEFAULT NULL,
  `proxy_type` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`ip`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
SET FOREIGN_KEY_CHECKS=1;
