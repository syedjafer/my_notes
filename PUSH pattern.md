
Bidirectional Connection. 

I want the response as soon as possible. 
- Client wants real time notification from backend. 
	- A user just logged in
	- a message is just received
- Push model is good for certain cases. 

What is Push ?
- client connects to a server
- server sends data to the client
- client doest have anything to request
- protocol must be bidirectional
- used by RabbitMq


Pros
- Real time

Cons
- clients must be online
- client might not be able to handle.
- requires a bidirectional protoco; 
- polling is preffered for light weigh client. 

