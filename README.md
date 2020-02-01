# processLimiter
Automatically monitor for and limit the CPU of processes using Python and cpulimit

## Dependencies
Python3 with psutil, cpulimit (tested on Debian 10)

## Setup
1. Edit and place the provided Unit file in /lib/systemd/system/
2. Place the Python file where your Unit file specifies
3. Edit the top of the Python file to suit your use case
4. Run the following commands to have systemd start the Python program automatically on startup 
```
sudo systemctl daemon-reload
sudo systemctl enable processLimiter.service
sudo reboot
```

## Testing 
1. After reboot, check that the systemctl service is working by running
```
sudo systemctl status processLimiter.service
```
2. Run the program you wish to CPU limit and check the usage using
```
top
```
(It may take some time for the program to start being limited, as the program only checks every 60 seconds by default)
