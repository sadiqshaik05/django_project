from django.shortcuts import render
def converter_view(request):
    result = None
    if request.method == "POST":
        ch = int(request.POST.get("choice"))
        val = float(request.POST.get("value"))
        match ch:
            case 1:
                F = val * (9/5) + 32
                result = f"{val}°C = {F:.2f}°F"
            case 2:
                K = val + 273.15
                result = f"{val}°C = {K:.2f}K"
            case 3:
                C = (val - 32) * (5/9)
                result = f"{val}°F = {C:.2f}°C"
            case 4:
                K = (val - 32) * (5/9) + 273.15
                result = f"{val}°F = {K:.2f}K"
            case 5:
                F = (val - 273.15) * (9/5) + 32
                result = f"{val}K = {F:.2f}°F"
            case 6:
                C = val - 273.15
                result = f"{val}K = {C:.2f}°C"
    return render(request, "converter.html", {"result": result})
