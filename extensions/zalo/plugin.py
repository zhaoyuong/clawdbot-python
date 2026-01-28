"""zalo channel plugin"""

from clawdbot.channels.registry import get_channel_registry
from clawdbot.channels.zalo import ZaloChannel


def register(api):
    """Register zalo channel"""
    channel = ZaloChannel()
    registry = get_channel_registry()
    registry.register(channel)
