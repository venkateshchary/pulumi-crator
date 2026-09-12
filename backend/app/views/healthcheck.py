from django.http import JsonResponse


def health_check(request):
    # Optional: Put a basic database query here if you want a readiness check
    from django.db import connection
    connection.ensure_connection()

    return JsonResponse({"status": "healthy"}, status=200)
