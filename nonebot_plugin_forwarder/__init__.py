import logging

from nonebot import on_message, logger
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot
from nonebot.rule import startswith
from nonebot.typing import T_State
from nonebot.params import State
import asyncio

from .config import forwarder_explict, forwarder_prefix, forwarder_dest_group, forwarder_source_group

rule = startswith(forwarder_prefix)
msg_matcher = on_message(rule, priority=10, block=False)


async def send_meg(bot: Bot, group_id: str, msg: str):
    logger.debug(f"消息转发至: {group_id}")
    await bot.send_group_msg(group_id=group_id, message=msg, auto_escape=False)


@msg_matcher.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    if str(event.group_id) in forwarder_source_group:
        flag = forwarder_explict[0] == "" or str(event.user_id) in forwarder_explict
        if flag and forwarder_dest_group[0] != "":
            msg = str(event.message)
            logger.debug(f"欲转发消息: {msg}")
            tasks = [send_meg(bot, gid, msg) for gid in forwarder_dest_group]
            await asyncio.wait(tasks)
