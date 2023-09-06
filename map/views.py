from django.shortcuts import render
import folium

def map(request):
    #Create map project
    m = folium.Map(location=[25.175, 121.449],zoom_start=16)
    folium.Marker([25.175, 121.449],tooltip='點擊',
                  popup=folium.Popup('淡江大學',max_width=10),
                  ).add_to(m)
    #獲取html的地圖顯示
    m = m._repr_html_()
    context = {
        'm':m,
    }
    return render(request, "NotSigningInBaseLayout.html",context)
# Create your views here.
