from abc import ABC, abstractmethod

class NotificationChannel(ABC):
    """通知渠道的基类"""
    
    @abstractmethod
    def send(self, title: str, content: str, receivers: list) -> bool:
        """
        发送通知
        :param title: 通知标题
        :param content: 通知内容
        :param receivers: 接收者列表
        :return: 发送是否成功
        """
        pass 