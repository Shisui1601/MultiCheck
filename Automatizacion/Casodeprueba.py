import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Función para escribir de manera más lenta
def escribir_lento(campo, texto, demora=0.1):
    for letra in texto:
        campo.send_keys(letra)
        time.sleep(demora)  # Pausa entre cada letra

# Función para guardar capturas de pantalla
def guardar_captura(driver, nombre_accion):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    nombre_archivo = f"captura_{nombre_accion}_{timestamp}.png"
    driver.save_screenshot(nombre_archivo)
    print(f"Captura de pantalla guardada como {nombre_archivo}")

# Configuración del WebDriver (Edge)
driver = webdriver.Edge()  # O usa webdriver.Chrome() si prefieres Chrome
driver.get("http://localhost:5156/")

try:
    # Esperar que el campo de Username esté visible y luego enviar el texto
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Username']"))
    )
    escribir_lento(username_field, "123456789", demora=0.1)  # Escribe lentamente el nombre de usuario
    time.sleep(1)  # Asegurarse de que el campo está completamente actualizado
    guardar_captura(driver, "login_username")

    # Esperar que el campo de Password esté visible y luego enviar el texto
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Password']"))
    )
    escribir_lento(password_field, "AQAAAAIAAYagAAAAEMtZny6XwtFbd+LJOkQ1E3vdAL+rmf7o2jkpcPyk+O+S6diWwIw3LmDeqCuI4TRr0w==", demora=0.1)  # Escribe lentamente la contraseña
    time.sleep(1)  # Asegurarse de que el campo está completamente actualizado
    guardar_captura(driver, "login_password")

    # Esperar que el botón Login esté clickable y hacer clic
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]"))
    )
    login_button.click()
    time.sleep(2)  # Asegurarse de que la página de inicio se cargue correctamente
    guardar_captura(driver, "login_button")

    # Verificar si el login fue exitoso
    WebDriverWait(driver, 10).until(
        EC.url_contains("/inicio")
    )
    print("Inicio de sesión exitoso.")
    time.sleep(2)  # Asegurarse de que la página se ha cargado
    guardar_captura(driver, "login_exitoso")

    # Navegar a la página de "agente"
    agente_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='agente']"))
    )
    agente_link.click()
    time.sleep(2)  # Pausar para asegurar que la página de agente se cargue
    guardar_captura(driver, "navegar_agente")

    # Navegar a los enlaces dentro de la barra lateral
    # 1. Registrar Multa
    registrar_multa_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/agente/registrar-multa']"))
    )
    registrar_multa_link.click()
    time.sleep(2)  # Pausar para asegurar que la página de Registrar Multa se cargue
    guardar_captura(driver, "registrar_multa")

    # 2. Listado de Multas
    listado_multa_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/agente/listado-multas']"))
    )
    listado_multa_link.click()
    time.sleep(2)  # Pausar para asegurar que la página de Listado de Multas se cargue
    guardar_captura(driver, "listado_multas")

    # 3. Mapa con Mis Multas
    mapa_multas_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/agente/mapa-multas']"))
    )
    mapa_multas_link.click()
    time.sleep(1)  # Pausar para asegurar que la página de Mapa con Mis Multas se cargue

    print("Recargando la página para asegurar que el mapa se muestre...")
    driver.refresh()  # Recarga la página
    time.sleep(2)
    guardar_captura(driver, "recarga_mapa")
    

    # 4. Comisión por Mes
    comision_mes_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/agente/comision-mes']"))
    )
    comision_mes_link.click()
    time.sleep(2)  # Pausar para asegurar que la página de Comisión por Mes se cargue
    guardar_captura(driver, "comision_mes")

    # 5. Acerca de
    acerca_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/agente/acerca']"))
    )
    acerca_link.click()
    time.sleep(2)  # Pausar para asegurar que la página Acerca de se cargue
    guardar_captura(driver, "acerca_de")

    # Haciendo clic en el botón Regresar para volver al inicio...
    regresar_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='logout-btn']"))
    )
    regresar_button.click()
    time.sleep(2)  # Asegurarse de que la página se recargue correctamente

    # oficina central
    oficina_central_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/oficina-central']"))
    )
    oficina_central_link.click()
    time.sleep(2)  # Pausar para asegurar que la página de Oficina Central se cargue
    guardar_captura(driver, "oficina_central")

    # 1. Gestionar Multas
    gestionar_multas_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/oficina-central/listado-multas']"))
    )
    gestionar_multas_link.click()
    time.sleep(2)  # Pausar para asegurar que la página de Gestionar Multas se cargue
    guardar_captura(driver, "gestionar_multas")

    # 2. Reporte de Ingresos
    reporte_ingresos_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/oficina-central/reporte-ingresos']"))
    )
    reporte_ingresos_link.click()
    time.sleep(2)  # Pausar para asegurar que la página de Reporte de Ingresos se cargue
    guardar_captura(driver, "reporte_ingresos")

    # 3. Mapa de Multas
    mapa_multas_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/oficina-central/mapa-multas']"))
    )
    mapa_multas_link.click()
    time.sleep(2)  # Pausar para asegurar que la página de Mapa de Multas se cargue
    guardar_captura(driver, "mapa_multas_oficina_central")

    # 4. Gestionar Agentes
    gestionar_agentes_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/oficina-central/gestionar-agentes']"))
    )
    gestionar_agentes_link.click()
    time.sleep(2)  # Pausar para asegurar que la página de Gestionar Agentes se cargue
    guardar_captura(driver, "gestionar_agentes_oficina_central")

    # 5. Salir
    salir_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/inicio']"))
    )
    salir_link.click()
    time.sleep(2)  # Pausar para asegurar que la página de Salir se cargue
    guardar_captura(driver, "salir")

finally:
    driver.quit()
