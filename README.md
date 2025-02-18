### Week 1



### Week 2

## Setup Environment for the project

# create python environment 

- python -m venv venv

# Initialize the virtual environment
        
- venv\Scripts\Activate "powershell"
- venv\Scripts\activate.bat "cmd"

 # Install dependencies
            
- pip install websockets influxdb-client matplotlib
        
# Set Up InfluxDB if not done before on Week 1

- docker run -d --name influxdb -p 8086:8086 -v influxdb:/var/lib/influxdb influxdb:latest
[docker setup](images/docker.png)
            
- We setup the initial user and oraganization
[influxdb setup](images/admi_setup.png)

- remember to save the API key token for example "wLVOD7Og3K2kR8OlRL_AfPCLBHnCM53fcRjoosXluFWMyIX0TmNVXCcM5mjGIvcy11Vt5lHroLZg9PD5UxSmYw=="

- We create a bucket with the name "iot_farm"
[create bucket](images/create_bucket.png)



