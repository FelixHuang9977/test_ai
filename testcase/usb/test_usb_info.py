from ..base_test import BaseTest

class TestUSBInfo(BaseTest):
    """USB device testing class"""
    
    def test_usb_list(self):
        """Test USB device listing"""
        result = self.run_command("lsusb")
        assert result['status'] == 0, "Failed to list USB devices"
        
    def test_usb_details(self):
        """Test USB device detailed information"""
        result = self.run_command("lsusb -v")
        assert result['status'] == 0, "Failed to get USB details"
        
    def test_usb_ports(self):
        """Test USB ports status"""
        result = self.run_command("ls -l /dev/bus/usb/")
        assert result['status'] == 0, "Failed to check USB ports"
        
    def test_usb_storage(self):
        """Test USB storage device detection"""
        result = self.run_command("lsblk -d -o NAME,TYPE,VENDOR,MODEL,TRAN")
        assert result['status'] == 0, "Failed to check USB storage devices"
        
    def test_usb_power(self):
        """Test USB power status"""
        result = self.run_command("cat /sys/bus/usb/devices/*/power/control")
        assert result['status'] == 0, "Failed to check USB power status"