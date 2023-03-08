from nonebot import logger
from pydantic import BaseModel, Extra


class Config(BaseModel, extra=Extra.ignore):
    forwarder_source_group: list = []
    forwarder_dest_group: list = []
    forwarder_prefix: list = [""]
    forwarder_explict: list = [""]
    forwarder_show_sender: str = "none"

    # 重载 Pydantic 的 __init__ 方法，字段不存在时打印warning
    def __init__(self, **data):
        super().__init__(**data)
        for field in self.__fields__.values():
            if field.name not in data:
                default_value = getattr(self, field.name)
                logger.warning(
                    f"[转发姬] 未发现配置项 {field.name} , 采用默认值: {default_value}")
