# Lab 5
Clone this repo to your machine to get started!

## Team Members
- Jaya Travis


## Lab Question Answers

Answer for Question 1: 

## Question 1: What is dBm? What values are considered good and bad for WiFi signal strength?

dBm is defined as "a signal strength or power level." Signals better than -85 decibels are considered usable and strong and a signal that's weaker is too problematic to be useful (i.e., results in dropped calls and incomplete data transmissions).

## Question 2: Why do we need to check the OS? What is the difference between the commands for each OS?
Checking the operating system to ensure the correct command is used for the specific operating system.


## Question 3: In your own words, what is subprocess.check_output doing? What does it return?
HINT: https://docs.python.org/3/library/subprocess.html#subprocess.check_output

subprocess.check.output runs the command in the OS with agruments and returns its output.

## Question 4: In your own words, what is re.search doing? What does it return?
HINT: https://docs.python.org/3/library/re.html#re.search

re.search scans through the "signal level" string looking for the frst location where the regualr expression 
pattern produces a match and returns a corresponding matching object. 

## Question 5: In the Windows case, why do we need to convert the signal quality to dBm?
HINT: https://learn.microsoft.com/en-us/windows/win32/api/wlanapi/ns-wlanapi-wlan_association_attributes?redirectedfrom=MSDN
    
Signal quality needs to be converted to dBm because signal quality returns a percentage of maximum signal strength between 0 to 100 
which needs to coverted to dBm.


## Question 6: What is the standard deviation? Why is it useful to calculate it?

A standard deviation (or σ) is a measure of how dispersed the data is in relation to the mean. 
Standard deviation is important because it helps in understanding the measurements when the signal data is distributed. 


     
## Question 7: What is a dataframe? Why is it useful to use a dataframe to store the data?
 HINT: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
 HINT: print the dataframe to see what it looks like
 print(df)
    
A DataFrame is a data structure that is useful in organizing data into a 2-dimensional table of rows and columns.

## Question 8: Why is it important to plot the error bars? What do they tell us?

The importance of inferential error bars are that their length gives a graphic signal of how much uncertainty there is in the data: in this case it tell us the certainy of the signal strength. Variation between samples. Higher error band means it more unreliable.

 
## Question 9: What did you observe from the plot? How does the signal strength change as you move between locations? Why do you think signal strength is weaker in certain locations?

What I oberved from the plot is that the kitchen signal had the stongest signal and the garage had the weakest signal as it was further away from the source. 

## Question 10: Do you notice any trends in the data? How does it differ from Part 1? What do you think is causing the differences?

Delay starts at high value when message size is zero. Delay decreases as message size increases. It reaches the lowest delay at 1000 bytes and delay starts to increase as byte size increases from 1000 bytes.

