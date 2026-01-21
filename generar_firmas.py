import os

# Lista de datos integrada
colaboradores = [
    ["Emmanuel Cervantes", "Líder Técnico", "emmanuel.cervantes@amin-tech.com", ""],
    ["Juan Pablo Torres", "Líder Técnico", "pablo.torres@amin-tech.com", ""],
    ["Ángel Flores", "Gerente de Servicios Compartidos", "angel.flores@amin-tech.com", "+52 222 708 9443"],
    ["Francisco Maldonado", "CEO", "francisco.maldonado@amin-tech.com", "+52 222 186 0398"],
    ["Ivan Muñoz", "COO", "ivan@amin-tech.com", "+52 221 165 3226"],
    ["Israel Cano", "Administrador de Base de Datos", "israel.cano@amin-tech.com", ""],
    ["Blanca Islas", "Coordinadora de Mesa de Ayuda", "blanca.islas@amin-tech.com", ""],
    ["Jaime Olivares", "Analista de Mesa de Ayuda", "jaime.olivares@amin-tech.com", ""],
    ["Jonathan Márquez", "Consultor Técnico", "jonathan.marquez@amin-tech.com", ""],
    ["Rafael Polanco", "Analista de Mesa de Ayuda", "rafael.polanco@amin-tech.com", ""],
    ["Ollivier Pérez", "Analista de Mesa de Ayuda", "ollivier.perez@amin-tech.com", ""],
    ["Joaquín Candia", "Consultor Técnico", "joaquin.candia@amin-tech.com", ""],
    ["Alan Joshep Salais", "Consultor Técnico", "joshep.salais@amin-tech.com", ""],
    ["Alejandra Cortés", "Consultor Técnico", "alejandra.cortes@amin-tech.com", ""],
    ["Andrea López", "Consultor Técnico", "andrea.lopez@amin-tech.com", ""],
    ["Aaron Morales", "Consultor Técnico", "aaron.morales@amin-tech.com", ""],
    ["Sofía Rodríguez", "Auxiliar Administrativo", "sofia.rodriguez@amin-tech.com", ""],
    ["Francisco Ruiz", "Consultor Técnico", "francisco.ruiz@amin-tech.com", ""],
    ["Kevin Sánchez", "Consultor Técnico", "kevin.sanchez@amin-tech.com", ""],
    ["Anahí Cerón Tochimani", "Gerente Comercial", "anahi.tochimani@amin-tech.com", "+52 558 078 0009"],
    ["Pahlevy Aldama", "Consultor Técnico", "pahlevy.adrian@amin-tech.com", ""],
    ["Luz Tochihuitl", "Analista de Mesa de Ayuda", "luz.tochihuitl@amin-tech.com", ""],
    ["Sofía Muñoz", "Consultor Técnico", "sofia.muñoz@amin-tech.com", ""],
    ["Arizbeth Gutiérrez", "Analista de Mesa de Ayuda", "arizbeth.gutierrez@amin-tech.com", ""],
    ["Guillermo Herrera", "Consultor Funcional", "guillermo.herrera@amin-tech.com", "+52 222 563 5431"],
    ["Luis Manuel González", "Consultor Funcional", "lgonzalez@amin-tech.com", ""],
    ["Guillermo Barrera", "Consultor Técnico", "guillermo.barrera@amin-tech.com", ""],
    ["Alejandro García", "Consultor Técnico", "alejandro.garcia@amin-tech.com", ""]
]

def generar_html(nombre, puesto, correo, telefono):
    # Lógica para el teléfono: si no hay, devolvemos cadena vacía
    fila_telefono = ""
    if telefono.strip():
        tel_link = telefono.replace(" ", "").replace("+", "")
        fila_telefono = f"""
        <tr>
            <td style="padding: 4px 10px 4px 0; vertical-align: middle">
                <img src="https://img.icons8.com/ios-filled/50/632CA6/phone.png" width="14" height="14" style="display: block" />
            </td>
            <td style="vertical-align: middle; padding: 4px 0">
                <a href="tel:{tel_link}" style="text-decoration: none; color: #444">{telefono}</a>
            </td>
        </tr>"""

    return f"""
<!doctype html>
<html lang="es">
<head><meta charset="UTF-8" /></head>
<body style="font-family: Arial, sans-serif; margin: 0; padding: 40px; background-color: #f4f4f4;">
    <table cellpadding="0" cellspacing="0" border="0" style="background-color: #ffffff; border-collapse: collapse; width: 550px; border-radius: 15px; overflow: hidden; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);">
        <tr>
            <td style="padding: 30px">
                <table cellpadding="0" cellspacing="0" border="0" style="border-collapse: collapse">
                    <tr>
                        <td style="padding-right: 25px; vertical-align: middle">
                            <img src="https://imagenbes.netlify.app/logos/ATnew.webp" width="100" height="100" alt="AT Logo" style="display: block; border-radius: 15px" />
                        </td>
                        <td style="width: 2px; vertical-align: middle; padding: 10px">
                            <div style="width: 2px; height: 210px; background-color: #632ca6"></div>
                        </td>
                        <td style="padding-left: 25px; vertical-align: middle">
                            <div style="font-size: 24px; font-weight: bold; color: #002d5c; margin-bottom: 2px;">{nombre}</div>
                            <div style="font-size: 15px; color: #632ca6; font-weight: bold; margin-bottom: 8px;">{puesto}</div>
                            <div style="padding-bottom: 7px">
                                <img src="https://imagenbes.netlify.app/logos/AMIN%20TECHNOLOGY%20LOGO%20FONDO%20TRANSPARENTE.png" height="35" width="140" alt="Amin Technology" style="display: block" />
                            </div>
                            <table cellpadding="0" cellspacing="0" border="0" style="font-size: 13px; color: #444; line-height: 1.5">
                                {fila_telefono}
                                <tr>
                                    <td style="padding: 4px 10px 4px 0; vertical-align: middle">
                                        <img src="https://img.icons8.com/ios-filled/50/632CA6/domain.png" width="14" height="14" style="display: block" />
                                    </td>
                                    <td style="vertical-align: middle; padding: 4px 0">
                                        <a href="https://www.amin-tech.com" style="text-decoration: none; color: #444">www.amin-tech.com</a>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 4px 10px 4px 0; vertical-align: middle">
                                        <img src="https://img.icons8.com/ios-filled/50/632CA6/new-post.png" width="14" height="14" style="display: block" />
                                    </td>
                                    <td style="vertical-align: middle; padding: 4px 0">
                                        <a href="mailto:{correo}" style="text-decoration: none; color: #444">{correo}</a>
                                    </td>
                                </tr>
                            </table>
                            <table cellpadding="0" cellspacing="0" border="0" style="margin-top: 15px">
                                <tr>
                                    <td style="padding-right: 12px">
                                        <a href="https://www.linkedin.com/company/amintechnology">
                                            <img src="https://img.icons8.com/ios-filled/50/002D5C/linkedin.png" width="18" height="18" />
                                        </a>
                                    </td>
                                    <td>
                                        <a href="https://www.instagram.com/amintechnologymx/">
                                            <img src="https://img.icons8.com/ios-filled/50/632CA6/instagram-new.png" width="18" height="18" />
                                        </a>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td style="padding: 20px 30px 30px 30px; border-top: 1px solid #eeeeee; text-align: left;">
                <div style="font-size: 10px; color: #a9a9a9; letter-spacing: 2px; text-transform: uppercase; font-weight: bold; font-family: Arial, sans-serif;">
                    Engineering Trust. Delivering Excellence.
                </div>
            </td>
        </tr>
    </table>
</body>
</html>
"""

# Ejecución
carpeta_salida = 'firmas_finales_amin'
if not os.path.exists(carpeta_salida):
    os.makedirs(carpeta_salida)

for c in colaboradores:
    nombre, puesto, correo, telefono = c
    html_contenido = generar_html(nombre, puesto, correo, telefono)
    
    nombre_archivo = f"{nombre.replace(' ', '_')}.html"
    ruta = os.path.join(carpeta_salida, nombre_archivo)
    
    with open(ruta, 'w', encoding='utf-8') as f:
        f.write(html_contenido)
    print(f"✅ Firma lista: {nombre}")

print(f"\n¡Éxito total! Revisa la carpeta '{carpeta_salida}'.")