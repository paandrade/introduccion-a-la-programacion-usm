fecha=raw_input('ingrese anio (dd mm aaaa): ')

if fecha[3:5]=='01':
    mes='enero'
elif fecha[3:5]=='02':
    mes='febrero'
elif fecha[3:5]=='03':
    mes='marzo'
elif fecha[3:5]=='04':
    mes='abril'
elif fecha[3:5]=='05':
    mes='mayo'
elif fecha[3:5]=='06':
    mes='junio'
elif fecha[3:5]=='07':
    mes='julio'
elif fecha[3:5]=='08':
    mes='agosto'
elif fecha[3:5]=='09':
    mes='septiembre'
elif fecha[3:5]=='10':
    mes='octubre'
elif fecha[3:5]=='11':
    mes='noviembre'
elif fecha[3:5]=='12':
    mes='diciembre'

print fecha[0:2],mes,fecha[5:10]
