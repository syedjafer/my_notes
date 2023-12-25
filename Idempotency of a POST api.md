
Idempotent - denoting an element of a set which is unchanged in value when multiplied or otherwise operated on by itself. 

![[Pasted image 20231225110205.png]]

Now, how to avoid duplicate request (during retry) in POST api ?

Operation, 

Adding an item to the cart -> post -> create a row in db
again retry -> post -> It should not create a new row. 

(i.e) We can retry many times, but it should only modify only one row in db. 


1. By default GET, PUT, DELETE are idempotent in nature. 
2. Post is not idempotent. and we have to make it idempotent. 

Even if you are calling GET, PUT, DELETE many times -> no side effecs. 
If you are calling POST request multiple times -> Side effects. 

Sideeffect example of POST: 
	1. Payment of 10rs from A to B
	2. On retrying it multiple times it causes a problem.


2 Side effects

Sequential
Parallel


1. Sequential

Client -> POST (add item to cart) -> Server (processing)
Client faced timeout. 
But server processed it.
But client doesnt know this, so client retry (duplicate request)


2. Parallel

Client -> original POST -> server
Client -> duplicate Post -> Server. 


How to resolve these ?


Approach for idempotency handling 

1. using idempotency key -> unique key -> uuid

Aggrement with client
1. Client should generate idempotency key
2. For each different operation, new ID key should be generated.

Flow:

1. User adds item to the cart
2. Client generates the idempotency key 
3. client set this IK in the request header and this can travel to server.
4. Server process the request. IK is present in the header.
5. Server will do validation -> validate if IK is present
6. If not IK present , sends HTTP 400 -> Validation Error
7. If IK is present, server will read the IK from DB -> If key not present in DB -> put an entry in DB -> {Key: IK Key, status: created }
8. IK has a lifecycle -> initial created/acquired <-> Closed
9. If call operation is success -> add item to cart -> it will consume or claim idempotency key. -> change the status of the key to consume. -> HTTP 201 -> operation is success -> resource is also created.
10. HTTP 200 -> No resource is created.
11. If its still processing -> HTTP 409 -> conflict.


Mutex -> Acquire , Release
Semaphore -> lock, unlock
Synchronize


Parallel -> Exclusive Lock


In distributed services, 

we can use the cache -> synchronization is much faster. 
