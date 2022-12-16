# Setup 

## Azure VM

1. Subscription: Azure for Students

2. Virtual Machine Name: MySQL

3. Region: (US) EAST US

4. Availability Zone: Zones 1

5. Image: Ubuntu Server 20.04 LTS -x64 Gen2

6. Size: Standard_D2s_v3 - 2 vcpus, 8 GiB Memory

7. Public Inbound Ports: Allow Selected Ports

8. Select Inbout Ports: HTTP (80), HTTPS (433), SSH (22)

9. Review and Create 

## Connect 

1. Open CMD Terinal 

2. SSH In: ssh -i <private key path> UserAdmin@4.236.187.210

## Set up OS image

1. Update OS command: sudo apt-get update

2. Install mysql command: sudo apt install mysql-server mysql-client

3. Login to mysql command: sudo mysql
