"""teams channel plugin"""

from clawdbot.channels.registry import get_channel_registry
from clawdbot.channels.teams import TeamsChannel


def register(api):
    """Register teams channel"""
    channel = TeamsChannel()
    registry = get_channel_registry()
    registry.register(channel)
