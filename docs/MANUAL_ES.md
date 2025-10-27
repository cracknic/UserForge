# UserForge v1.0.0 - Manual Oficial en Español

Bienvenido al manual oficial de UserForge. Este documento proporciona una guía completa de cada característica, argumento y flujo de trabajo disponible en UserForge v1.0.0. Para un resumen rápido, por favor consulta el archivo [README.md](../README.md).

## Tabla de Contenidos

1.  [Introducción](#introducción)
2.  [Conceptos Clave](#conceptos-clave)
3.  [Instalación](#instalación)
4.  [Referencia Completa de Argumentos](#referencia-completa-de-argumentos)
5.  [Guías Detalladas de Características](#guías-detalladas-de-características)
    -   [Patrones de Contraseñas Corporativas CRÍTICOS](#patrones-de-contraseñas-corporativas-críticos)
    -   [Profundidad de Generación](#profundidad-de-generación)
    -   [Localización](#localización)
    -   [Control de Leet Speak](#control-de-leet-speak)
    -   [Gestión de Prefijos/Sufijos](#gestión-de-prefijossufijos)
6.  [Flujos de Trabajo y Ejemplos Prácticos](#flujos-de-trabajo-y-ejemplos-prácticos)
7.  [Formatos de Salida](#formatos-de-salida)
8.  [Licencia](#licencia)

---

## 1. Introducción

UserForge es una herramienta de línea de comandos diseñada para pentesters y profesionales de la seguridad. Su propósito principal es generar listas de nombres de usuario y contraseñas altamente realistas y efectivas para atacar entornos de Directorio Activo (AD) y otros sistemas de autenticación.

## 2. Conceptos Clave

-   **Generación Basada en Patrones:** UserForge no utiliza caracteres aleatorios. Combina información base (nombres, empresa, año) con cientos de patrones predefinidos (ej. `nombre.apellido`, `empresaAAAA!`, `EstacionAAAA@`).
-   **Niveles de Profundidad:** La complejidad y el tamaño de la salida se controlan mediante un simple nivel de profundidad (`-d 1` a `-d 5`). El Nivel 1 es rápido y pequeño, mientras que el Nivel 5 es exhaustivo.
-   **Patrones Basados en Investigación:** Los patrones más efectivos, marcados como **CRÍTICOS**, se derivan del análisis de volcados masivos de contraseñas, apuntando a políticas corporativas comunes como la rotación de contraseñas cada 90 días.

## 3. Instalación

UserForge es un script de Python independiente sin dependencias externas. Requiere Python 3.6 o superior.

```bash
# 1. Clona el repositorio desde GitHub
git clone https://github.com/cracknic/userforge.git
cd userforge

# 2. (Opcional) Ejecuta el instalador para crear un enlace simbólico en /usr/local/bin
# Esto te permite ejecutar 'userforge' desde cualquier directorio.
chmod +x install.sh
sudo ./install.sh

# Para desinstalar el enlace simbólico:
sudo ./install.sh --uninstall

# 3. Si prefieres no instalarlo en todo el sistema, puedes ejecutarlo directamente:
python3 userforge.py [argumentos]
```

## 4. Referencia Completa de Argumentos

Esta tabla detalla los **40 argumentos** disponibles en UserForge v1.0.0.

| Argumento | Corto | Descripción | Por Defecto | Ejemplo |
|---|---|---|---|---|
| **Opciones Principales** | | | |
| `--input` | `-i` | Ruta al archivo de entrada con nombres (un nombre completo por línea). | `None` | `-i nombres.txt` |
| `--depth` | `-d` | Profundidad de generación (1-5). Mayor es más completo. | `3` | `-d 4` |
| `--passwords` | | Generar patrones de contraseñas además de nombres de usuario. | `False` | `--passwords` |
| `--emails` | | Generar direcciones de email para los dominios dados (separados por comas). | `None` | `--emails ejemplo.com` |
| `--company-name` | | Nombre de la empresa objetivo para patrones corporativos. | `None` | `--company-name "Acme Corp"` |
| `--output` | `-o` | Directorio de salida para guardar las listas de palabras generadas. | `userforge_output` | `-o /tmp/listas` |
| `--format` | | Formato de salida: `txt`, `json`, `xml`, o `all`. | `txt` | `--format all` |
| `--verbose` | `-v` | Habilitar registro detallado para ver el progreso. | `False` | `-v` |
| **Filtro por Longitud** | | | |
| `--min-user-length` | | Longitud mínima para los nombres de usuario generados. | `4` | `--min-user-length 6` |
| `--max-user-length` | | Longitud máxima para los nombres de usuario generados. | `30` | `--max-user-length 20` |
| `--min-pass-length` | | Longitud mínima para las contraseñas generadas. | `6` | `--min-pass-length 8` |
| `--max-pass-length` | | Longitud máxima para las contraseñas generadas. | `50` | `--max-pass-length 16` |
| **Localización** | | | |
| `--country` | | Código de país para patrones localizados (ej. estaciones). | `US` | `--country DE` |
| `--language` | | Idioma para meses, estaciones y palabras comunes. | `EN` | `--language ES` |
| **Leet Speak** | | | |
| `--leet` | | Nivel global de leet speak (0-3). | `0` | `--leet 2` |
| `--leet-user` | | Nivel de leet speak solo para nombres de usuario (0-3). | `0` | `--leet-user 1` |
| `--leet-password` | | Nivel de leet speak solo para contraseñas (0-3). | `0` | `--leet-password 3` |
| **Prefijos/Sufijos** | | | |
| `--user-prefix` | | Añadir un prefijo a todos los nombres de usuario generados. | `""` | `--user-prefix "test-"` |
| `--user-suffix` | | Añadir un sufijo a todos los nombres de usuario generados. | `""` | `--user-suffix ".adm"` |
| `--pass-prefix` | | Añadir un prefijo a todas las contraseñas generadas. | `""` | `--pass-prefix "!"` |
| `--pass-suffix` | | Añadir un sufijo a todas las contraseñas generadas. | `""` | `--pass-suffix "#"` |
| **Mejoras de Contraseñas** | | | |
| `--years` | | Rango de años para patrones temporales (ej. "2023-2026"). | Año Actual | `--years 2020-2025` |
| `--common-words` | | Palabras comunes adicionales para patrones de contraseñas (separadas por comas). | `None` | `--common-words "Proyecto,Secreto"` |
| `--keyboard-patterns` | | Incluir patrones basados en teclado (ej. `qwerty`, `asdfgh`). | `False` | `--keyboard-patterns` |
| `--numeric-sequences` | | Incluir secuencias numéricas comunes (ej. `123456`, `987654`). | `False` | `--numeric-sequences` |
| `--rotation-count` | | Número de contraseñas incrementales a generar (ej. `Password1!` a `PasswordN!`). | `12` | `--rotation-count 24` |
| `--quarters` | | Incluir patrones de trimestres fiscales (ej. `Q1-2024`, `FY2024`). | `False` | `--quarters` |
| `--departments` | | Incluir patrones basados en departamentos (ej. `IT2024`, `HR2024`). | `False` | `--departments` |
| `--user-depth` | `-ud` | Profundidad de generación solo para nombres de usuario (1-5). Sobrescribe `--depth` para usernames. | `None` | `-ud 2` |
| `--pass-depth` | `-pd` | Profundidad de generación solo para contraseñas (1-5). Sobrescribe `--depth` para passwords. | `None` | `-pd 5` |
| **Opciones Avanzadas** | | | |
| `--company-size` | | Tamaño de la compañía para optimización de patrones: `startup`, `smb`, `enterprise`, `medium`. | `medium` | `--company-size enterprise` |
| `--complexity` | | Nivel de complejidad de contraseñas: `low`, `medium`, `high`. | `low` | `--complexity high` |
| `--optimize` | | Activar optimización inteligente de patrones. | `False` | `--optimize` |
| `--smart` | | Modo inteligente con análisis contextual. | `False` | `--smart` |
| `--analyze` | | Generar análisis estadístico de las wordlists. | `False` | `--analyze` |
| `--target-company` | | Compañía objetivo para patrones avanzados y específicos. | `""` | `--target-company "Microsoft"` |
| `--roles` | | Lista de roles/títulos personalizados (separados por comas). | `""` | `--roles "CEO,CTO,Admin"` |
| `--symbol-positions` | | Dónde colocar símbolos en contraseñas: `start`, `end`, `both`, `random`. | `None` | `--symbol-positions end` |
| `--seasons-only` | | Usar solo patrones basados en estaciones del año. | `False` | `--seasons-only` |
| **Modo Interactivo** | | | |
| `--interactive` | `-I` | Activar modo interactivo para configuración guiada. | `False` | `-I` |


# 5. Guías Detalladas de Características


### 5.2 Profundidad Independiente

UserForge v1.0.0 permite control granular sobre la profundidad de generación mediante argumentos separados para usernames y passwords.

#### `--user-depth` / `-ud`

**Descripción:** Controla la profundidad de generación solo para nombres de usuario (1-5).

**Valor por defecto:** `None` (usa el valor de `--depth`)

**Casos de uso:**
- Enumeración exhaustiva de usuarios con pocas contraseñas
- Cuando conoces las contraseñas pero necesitas descubrir usuarios

**Ejemplo:**
```bash
# Muchos usernames, pocas passwords
userforge -i nombres.txt -ud 5 -pd 1 --passwords
```

**Resultado:** ~8,000 usernames, ~500 passwords

---

#### `--pass-depth` / `-pd`

**Descripción:** Controla la profundidad de generación solo para contraseñas (1-5).

**Valor por defecto:** `None` (usa el valor de `--depth`)

**Casos de uso:**
- Ataque con usuario conocido (ej: admin)
- Password spraying con lista reducida de usuarios

**Ejemplo:**
```bash
# Pocos usernames, muchas passwords
userforge -i admin.txt -ud 1 -pd 5 --passwords
```

**Resultado:** ~150 usernames, ~10,000 passwords

---

### 5.3 Opciones Avanzadas

#### `--company-size`

**Descripción:** Especifica el tamaño de la compañía objetivo para optimizar patrones de email y estructura organizacional.

**Valores:** `startup`, `smb`, `enterprise`, `medium`

**Valor por defecto:** `medium`

**Impacto:**
- `startup`: Patrones simples, pocos departamentos
- `smb`: Estructura básica
- `medium`: Balance entre simplicidad y complejidad
- `enterprise`: Estructura compleja, muchos departamentos

**Ejemplo:**
```bash
userforge -i empleados.txt --emails company.com --company-size enterprise
```

---

#### `--complexity`

**Descripción:** Nivel de complejidad para generación de contraseñas.

**Valores:** `low`, `medium`, `high`

**Valor por defecto:** `low`

**Impacto:**
- `low`: Patrones básicos (Password123!)
- `medium`: Combinaciones estándar (Welcome@2024)
- `high`: Patrones complejos (C0mp@nyN@me2024!)

**Ejemplo:**
```bash
userforge -i nombres.txt --passwords --complexity high -d 4
```

---

#### `--optimize`

**Descripción:** Activa optimización inteligente que reduce patrones redundantes y prioriza los más efectivos.

**Valor por defecto:** `False`

**Beneficios:**
- Reduce tamaño de wordlist en ~30%
- Mantiene patrones más efectivos
- Elimina duplicados avanzados

**Ejemplo:**
```bash
userforge -i nombres.txt --passwords -d 5 --optimize
```

---

#### `--smart`

**Descripción:** Modo inteligente con análisis contextual y adaptación de patrones.

**Valor por defecto:** `False`

**Características:**
- Analiza el contexto de la compañía
- Ajusta patrones según el sector
- Prioriza patrones basados en estadísticas

**Ejemplo:**
```bash
userforge -i nombres.txt --passwords --company-name "TechCorp" --smart
```

---

#### `--analyze`

**Descripción:** Genera análisis estadístico completo de las wordlists generadas.

**Valor por defecto:** `False`

**Información generada:**
- Distribución de longitudes
- Caracteres más comunes
- Patrones identificados
- Métricas de complejidad

**Ejemplo:**
```bash
userforge -i nombres.txt --passwords -d 3 --analyze
```

---

#### `--target-company`

**Descripción:** Especifica una compañía objetivo para generar patrones específicos y contextuales.

**Valor por defecto:** `""`

**Uso:**
- Patrones basados en productos de la compañía
- Acrónimos y abreviaturas
- Términos específicos del sector

**Ejemplo:**
```bash
userforge -i nombres.txt --passwords --target-company "Microsoft" -d 4
```

**Patrones generados:**
- `Azure2024!`
- `Office365@`
- `Windows2024`
- `MSFT2024!`

---

#### `--roles`

**Descripción:** Lista personalizada de roles/títulos para generar patrones específicos.

**Valor por defecto:** `""`

**Formato:** Separados por comas

**Ejemplo:**
```bash
userforge -i nombres.txt --passwords --roles "CEO,CTO,Admin,Manager" -d 3
```

**Patrones generados:**
- `JohnCEO2024`
- `SmithAdmin!`
- `MariaManager@2024`

---

#### `--symbol-positions`

**Descripción:** Controla dónde se colocan los símbolos en las contraseñas.

**Valores:** `start`, `end`, `both`, `random`

**Valor por defecto:** `None` (automático)

**Ejemplo:**
```bash
userforge -i nombres.txt --passwords --symbol-positions end -d 3
```

**Resultado:**
- `Password2024!` (end)
- `!Password2024` (start)
- `!Password2024!` (both)

---

#### `--seasons-only`

**Descripción:** Genera solo patrones basados en estaciones del año.

**Valor por defecto:** `False`

**Uso:** Útil para ataques dirigidos cuando se conoce que la política usa estaciones.

**Ejemplo:**
```bash
userforge -i nombres.txt --passwords --seasons-only --language ES
```

**Patrones generados:**
- `Primavera2024`
- `Verano2024!`
- `Otoño2024@`
- `Invierno2024#`

---

### 5.4 Modo Interactivo

#### `--interactive` / `-I`

**Descripción:** Activa el modo interactivo que guía al usuario a través de todas las opciones disponibles.

**Valor por defecto:** `False`

**Características:**
- Preguntas contextuales
- Valores por defecto sugeridos
- Validación de entrada
- Explicaciones de cada opción

**Ejemplo:**
```bash
userforge -i nombres.txt -I
```

**Flujo interactivo:**
1. ¿Generar contraseñas? (y/n)
2. ¿Profundidad unificada o separada?
3. ¿Nombre de la compañía?
4. ¿Usar leet speak?
5. ¿Añadir prefijos/sufijos?
6. ... (y más)

**Beneficio:** Ideal para usuarios nuevos o cuando no recuerdas todos los argumentos.



Esta sección proporciona una guía exhaustiva de cada argumento disponible en UserForge v1.0.0, organizada por categorías funcionales.

---

## 5.1 Opciones Principales

### 5.1.1 `--input` / `-i` (REQUERIDO)

**Descripción:** Especifica la ruta al archivo de entrada que contiene los nombres completos.

**Formato del archivo:**
- Un nombre completo por línea
- Formato: `Nombre Apellido` o `Nombre Apellido1 Apellido2`
- Soporta caracteres UTF-8 (acentos, ñ, etc.)
- Líneas vacías son ignoradas

**Ejemplo de archivo (`nombres.txt`):**
```
John Michael Smith
María García López
Emilio Dahl Herce
Jean-Pierre Dubois
李明 (Li Ming)
```

**Uso:**
```bash
userforge -i nombres.txt
userforge --input /ruta/completa/nombres.txt
```

**Validación:**
- Nombres con caracteres especiales inválidos son omitidos con advertencia
- Nombres con menos de 2 palabras son aceptados pero generan menos patrones
- Se registra el número de nombres válidos cargados

**Consejos:**
- Usa OSINT (LinkedIn, sitio web corporativo) para recopilar nombres
- Incluye variaciones de nombres (con/sin segundo nombre)
- Para organizaciones grandes, enfócate en departamentos específicos

---

### 5.1.2 `--depth` / `-d`

**Descripción:** Controla la profundidad de generación para nombres de usuario y contraseñas de forma unificada.

**Valores:** 1-5 (Por defecto: 3)

**Desglose por nivel:**

#### Nivel 1 - Básico (~150 patrones por nombre)
**Patrones generados:**
- Nombres simples: `john`, `smith`
- Iniciales: `js`, `jms`
- Combinaciones básicas: `johnsmith`, `smithjohn`
- Números simples: `john1`, `smith2`

**Uso recomendado:** Enumeración rápida inicial

**Ejemplo:**
```bash
userforge -i nombres.txt -d 1
```

**Salida esperada para "John Smith":**
```
john
smith
jsmith
smithj
js
john1
smith1
```

---

#### Nivel 2 - Estándar (~500 patrones por nombre)
**Patrones adicionales:**
- Separadores: `john.smith`, `john-smith`, `john_smith`
- Inversiones: `smithjohn`, `smith.john`
- Números al final: `jsmith01`, `jsmith99`
- Iniciales extendidas: `j.smith`, `john.s`

**Uso recomendado:** Ataques estándar de AD

**Ejemplo:**
```bash
userforge -i nombres.txt -d 2 --passwords
```

**Salida esperada:**
```
# Usernames
john.smith
j.smith
smith.john
jsmith01
jsmith2024

# Passwords
Welcome2024
Password123
JohnSmith2024
```

---

#### Nivel 3 - Avanzado (~1,000 patrones por nombre) **[POR DEFECTO]**
**Patrones adicionales:**
- Años: `jsmith2024`, `john2025`
- Estaciones: `JohnWinter2024`, `SmithSummer`
- Meses: `JohnJanuary`, `SmithDecember2024`
- Patrones corporativos básicos: `JohnCompany`, `SmithCorp2024`

**Uso recomendado:** Ataques corporativos equilibrados

**Ejemplo:**
```bash
userforge -i nombres.txt -d 3 --passwords --company-name "TechCorp"
```

**Salida esperada:**
```
# Usernames
jsmith2024
john.smith2025
j.smith.tech

# Passwords
Welcome2024!
TechCorp2024
JohnSmithWinter2024
TechCorpJanuary2025
```

---

#### Nivel 4 - Extensivo (~2,000 patrones por nombre)
**Patrones adicionales:**
- Leet speak básico: `j0hn`, `sm1th`
- Combinaciones complejas: `JohnSmithTechCorp2024`
- Variaciones de mayúsculas: `JOHN`, `JoHn`, `jOhN`
- Rotaciones: `Welcome1!`, `Welcome2!`, ..., `Welcome12!`

**Uso recomendado:** Ataques exhaustivos en objetivos específicos

**Ejemplo:**
```bash
userforge -i nombres.txt -d 4 --passwords --company-name "MegaCorp" --quarters
```

**Salida esperada:**
```
# Passwords
Welcome1!
Welcome2!
MegaCorpQ1-2024
JohnSmith@MegaCorp
M3g4Corp2024!
Q1-2024!
FY2024MegaCorp
```

---

#### Nivel 5 - Máximo (~8,000+ patrones por nombre)
**Patrones adicionales:**
- Todas las combinaciones posibles
- Leet speak avanzado: `j0hn$m1th`
- Patrones de teclado: `qwerty`, `asdfgh`
- Secuencias numéricas: `123456`, `987654`
- Todas las variaciones de departamentos, trimestres, roles

**Uso recomendado:** Ataques de último recurso o auditorías exhaustivas

**⚠️ ADVERTENCIA:** Puede generar archivos grandes

**Ejemplo:**
```bash
userforge -i nombres.txt -d 5 --passwords --company-name "GlobalCorp" --departments --quarters --rotation-count 24
```

**Salida esperada:** Miles de patrones por nombre

---

### 5.1.3 `--user-depth` / `-ud` y `--pass-depth` / `-pd`

**Descripción:** Control independiente de profundidad para usernames y passwords.

**Ventajas:**
- Mayor flexibilidad en ataques dirigidos
- Optimización de recursos (generar muchos users, pocas passwords o viceversa)
- Útil cuando conoces el username pero no la password

**Casos de uso:**

#### Caso 1: Usuario conocido, password desconocida
```bash
userforge -i admin.txt -ud 1 -pd 5 --passwords --company-name "TechCorp"
```
**Resultado:**
- Pocos usernames (solo variaciones básicas de "admin")
- Miles de passwords (exhaustivo)

---

#### Caso 2: Enumeración de usuarios
```bash
userforge -i nombres.txt -ud 5 --format all
```
**Resultado:**
- Miles de usernames (máxima cobertura)
- Sin passwords (no especificado `--passwords`)

---

#### Caso 3: Ataque balanceado con prioridad en passwords
```bash
userforge -i nombres.txt -ud 3 -pd 5 --passwords
```
**Resultado:**
- ~1,000 usernames por nombre (avanzado)
- ~8,000 passwords por nombre (máximo)

---

### 5.1.4 `--passwords`

**Descripción:** Activa la generación de patrones de contraseñas.

**Sin este flag:** Solo se generan usernames

**Patrones de contraseñas generados:**
- Basados en nombres: `JohnSmith2024`, `SmithJohn!`
- Basados en compañía: `TechCorp2024!`, `CompanyName@2025`
- Temporales: `Welcome2024`, `Password2025!`
- Departamentos: `IT2024!`, `Sales2025@`
- Trimestres: `Q1-2024`, `FY2025!`
- Rotaciones: `Welcome1!` a `Welcome12!`

**Ejemplo básico:**
```bash
userforge -i nombres.txt --passwords
```

**Ejemplo avanzado:**
```bash
userforge -i nombres.txt --passwords \
  --company-name "MegaCorp" \
  --quarters \
  --departments \
  --rotation-count 24 \
  --years 2020-2025
```

---

### 5.1.5 `--emails`

**Descripción:** Genera direcciones de email para los dominios especificados.

**Formato:** Dominios separados por comas

**Patrones generados:**
- `john.smith@company.com`
- `jsmith@company.com`
- `j.smith@company.com`
- `smithj@company.com`
- `john@company.com`

**Ejemplo con un dominio:**
```bash
userforge -i nombres.txt --emails company.com
```

**Ejemplo con múltiples dominios:**
```bash
userforge -i nombres.txt --emails company.com,corp.local,company.net
```

**Salida:**
```
john.smith@company.com
john.smith@corp.local
john.smith@company.net
jsmith@company.com
jsmith@corp.local
jsmith@company.net
```

**Uso práctico:**
- Ataques de phishing
- Enumeración de Office 365
- Password spraying contra servicios web

---

### 5.1.6 `--company-name`

**Descripción:** Nombre de la compañía objetivo para generar patrones corporativos.

**Impacto:** Genera cientos de patrones adicionales combinando el nombre de la compañía con:
- Nombres de usuarios
- Años
- Estaciones
- Departamentos
- Trimestres

**Ejemplo:**
```bash
userforge -i nombres.txt --passwords --company-name "TechCorp"
```

**Patrones generados:**
```
# Usernames
john.techcorp
jsmith@techcorp
techcorp.john

# Passwords
TechCorp2024!
JohnTechCorp2024
TechCorpWelcome!
TechCorpQ1-2024
TechCorpIT2024
Welcome@TechCorp
```

**Consejos:**
- Usa el nombre completo: "TechCorp Inc"
- Prueba variaciones: "TechCorp", "Tech Corp", "TC"
- Incluye acrónimos comunes de la compañía

---

### 5.1.7 `--output` / `-o`

**Descripción:** Directorio de salida para guardar los archivos generados.

**Por defecto:** `UserForge_Output/UserForge_Output_YYYYMMDD_HHMMSS`

**Estructura de salida:**
```
output_directory/
├── combined/
│   ├── all_usernames.txt
│   ├── all_passwords.txt
│   ├── all_usernames.json  (si --format all)
│   ├── all_passwords.json
│   ├── all_usernames.xml
│   └── all_passwords.xml
├── by_person/
│   ├── john_smith/
│   │   ├── usernames.txt
│   │   ├── passwords.txt
│   │   ├── usernames.json  (si --format all)
│   │   └── passwords.json
│   └── maria_garcia/
│       └── ...
└── userforge.log
```

**Ejemplo:**
```bash
userforge -i nombres.txt --passwords -o /tmp/ataque_techcorp
```

---

### 5.1.8 `--format`

**Descripción:** Formato de los archivos de salida.

**Opciones:** `txt`, `json`, `xml`, `all`

**Por defecto:** `txt`

#### Formato TXT
```
john.smith
jsmith
j.smith
```

#### Formato JSON
```json
{
  "usernames": [
    "john.smith",
    "jsmith",
    "j.smith"
  ],
  "metadata": {
    "count": 3,
    "generated_at": "2024-10-27T10:30:00",
    "source": "John Smith"
  }
}
```

#### Formato XML
```xml
<?xml version="1.0" encoding="UTF-8"?>
<wordlist>
  <usernames>
    <username>john.smith</username>
    <username>jsmith</username>
    <username>j.smith</username>
  </usernames>
  <metadata>
    <count>3</count>
    <generated_at>2024-10-27T10:30:00</generated_at>
  </metadata>
</wordlist>
```

**Ejemplo:**
```bash
userforge -i nombres.txt --passwords --format all
```

---

### 5.1.9 `--verbose` / `-v`

**Descripción:** Activa el logging detallado.

**Información mostrada:**
- Archivo de entrada y número de nombres cargados
- Configuración del generador (depth, leet, etc.)
- Progreso de procesamiento con barra de progreso
- Estadísticas finales (usernames/passwords generados)
- Tiempo de ejecución
- Ubicación de archivos de salida

**Ejemplo sin verbose:**
```bash
$ userforge -i nombres.txt --passwords
✓ Generated 504 usernames
✓ Generated 2,124 passwords
```

**Ejemplo con verbose:**
```bash
$ userforge -i nombres.txt --passwords -v

[INFO] Input file: nombres.txt
[INFO] Reading input file...
[INFO] Loaded 3 valid name(s)
[INFO] Output directory: /home/user/UserForge_Output/UserForge_Output_20241027_103000
[INFO] Initializing pattern generator...
[INFO]   ├─ Depth Level: 3
[INFO]   ├─ Leet Speak: Level 0
[INFO]   ├─ Company Size: medium
[INFO]   ├─ Language: EN
[INFO]   └─ Country: US
[INFO] Processing 3 name(s)...
Processing names: |████████████████████████████████████████| 100.0% (3/3)
[INFO]   [1/3] Processing: John Smith
[INFO]   [2/3] Processing: Maria Garcia
[INFO]   [3/3] Processing: Emilio Dahl
[SUCCESS] ✓ Generated 504 unique usernames
[SUCCESS] ✓ Generated 2,124 unique passwords
[INFO] Writing output files...
[SUCCESS] ✓ Output written to: /home/user/UserForge_Output/UserForge_Output_20241027_103000

=== SUMMARY ===
📊 Statistics:
  • Total Names Processed: 3
  • Unique Usernames: 504
  • Unique Passwords: 2,124
  • Output Directory: /home/user/UserForge_Output/UserForge_Output_20241027_103000
  • Execution Time: 2.34 seconds
```

---

## 5.2 Filtros de Longitud

### 5.2.1 `--min-user-length`

**Descripción:** Longitud mínima para usernames generados.

**Por defecto:** 3

**Uso:** Filtrar usernames demasiado cortos que no cumplen políticas corporativas.

**Ejemplo:**
```bash
userforge -i nombres.txt --min-user-length 6
```

**Resultado:**
- ✅ `jsmith` (6 caracteres)
- ✅ `john.smith` (10 caracteres)
- ❌ `js` (2 caracteres - filtrado)
- ❌ `john` (4 caracteres - filtrado)

---

### 5.2.2 `--max-user-length`

**Descripción:** Longitud máxima para usernames generados.

**Por defecto:** 50

**Uso:** Evitar usernames excesivamente largos que pueden ser rechazados por sistemas.

**Ejemplo:**
```bash
userforge -i nombres.txt --max-user-length 20
```

**Resultado:**
- ✅ `jsmith` (6 caracteres)
- ✅ `john.smith.techcorp` (19 caracteres)
- ❌ `john.smith.techcorp.2024` (24 caracteres - filtrado)

---

### 5.2.3 `--min-pass-length`

**Descripción:** Longitud mínima para passwords generadas.

**Por defecto:** 8

**Uso:** Cumplir con políticas de contraseñas corporativas.

**Ejemplo:**
```bash
userforge -i nombres.txt --passwords --min-pass-length 12
```

**Resultado:**
- ✅ `Welcome2024!` (12 caracteres)
- ✅ `TechCorp@2024` (13 caracteres)
- ❌ `Pass123!` (8 caracteres - filtrado)
- ❌ `Welcome!` (8 caracteres - filtrado)

---

### 5.2.4 `--max-pass-length`

**Descripción:** Longitud máxima para passwords generadas.

**Por defecto:** 50

**Uso:** Evitar passwords excesivamente largas.

**Ejemplo:**
```bash
userforge -i nombres.txt --passwords --max-pass-length 16
```

**Resultado:**
- ✅ `Welcome2024!` (12 caracteres)
- ❌ `JohnSmithTechCorp2024!` (23 caracteres - filtrado)

---

## 5.3 Localización

### 5.3.1 `--country`

**Descripción:** Código de país para patrones localizados.

**Por defecto:** `US`

**Países soportados:** US, UK, CA, AU, DE, FR, ES, IT, PT, MX

**Impacto:**
- Formatos de fecha (DD/MM/YYYY vs MM/DD/YYYY)
- Fiestas nacionales
- Patrones culturales

**Ejemplo:**
```bash
userforge -i nombres.txt --passwords --country ES --language ES
```

**Patrones generados (España):**
```
# Estaciones en español
JohnVerano2024
SmithInvierno2025

# Fiestas españolas
12Octubre2024  (Día de la Hispanidad)
6Enero2025     (Día de Reyes)

# Formato de fecha español
25122024       (DD/MM/YYYY)
```

---

### 5.3.2 `--language`

**Descripción:** Idioma para meses, estaciones y palabras comunes.

**Por defecto:** `EN`

**Idiomas soportados:** EN, ES, FR, DE, IT, PT

**Impacto:**
- Nombres de meses: `January` vs `Enero` vs `Janvier`
- Estaciones: `Summer` vs `Verano` vs `Été`
- Palabras comunes: `Password` vs `Contraseña` vs `Mot de passe`

**Ejemplo con español:**
```bash
userforge -i nombres.txt --passwords --language ES
```

**Patrones generados:**
```
# Meses en español
JohnEnero2024
SmithFebrero2025
MariaMarzo2024

# Estaciones
JohnVerano2024
SmithOtoño2025

# Palabras comunes
Contraseña2024!
Bienvenido2025@
```

**Ejemplo con francés:**
```bash
userforge -i nombres.txt --passwords --language FR --country FR
```

**Patrones generados:**
```
# Meses en francés
JohnJanvier2024
SmithFévrier2025

# Estaciones
JohnÉté2024
SmithHiver2025

# Palabras comunes
MotDePasse2024!
Bienvenue2025@
```

---

## 5.4 Leet Speak

### 5.4.1 `--leet`

**Descripción:** Nivel global de leet speak aplicado a usernames y passwords.

**Valores:** 0-3 (Por defecto: 0)

**Niveles:**

#### Nivel 0 - Desactivado
Sin transformación.

#### Nivel 1 - Básico
**Sustituciones:**
- `e → 3`
- `a → 4`
- `o → 0`
- `i → 1`

**Ejemplo:**
```bash
userforge -i nombres.txt --passwords --leet 1
```

**Salida:**
```
# Original
john.smith
Welcome2024

# Leet Nivel 1
j0hn.sm1th
W3lc0m32024
```

---

#### Nivel 2 - Medio
**Sustituciones adicionales:**
- `s → 5`
- `t → 7`
- `l → 1`

**Ejemplo:**
```bash
userforge -i nombres.txt --passwords --leet 2
```

**Salida:**
```
# Original
john.smith
TechCorp2024

# Leet Nivel 2
j0hn.5m17h
73chC0rp2024
```

---

#### Nivel 3 - Avanzado
**Sustituciones adicionales:**
- `s → $`
- `a → @`
- `i → !`

**Ejemplo:**
```bash
userforge -i nombres.txt --passwords --leet 3
```

**Salida:**
```
# Original
john.smith
Password2024

# Leet Nivel 3
j0hn.$m!7h
P@$$w0rd2024
```

---

### 5.4.2 `--leet-user`

**Descripción:** Nivel de leet speak aplicado SOLO a usernames.

**Uso:** Cuando solo quieres transformar usernames.

**Ejemplo:**
```bash
userforge -i nombres.txt --passwords --leet-user 2
```

**Salida:**
```
# Usernames con leet
j0hn.5m17h
m@r14.g4rc14

# Passwords sin leet
Welcome2024
TechCorp2024
```

---

### 5.4.3 `--leet-password`

**Descripción:** Nivel de leet speak aplicado SOLO a passwords.

**Uso:** Cuando solo quieres transformar passwords (más común).

**Ejemplo:**
```bash
userforge -i nombres.txt --passwords --leet-password 3
```

**Salida:**
```
# Usernames sin leet
john.smith
maria.garcia

# Passwords con leet
W3lc0m3@2024
T3chC0rp$2024
P@$$w0rd!
```

---

## 5.5 Prefijos y Sufijos (Modo Dual)

### 5.5.1 `--user-prefix`

**Descripción:** Añade un prefijo a todos los usernames generados.

**Modo Dual:** Genera AMBAS versiones (con y sin prefijo).

**Ejemplo:**
```bash
userforge -i nombres.txt --user-prefix "corp_"
```

**Salida:**
```
# Versión original
john.smith
jsmith
j.smith

# Versión con prefijo
corp_john.smith
corp_jsmith
corp_j.smith
```

**Uso práctico:**
- Convenciones de naming corporativas
- Prefijos de departamento: `it_`, `admin_`, `dev_`
- Prefijos de ubicación: `us_`, `eu_`, `asia_`

---

### 5.5.2 `--user-suffix`

**Descripción:** Añade un sufijo a todos los usernames generados.

**Modo Dual:** Genera AMBAS versiones (con y sin sufijo).

**Ejemplo:**
```bash
userforge -i nombres.txt --user-suffix ".adm"
```

**Salida:**
```
# Versión original
john.smith
jsmith

# Versión con sufijo
john.smith.adm
jsmith.adm
```

**Uso práctico:**
- Cuentas administrativas: `.adm`, `.admin`, `_admin`
- Cuentas de servicio: `.svc`, `.service`
- Cuentas de prueba: `.test`, `.dev`

---

### 5.5.3 `--pass-prefix`

**Descripción:** Añade un prefijo a todas las passwords generadas.

**Modo Dual:** Genera AMBAS versiones (con y sin prefijo).

**Ejemplo:**
```bash
userforge -i nombres.txt --passwords --pass-prefix "P@"
```

**Salida:**
```
# Versión original
Welcome2024
TechCorp2024

# Versión con prefijo
P@Welcome2024
P@TechCorp2024
```

**Uso práctico:**
- Cumplir políticas que requieren símbolo al inicio
- Patrones corporativos específicos

---

### 5.5.4 `--pass-suffix`

**Descripción:** Añade un sufijo a todas las passwords generadas.

**Modo Dual:** Genera AMBAS versiones (con y sin sufijo).

**Ejemplo:**
```bash
userforge -i nombres.txt --passwords --pass-suffix "!"
```

**Salida:**
```
# Versión original
Welcome2024
TechCorp2024

# Versión con sufijo
Welcome2024!
TechCorp2024!
```

**Uso práctico:**
- Cumplir políticas que requieren símbolo al final
- Patrón muy común en contraseñas corporativas

---

## 5.6 Mejoras de Contraseñas

### 5.6.1 `--years`

**Descripción:** Rango de años para patrones temporales.

**Formato:** `YYYY-YYYY` (rango) o `YYYY,YYYY,YYYY` (lista)

**Por defecto:** Año actual

**Ejemplo con rango:**
```bash
userforge -i nombres.txt --passwords --years 2020-2025
```

**Patrones generados:**
```
Welcome2020
Welcome2021
Welcome2022
Welcome2023
Welcome2024
Welcome2025
TechCorp2020!
TechCorp2021!
...
```

**Ejemplo con lista:**
```bash
userforge -i nombres.txt --passwords --years 2020,2023,2024,2025
```

**Patrones generados:**
```
Welcome2020
Welcome2023
Welcome2024
Welcome2025
```

**Uso práctico:**
- Rotación de contraseñas anuales
- Auditorías de contraseñas antiguas
- Ataques dirigidos a años específicos

---

### 5.6.2 `--common-words`

**Descripción:** Palabras comunes adicionales para patrones de contraseñas.

**Formato:** Palabras separadas por comas

**Ejemplo:**
```bash
userforge -i nombres.txt --passwords --common-words "Proyecto,Secreto,Confidencial"
```

**Patrones generados:**
```
Proyecto2024!
Secreto2025@
Confidencial2024
JohnProyecto2024
SmithSecreto!
ProyectoTechCorp2024
```

**Uso práctico:**
- Palabras específicas de la industria
- Nombres de proyectos internos
- Jerga corporativa

---

### 5.6.3 `--keyboard-patterns`

**Descripción:** Incluye patrones basados en disposición de teclado.

**Patrones generados:**
```
qwerty
asdfgh
zxcvbn
qwerty123
asdfgh2024
qwertyTechCorp
```

**Ejemplo:**
```bash
userforge -i nombres.txt --passwords --keyboard-patterns
```

**Uso práctico:**
- Contraseñas débiles comunes
- Usuarios que usan patrones de teclado por comodidad

---

### 5.6.4 `--numeric-sequences`

**Descripción:** Incluye secuencias numéricas comunes.

**Patrones generados:**
```
123456
654321
111111
123456789
987654321
12345678
```

**Ejemplo:**
```bash
userforge -i nombres.txt --passwords --numeric-sequences
```

**Combinaciones con otros patrones:**
```
Welcome123456
TechCorp654321
Password123456789
```

---

### 5.6.5 `--rotation-count`

**Descripción:** Número de contraseñas incrementales a generar.

**Por defecto:** 12 (para rotación trimestral de 90 días)

**Patrón:** El patrón MÁS EXITOSO en entornos corporativos.

**Explicación:** Cuando los empleados son forzados a cambiar su contraseña cada 90 días, la mayoría simplemente incrementa un número:
- Mes 1: `Welcome1!`
- Mes 4: `Welcome2!`
- Mes 7: `Welcome3!`
- etc.

**Ejemplo con 12 rotaciones (3 años):**
```bash
userforge -i nombres.txt --passwords --rotation-count 12
```

**Patrones generados:**
```
Welcome1!
Welcome2!
Welcome3!
...
Welcome12!

Password1@
Password2@
...
Password12@

TechCorp1!
TechCorp2!
...
TechCorp12!
```

**Ejemplo con 24 rotaciones (6 años):**
```bash
userforge -i nombres.txt --passwords --rotation-count 24
```

**Uso práctico:**
- Ataques contra políticas de rotación de 90 días
- Auditorías de contraseñas antiguas
- Detección de patrones incrementales

---

### 5.6.6 `--quarters`

**Descripción:** Incluye patrones de trimestres fiscales.

**Patrones generados:**
```
Q1-2024
Q2-2024
Q3-2024
Q4-2024
FY2024
FY2025
Fiscal2024
Q1-2024!
Q1FY2024
```

**Ejemplo:**
```bash
userforge -i nombres.txt --passwords --quarters --years 2023-2025
```

**Patrones generados:**
```
Q1-2023
Q2-2023
Q3-2023
Q4-2023
Q1-2024
Q2-2024
Q3-2024
Q4-2024
Q1-2025
Q2-2025
FY2023
FY2024
FY2025
TechCorpQ1-2024
Q1-2024TechCorp!
```

**Uso práctico:**
- Empresas financieras
- Empresas contables
- Empresas que cotizan en bolsa
- Departamentos de finanzas

---

### 5.6.7 `--departments`

**Descripción:** Incluye patrones basados en departamentos corporativos.

**Departamentos incluidos:**
- IT, HR, Sales, Marketing, Finance, Legal
- Accounting, Admin, Support, Engineering, Operations
- Management, Executive, Security, Audit

**Patrones generados:**
```
IT2024!
HR2025@
Sales2024
Marketing2025!
Finance2024@
ITDept2024
HRTeam2025
SalesTeam!
ITTechCorp2024
HRTechCorp2025
```

**Ejemplo:**
```bash
userforge -i nombres.txt --passwords --departments --company-name "TechCorp"
```

**Patrones generados:**
```
IT2024!
ITTechCorp2024
TechCorpIT2024
ITDept2024!
HR2024@
HRTechCorp2025
TechCorpHR2025
HRTeam2025!
```

**Uso práctico:**
- Contraseñas compartidas de departamento
- Cuentas de servicio departamentales
- Buzones compartidos

---

## 5.7 Modo Interactivo

### `--interactive` / `-I`

**Descripción:** Activa el modo interactivo guiado.

**Características:**
- Preguntas paso a paso
- Valores por defecto sugeridos
- Validación de entrada
- Explicaciones contextuales

**Ejemplo de sesión:**
```bash
$ userforge -i nombres.txt -I

=== UserForge Interactive Mode ===

[1/15] Generate passwords? (y/n) [n]: y
[2/15] Generate emails? (y/n) [n]: y
[3/15] Email domains (comma-separated): techcorp.com,corp.local

[4/15] Use separate depth for users/passwords? (y/n) [n]: y
[5/15] User depth (1-5) [3]: 2
[6/15] Password depth (1-5) [3]: 5

[7/15] Company name []: TechCorp
[8/15] Country code (US/UK/CA/AU/DE/FR/ES/IT/PT/MX) [US]: US
[9/15] Language (EN/ES/FR/DE/IT/PT) [EN]: EN

[10/15] Enable leet speak? (y/n) [n]: y
[11/15] Leet level for users (0-3) [0]: 0
[12/15] Leet level for passwords (0-3) [0]: 2

[13/15] Enable quarters patterns? (y/n) [n]: y
[14/15] Enable departments patterns? (y/n) [n]: y
[15/15] Output format (txt/json/xml/all) [txt]: all

=== Configuration Summary ===
✓ Input: nombres.txt
✓ Passwords: Yes
✓ Emails: techcorp.com, corp.local
✓ User Depth: 2
✓ Pass Depth: 5
✓ Company: TechCorp
✓ Quarters: Yes
✓ Departments: Yes
✓ Leet (passwords): Level 2
✓ Format: all

Proceed? (y/n) [y]: y

[INFO] Processing...
```

---

## 5.8 Consejos

### Para Enumeración de Usuarios
1. Comienza con `-d 2` para rapidez
2. Usa `--emails` si conoces los dominios
3. Incrementa a `-d 3` o `-d 4` si no tienes éxito
4. Usa `--format all` para integración con otras herramientas

### Para Password Spraying
1. Usa `-d 3` como punto de partida
2. **SIEMPRE** incluye `--quarters` y `--departments`
3. Usa `--rotation-count 12` como mínimo
4. Especifica `--company-name` si la conoces
5. Ajusta `--min-pass-length` según la política detectada
6. Usa `--leet-password 1` o `2` para mayor cobertura

### Para Ataques Dirigidos
1. Usa `-ud 2 -pd 5` si conoces el username
2. Investiga la compañía (OSINT) para `--common-words`
3. Usa `--years` con rango amplio (ej: 2018-2025)
4. Combina `--quarters`, `--departments` y `--rotation-count 24`

### Para Auditorías
1. Usa `-d 5` para máxima cobertura
2. Incluye TODOS los flags de mejoras
3. Usa `--format all` para análisis posterior
4. Documenta el tiempo de generación

### Optimización de Recursos
1. Usa filtros de longitud para reducir tamaño
2. Comienza con depth bajo y aumenta gradualmente
3. Usa `-ud` y `-pd` independientes para control fino
4. Monitorea el tamaño de salida con `-v`

---


## 6. Flujos de Trabajo y Ejemplos Prácticos

-   **Enumeración Inicial:** Comienza con una profundidad baja para encontrar rápidamente nombres de usuario comunes.
    -   `userforge -i nombres.txt -d 2 -o usuarios_iniciales`

-   **Password Spray Estándar:** Un ataque equilibrado para un objetivo corporativo típico.
    -   `userforge -i nombres.txt -d 3 --passwords --company-name "MegaCorp" --quarters -o listas_spray`

-   **Objetivo de Alta Seguridad:** Para entornos con políticas de contraseñas estrictas.
    -   `userforge -i nombres.txt -d 4 --passwords --min-pass-length 12 --leet-password 2 -o listas_seguras`

-   **Ataque Total (Máxima Cobertura):** Cuando necesitas intentarlo todo.
    -   `userforge -i nombres.txt -d 5 --passwords --format all --company-name "GlobalCorp" --departments --quarters --rotation-count 24 --leet-password 1 -o ataque_total`


### Ejemplo 1: Enumeración Básica
```bash
userforge -i nombres.txt -d 2 -o usuarios_basicos
```

### Ejemplo 2: Password Spray Estándar
```bash
userforge -i nombres.txt -d 3 --passwords \
  --company-name "MegaCorp" \
  --quarters \
  --rotation-count 12 \
  -o spray_megacorp
```

### Ejemplo 3: Ataque Dirigido con Leet Speak
```bash
userforge -i nombres.txt -d 4 --passwords \
  --company-name "TechCorp" \
  --leet-password 2 \
  --min-pass-length 12 \
  --years 2022-2025 \
  -o ataque_techcorp
```

### Ejemplo 4: Ataque Exhaustivo
```bash
userforge -i nombres.txt -ud 5 -pd 5 --passwords \
  --company-name "GlobalCorp" \
  --departments \
  --quarters \
  --rotation-count 24 \
  --keyboard-patterns \
  --numeric-sequences \
  --common-words "Project,Secret,Internal" \
  --years 2020-2025 \
  --format all \
  -v \
  -o ataque_total
```

### Ejemplo 5: Localización Española
```bash
userforge -i nombres.txt -d 3 --passwords \
  --company-name "Empresa SA" \
  --language ES \
  --country ES \
  --quarters \
  --departments \
  -o ataque_espana
```

### Ejemplo 6: Emails + Usernames
```bash
userforge -i nombres.txt -d 3 \
  --emails company.com,corp.local,company.net \
  --format all \
  -o enumeracion_emails
```

### Ejemplo 7: Prefijos/Sufijos
```bash
userforge -i nombres.txt -d 3 --passwords \
  --user-prefix "corp_" \
  --user-suffix ".adm" \
  --pass-prefix "P@" \
  --pass-suffix "!" \
  --company-name "TechCorp" \
  -o modo_dual
```



### Ejemplo 8: Ataque a Infraestructura Financiera
**Escenario:** Pentesting en un banco o entidad financiera con políticas estrictas de contraseñas.

**Características:**
- Uso intensivo de patrones de trimestres fiscales
- Complejidad alta
- Años recientes (políticas de rotación trimestral)
- Departamentos financieros

```bash
userforge -i cfo_names.txt -pd 5 --passwords \
  --company-name "BankCorp" \
  --quarters \
  --departments \
  --years 2023-2025 \
  --complexity high \
  --min-pass-length 12 \
  --rotation-count 16 \
  --format json \
  -v \
  -o ataque_financiero
```

**Patrones generados:**
- `BankCorpQ1-2024!`
- `FinanceQ2-2024@`
- `FY2024BankCorp#`
- `Q3-2024Finance!`

**Tasa de éxito esperada:** ~55% en entornos financieros

---

### Ejemplo 9: Enumeración de Active Directory Empresarial
**Escenario:** Descubrimiento de cuentas de usuario en un AD de gran empresa.

**Características:**
- Alta profundidad de usernames
- Generación de emails con múltiples dominios
- Tamaño de empresa grande
- Sin contraseñas (solo enumeración)

```bash
userforge -i empleados_500.txt -ud 5 \
  --emails company.local,corp.company.com,company.net \
  --company-size enterprise \
  --format txt \
  -o enumeracion_ad
```

**Resultado esperado:**
- ~8,000 variantes de username por persona
- Emails en 3 dominios
- Total: ~12,000,000 combinaciones para 500 empleados

**Uso:** Alimentar herramientas como `kerbrute` o `ldapsearch`

---

### Ejemplo 10: Password Spraying con Patrones Corporativos
**Escenario:** Ataque de password spraying contra AD con lista reducida de usuarios conocidos.

**Características:**
- Usuarios conocidos (admin, service accounts)
- Profundidad alta de passwords
- Patrones corporativos críticos
- Modo inteligente

```bash
userforge -i admin_accounts.txt -ud 1 -pd 4 --passwords \
  --departments \
  --quarters \
  --rotation-count 24 \
  --target-company "TechCorp" \
  --smart \
  --optimize \
  --min-pass-length 8 \
  -o spray_corporativo
```

**Patrones generados:**
- `IT2024!`, `IT2024@`, `IT2024#`
- `Q1-2024!`, `Q2-2024!`
- `TechCorp1!`, `TechCorp2!`, ..., `TechCorp24!`

**Ventaja:** Reduce lockouts con patrones altamente efectivos

---

### Ejemplo 11: Ataque Dirigido con Inteligencia OSINT
**Escenario:** Ataque a un ejecutivo específico usando información de LinkedIn/redes sociales.

**Características:**
- Un solo objetivo (CEO, CTO)
- Roles personalizados
- Palabras clave de OSINT
- Máxima profundidad

```bash
userforge -i ceo.txt -pd 5 --passwords \
  --roles "CEO,President,Director,Founder" \
  --common-words "Vision,Strategy,Growth,Innovation,Leadership" \
  --company-name "StartupXYZ" \
  --target-company "Google" \
  --years 2024-2025 \
  --leet-password 2 \
  --complexity high \
  -o ataque_ceo
```

**Patrones generados:**
- `JohnCEO2024!`
- `VisionStartupXYZ@`
- `L3@d3rship2024!`
- `GoogleFounder2025#`

**Información OSINT útil:**
- Proyectos mencionados en LinkedIn
- Palabras clave de tweets
- Intereses personales

---

### Ejemplo 12: Generación Masiva para Hashcat
**Escenario:** Crear wordlist masiva para cracking offline con Hashcat/John.

**Características:**
- Máxima profundidad
- Todos los patrones activados
- Optimización desactivada (queremos volumen)
- Formato texto plano

```bash
userforge -i all_employees_1000.txt -ud 3 -pd 5 --passwords \
  --keyboard-patterns \
  --numeric-sequences \
  --quarters \
  --departments \
  --years 2020-2025 \
  --rotation-count 36 \
  --leet-password 3 \
  --common-words "Company,Project,Secret,Internal,Confidential" \
  --format txt \
  -v \
  -o wordlist_hashcat
```

**Resultado esperado:**
- ~15,000 passwords por persona
- Total: ~15,000,000 passwords para 1,000 empleados
- Tamaño: ~200-300 MB

**Uso con Hashcat:**
```bash
hashcat -m 1000 -a 0 hashes.txt wordlist_hashcat/combined/all_passwords.txt
```

---

### Ejemplo 13: Auditoría de Políticas de Contraseñas
**Escenario:** Verificar si las contraseñas de la organización cumplen con la política.

**Características:**
- Análisis estadístico activado
- Filtros de longitud según política
- Complejidad definida
- Generación de reporte

```bash
userforge -i sample_users.txt -pd 3 --passwords \
  --analyze \
  --min-pass-length 12 \
  --max-pass-length 20 \
  --complexity high \
  --company-name "SecureCorp" \
  --format all \
  -o auditoria_politicas
```

**Análisis generado:**
- Distribución de longitudes
- Complejidad promedio
- Patrones más comunes
- Recomendaciones

---

### Ejemplo 14: Ataque Multi-Idioma
**Escenario:** Empresa multinacional con empleados de diferentes países.

**Características:**
- Múltiples ejecuciones con diferentes idiomas
- Patrones localizados
- Combinación de resultados

```bash
# España
userforge -i nombres_es.txt -d 3 --passwords \
  --language ES --country ES \
  --company-name "GlobalCorp" \
  -o ataque_es

# Francia
userforge -i nombres_fr.txt -d 3 --passwords \
  --language FR --country FR \
  --company-name "GlobalCorp" \
  -o ataque_fr

# Alemania
userforge -i nombres_de.txt -d 3 --passwords \
  --language DE --country DE \
  --company-name "GlobalCorp" \
  -o ataque_de

# Combinar resultados
cat ataque_*/combined/all_passwords.txt | sort -u > wordlist_multinacional.txt
```

**Patrones por idioma:**
- ES: `Primavera2024`, `Verano2024`
- FR: `Printemps2024`, `Été2024`
- DE: `Frühling2024`, `Sommer2024`

---

### Ejemplo 15: Modo Interactivo para Principiantes
**Escenario:** Usuario nuevo que no conoce todos los argumentos.

```bash
userforge -i nombres.txt -I
```

**Flujo interactivo:**
```
UserForge v1.0.0 - Interactive Mode

1. Generate passwords? (y/n) [n]: y
2. Use separate depth for users/passwords? (y/n) [n]: y
3. User depth (1-5) [3]: 2
4. Password depth (1-5) [3]: 5
5. Company name [None]: TechCorp
6. Use leet speak? (y/n) [n]: y
7. Leet level for passwords (0-3) [0]: 2
8. Add prefixes/suffixes? (y/n) [n]: n
9. Include quarters? (y/n) [n]: y
10. Include departments? (y/n) [n]: y
11. Output format (txt/json/xml/all) [txt]: all
12. Verbose mode? (y/n) [n]: y

Generating wordlists...
✓ Generated 264 usernames
✓ Generated 7,375 passwords
✓ Output saved to: UserForge_Output_20241027_123456
```

**Ventaja:** Guía paso a paso con explicaciones

---

## Tabla Resumen de Casos de Uso

| Caso de Uso | Profundidad | Argumentos Clave | Resultado Esperado |
|-------------|-------------|------------------|-------------------|
| **Enumeración Básica** | `-d 2` | Ninguno | ~500 usernames |
| **Password Spray Estándar** | `-d 3` | `--quarters`, `--company-name` | ~2,000 passwords |
| **Infraestructura Financiera** | `-pd 5` | `--quarters`, `--complexity high` | ~10,000 passwords |
| **Enumeración AD** | `-ud 5` | `--emails`, `--company-size` | ~8,000 usernames |
| **Ataque OSINT** | `-pd 5` | `--roles`, `--common-words` | ~12,000 passwords |
| **Hashcat Masivo** | `-pd 5` | Todos los patrones | ~15,000 passwords/persona |
| **Auditoría** | `-pd 3` | `--analyze`, `--complexity` | Reporte estadístico |
| **Multi-Idioma** | `-d 3` | `--language`, `--country` | Patrones localizados |

---


## 7. Formatos de Salida

Usa el argumento `--format` para especificar la salida deseada.

-   `--format txt`: Por defecto. Crea archivos de texto simples (`.txt`).
-   `--format json`: Crea archivos JSON estructurados (`.json`), útiles para la integración con otras herramientas.
-   `--format xml`: Crea archivos XML (`.xml`).
-   `--format all`: Genera la salida en los tres formatos simultáneamente.

## 8. Licencia

UserForge está licenciado bajo la Licencia Pública General de GNU v3.0. Eres libre de usarlo, modificarlo y distribuirlo bajo los términos de la licencia. Consulta el archivo [LICENSE](../LICENSE) para el texto completo.

