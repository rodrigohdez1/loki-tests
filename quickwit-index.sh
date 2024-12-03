#!/bin/bash
docker cp nginx-index-config.yaml  quickwit-quickwit-1:/tmp/ 
docker exec -it  quickwit-quickwit-1 quickwit index create --index-config /tmp/index-config.yaml
#!/bin/bash
docker exec -it  quickwit-quickwit-1 quickwit index delete --index index-name
