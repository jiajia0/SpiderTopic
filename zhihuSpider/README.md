 - 利用scrapy爬取[个人知乎首页](http://www.zhihu.com/)下的问题及回答，并且存入本地的mysql数据库中。

 - 创建spider数据库，并创建相关结构表：

 - 使用zhihu_question.sql和zhihu_answer.sql导入表结构。

 - 修改settings下的相关数据库配置，即可运行main函数进行爬取保存。

  - 需要输入个人账号信息，只支持手机号码格式登录。