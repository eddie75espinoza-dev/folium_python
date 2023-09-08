import folium

#crear un mapa centrado en las coordenadas
mapa = folium.Map(location=[-34.619,-58.365], zoom_start=17)

#agregar marcadores en las coordenadas (-34.631803,-58.385358), (-34.631924,-58.385349)
folium.Marker(
    location=[-34.619302,-58.365347], 
    icon=folium.Icon(color="red"),
    popup="Alicia Moreau 1800",
    ).add_to(mapa)

folium.Marker(
    location=[-34.619898,-58.365212], 
    icon=folium.Icon(color="green")
    ).add_to(mapa)


#mostrar el mapa
mapa.save(r"C:\Users\usuario\Desktop\pylocal\map_folium\mapa1.html")