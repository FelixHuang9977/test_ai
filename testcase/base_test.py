import subprocess
import pytest
import logging
import os

class BaseTest:
    """Base class for all system diagnostic tests"""
    
    @classmethod
    def setup_class(cls):
        """Setup logging for the test class"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        cls.logger = logging.getLogger(cls.__name__)
    
    def run_command(self, command):
        """Execute a shell command and return the result"""
        try:
            result = subprocess.run(
                command,
                shell=True,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Command failed: {e}")
            self.logger.error(f"stderr: {e.stderr}")
            raise
    
    def get_system_info(self):
        """Get basic system information"""
        info = {}
        try:
            info['hostname'] = self.run_command('hostname')
            info['os'] = self.run_command('uname -a')
            return info
        except Exception as e:
            self.logger.error(f"Failed to get system info: {e}")
            raise