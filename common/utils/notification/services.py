from typing import List
from .base import NotificationChannel
from .email_channel import EmailChannel

class NotificationService:
    def __init__(self):
        self.channels: List[NotificationChannel] = [
            EmailChannel(),
            # 后续可以添加其他渠道
            # DingTalkChannel(),
            # FeishuChannel(),
            # WeChatChannel(),
        ]
    
    def send_notification(self, title: str, content: str, receivers: list):
        """
        发送通知到所有配置的渠道
        """
        results = []
        for channel in self.channels:
            result = channel.send(title, content, receivers)
            results.append(result)
        return all(results)  # 所有渠道都发送成功才返回True 