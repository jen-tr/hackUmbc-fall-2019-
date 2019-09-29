How to Mongo

1. run `sudo docker run --name some-mongo -d mongo:3.4-xenial`
2. run `sudo docker ps` to get container ID (should be a hex string, first entry in the table)
3. run `sudo docker exec -it [CONTAINER_ID] cat /etc/hosts` to get the container IP (should be the last line)
4. change the IP in the python file to the right IP.
5. `sudo docker exec -it [CONTAINER_ID] mongo` to drop to a mongo command line to set up anything else/view the DB
