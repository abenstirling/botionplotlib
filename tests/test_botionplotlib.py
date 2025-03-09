import unittest
import matplotlib.pyplot as plt
import numpy as np
import os
import shutil

# Import the package
import botionplotlib

class TestBotionplotlib(unittest.TestCase):
    
    def setUp(self):
        # Create a test directory
        if os.path.exists('botionplotlib_output'):
            shutil.rmtree('botionplotlib_output')
        os.makedirs('botionplotlib_output', exist_ok=True)
    
    def tearDown(self):
        # Clean up test directory
        if os.path.exists('botionplotlib_output'):
            shutil.rmtree('botionplotlib_output')
    
    def test_plot_creation(self):
        # Create a simple plot
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        
        plt.figure()
        plt.plot(x, y, label='Sine')
        plt.title('Test Plot')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.grid(True)
        plt.show()
        
        # Check if the file was created
        self.assertTrue(os.path.exists('botionplotlib_output/test_plot.png'))

if __name__ == '__main__':
    unittest.main() 