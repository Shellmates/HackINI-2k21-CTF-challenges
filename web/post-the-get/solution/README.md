# Post the Get

## Write-up

To solve this problem I used curl :  

```bash
curl -X POST http://localhost:3000/send
```

Basically this line sends a POST request to the given url with the -X flag, so here we do a POST request instead of a GET request that the form actually does.  

You can also use [Postman](https://www.postman.com/) or other tools to solve this challenge.

## Flag

`shellmates{7HE_w3B_is_w31RD}`
