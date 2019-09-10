# From other.
link_data = "https://smartdata-csv-demo.s3.amazonaws.com/data/LEED.xlsx"
link_img = "https://smartdata-csv-demo.s3.amazonaws.com/data/"
link_glosario="https://smartdata-csv-demo.s3.amazonaws.com/data/"
info_header=[ {"titulo":None,"Fuente":None, "LinkDatosOriginales":None, 
               "comment":None, "linkPlot":None,"glosario":None}]

info_header[0]["titulo"]="LEED"
info_header[0]["Fuente"]="LEED"
info_header[0]["LinkDatosOriginales"]=link_data
info_header[0]["comment"]="LEED"+": obtenido desde USGBC"
info_header[0]["linkPlot"]=""
info_header[0]["glosario"]=link_glosario+"general.pdf"


Link="./Public/data/Sustentabilidad.xlsx"
import geojson

file_leed='leed.geojson'
with open(file_leed) as f:
    gj = geojson.load(f)

for element in gj['features']:
    if element['properties']["IsCertified"] == "Yes":
        element['properties']["tooltip"]={ "Nombre":element['properties']["ProjectName"], 
                                           "Tipo:":element['properties']["ProjectTypes"],
                                           "Certificación":element['properties']["CertLevel"],
                                          "Año":element['properties']["CertDate"].split(" ")[0],
                                         }

    else:
         element['properties']["tooltip"]=  { "Nombre":element['properties']["ProjectName"], 
                                              "Certificación": "En Tramite"}
            
    element['properties']["color"]='green'
print("ok")
#GEO 2

file2="ces.geojson"
with open(file2) as f:
    gj2 = geojson.load(f)
    
for element in gj2['features']:
    if element['properties']["ESTADO"] == "Certificado":
        
        element['properties']["tooltip"]={ "Nombre":element['properties']["PROYECTO"], 
                                           "PROGRAMA":element['properties']["PROGRAMA"],
                                           "CATEGORÍA":element['properties']["CATEGORiA"],
                                          "Fecha":element['properties']["AnO CERTIFICACION"]
                                         }
        
    else:
         element['properties']["tooltip"]={  "Nombre":element['properties']["PROYECTO"], 
                                           "Certificación": "En Tramite"}
    element['properties']["color"]='red'
    gj['features'].append(element)
    
gj = [info_header,gj ]



with open('leed_ces.geojson', 'w') as outfile:
	     geojson.dump(gj, outfile)