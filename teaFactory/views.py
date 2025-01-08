from django.http import HttpResponse



def home(request):
    return HttpResponse("Test Server")

@csrf_exempt  # Disable CSRF for simplicity during development
def add_supplier(request):
    if request.method == 'POST':
        data = json.loads(request.body)  # Parse JSON data
        name = data.get('name')
        address = data.get('address')
        contact = data.get('contact')
        email = data.get('email')

        # Add logic to process data (e.g., save to database)
        print(f"Received supplier: {name}, {address}, {contact}, {email}")

        return JsonResponse({'message': 'Supplier added successfully!'})

    return JsonResponse({'error': 'Invalid request method'}, status=400)