run webserver with:

`python3 app.py`

cd into `imgtest`

`curl -F "file=@img.jpg" http://127.0.0.1:8000/send`

will send a file to webserver, it will classify it and return its ML guess


TODO: change curl request to something more useable 

TODO: change response format to something more usable
