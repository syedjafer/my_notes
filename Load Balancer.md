Load balancer will distribute the traffic appropriately so that a single server. 

2 types of load balancer:
* L4 - Network Layer LB (TCP port/UDP port/ IP Address / Source and Destination)
* L7 - Application Layer (Can read your header, session, cookies, cache, data)



L4 - Network Load Balancer: 

Static Algorithms
1. Round robin
2. Weighted round robin
3. IP Hash

Dynamic Algorithms
1. Least Connection
2. Weighted Least Connection
3. Least Response Time

Static Algorithms: 

**Round Robin**

![[Pasted image 20231226114824.png]]

Advantages: 
- Very Easy Implementation
- Equally Distributed

Disadvantages:
- One server with high capacity and another with low, both will be treated as same. 
- Chance that low capacity server will go down because of overload of requests. 


**Weighted Round Robin**

Same as Round robin but with weights. So the high capacity server will get more request to process. 

Advantages:
- Low capacity server, will get saved from receiving the large no of requests. 
- Easy to implement as Weights are static, no dynamic computation

Disadvantages:
- If requests have different processing time, then its possible that Low capacity server get high processing requests and get overburdened. 

IP Hash:  Consistent Hashing.

Based on the hash of the ip address it redirects the request to the server. 

Advantages:
- Same client need to connect to same server. 
- Easy to implement

Disadvantages
- if the client request is coming through the PROXY [[Proxy Server]]then all the clients will have the same source IP address, this will overload one server. 
- Can not ensure equal distribution. 



Dynamic Algorithms

1. Least Active Connection

Based on the number of active connections, requests are distributed. 

Advantages:
- overburdened of server is less when server has equal capacity. 

Disadvantages:
- TCP connections can be ACTIVE but possible its not having any Traffic.
- No difference between low capacity and high capacity servers. 

2. Weighted Least connection

Same as before, but with weight. 
It calculates the ratio of active connection with the capacity. 

3. Least Response Time

Time interval between sending a request and receiving the response from the server. 

Active Connection * Least TTFB , if clash, follow round robin. 





