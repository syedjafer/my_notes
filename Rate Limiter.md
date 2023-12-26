Why we need a rate limiter ?

In DDOS attacker send unwanted request to the server. Which will deplete the ram, memory etc..

To prevent DDOS, we bring in the rate limiter. 

Algorithms
1. Token Bucket
2. Leaking Bucket 
3. Fixed Window counter
4. Sliding window log
5. Sliding window counter


**Token Bucket**

Bucket has capacity. eg: 4
Refiller -> To keep add token after a partcular time. 
![[Pasted image 20231225185814.png]]

for each user, there are some tokens/times allowed to execute the request. and the refiller will increase the token bucket. 

if there is no token available then it will return 429 - Excess request per given time. 

**Leaky bucket**

Many requests are coming -> to a fixed bucket -> which has a leak (constant rate ) -> these request are processed. 

Its implemented through queue. 

![[Pasted image 20231225190316.png]]

Fixed window counter

In the fixed time, only the allowed no. of request is processed. 


Sliding window log: 

Same as fixed window counter, but it will log the value. 


Sliding window counter: 
Fixed window counter + Sliding window log. 