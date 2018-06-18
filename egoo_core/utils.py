def response_message(status_code):
    element = { 
        200: {"message":"The request has succeeded. An entity corresponding to the requested resource is sent in the response.", "severity":"OK"},
        201: {"message":"The request has been fulfilled and resulted in a new resource being created.", "saverity":"CREATED"},
        204: {"message":"The server successfully processed the request, but is not returning any content.", "saverity":"NO CONTENT"},
        400: {"message":"The request could not be understood by the server due to malformed syntax or request.", "saverity":"INVALID REQUEST"},
        404: {"message":"The server has not found anything matching the request.Boron", "saverity":"NOT FOUND"},
        500: {"message":"The server encountered an unexpected condition which prevented it from fulfilling the request.", "saverity":"INTERNAL SERVER ERROR"}
    }
    if status_code:
        codes = element[status_code]
    return codes