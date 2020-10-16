# Requirements Engineering: Prototype
Prototype for the requirements engineering course (2019) of the master software engineering. In this project we aim to find out what constitutes trust in sharing economy platforms like airbnb. 

## Code
### Areas
* Vue:        ./frontend
* Nginx:      ./server

#Typical workflow:
#### 1. development
1.1 ```./manage.sh run dev frontend```

Opens bash inside development frontend container, use ```npm run serve``` to start

## Background
During our previous research we have found that trust is an important factor surrounding the adoption of a shared economy platform, but it seems hard to quantify and therefore to test trust. This is partially due to the different definitions there are of trust and it is perceived as a feeling. This makes it difficult to be objective about trust.
As a result, making concrete requirements about "how much trust is required" is difficult. 
In this prototype, we propose an experiment where we attempt to find what aspects on listings influence trust, and whether trust influences the willingness of participants to use the platform.

Through literature we have found that trust can be built by using several trust elements such as a review system in combination with a (personal) photo for each listing. During this prototyping experiment we want to test to what extent these elements influence trust, as well to validate (or refute) our hypotheses. Important to acknowledge is that we can only trust the a priori perceived trustworthiness \parencite{measuringtrust} with this prototyping session (i.e., how much does the consumer trust a listing / the website from its features alone). We cannot test whether the trust was misplaced (e.g., the user posting the listing has ill will) or not because our system is not (yet) a reality.

To clarify, the goal of the platform is not that every listing should appear trustworthy; instead, our goal is to give the storage providers the tools to display accurate information to give the consumers the chance to trust the right people. This is our secondary hypothesis: we believe that people need to be informed to make decisions about trust. This hypothesis is supported by literature. During this prototype we will test whether the types of information we supply (the tools) do have an impact on this perceived trustworthiness of the listings and the platform, and therefore whether they are a requirement to increase trust of the platform and listings, or not.

