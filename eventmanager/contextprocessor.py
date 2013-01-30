def contextprocessor(request):
    print 'asdfasdf'
    if hasattr(request, 'user'):
        return { 'user' : request.user }
    return {}
