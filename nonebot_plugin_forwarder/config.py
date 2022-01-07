from nonebot import get_driver, logger

forwarder_source_group = get_driver().config.forwarder_source_group
forwarder_dest_group = get_driver().config.forwarder_dest_group
forwarder_prefix = get_driver().config.forwarder_prefix
forwarder_explict = get_driver().config.forwarder_explict

if not forwarder_source_group:
    forwarder_source_group = [""]
    logger.info("未检测到forwarder_source_group配置")
if not forwarder_dest_group:
    forwarder_dest_group = [""]
    logger.info("未检测到forwarder_dest_group配置")
if not forwarder_prefix:
    forwarder_prefix = [""]
    logger.info("未检测到forwarder_prefix配置，默认为['']")
if not forwarder_explict:
    forwarder_explict = [""]
    logger.info("未检测到forwarder_explict配置，默认为['']")
