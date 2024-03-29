## Requirements:
- This algorithm is implemented and tested using Python version 3.7.10.
- Use ```pip install -r /path/to/requirements.txt``` to install Flask and other modules necessary.

## Simple Flask Implementation:
- The BaseURL is set to ```http://127.0.0.1:5000/``` and the endpoint is set to ```test```.
- Simply use python ```requests``` to test the server.

  - Sample request with payload attached to it.
      ```
      import requests
      r = requests.post('http://127.0.0.1:5000/test', json={"key": "value"})
      print("Request with payload.\n",r.json())
      ``` 
  - Sample request without any payload.
      ```
      import requests
      r = requests.post('http://127.0.0.1:5000/test', json=None)
      print("Request without any payload.\n",r.json())
      ``` 
