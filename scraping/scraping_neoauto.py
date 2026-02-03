from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, csv

start_time = time.time()

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144 Safari/537.36"
)

service = Service(r"C:\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

datos = []
paginas_incompletas = []

TARJETAS_ESPERADAS = 22
MAX_SCROLLS = 15
MAX_REINTENTOS_PAGINA = 3

TIPOS_COMBUSTIBLE = [
    "Gasolina", "Diesel", "Diésel", "Gas GLP", "Gas GNV",
    "Gas", "Dual", "Híbrido", "Gasolina-Híbrido", "Eléctrico"
]

TIPOS_TRANSMISION = [
    "Automática", "Automática - Secuencial", "Mecánica"
]

CARD_XPATH = "//div[contains(@class,'relative box-border')][.//span[contains(@class,'text-title-x-large')]]"

# Recorrer páginas
for page in range(1, 26):
    url = f"https://neoauto.com/venta-de-autos-usados-en-lima?page={page}"
    intento = 1
    cards = []

    while intento <= MAX_REINTENTOS_PAGINA:
        driver.get(url)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.text-title-x-large"))
        )

        scroll_count = 0
        while len(driver.find_elements(By.XPATH, CARD_XPATH)) < TARJETAS_ESPERADAS and scroll_count < MAX_SCROLLS:
            driver.execute_script("window.scrollBy(0, 900);")
            time.sleep(1.5)
            scroll_count += 1

        cards = driver.find_elements(By.XPATH, CARD_XPATH)

        print(f"🔎 Página {page} | intento {intento}: {len(cards)} tarjetas (scrolls: {scroll_count})")

        if len(cards) >= TARJETAS_ESPERADAS:
            break  # página sana
        else:
            intento += 1
            time.sleep(2)  # pequeño respiro antes del refresh

    if len(cards) != TARJETAS_ESPERADAS:
        paginas_incompletas.append((page, len(cards)))

    # Extraer datos
    for card in cards:
        try:
            marca_modelo = card.find_element(By.CSS_SELECTOR, "span.text-title-x-large").text
        except:
            marca_modelo = ""

        try:
            precio = card.find_element(By.CSS_SELECTOR, "div.text-title-large.font-bold").text
        except:
            precio = ""

        try:
            km = card.find_elements(By.CSS_SELECTOR, "span.text-label-small.text-neutral-strong")[0].text
        except:
            km = "0 km"

        transmision = ""
        spans = card.find_elements(By.CSS_SELECTOR, "span[title]")
        for t in spans:
            for tipo in TIPOS_TRANSMISION:
                if tipo.lower() in t.text.lower():
                    transmision = tipo
                    break
            if transmision:
                break

        combustible = ""
        for t in spans:
            for tipo in TIPOS_COMBUSTIBLE:
                if tipo.lower() in t.text.lower():
                    combustible = tipo
                    break
            if combustible:
                break

        try:
            enlace = card.find_element(By.CSS_SELECTOR, "a[href*='auto/usado']").get_attribute("href")
        except:
            enlace = ""

        datos.append([marca_modelo, precio, km, transmision, combustible, enlace])

# Guardar CSV
with open("Datos_autos_raw.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Marca_Modelo", "Precio", "Km", "Transmision", "Combustible", "URL"])
    writer.writerows(datos)

driver.quit()

elapsed = round(time.time() - start_time, 2)
print(f"✅ Datos guardados: {len(datos)} registros en {elapsed} segundos")

if paginas_incompletas:
    print("⚠️ Páginas incompletas:")
    for p, c in paginas_incompletas:
        print(f" - Página {p}: {c} tarjetas")
