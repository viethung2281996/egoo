from rest_framework.response import Response

class StandradResponse():
  def __init__(self, data, status_code):
    self.data = data
    self.status_code = status_code

  def response_message(self):
    element = { 
      200: {"message":"The request has succeeded. An entity corresponding to the requested resource is sent in the response.", "severity":"OK"},
      201: {"message":"The request has been fulfilled and resulted in a new resource being created.", "saverity":"CREATED"},
      204: {"message":"The server successfully processed the request, but is not returning any content.", "saverity":"NO CONTENT"},
      400: {"message":"The request could not be understood by the server due to malformed syntax or request.", "saverity":"INVALID REQUEST"},
      404: {"message":"The server has not found anything matching the request.Boron", "saverity":"NOT FOUND"},
      500: {"message":"The server encountered an unexpected condition which prevented it from fulfilling the request.", "saverity":"INTERNAL SERVER ERROR"},
      502: {"message":"Bad request"}
    }
    if self.status_code:
      codes = element[self.status_code]
    return codes

  def get_response(self):
    result = {
      "data":self.data,
      "message_code":self.response_message(),
      "status_code": self.status_code
    }
    return Response(result, self.status_code)
