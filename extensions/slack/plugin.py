"""Slack channel plugin"""

from clawdbot.channels.registry import get_channel_registry
from clawdbot.channels.slack import SlackChannel


def register(api):
    """Register Slack channel"""
    channel = SlackChannel()
    registry = get_channel_registry()
    registry.register(channel)
