
# def CustomFunctionMiddleware(get_response):
#     # one time configuration or initialization
#     print("CustomFunction: One time configuration")

#     def middleware(request):
#         # code to be executed for each request before the view 
#         # (and later middleware) are called.
#         print("CustomFunction: Before view")

#         response = get_response(request)

#         # code to be executed for each request/response after the view is called.
#         print("CustomFunction: After view")

#         return response
#     return middleware


from django.http import HttpResponse


class CustomClassMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        # one time configuration or initialization
        print("CustomClass: One time configuration")

    def __call__(self,request):
        # code to be executed for each request before the view 
        # (and later middleware) are called.
        print("CustomClass: Before view")

        response = self.get_response(request)

        # Returning response from middle ware without calling view
        # response = HttpResponse("CustomClass: Response from middleware")

        # code to be executed for each request/response after the view is called.
        print("CustomClass: After view")

        return response
    
    # This method is called just before calling view. 
    # It can be used to modify the request or return response 
    # without calling view.
    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     print("CustomClass: process_view")
    #     # Returning response from middle ware without calling view
    #     # return HttpResponse("CustomClass: Response from process_view")
    #     return None

    # This method is called when view raises an exception. 
    # It can be used to handle the exception and 
    # return response without calling view.
    # def process_exception(self, request, exception):
    #     print("CustomClass: process_exception")
    #     print("Exception: ", exception)
    #     # Returning response from middle ware without calling view
    #     # return HttpResponse("CustomClass: Response from process_exception")    
    #     return None   
    
    # This method is called just after the view is called and 
    # before the template is rendered. 
    # It can be used to modify the response or 
    # return response without rendering template.
    def process_template_response(self, request, response):
        print("CustomClass: process_template_response: Just called after the view")
        # Returning response from middle ware without calling view
        # return HttpResponse("CustomClass: Response from process_template_response")    
        response.context_data['context_from_middleware_process_template_response'] = "This is context from middleware process_template_response"    
        return response
    
        