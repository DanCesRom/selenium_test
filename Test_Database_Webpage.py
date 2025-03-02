from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Configuracion para Chrome
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--log-level=3")  # Oculta mensajes innecesarios en Chrome

# Configuracion para Edge
edge_options = EdgeOptions()
edge_options.add_argument("--no-sandbox")
edge_options.add_argument("--log-level=3")  # Oculta mensajes en Edge

# Configuracion para Firefox
firefox_options = FirefoxOptions()
firefox_options.add_argument("--no-sandbox")
firefox_options.log.level = "fatal"  # Reduce logs en Firefox

# Crear drivers para cada navegador
drivers = {
    "Chrome": webdriver.Chrome(options=chrome_options),
    "Firefox": webdriver.Firefox(options=firefox_options),
    "Edge": webdriver.Edge(options=edge_options)
}

url = "https://loupaws.pythonanywhere.com/"

# Iniciar pruebas en cada navegador
for name, driver in drivers.items():
    try:
        print(f"Iniciando prueba en {name}...")
        driver.get(url)

        wait = WebDriverWait(driver, 10)

        # Iniciar sesion
        password_box = wait.until(EC.visibility_of_element_located((By.ID, "password")))

        # Desplazar la pagina para visualizar el campo de contrasena
        driver.execute_script("arguments[0].scrollIntoView();", password_box)
        time.sleep(1)
        password_box.click()
        password_box.send_keys("Lrm-Qkixx")

        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']")))
        submit_button.click()

        print(f"Prueba en {name} ejecutada con exito.")

        # Esperar y realizar acciones en la pagina
        wait = WebDriverWait(driver, 5)

        # Seleccionar Set Name
        select_box = wait.until(EC.presence_of_element_located((By.ID, "set_name")))
        select = Select(select_box)
        time.sleep(2)  # Esperar antes de seleccionar
        select.select_by_visible_text("Prismatic Evolutions")
        time.sleep(1)

        # Seleccionar Regulation
        select_box = wait.until(EC.presence_of_element_located((By.ID, "regulation")))
        select = Select(select_box)
        select.select_by_visible_text("H")
        time.sleep(1)

        # Seleccionar Rarity
        select_box = wait.until(EC.presence_of_element_located((By.ID, "rarity")))
        select = Select(select_box)
        select.select_by_visible_text("Full Art")
        time.sleep(1)

        # Esperar que los resultados aparezcan
        results_box = wait.until(EC.visibility_of_element_located((By.ID, "cards-container")))
        driver.execute_script("arguments[0].scrollIntoView();", results_box)
        time.sleep(2)

        # Seleccionar cantidad de cartas aleatoriamente
        card_elements = driver.find_elements(By.CLASS_NAME, "card")

        if card_elements:
            num_cards_to_select = random.randint(1, min(3, len(card_elements)))  
            selected_cards = random.sample(card_elements, num_cards_to_select)

            for card in selected_cards:
                try:
                    quantity_input = card.find_element(By.CLASS_NAME, "quantity-input")
                    driver.execute_script("arguments[0].scrollIntoView();", quantity_input)
                    time.sleep(1)

                    quantity = random.randint(1, 3)  
                    quantity_input.clear()
                    quantity_input.send_keys(str(quantity))
                    print(f"Seleccionada cantidad {quantity} para carta: {card.get_attribute('data-card-id')}")

                except Exception as e:
                    print(f"No se pudo seleccionar cantidad en una carta: {e}")

        check_owned_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/owned' and contains(@class, 'button')]")))
        check_owned_button.click()
        time.sleep(4)

        # Captura de pantalla despues de la prueba
        screenshot_path = f"{name}_test_successful.png"
        driver.save_screenshot(screenshot_path)
        print(f"Captura de pantalla guardada como: {screenshot_path}")

    except Exception as e:
        print(f"Error en {name}: {e}")
    
    finally:
        if name == list(drivers.keys())[-1]:  # Solo en el ultimo navegador (Edge)
            try:
                clear_button = wait.until(EC.element_to_be_clickable((By.ID, "clear-button")))
                driver.execute_script("arguments[0].scrollIntoView();", clear_button)
                time.sleep(1)
                clear_button.click()
                print("Boton 'Clear Database' clickeado exitosamente.")
            except Exception as e:
                print(f"Error al hacer clic en 'Clear Database': {e}")

        driver.quit()
