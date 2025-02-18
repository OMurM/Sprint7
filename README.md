### Week 1



### Week 2

    1. Setup Environment for the project

        1.1. create python environment 
        
            - python -m venv venv

        1.2. Initialize the virtual environment
        
            - venv\Scripts\Activate "powershell"
            - venv\Scripts\activate.bat "cmd"

        1.3. Install dependencies
            
            - pip install websockets influxdb-client matplotlib
        
        1.4. Set Up InfluxDB if not done before on Week 1

            - docker run -d --name influxdb -p 8086:8086 -v influxdb:/var/lib/influxdb influxdb:latest
                [docker setup](images/docker.png)
        

