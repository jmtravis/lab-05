import platform
import time
import pandas as pd
import plotly.express as px
import numpy as np
import subprocess
import re

def get_wifi_signal_strength() -> int:
    """Get the signal strength of the wifi connection.
    
    Returns:
        The signal strength in dBm.
    """
    # Question 1: What is dBm? What values are considered good and bad for WiFi signal strength?
    # dBm is defined as "a signal strength or power level." Signals better than -85 decibels are considered usable and strong and a signal that's weaker is too problematic to be useful 
    #  (i.e., results in dropped calls and incomplete data transmissions).

    # Question 2: Why do we need to check the OS? What is the difference between the commands for each OS?
    #  Checking the operating system to ensure the correct command is used for the specific operating system.


    # Question 3: In your own words, what is subprocess.check_output doing? What does it return?
    # HINT: https://docs.python.org/3/library/subprocess.html#subprocess.check_output
    # subprocess.check.output runs the command in the OS with agruments and returns its output.

    # Question 4: In your own words, what is re.search doing? What does it return?
    # HINT: https://docs.python.org/3/library/re.html#re.search
    # re.search scans through the "signal level" string looking for the frst location where the regualr expression 
    # pattern produces a match and returns a corresponding matching object. 

    # Question 5: In the Windows case, why do we need to convert the signal quality to dBm?
    # HINT: https://learn.microsoft.com/en-us/windows/win32/api/wlanapi/ns-wlanapi-wlan_association_attributes?redirectedfrom=MSDN
    # Signal quality needs to be converted to dBm because signal quality returns a percentage of maximum signal strength between 0 to 100 
    # which needs to coverted to dBm.

    if platform.system() == 'Linux': # Linux
        output = subprocess.check_output("iwconfig wlan0", shell=True)
        match = re.search(r"Signal level=(-?\d+) dBm", output.decode('utf-8'))
        signal_strength = int(match.group(1))
    elif platform.system() == 'Windows': # Windows
        output = subprocess.check_output("netsh wlan show interfaces", shell=True)
        match = re.search(r"Signal\s*:\s*(\d+)%", output.decode('utf-8'))
        signal_quality = int(match.group(1))
        signal_strength = -100 + signal_quality / 2
    elif platform.system() == 'Darwin': # Mac
        output = subprocess.check_output("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I", shell=True)
        match = re.search(r"agrCtlRSSI:\s*(-?\d+)", output.decode('utf-8'))
        signal_strength = int(match.group(1))
    else:
        raise Exception("Unknown OS")

    return signal_strength

def main():
    # Choose at least 5 locations to sample the signal strength at
    # These can be rooms in your house, hallways, different floors, outside, etc. (as long as you can get a WiFi signal)
    locations = ['bedroom', 'living room', 'kitchen', 'bathroom', 'garage']
    samples_per_location = 10 # number of samples to take per location
    time_between_samples = 1 # time between samples (in seconds)

    data = [] # list of data points
    for location in locations:
        print(f"Go to the {location} and press enter to start sampling")
        input() # wait for the user to press enter
        signal_strengths = [] # list of signal strengths at this location

        # TODO: collect 10 samples of the signal strength at this location, waiting 1 second between each sample
        # HINT: use the get_wifi_signal_strength function
        for i in range (samples_per_location):
            signal_strengths.append(get_wifi_signal_strength())
        
        
        # TODO: calculate the mean and standard deviation of the signal strengths you collected at this location
        signal_strength_mean = np.mean(signal_strengths)
        signal_strength_std = np.std(signal_strengths)

        # Question 6: What is the standard deviation? Why is it useful to calculate it?
        # A standard deviation (or σ) is a measure of how dispersed the data is in relation to the mean. 
        # Standard deviation is important because it helps in understanding the measurements when the signal data is distributed. 


        data.append((location, signal_strength_mean, signal_strength_std))

    # create a dataframe from the data
    df = pd.DataFrame(data, columns=['location', 'signal_strength_mean', 'signal_strength_std'])

    # Question 7: What is a dataframe? Why is it useful to use a dataframe to store the data?
    # HINT: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
    # HINT: print the dataframe to see what it looks like
    # print(df)
    #  print(df.head())
    # A DataFrame is a data structure that is useful in organizing data into a 2-dimensional table of rows and columns.
   

    # TODO: plot the data as a bar chart using plotly
    # HINT: https://plotly.com/python/bar-charts/
    # NOTE: use the error_y parameter of px.bar to plot the error bars (1 standard deviation)
    #   documentation: https://plotly.com/python-api-reference/generated/plotly.express.bar.html
    fig = px.bar(df,  x= 'location', y= 'signal_strength_mean', error_y = 'signal_strength_std', labels = {'locations': 'locations', 'signal_strength_mean': 'Signal Strength Mean'}
        
    )

    # Question 8: Why is it important to plot the error bars? What do they tell us?
    # The importance of inferential error bars are that their length gives a graphic signal of 
    # how much uncertainty there is in the data: in this case it tell us the certainy of the signal strength. Variation between samples.
    # Higher error band means it more unreliable.

    # write the plot to a file - make sure to commit the PNG file to your repository along with your code
    fig.write_image("signal_strength.png")

    # Question 9: What did you observe from the plot? How does the signal strength change as you move between locations?
    #             Why do you think signal strength is weaker in certain locations?
    # What I oberved from the plot is that the kitchen signal had the stongest signal and the garage had the weakest signal 
    # as it was further away from the source. 


if __name__ == "__main__":
    main()
