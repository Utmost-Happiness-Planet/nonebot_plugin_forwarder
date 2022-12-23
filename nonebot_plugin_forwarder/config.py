from nonebot import get_driver, logger

config = get_driver().config.dict()

if 'forwarder_source_group' not in config:
    logger.warning('[转发姬] 未发现配置项 `forwarder_source_group` , 采用默认值: []')
if 'forwarder_dest_group' not in config:
    logger.warning('[转发姬] 未发现配置项 `forwarder_dest_group` , 采用默认值: []')
if 'forwarder_prefix' not in config:
    logger.warning('[转发姬] 未发现配置项 `forwarder_prefix` , 采用默认值: [""]')
if 'forwarder_explict' not in config:
    logger.warning('[转发姬] 未发现配置项 `forwarder_explict` , 采用默认值: [""]')
if 'forwarder_show_sender' not in config:
    logger.warning('[转发姬] 未发现配置项 `forwarder_show_sender` , 采用默认值: False')


forwarder_source_group = config.get('forwarder_source_group', [])
forwarder_dest_group = config.get('forwarder_dest_group', [])
forwarder_prefix = config.get('forwarder_prefix', [""])
forwarder_explict = config.get('forwarder_explict', [""])
forwarder_show_sender = config.get('forwarder_show_sender', False)
