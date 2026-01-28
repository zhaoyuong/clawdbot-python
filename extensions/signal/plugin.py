"""Signal channel plugin"""

from clawdbot.channels.registry import get_channel_registry
from clawdbot.channels.signal import SignalChannel


def register(api):
    """Register Signal channel"""
    channel = SignalChannel()
    registry = get_channel_registry()
    registry.register(channel)
