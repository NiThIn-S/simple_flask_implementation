#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing necessary Modules
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin


# In[ ]:


# Set the desired endpoint.
endpoint = "/test"


# In[ ]:


def resp_msg(code):
    """
    Function to determine the response based the input given.
    var 'code' takes Boolean values.
    """
    if bool(code):
        # Data to include in response
        data = {'message': 'This request had Payload attached to it.', 'code': "True"}
    else:
        # Data to include in response
        data = {'message': 'This request had no payload.', 'code': "False"}
    return make_response(jsonify(data), 201)


# In[ ]:


# Creating a Flask app with CORS policy for satisfying the \
# cross-origin policy that is required by the end browser used.
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors=CORS(app)

# Establishing an endpoint to test and processing the request.
@app.route(endpoint,methods=["GET","POST"])
@cross_origin()
def test_res():
    """ 
    Function is to determine if there is any payload attached to the request.
    """
    try:
        # Detecting the payload.
        assert(isinstance(request.json,dict))
        return resp_msg(code=1)
    except:
        return resp_msg(code=0)


# In[ ]:


if __name__ == '__main__':
    # Running simple server 
    #from werkzeug.serving import run_simple
    #run_simple('127.0.0.1',5000,app)
    
    # Running the server 
    app.run(host='127.0.0.1', port=5000)

