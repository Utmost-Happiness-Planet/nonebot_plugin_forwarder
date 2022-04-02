from nonebot import get_driver, logger

config = get_driver().config

if not hasattr(config, "forwarder_source_group"):
    forwarder_source_group = [""]
    logger.info("未检测到forwarder_source_group配置")
else:
    forwarder_source_group = config.forwarder_source_group

if not hasattr(config, "forwarder_dest_group"):
    forwarder_dest_group = [""]
    logger.info("未检测到forwarder_dest_group配置")
else:
    forwarder_dest_group = config.forwarder_dest_group

if not hasattr(config, "forwarder_prefix"):
    forwarder_prefix = [""]
    logger.info("未检测到forwarder_prefix配置，默认为['']")
else:
    forwarder_prefix = config.forwarder_prefix
if not hasattr(config, "forwarder_explict"):
    forwarder_explict = [""]
    logger.info("未检测到forwarder_explict配置，默认为['']")
else:
    forwarder_explict = config.forwarder_explict
