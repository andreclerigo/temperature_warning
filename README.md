# :warning:Temperature Warning Script  
This project was made when I realised someone covered my Raspberry Pi and it was constantly running at 99ºC  
This script will send yourself an email when the device is above 70ºC (this value can be changed on the .py)

## Usage
### Setup your email
Create a `.env` file on the same directory as `script.py`
```
EMAIL="YOUR_EMAIL_HERE"
PASSWORD="YOUR_PASSWORD_HERE"
```

### Create a service
On `line 7` in `temp.service`  
Change `/home/pi/temperature_warning/script.py` to `your_path_to_file/temperature_warning/script.py`  
If you aren't sure what's the path to the file go inside the directory that contains the file and do `pwd` on the terminal  

Now open the terminal on `temperature_warning/` and run  
```
sudo cp temp.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start temp.service 
sudo systemctl enable temp.service
```
The last command is to make sure that the service is started on system startup

**Note:** Currently this script is done for emails from gmail

## Realtime Information
To get the current temperature on CPU and GPU run the shell script  
`watch ./pi-temp.sh` to get the information at all time  
`./pi-temp.sh` to get the temperature once  
