from django.test import TestCase
from django.core.management import call_command
from unittest.mock import patch
import time

class TestSchedulerCommands(TestCase):
    @patch('apps.scheduler.scheduler.start')
    def test_run_scheduler_command(self, mock_start):
        """测试运行调度器命令"""
        with self.assertRaises(KeyboardInterrupt):
            with patch('time.sleep', side_effect=KeyboardInterrupt):
                call_command('run_scheduler')
        
        mock_start.assert_called_once() 