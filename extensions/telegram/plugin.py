"""Telegram channel plugin"""

from clawdbot.channels.registry import get_channel_registry
from clawdbot.channels.telegram import TelegramChannel


def register(api):
    """Register Telegram channel"""
    channel = TelegramChannel()
    registry = get_channel_registry()
    registry.register(channel)
