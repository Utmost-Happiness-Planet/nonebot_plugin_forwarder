<div align='center'>

  # Forwarder
  
  ✨ 一个基于 [NoneBot2](https://github.com/nonebot/nonebot2) 的插件, 她可以将甲群的消息转发到乙群。 ✨
  
</div>

<p align="center">
  
  <a href="https://github.com/ninthseason/nonebot-plugin-directlinker/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-GPL3.0-informational">
  </a>
  
  <a href="https://github.com/nonebot/nonebot2">
    <img src="https://img.shields.io/badge/nonebot-v2-green">
  </a>
  
  <a href="">
    <img src="https://img.shields.io/badge/release-v2.0-orange">
  </a>
  
</p>

> *其实她还有另一个名字 —— 转发姬。*

### ⭐功能

准确的说。她可以将若干个源群(Source Groups)中满足特定规则的消息转发到若干个目标群(Destination Groups)中。

### 🎞用途

1. 多群广播
2. 无情的转发机器

### 📕用法

需要在`.env.*`中有如下配置：

```python
forwarder_source_group = ["<QQ群号>"]  # 源信息群
forwarder_dest_group = ["<QQ群号>"]  # 目标群
forwarder_prefix = ["<前缀格式>"]  # 触发转发的消息前缀 ( [""] 则为全部转发)
forwarder_explict = ["<QQ号>"]  # 指定只有特定人消息被转发 ( [""] 则为全部转发)
```

按常规方法安装插件即可。

### 已知BUG

形如 `<三个汉字><图片>` 的信息无法转发，原因未知。

### 🎈致谢

感谢某个沙雕分享群，让我萌生出把里面的沙雕消息自动转发给我的其他群的想法。
