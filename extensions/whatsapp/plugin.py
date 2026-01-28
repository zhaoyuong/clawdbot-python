"""WhatsApp channel plugin"""

from clawdbot.channels.registry import get_channel_registry
from clawdbot.channels.whatsapp import WhatsAppChannel


def register(api):
    """Register WhatsApp channel"""
    channel = WhatsAppChannel()
    registry = get_channel_registry()
    registry.register(channel)
