docker context create --docker 'host=ssh:/ubuntu@*server-link*' *container-name*
docker context ls
docker context use *container-name*
***
docker compose down --rmi all -v
docker compose up -d
docker compose up -d --build
docker ps                            
docker ps -a                         
docker exec -ti *container-name* sh  
docker logs *container-name*         
docker down                          
docker container rm *container-name* 
***
https://github.com/LS-Shikano/LithuanianBallot/blob/e4a65156ee3c838a395ebce0ba04a5132c1a7156/bw-cloud-otree-setup.md