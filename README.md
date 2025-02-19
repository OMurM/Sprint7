# Week 1

> Analize the component structure used in the python codes I gave you

> (Optional) Create a thingsboard with docker-compose in a kali linux or equivalent. Remember to change the name of the virtual machine and put your initials.

> (Optional) Test the examples of the folder EjemplosComponentes

> Create a database InfluxDB using docker

> Test all the codes showed in folder InfluxDB

**Remember that the subscription need to have code executed in the server.**

> Create a video showing all work perfect

## Analize the component strucutre used int the python codes I gave you

## Create a thingsboard with docker-compose in a kali linux or equivalent

For creating a thingsboard with docker-compose we will use docker desktop.
- Create the volumes were the database and the logs will be saved 

    docker volume create mytb-data

    docker volume create mytb-logs

- Create the **docker-compose.yml** 

```yml

services:
    mytb:
        image: thingsboard/tb-postgres
        ports:
            - "8080:8080"
            - "1883:1883"
            - "5683-5688:5683-5688/udp"
        volumes:
            - mytb-data-OMM:/data
            - mytb-logs-OMM:/var/log/thingsboard
    environment:
        TB_QUEUE_TYPE: "inmemory"
    restart: on-failure
volumes:
    mytb-data:
        external: true
    mytb-logs:
        external: true

```

- Run the docker-compose
```sh
docker-compose up

docker-compose up -d 

```
![ThingsBoard](images/ThingsBoardUp.png)

- Acces via web browser to http://localhost:8080 and add the default credentials to login

    System Administrator: sysadmin@thingsboard.org / sysadmin

    Tenant Administrator: tenant@thingsboard.org / tenant
    
    Customer User: customer@thingsboard.org / customer

![ThingsBoardLogin](images/ThingsBoardLogin.png)

- Look the ThingsBoard dashboard

![ThingsBoardDashboard](images/ThingsBoardDashboard.png)

## Test the examples of the folder EjemplosComponentes

## Create a database InfluxDB using docker

## Test all the codes showed in folder InfluxDB

# Week 2

## ToDo

> Simulate a farm IoT with python, Influxdb and Websocket using components ☑️
> Create 2-3 sensors 
> Simulate 2 actuators with python (this should be a subscription)
> Generate some dashboards using graph
> Generate some alerts
> All need to be create using the concept of components (reusing code)

## Setup Environment for the project

### create python environment 

    python -m venv venv

### Initialize the virtual environment
        
    venv\Scripts\Activate "powershell"
    venv\Scripts\activate.bat "cmd"

### Install dependencies
            
    pip install websockets influxdb-client matplotlib
        
### Set Up InfluxDB if not done before on Week 1

    docker run -d --name influxdb -p 8086:8086 -v influxdb:/var/lib/influxdb influxdb:latest

![docker setup](images/docker.png)
            
### We setup the initial user and oraganization

![influxdb setup](images/admi_setup.png)

> remember to save the API key token for example "wLVOD7Og3K2kR8OlRL_AfPCLBHnCM53fcRjoosXluFWMyIX0TmNVXCcM5mjGIvcy11Vt5lHroLZg9PD5UxSmYw=="

### We create a bucket with the name "iot_farm"
![create bucket](images/create_bucket.png)


