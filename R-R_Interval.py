import matlab.engine
import numpy as np
import pandas as pd

# Start MATLAB Engine

eng = matlab.engine.start_matlab()
try:
	# Load ECG signal from CSV file
	eng.addpath('C:\Users\rohan\OneDrive\Desktop\ecgsite\rrin')
	eng.cd('C:\Users\rohan\OneDrive\Desktop\ecgsite\rrin')
	# Call the MATLAB function
	y_filt = eng.rrinterval()
	print(int(y_filt["avg_rr_intervals"]))
	print(int(y_filt["hbpermin"]))
	print(int(y_filt["std_value"]))
finally:
	# Stop MATLAB Engine
	eng.quit()