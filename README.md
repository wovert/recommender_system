# 推荐系统

## 什么是推荐系统

> 推荐系统是指通过人工和非人工向用户建议购买/浏览物品的有规律行动

- 系统
  - 自然界的系统
  - 计算机工业中的系统

## 推荐系统应用领域

- 商品品类多，用户有规模是推荐系统
- 生活快消品和内容快消品是主要变现领域（这两个领域应用优势，如何解决消费者痛点）
- 推荐系统将在共享经济领域掀起一阵大浪【如何准确的实现共享经济的价值】
- 车载消费体系

## 优酷最初推荐系统版图

- 推荐算法
  - 基于内容推荐
  - 基于知识推荐
  - 协同过滤推荐
- 推荐排序
  - 通用解决方案
  - 混合解决方案
- 推荐基础研究
  - 协同过滤算法移植优化
- 推荐引擎及优化
  - 减少响应时间
  - 正价更多复杂的推荐机制
- 推荐融合
  - 基于不同数据源产生的推荐结果
  - 分配比例
- NLP
  - 自然语言处理、图像图像处理

## 推荐系统工种细分

- 推荐算法工程师
- 全栈工程师
- 算法研究员
- 推荐引擎工程师

## AI是什么？

> 从机器角度执行具体任务的目标最大化过程就是人工智能的表现

## IMDJ电影推荐系统剖析

- Internet Moview Database 【媒体库】
  - 440万个影片信息
  - 包含电影、综艺、电视剧等节目详细信息
  - 电影数据挖掘从业者必爬的网站

- Internet Moview Database 【用户资源】
  - 7千6百万个注册会员
  - 专业电影看客比去的门户网站
  - 通过增值服务盈利

### Why IMDB

- 最悠久的历史【28年】
- 最忠实的用户的群体
- 最完整的电影信息

## Netflix 电影推荐系统深度

> Netflix is an American entertainment company founded by Reed Hastings and Marc Randolph on august 29, 1997, in Scotts Valley, California. It specializes in and provides streaming media and video-on-demand online and DVD by mail. In 2013, Netflix expanded into film and television production, as well as online distribution. As of 2017, the compoany has its headquarters in Logs Gatos, California.

## 推荐引擎

### 推荐引擎内部逻辑

#### 推荐引擎模块

- 接受请求
- 处理请求
- 返回结果

#### 制造日志

- 日志格式
  - cookie
  - uid 用户编号
  - user agent 代理信息
  - ip 地址
  - video_id 视频编号
  - topic
  - order_id 订单=>付费观看
  - log_type
- 日志种类
  - 点击
  - 播放
  - 点赞
  - 收藏
  - 付费观看
  - 站外分享
  - 评论