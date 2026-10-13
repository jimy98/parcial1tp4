import json

# Generador con opciones concisas, homogéneas en longitud y sin pistas visuales por tamaño.
# Todas las opciones de cada pregunta tienen una longitud similar y van al grano.
# Las explicaciones y definiciones completas se mantienen intactas en la sección de feedback.

questions = [
    # ==========================================
    # BLOQUE 1: GIT EN ENTORNOS DISTRIBUIDOS (16 preguntas)
    # ==========================================
    {
        "id": 1,
        "category": "Git Distribuido",
        "type": "multiple_choice",
        "question": "¿Cuál es la diferencia estructural de nodos entre un CVCS tradicional y Git?",
        "options": [
            {
                "text": "CVCS tiene un nodo central único; en Git cada desarrollador es potencialmente un nodo o repositorio.",
                "definition": "Correcto: en CVCS todos dependen del servidor central; en Git cada copia local es un repositorio completo con historial y capacidad de publicar."
            },
            {
                "text": "CVCS descentraliza los repositorios; en Git todos los usuarios sincronizan únicamente con un solo nodo.",
                "definition": "Incorrecto: invierte por completo los roles. Git es distribuido y CVCS es centralizado."
            },
            {
                "text": "CVCS almacena todo el historial localmente; en Git el historial se guarda siempre en la nube remota.",
                "definition": "Incorrecto: en Git el historial completo reside en cada máquina local."
            },
            {
                "text": "CVCS permite crear ramas ilimitadas; en Git los desarrolladores solo tienen permisos de lectura.",
                "definition": "Incorrecto: en Git las ramas son ultraligeras y cada usuario tiene permisos plenos en local."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 1: En los sistemas centralizados cada desarrollador es un nodo de trabajo consumidor de un repositorio central. En Git, cada desarrollador es potencialmente un nodo o un repositorio completo."
    },
    {
        "id": 2,
        "category": "Git Distribuido",
        "type": "multiple_choice",
        "question": "En un flujo centralizado, si John hace push primero y luego Jessica intenta hacer push del suyo, ¿qué hace Git?",
        "options": [
            {
                "text": "Sobrescribe automáticamente los commits de John con los cambios de Jessica.",
                "definition": "Incorrecto: Git nunca sobrescribe commits silenciosamente sin intervención."
            },
            {
                "text": "Rechaza el push de Jessica porque está intentando enviar cambios no rápidos.",
                "definition": "Correcto: el servidor rechaza el push non-fast-forward hasta que Jessica haga fetch y merge."
            },
            {
                "text": "Bloquea el repositorio de forma permanente hasta que intervenga el administrador.",
                "definition": "Incorrecto: no existe un bloqueo de repositorio; es un rechazo de comando habitual."
            },
            {
                "text": "Crea una nueva rama pública en el servidor para almacenar ambos cambios.",
                "definition": "Incorrecto: Git no inventa ramas automáticas en el servidor remoto."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 2: Git rechaza el push de Jessica avisando que son 'cambios no rápidos' (non-fast-forward). Jessica debe descargar y fusionar antes de empujar."
    },
    {
        "id": 3,
        "category": "Git Distribuido",
        "type": "true_false",
        "question": "En el flujo de trabajo centralizado, la necesidad de fusionar el trabajo previo antes de subir cambios aplica tanto a Git como a Subversion.",
        "options": [
            {
                "text": "Verdadero",
                "definition": "Correcto: el documento afirma expresamente que 'Este concepto es válido tanto en Git como en Subversion'."
            },
            {
                "text": "Falso",
                "definition": "Incorrecto: el principio de no sobrescribir trabajo ajeno en repositorios centrales es universal en CVCS y Git."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 1: 'El segundo desarrollador debe fusionar el trabajo del primero antes de subir sus cambios, para no sobrescribir los cambios del primero. Este concepto es válido tanto en Git como en Subversion'."
    },
    {
        "id": 4,
        "category": "Git Distribuido",
        "type": "multiple_choice",
        "question": "En el Flujo Administrador-Integración, ¿qué representa el repositorio 'canónico'?",
        "options": [
            {
                "text": "El repositorio oficial del proyecto.",
                "definition": "Correcto: es el repositorio oficial que representa la versión de referencia definitiva."
            },
            {
                "text": "La copia local de cada desarrollador.",
                "definition": "Incorrecto: esa es la copia o clon de trabajo privado."
            },
            {
                "text": "Una rama temporal para pruebas unitarias.",
                "definition": "Incorrecto: no es una rama efímera, es el repositorio maestro del proyecto."
            },
            {
                "text": "El servidor proxy de caché de la empresa.",
                "definition": "Incorrecto: no tiene relación con infraestructura proxy."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 2: 'Este escenario a menudo incluye un repositorio canónico que representa el proyecto \"oficial\"'."
    },
    {
        "id": 5,
        "category": "Git Distribuido",
        "type": "multiple_choice",
        "question": "En el flujo Administrador-Integración, ¿qué pasos realiza el contribuidor para aportar código?",
        "options": [
            {
                "text": "Hace push directo sobre la rama principal del repositorio oficial.",
                "definition": "Incorrecto: los contribuidores no tienen permiso de escritura sobre el repositorio oficial."
            },
            {
                "text": "Clona el repo oficial, hace cambios, empuja a su copia pública y avisa al admin.",
                "definition": "Correcto: clona, realiza commits locales, empuja a su fork público y pide al integrador que haga pull."
            },
            {
                "text": "Descarga un archivo .zip, modifica el código y lo envía por correo electrónico.",
                "definition": "Incorrecto: el flujo utiliza repositorios públicos remotos, no archivos zip."
            },
            {
                "text": "Modifica directamente los archivos en el servidor de producción del cliente.",
                "definition": "Incorrecto: mala práctica extrema de despliegue."
            }
        ],
        "correct_answer": 1,
        "explanation": "Páginas 2 y 3: El contribuidor clona el repositorio, realiza cambios, hace push en su copia pública y solicita al administrador que incorpore los cambios."
    },
    {
        "id": 6,
        "category": "Git Distribuido",
        "type": "multiple_choice",
        "question": "¿Cuál es la ventaja principal del flujo Administrador-Integración para los colaboradores?",
        "options": [
            {
                "text": "Obliga a sincronizar cambios en un horario fijo.",
                "definition": "Incorrecto: este flujo elimina las dependencias de horario estricto."
            },
            {
                "text": "Cada parte puede trabajar a su propio ritmo.",
                "definition": "Correcto: los contribuidores pueden seguir avanzando sin esperar la aprobación inmediata del administrador."
            },
            {
                "text": "Impide por completo cualquier conflicto de merge.",
                "definition": "Incorrecto: los conflictos aún pueden existir si se modifican las mismas líneas."
            },
            {
                "text": "Elimina el uso de ramas y commits intermedios.",
                "definition": "Incorrecto: las ramas siguen siendo fundamentales en este esquema."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 3: 'Los contribuidores no tienen que esperar a que el proyecto incorpore sus cambios; cada parte puede trabajar a su propio ritmo'."
    },
    {
        "id": 7,
        "category": "Git Distribuido",
        "type": "fill_in_the_blank",
        "question": "Completar: Plataformas como GitHub o GitLab facilitan el flujo Administrador-Integración al permitir hacer un ______ del proyecto para introducir cambios.",
        "correct_answer": "fork",
        "accepted_answers": ["fork", "bifurcacion", "bifurcación"],
        "explanation": "Un 'fork' es una copia pública del repositorio en la cuenta de un usuario que permite trabajar independientemente y luego proponer cambios."
    },
    {
        "id": 8,
        "category": "Git Distribuido",
        "type": "multiple_choice",
        "question": "¿En qué tipo de proyectos se utiliza típicamente el flujo Dictador-Tenientes?",
        "options": [
            {
                "text": "Pequeños sitios web de uno o dos desarrolladores.",
                "definition": "Incorrecto: genera una burocracia jerárquica innecesaria para equipos chicos."
            },
            {
                "text": "Grandes proyectos con cientos de personas, como Linux.",
                "definition": "Correcto: citado textualmente en el PDF con el ejemplo canónico del kernel de Linux."
            },
            {
                "text": "Equipos ágiles que no utilizan control de versiones.",
                "definition": "Incorrecto: este flujo se basa enteramente en las capacidades distribuidas de Git."
            },
            {
                "text": "Proyectos personales sin ningún tipo de jerarquía.",
                "definition": "Incorrecto: el modelo se fundamenta en una estructura estrictamente jerárquica."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 3: 'Generalmente es utilizado por grandes proyectos con cientos de colaboradores; un ejemplo famoso es el kernel de Linux'."
    },
    {
        "id": 9,
        "category": "Git Distribuido",
        "type": "multiple_choice",
        "question": "En el flujo Dictador-Tenientes, ¿qué rol desempeñan los 'tenientes'?",
        "options": [
            {
                "text": "Administran la integración de partes específicas del proyecto.",
                "definition": "Correcto: son administradores de integración encargados de subsistemas o módulos determinados."
            },
            {
                "text": "Son servidores automatizados que rechazan commits inválidos.",
                "definition": "Incorrecto: son personas con roles técnicos de liderazgo, no bots."
            },
            {
                "text": "Son los únicos usuarios autorizados a publicar en producción.",
                "definition": "Incorrecto: esa potestad la tiene el dictador benévolo en el repo de referencia."
            },
            {
                "text": "Son programadores novatos que solo tienen permiso de lectura.",
                "definition": "Incorrecto: tienen privilegios de integración muy elevados sobre sus áreas."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 3: 'Varios administradores de integración están a cargo de ciertas partes del repositorio. Se les llaman tenientes'."
    },
    {
        "id": 10,
        "category": "Git Distribuido",
        "type": "multiple_choice",
        "question": "¿Cuál es la jerarquía correcta de integración en el flujo Dictador-Tenientes?",
        "options": [
            {
                "text": "Desarrollador -> Dictador -> Tenientes -> Master.",
                "definition": "Incorrecto: el dictador no recibe cambios directos de los desarrolladores."
            },
            {
                "text": "Desarrollador -> Tenientes -> Dictador -> Repo de referencia.",
                "definition": "Correcto: los desarrolladores entregan a los tenientes; los tenientes entregan al dictador y este publica."
            },
            {
                "text": "Tenientes -> Desarrollador -> Dictador -> Producción.",
                "definition": "Incorrecto: los desarrolladores son la base y no integran el trabajo de los tenientes."
            },
            {
                "text": "Dictador -> Tenientes -> Desarrollador -> Servidor central.",
                "definition": "Incorrecto: invierte el flujo de integración de código ascendente."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 3: Los desarrolladores fusionan en sus ramas; los tenientes fusionan las ramas de los desarrolladores; el dictador fusiona las ramas de los tenientes y hace push al repositorio de referencia."
    },
    {
        "id": 11,
        "category": "Git Distribuido",
        "type": "true_false",
        "question": "El flujo de trabajo Dictador-Tenientes es el más común y habitual en la mayoría de las empresas.",
        "options": [
            {
                "text": "Verdadero",
                "definition": "Incorrecto: el PDF aclara de forma explícita que este tipo de flujo 'no es común'."
            },
            {
                "text": "Falso",
                "definition": "Correcto: solo se reserva para proyectos gigantescos o con estructuras altamente jerárquicas."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 3: 'Este tipo de flujo de trabajo no es común, pero puede ser útil en proyectos muy grandes o en entornos altamente jerárquicos'."
    },
    {
        "id": 12,
        "category": "Git Distribuido",
        "type": "fill_in_the_blank",
        "question": "Completar: En el flujo Dictador-Tenientes, el repositorio del ______ sirve como el repositorio de referencia del cual todos deben hacer pull.",
        "correct_answer": "dictador",
        "accepted_answers": ["dictador", "dictador benevolo", "dictador benévolo"],
        "explanation": "El repositorio del 'dictador' o 'dictador benévolo' actúa como la fuente de verdad definitiva de la que leen todos."
    },
    {
        "id": 13,
        "category": "Git Distribuido",
        "type": "multiple_choice",
        "question": "¿Qué característica de Git permite a cientos de desarrolladores trabajar en un flujo centralizado sin bloquearse?",
        "options": [
            {
                "text": "Su ligero y potente modelo de ramificación.",
                "definition": "Correcto: permite trabajar a través de docenas de ramas simultáneas de manera exitosa."
            },
            {
                "text": "El bloqueo automático de archivos en edición.",
                "definition": "Incorrecto: Git no utiliza bloqueos pesados de archivos (file locking) al estilo CVCS antiguo."
            },
            {
                "text": "La prohibición de realizar fusiones locales.",
                "definition": "Incorrecto: las fusiones locales son parte integral del uso diario de Git."
            },
            {
                "text": "La asignación de turnos diarios por usuario.",
                "definition": "Incorrecto: no se utilizan turnos; el trabajo es concurrente."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 2: 'Con el modelo de ramificación de Git, es posible que cientos de desarrolladores trabajen con éxito en un único proyecto a través de docenas de ramas simultáneamente'."
    },
    {
        "id": 14,
        "category": "Git Distribuido",
        "type": "multiple_choice",
        "question": "En el flujo Administrador-Integración, ¿qué acción realiza el administrador al recibir una solicitud?",
        "options": [
            {
                "text": "Borra el repositorio público del contribuidor.",
                "definition": "Incorrecto: el administrador no tiene ni necesita permisos de borrado sobre el fork del usuario."
            },
            {
                "text": "Agrega el remoto, prueba localmente y empuja al repo oficial.",
                "definition": "Correcto: añade el repositorio remoto, prueba los cambios, fusiona y publica en el repositorio canónico."
            },
            {
                "text": "Reescribe todo el código del colaborador desde cero.",
                "definition": "Incorrecto: el propósito de la integración es incorporar el código validado."
            },
            {
                "text": "Solicita las credenciales personales de la cuenta ajena.",
                "definition": "Incorrecto: no requiere acceso a la cuenta ajena; solo lectura de su repo público."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 2: El administrador agrega el repositorio del contribuidor como remoto, prueba los cambios localmente, los combina y los envía al repositorio principal."
    },
    {
        "id": 15,
        "category": "Git Distribuido",
        "type": "multiple_choice",
        "question": "¿Qué esquema de permisos define al flujo Administrador-Integración?",
        "options": [
            {
                "text": "Escritura en su propio repo público y lectura en los demás.",
                "definition": "Correcto: fórmula exacta descripta en la página 2 para este modelo de colaboración."
            },
            {
                "text": "Escritura compartida en el repositorio canónico para todos.",
                "definition": "Incorrecto: eso describe un flujo centralizado clásico con acceso de empuje compartido."
            },
            {
                "text": "Lectura y escritura restringidas a un único equipo físico.",
                "definition": "Incorrecto: no tiene que ver con restricciones de hardware."
            },
            {
                "text": "Acceso de solo lectura universal sin permiso de clonación.",
                "definition": "Incorrecto: en Git la clonación es libre para cualquier lector del proyecto."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 2: 'cada desarrollador tenga acceso de escritura a su propio repositorio público y acceso de lectura a todos los demás'."
    },
    {
        "id": 16,
        "category": "Git Distribuido",
        "type": "multiple_choice",
        "question": "¿Qué beneficio principal obtiene el líder del proyecto al aplicar el flujo Dictador-Tenientes?",
        "options": [
            {
                "text": "Evita tener que escribir pruebas unitarias de software.",
                "definition": "Incorrecto: el flujo organizativo no reemplaza las pruebas de calidad."
            },
            {
                "text": "Delega trabajo y recopila código ya integrado en varios puntos.",
                "definition": "Correcto: evita el cuello de botella centralizando la integración previa en tenientes confiables."
            },
            {
                "text": "Elimina por completo la necesidad de usar ramas master.",
                "definition": "Incorrecto: las ramas master de cada teniente y del dictador son el eje del flujo."
            },
            {
                "text": "Permite que cualquier persona haga push directo a producción.",
                "definition": "Incorrecto: al contrario, establece un filtro jerárquico estricto."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 3: 'Permite al líder del proyecto (el dictador) delegar gran parte del trabajo y recopilar grandes subconjuntos de código en múltiples puntos antes de integrarlos'."
    },

    # ==========================================
    # BLOQUE 2: CONCEPTO DE API Y APIS WEB (12 preguntas)
    # ==========================================
    {
        "id": 17,
        "category": "Fundamentos de API",
        "type": "multiple_choice",
        "question": "¿Qué es conceptualmente una API según el material de estudio?",
        "options": [
            {
                "text": "Un tipo de base de datos relacional para guardar registros.",
                "definition": "Incorrecto: una API no almacena datos de forma persistente ni es un motor de BD."
            },
            {
                "text": "Código que permite comunicar y compartir datos entre aplicaciones.",
                "definition": "Correcto: Interfaz de Programación de Aplicaciones que conecta sistemas distintos."
            },
            {
                "text": "Un compilador de código fuente para aplicaciones móviles.",
                "definition": "Incorrecto: no compila ni genera código binario."
            },
            {
                "text": "Un cable de fibra óptica para conectar computadoras en red.",
                "definition": "Incorrecto: es una interfaz de software, no un elemento físico de hardware."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 4: 'Una Interfaz de Programación de Aplicaciones (API) es una pieza de código que permite a diferentes aplicaciones comunicarse entre sí y compartir información y funcionalidades'."
    },
    {
        "id": 18,
        "category": "Fundamentos de API",
        "type": "multiple_choice",
        "question": "¿Por qué en la práctica se afirma que una API actúa como un 'contrato'?",
        "options": [
            {
                "text": "Porque define qué pedir, cómo pedirlo y la forma de la respuesta.",
                "definition": "Correcto: establece especificaciones claras sin necesidad de conocer los detalles internos ajenos."
            },
            {
                "text": "Porque cobra una tarifa monetaria obligatoria por cada request.",
                "definition": "Incorrecto: el término 'contrato' es arquitectónico y de especificación, no comercial."
            },
            {
                "text": "Porque exige firmar un acuerdo legal antes de enviar un paquete.",
                "definition": "Incorrecto: no hace referencia a documentos legales físicos o firmas jurídicas."
            },
            {
                "text": "Porque obliga a que ambos sistemas utilicen el mismo lenguaje.",
                "definition": "Incorrecto: las APIs promueven la interoperabilidad entre lenguajes completamente distintos."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 4: 'actúa como un contrato: define qué datos se pueden pedir, cómo se hacen esas peticiones y qué forma tendrán las respuestas'."
    },
    {
        "id": 19,
        "category": "Fundamentos de API",
        "type": "multiple_choice",
        "question": "¿Cuál de los siguientes es un ejemplo cotidiano de consumo de API citado en el PDF?",
        "options": [
            {
                "text": "Una app del clima consumiendo datos de un servicio externo.",
                "definition": "Correcto: citado textualmente en la página 4 como ejemplo cotidiano."
            },
            {
                "text": "Formatear un disco rígido local en sistema de archivos NTFS.",
                "definition": "Incorrecto: es una operación de bajo nivel del sistema operativo local."
            },
            {
                "text": "Editar código fuente sin conexión en un editor de texto plano.",
                "definition": "Incorrecto: trabajo en local que no interactúa con servicios externos."
            },
            {
                "text": "Desfragmentar la memoria RAM de un servidor de cómputo.",
                "definition": "Incorrecto: tarea de mantenimiento del kernel del sistema operativo."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 4: Ejemplos cotidianos: app del clima consumiendo servicio externo, app de tareas que guarda en servidor, y frontend obteniendo productos de backend."
    },
    {
        "id": 20,
        "category": "Fundamentos de API",
        "type": "multiple_choice",
        "question": "¿A través de qué protocolo y en qué formatos opera típicamente una API Web?",
        "options": [
            {
                "text": "Protocolo FTP enviando exclusivamente texto comprimido en zip.",
                "definition": "Incorrecto: FTP es para transferencia de ficheros y no es el estándar de las APIs web."
            },
            {
                "text": "Protocolos HTTP o HTTPS intercambiando formatos como JSON o XML.",
                "definition": "Correcto: estándar de la web según se define explícitamente en la página 4."
            },
            {
                "text": "Protocolo Bluetooth enviando exclusivamente binarios en crudo.",
                "definition": "Incorrecto: Bluetooth opera en redes de área personal inalámbricas, no web."
            },
            {
                "text": "Protocolo SMTP intercambiando correos electrónicos automáticos.",
                "definition": "Incorrecto: SMTP se utiliza exclusivamente para envío de correo electrónico."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 4: Las APIs web se consumen usando protocolos web (normalmente HTTP o HTTPS) y devuelven respuestas procesables como JSON o XML."
    },
    {
        "id": 21,
        "category": "Fundamentos de API",
        "type": "multiple_choice",
        "question": "¿Cuáles son los 5 tipos de APIs Web mencionados en el documento?",
        "options": [
            {
                "text": "REST, SOAP, GraphQL, Webhook y RPC.",
                "definition": "Correcto: la lista completa y exacta provista en la página 4 del texto."
            },
            {
                "text": "TCP, UDP, IP, ICMP y DNS.",
                "definition": "Incorrecto: protocolos de la pila de red de internet."
            },
            {
                "text": "HTML, CSS, JavaScript, TypeScript y Python.",
                "definition": "Incorrecto: lenguajes de desarrollo web y frontend."
            },
            {
                "text": "MySQL, PostgreSQL, MongoDB, SQLite y Redis.",
                "definition": "Incorrecto: sistemas gestores de bases de datos."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 4: Lista formal de tipos de APIs WEB: REST, SOAP, GraphQL, Webhook, RPC."
    },
    {
        "id": 22,
        "category": "Fundamentos de API",
        "type": "multiple_choice",
        "question": "¿Por qué REST suele ser la opción más simple para comenzar en APIs web?",
        "options": [
            {
                "text": "Porque elimina la necesidad de configurar servidores de red.",
                "definition": "Incorrecto: siempre se requiere un servidor que atienda las peticiones."
            },
            {
                "text": "Porque aprovecha la estructura natural de HTTP ya existente.",
                "definition": "Correcto: utiliza URLs, métodos (GET/POST), códigos de estado y encabezados nativos."
            },
            {
                "text": "Porque no permite que se generen errores durante la ejecución.",
                "definition": "Incorrecto: los errores ocurren y se comunican con códigos 4xx o 5xx."
            },
            {
                "text": "Porque no requiere tener conocimientos previos de programación.",
                "definition": "Incorrecto: requiere comprender desarrollo y arquitectura de software."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 4: 'REST suele ser la opción más simple para comenzar porque aprovecha la estructura natural de HTTP: URLs, métodos, códigos de estado y formato de intercambio de datos'."
    },
    {
        "id": 23,
        "category": "Fundamentos de API",
        "type": "fill_in_the_blank",
        "question": "Completar: El acrónimo REST significa REpresentational State ______ (Transferencia de Estado Representacional).",
        "correct_answer": "Transfer",
        "accepted_answers": ["Transfer", "transfer"],
        "explanation": "REST proviene del inglés Representational State Transfer, acuñado formalmente por Roy Fielding."
    },
    {
        "id": 24,
        "category": "Fundamentos de API",
        "type": "true_false",
        "question": "REST es una tecnología concreta y una librería que se debe instalar obligatoriamente mediante npm en el proyecto.",
        "options": [
            {
                "text": "Verdadero",
                "definition": "Incorrecto: REST no es software, ejecutable ni paquete de código descargable."
            },
            {
                "text": "Falso",
                "definition": "Correcto: el documento aclara textualmente: 'No es una tecnología ni una librería. Es un conjunto de reglas y buenas prácticas'."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 5: 'No es una tecnología ni una librería. Es un conjunto de reglas y buenas prácticas para diseñar servicios web de forma simple, predecible y escalable'."
    },
    {
        "id": 25,
        "category": "Fundamentos de API",
        "type": "multiple_choice",
        "question": "En REST, ¿qué recibe el cliente en lugar del objeto 'crudo' almacenado en la base de datos?",
        "options": [
            {
                "text": "Una consulta SQL sin ejecutar.",
                "definition": "Incorrecto: nunca se exponen consultas SQL al cliente por seguridad."
            },
            {
                "text": "Una representación del recurso.",
                "definition": "Correcto: el cliente recibe una representación adaptada al contexto (generalmente en JSON)."
            },
            {
                "text": "La memoria física del servidor.",
                "definition": "Incorrecto: la memoria interna del servidor nunca es accesible por el cliente."
            },
            {
                "text": "El archivo binario del backend.",
                "definition": "Incorrecto: no se descargan ejecutables de servidor al cliente."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 5: 'En REST, el cliente no suele recibir el objeto \"crudo\" que existe en la base de datos. Recibe una representación de ese recurso, generalmente en JSON'."
    },
    {
        "id": 26,
        "category": "Fundamentos de API",
        "type": "multiple_choice",
        "question": "Según el ejemplo de un 'libro' en el PDF, ¿cómo puede variar su representación según el contexto?",
        "options": [
            {
                "text": "El libro se elimina de la base si la vista pedida es simple.",
                "definition": "Incorrecto: una consulta de lectura no destruye los datos en la base de datos."
            },
            {
                "text": "Una vista simple muestra pocos campos y una detallada añade más.",
                "definition": "Correcto: el mismo recurso puede tener distintas representaciones sin cambiar la entidad base."
            },
            {
                "text": "El libro cambia obligatoriamente de identificador en cada request.",
                "definition": "Incorrecto: los identificadores deben ser estables y no fluctuar."
            },
            {
                "text": "La vista detallada solo se puede entregar en formato papel.",
                "definition": "Incorrecto: todas las respuestas se envían en formatos digitales estructurados."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 5: Una vista simple puede enviar título, autor y año; mientras que una vista detallada también incluye descripción, categoría, stock y precio."
    },
    {
        "id": 27,
        "category": "Fundamentos de API",
        "type": "true_false",
        "question": "La idea central de REST es que el cliente determine cómo se guardan los datos en la base de datos del servidor.",
        "options": [
            {
                "text": "Verdadero",
                "definition": "Incorrecto: viola el desacoplamiento cliente-servidor y el principio de REST."
            },
            {
                "text": "Falso",
                "definition": "Correcto: la idea central es que el servidor controle la representación y el cliente trabaje con recursos identificados por URL."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 5: 'La idea central es que el servidor controle la forma de la representación y que el cliente trabaje con recursos bien identificados por URL'."
    },
    {
        "id": 28,
        "category": "Fundamentos de API",
        "type": "multiple_choice",
        "question": "¿Por qué el material menciona específicamente a Express en el contexto de APIs Web?",
        "options": [
            {
                "text": "Porque es el único framework web permitido por el protocolo HTTP.",
                "definition": "Incorrecto: HTTP es independiente de cualquier framework o tecnología."
            },
            {
                "text": "Porque facilita mucho el desarrollo de APIs web en la materia.",
                "definition": "Correcto: citado textualmente en la página 4 como herramienta facilitadora."
            },
            {
                "text": "Porque reemplaza por completo a los comandos básicos de Git.",
                "definition": "Incorrecto: Git es control de versiones y Express es desarrollo backend."
            },
            {
                "text": "Porque impide que los clientes utilicen peticiones GET.",
                "definition": "Incorrecto: Express implementa y gestiona rutas GET de forma nativa."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 4: 'En esta materia nos vamos a concentrar en APIs web porque son las más comunes en aplicaciones modernas y porque Express facilita mucho su desarrollo'."
    },

    # ==========================================
    # BLOQUE 3: BENEFICIOS DE REST (14 preguntas)
    # ==========================================
    {
        "id": 29,
        "category": "Beneficios de REST",
        "type": "multiple_choice",
        "question": "¿Cuáles son los 7 beneficios formales de los sistemas organizados con REST listados en la página 5?",
        "options": [
            {
                "text": "Rendimiento, Escalabilidad, Simplicidad, Modificabilidad, Portabilidad, Fiabilidad y Visibilidad.",
                "definition": "Correcto: los 7 beneficios exactos explicados en detalle en las páginas 5 y 6."
            },
            {
                "text": "Velocidad de CPU, Memoria RAM, Cifrado, Minificación, Transpilación, Ofuscación y Tipado.",
                "definition": "Incorrecto: conceptos de compilación y optimización de código."
            },
            {
                "text": "Creación, Lectura, Actualización, Eliminación, Paginación, Filtrado y Orden.",
                "definition": "Incorrecto: operaciones de datos CRUD habituales."
            },
            {
                "text": "Consistencia, Latencia cero, Tolerancia a fallos, Anonimato, Backup, Bloqueo y Réplica.",
                "definition": "Incorrecto: conceptos generales de sistemas distribuidos y bases de datos."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 5: Rendimiento, Escalabilidad de la interacción de componentes, Simplicidad de interfaz, Modificabilidad de los componentes, Portabilidad, Fiabilidad, Visibilidad."
    },
    {
        "id": 30,
        "category": "Beneficios de REST",
        "type": "multiple_choice",
        "question": "¿Por qué REST favorece el RENDIMIENTO del sistema?",
        "options": [
            {
                "text": "Porque sobreescribe los drivers gráficos de la computadora.",
                "definition": "Incorrecto: no tiene relación con el hardware gráfico del equipo."
            },
            {
                "text": "Por usar recursos bien definidos, respuestas compactas y caché.",
                "definition": "Correcto: JSON liviano y caché reducen consultas innecesarias y tiempo de respuesta."
            },
            {
                "text": "Porque elimina el uso del protocolo TCP/IP en la red.",
                "definition": "Incorrecto: HTTP y REST se ejecutan sobre la capa de transporte TCP/IP."
            },
            {
                "text": "Porque fuerza a que las respuestas estén siempre vacías.",
                "definition": "Incorrecto: la mayoría de respuestas transportan el cuerpo de la representación."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 5: 'Rendimiento: al trabajar con recursos bien definidos, respuestas compactas y formatos como JSON, la comunicación suele ser liviana. Además, cuando la API usa caché correctamente, evita consultas innecesarias y reduce el tiempo de respuesta'."
    },
    {
        "id": 31,
        "category": "Beneficios de REST",
        "type": "multiple_choice",
        "question": "¿En qué consiste la 'ESCALABILIDAD DE LA INTERACCIÓN DE COMPONENTES' en REST?",
        "options": [
            {
                "text": "Al ser peticiones independientes, el servidor puede distribuir carga.",
                "definition": "Correcto: como no hay sesiones atadas a un nodo, la carga se reparte entre varias instancias."
            },
            {
                "text": "En forzar a que todos los clientes usen una sola máquina central.",
                "definition": "Incorrecto: eso limita la escalabilidad y crea un punto único de fallo."
            },
            {
                "text": "En exigir que el servidor duplique su memoria RAM cada semana.",
                "definition": "Incorrecto: eso describe escalabilidad vertical forzada."
            },
            {
                "text": "En mantener una conexión de socket TCP abierta para siempre.",
                "definition": "Incorrecto: REST se basa en peticiones HTTP desacopladas sin estado."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 5: 'Como las peticiones son independientes, el servidor puede distribuir la carga entre varias instancias y crecer sin cambiar la forma de uso para el cliente'."
    },
    {
        "id": 32,
        "category": "Beneficios de REST",
        "type": "multiple_choice",
        "question": "¿Cómo se explica el beneficio de 'SIMPLICIDAD DE INTERFAZ' en REST?",
        "options": [
            {
                "text": "La interfaz de usuario gráfica solo puede tener un botón.",
                "definition": "Incorrecto: no se refiere al diseño visual de la interfaz de usuario (UI)."
            },
            {
                "text": "Aprender métodos uniformes (GET/POST/PUT) aplica a muchos recursos.",
                "definition": "Correcto: la uniformidad conceptual reduce la curva de aprendizaje y facilita documentar."
            },
            {
                "text": "El servidor solo puede exponer una única ruta para toda la web.",
                "definition": "Incorrecto: una API REST suele exponer múltiples rutas de recursos."
            },
            {
                "text": "Se prohíbe documentar la API para mantenerla breve.",
                "definition": "Incorrecto: al contrario, la simplicidad hace más fácil documentarla."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 6: 'Simplicidad de interfaz: REST propone una manera uniforme de trabajar... permite aplicar ese conocimiento a muchos recursos distintos. Eso reduce la curva de aprendizaje y hace más fácil documentar la API'."
    },
    {
        "id": 33,
        "category": "Beneficios de REST",
        "type": "multiple_choice",
        "question": "¿En qué se traduce la 'MODIFICABILIDAD DE LOS COMPONENTES' gracias al desacoplamiento?",
        "options": [
            {
                "text": "El backend puede cambiar su base de datos sin romper al cliente.",
                "definition": "Correcto: mientras se respete el contrato de la API y la URL visible, la lógica interna puede mutar."
            },
            {
                "text": "Cualquier cambio interno exige reprogramar todo el frontend.",
                "definition": "Incorrecto: eso representaría un acoplamiento indeseable."
            },
            {
                "text": "El usuario final puede editar el código fuente del servidor.",
                "definition": "Incorrecto: falla grave de seguridad sin relación con REST."
            },
            {
                "text": "Los métodos HTTP cambian de nombre según la base de datos.",
                "definition": "Incorrecto: los métodos HTTP son estándares y fijos."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 6: 'el backend puede reorganizar su lógica interna o reemplazar su base de datos sin cambiar la URL ni el contrato visible al cliente'."
    },
    {
        "id": 34,
        "category": "Beneficios de REST",
        "type": "multiple_choice",
        "question": "¿Qué significa la 'PORTABILIDAD' en una API REST?",
        "options": [
            {
                "text": "Que el servidor debe pesar menos de un megabyte en el disco.",
                "definition": "Incorrecto: portabilidad no se refiere al tamaño del archivo."
            },
            {
                "text": "Que cualquier cliente capaz de usar HTTP puede consumirla.",
                "definition": "Correcto: puede ser consumida desde navegador, móvil, escritorio u otros servicios sin importar tecnologías."
            },
            {
                "text": "Que solo funciona en dispositivos con baterías portátiles.",
                "definition": "Incorrecto: confusión coloquial con el término portátil."
            },
            {
                "text": "Que la API debe cambiar de IP pública todos los días.",
                "definition": "Incorrecto: perjudicaría la estabilidad de los identificadores."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 6: 'Portabilidad: una API REST puede ser consumida desde navegador, aplicaciones móviles, programas de escritorio u otros servicios... sin importar en qué tecnología esté hecho'."
    },
    {
        "id": 35,
        "category": "Beneficios de REST",
        "type": "multiple_choice",
        "question": "¿Por qué la ausencia de estado (stateless) incrementa la FIABILIDAD del sistema?",
        "options": [
            {
                "text": "Si una instancia falla, otra puede atender la siguiente petición.",
                "definition": "Correcto: como cada request trae toda la información, no hay dependencia oculta de memoria previa."
            },
            {
                "text": "Porque garantiza que el hardware del servidor jamás se dañará.",
                "definition": "Incorrecto: ningún diseño de software previene fallos físicos de hardware."
            },
            {
                "text": "Porque el cliente guarda una copia completa de la base de datos.",
                "definition": "Incorrecto: el cliente solo tiene la representación del recurso pedido."
            },
            {
                "text": "Porque prohíbe el uso de servidores intermedios y proxies.",
                "definition": "Incorrecto: al contrario, la fiabilidad stateless facilita el uso de múltiples servidores."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 6: 'la ausencia de estado en el servidor reduce dependencias ocultas entre una petición y la siguiente. Si una instancia falla, otra puede atender la próxima solicitud porque cada request trae la información necesaria'."
    },
    {
        "id": 36,
        "category": "Beneficios de REST",
        "type": "multiple_choice",
        "question": "¿Cómo contribuye el uso estándar de HTTP a la VISIBILIDAD del sistema?",
        "options": [
            {
                "text": "Aumentando el contraste de los monitores de los usuarios.",
                "definition": "Incorrecto: chiste que confunde visibilidad técnica con luminosidad de pantalla."
            },
            {
                "text": "Facilita monitorear peticiones, tiempos y errores con logs o proxies.",
                "definition": "Correcto: permite inspeccionar el tráfico de red mediante herramientas de observación estándar."
            },
            {
                "text": "Mostrando las contraseñas de los usuarios en texto claro.",
                "definition": "Incorrecto: vulnerabilidad crítica de seguridad."
            },
            {
                "text": "Eliminando los registros para no dejar rastros de auditoría.",
                "definition": "Incorrecto: lo opuesto a la visibilidad y observabilidad."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 6: 'Visibilidad: al usar HTTP de manera estándar, es más fácil monitorear lo que ocurre. Se pueden registrar peticiones, medir tiempos de respuesta, leer códigos de estado y detectar errores'."
    },
    {
        "id": 37,
        "category": "Beneficios de REST",
        "type": "true_false",
        "question": "En contextos educativos, REST tiene la ventaja de combinar conceptos fáciles de entender con herramientas muy usadas en la industria.",
        "options": [
            {
                "text": "Verdadero",
                "definition": "Correcto: afirmación explícita del final de la página 6 del texto."
            },
            {
                "text": "Falso",
                "definition": "Incorrecto: el PDF resalta expresamente su gran valor pedagógico y profesional."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 6: 'En contextos educativos y de proyectos iniciales, REST tiene la ventaja de que combina conceptos fáciles de entender con herramientas muy usadas en la industria'."
    },
    {
        "id": 38,
        "category": "Beneficios de REST",
        "type": "fill_in_the_blank",
        "question": "Completar: Cuando la API usa ______ correctamente, evita consultas innecesarias y reduce el tiempo de respuesta.",
        "correct_answer": "caché",
        "accepted_answers": ["cache", "caché", "el caché", "la caché"],
        "explanation": "El uso adecuado de la caché almacena respuestas temporalmente para no sobrecargar el servidor."
    },
    {
        "id": 39,
        "category": "Beneficios de REST",
        "type": "true_false",
        "question": "Para ser considerada útil, una API RESTful está estrictamente obligada a cumplir todas sus restricciones de forma absoluta en cualquier escenario.",
        "options": [
            {
                "text": "Verdadero",
                "definition": "Incorrecto: el PDF indica que no necesita cumplirlas todas de forma absoluta."
            },
            {
                "text": "Falso",
                "definition": "Correcto: 'Una API RESTful no necesita cumplirlas todas de forma absoluta en cualquier caso, pero cuanto más se acerque a ellas, más coherente será su diseño'."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 6: 'Una API RESTful no necesita cumplirlas todas de forma absoluta en cualquier caso, pero cuanto más se acerque a ellas, más coherente será su diseño'."
    },
    {
        "id": 40,
        "category": "Beneficios de REST",
        "type": "fill_in_the_blank",
        "question": "Completar: El desacoplamiento que permite modificar el backend sin romper el contrato del cliente se llama Modificabilidad de los ______.",
        "correct_answer": "componentes",
        "accepted_answers": ["componentes", "componente"],
        "explanation": "Página 6: 'Modificabilidad de los componentes'."
    },
    {
        "id": 41,
        "category": "Beneficios de REST",
        "type": "multiple_choice",
        "question": "¿Por qué el formato JSON favorece el rendimiento en la comunicación de una API REST?",
        "options": [
            {
                "text": "Porque transporta datos de forma liviana y compacta.",
                "definition": "Correcto: la sintaxis concisa de clave-valor evita la sobrecarga de formatos más pesados."
            },
            {
                "text": "Porque duplica la longitud de los mensajes con etiquetas.",
                "definition": "Incorrecto: eso describe la verbosidad de XML, no de JSON."
            },
            {
                "text": "Porque cifra automáticamente la información sin clave.",
                "definition": "Incorrecto: JSON es texto plano; la seguridad en tránsito la da HTTPS."
            },
            {
                "text": "Porque sustituye por completo la necesidad de un backend.",
                "definition": "Incorrecto: JSON es solo un formato de serialización de datos."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 5: 'al trabajar con recursos bien definidos, respuestas compactas y formatos como JSON, la comunicación suele ser liviana'."
    },
    {
        "id": 42,
        "category": "Beneficios de REST",
        "type": "multiple_choice",
        "question": "¿Qué elemento preserva la compatibilidad con el cliente cuando el servidor cambia su lógica interna?",
        "options": [
            {
                "text": "El respeto al contrato de la API y a la URL visible.",
                "definition": "Correcto: mientras no cambie la especificación pública acordada, el cliente no sufrirá rupturas."
            },
            {
                "text": "El uso exclusivo de cookies locales en el navegador.",
                "definition": "Incorrecto: las cookies no aseguran el desacoplamiento de esquemas de datos."
            },
            {
                "text": "El reinicio obligatorio del router del usuario.",
                "definition": "Incorrecto: carece de sentido en la arquitectura de software."
            },
            {
                "text": "La prohibición de actualizar las versiones de la base.",
                "definition": "Incorrecto: precisamente REST permite actualizar la base de datos libremente."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 6: 'el backend puede reorganizar su lógica interna o reemplazar su base de datos sin cambiar la URL ni el contrato visible al cliente'."
    },

    # ==========================================
    # BLOQUE 4: RESTRICCIONES DE REST (14 preguntas)
    # ==========================================
    {
        "id": 43,
        "category": "Restricciones RESTful",
        "type": "multiple_choice",
        "question": "¿Cuáles son las 6 restricciones formales de una arquitectura RESTful?",
        "options": [
            {
                "text": "Cliente-servidor, Sin estados, Cacheable, Interfaz uniforme, Capas y Código bajo demanda.",
                "definition": "Correcto: las 6 restricciones exactas descriptas en las páginas 6 a 8 del PDF."
            },
            {
                "text": "Autenticación, Encriptación, Compresión, Paginación, Filtrado y Docker.",
                "definition": "Incorrecto: técnicas de desarrollo e infraestructura, no restricciones teóricas de REST."
            },
            {
                "text": "GET, POST, PUT, DELETE, PATCH y OPTIONS.",
                "definition": "Incorrecto: métodos del protocolo HTTP, no restricciones arquitectónicas."
            },
            {
                "text": "HTML, CSS, JavaScript, Servidor Node, MongoDB y Git.",
                "definition": "Incorrecto: tecnologías de una pila de desarrollo específica."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 6: Las 6 restricciones son: Cliente-servidor, Sin estados, Cacheable, Interfaz uniforme, Sistema en capas, Código bajo demanda (opcional)."
    },
    {
        "id": 44,
        "category": "Restricciones RESTful",
        "type": "multiple_choice",
        "question": "¿Qué separación de responsabilidades establece la restricción CLIENTE-SERVIDOR?",
        "options": [
            {
                "text": "Cliente: interfaz y experiencia; Servidor: lógica, datos y respuestas.",
                "definition": "Correcto: separación limpia de responsabilidades citada en la página 7."
            },
            {
                "text": "Cliente: base de datos; Servidor: renderizado de pantallas de usuario.",
                "definition": "Incorrecto: invierte las responsabilidades fundamentales de la arquitectura."
            },
            {
                "text": "Cliente y servidor deben compartir la misma memoria física siempre.",
                "definition": "Incorrecto: se busca la independencia total de plataformas y procesos."
            },
            {
                "text": "El cliente solo puede enviar datos pero nunca recibir respuestas.",
                "definition": "Incorrecto: la interacción es bidireccional mediante petición y respuesta."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 7: 'El cliente se ocupa de la interfaz, la experiencia de uso y la interacción con el usuario. El servidor se ocupa de la lógica de negocio, el acceso a datos y la generación de respuestas'."
    },
    {
        "id": 45,
        "category": "Restricciones RESTful",
        "type": "multiple_choice",
        "question": "¿Qué exige la restricción 'SIN ESTADOS' (Stateless) en cada petición enviada al servidor?",
        "options": [
            {
                "text": "El servidor debe almacenar el historial previo del usuario en RAM.",
                "definition": "Incorrecto: viola directamente la restricción de sin estados."
            },
            {
                "text": "Cada request debe contener toda la información para ser entendido.",
                "definition": "Correcto: el servidor no depende de sesiones guardadas en memoria entre requests."
            },
            {
                "text": "El cliente debe enviar una solicitud vacía antes de enviar datos.",
                "definition": "Incorrecto: no existe tal requisito técnico en el estándar."
            },
            {
                "text": "El servidor debe reiniciar su proceso después de cada respuesta.",
                "definition": "Incorrecto: los servidores atienden concurrentemente miles de peticiones sin reiniciar."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 7: 'cada petición debe contener toda la información necesaria para ser entendida por el servidor. El servidor no debería depender de datos guardados en memoria sobre interacciones anteriores'."
    },
    {
        "id": 46,
        "category": "Restricciones RESTful",
        "type": "multiple_choice",
        "question": "En sistemas reales, ¿cómo se implementa habitualmente la autenticación bajo el principio Stateless?",
        "options": [
            {
                "text": "Mediante tokens como JWT o sesiones almacenadas externamente.",
                "definition": "Correcto: el token viaja en cada request para que el proceso no retenga estado local."
            },
            {
                "text": "Guardando los datos del usuario en variables globales del servidor.",
                "definition": "Incorrecto: esto acopla la sesión al proceso e impide balancear carga."
            },
            {
                "text": "Pidiendo que el usuario ingrese su contraseña por teléfono.",
                "definition": "Incorrecto: absurdo técnico."
            },
            {
                "text": "Deshabilitando cualquier tipo de validación de seguridad.",
                "definition": "Incorrecto: inaceptable en sistemas en producción."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 7: 'este principio suele combinarse con autenticación por token, como JWT o sesiones almacenadas externamente, para no guardar el estado de la interacción dentro del proceso del servidor'."
    },
    {
        "id": 47,
        "category": "Restricciones RESTful",
        "type": "multiple_choice",
        "question": "¿Cuáles son las 4 mejoras que aporta el principio Stateless según el esquema de la página 7?",
        "options": [
            {
                "text": "Visibilidad, Escalabilidad, Fiabilidad e Implementación más fácil.",
                "definition": "Correcto: las 4 mejoras concretas enumeradas bajo 'Stateless - Mejoras' en el PDF."
            },
            {
                "text": "Velocidad de WiFi, Resolución de pantalla, Batería y Audio.",
                "definition": "Incorrecto: factores de hardware ajenos a la arquitectura de software."
            },
            {
                "text": "Cero consumo de CPU, Menos líneas CSS, Más HTML y Cifrado SSL.",
                "definition": "Incorrecto: mezcla arbitraria sin sustento teórico."
            },
            {
                "text": "Persistencia en RAM, Sesiones activas, Monolitos y Acoplamiento.",
                "definition": "Incorrecto: son precisamente las prácticas que stateless busca evitar."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 7: 'Stateless - Mejoras: Visibilidad (monitoreo), Escalabilidad, Fiabilidad, Implementación más fácil'."
    },
    {
        "id": 48,
        "category": "Restricciones RESTful",
        "type": "multiple_choice",
        "question": "¿Qué establece la restricción 'CACHEABLE'?",
        "options": [
            {
                "text": "Una respuesta puede reutilizarse por un tiempo sin consultar al servidor.",
                "definition": "Correcto: ahorra ancho de banda y reduce latencia al no rehacer consultas idénticas."
            },
            {
                "text": "Todas las respuestas deben borrarse de memoria en menos de un segundo.",
                "definition": "Incorrecto: eso anularía el propósito del cacheo."
            },
            {
                "text": "El servidor debe imprimir en papel cada respuesta enviada.",
                "definition": "Incorrecto: broma inverosímil."
            },
            {
                "text": "Los datos deben guardarse permanentemente sin posibilidad de caducar.",
                "definition": "Incorrecto: la caché tiene políticas de expiración y revalidación."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 8: 'La cacheabilidad significa que una respuesta puede reutilizarse durante un tiempo sin volver a consultar al servidor. Esto reduce latencia y tráfico de red'."
    },
    {
        "id": 49,
        "category": "Restricciones RESTful",
        "type": "multiple_choice",
        "question": "¿Qué tipo de recursos se suelen cachear normalmente según el texto?",
        "options": [
            {
                "text": "Transacciones financieras en vivo con saldos al segundo.",
                "definition": "Incorrecto: datos altamente volátiles y críticos que no toleran desactualización diferida."
            },
            {
                "text": "Recursos que cambian poco o toleran actualización diferida.",
                "definition": "Correcto: imágenes, catálogos o datos públicos citados en la página 8."
            },
            {
                "text": "Códigos de verificación temporales de un solo uso (OTP).",
                "definition": "Incorrecto: contraseñas de un solo uso nunca se cachean."
            },
            {
                "text": "Únicamente las respuestas que devuelven errores del servidor.",
                "definition": "Incorrecto: no tiene sentido cachear fallos internos como política general."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 8: 'Normalmente se cachean recursos que cambian poco o que toleran cierta actualización diferida, como imágenes, catálogos o datos públicos'."
    },
    {
        "id": 50,
        "category": "Restricciones RESTful",
        "type": "multiple_choice",
        "question": "¿Qué encabezados HTTP apoyan la cacheabilidad según el documento?",
        "options": [
            {
                "text": "Cache-Control, ETag o Last-Modified.",
                "definition": "Correcto: cabeceras estándar citadas textualmente en la página 8 del PDF."
            },
            {
                "text": "Content-Type, User-Agent y Host.",
                "definition": "Incorrecto: cabeceras de metadatos de formato y cliente, no de caché."
            },
            {
                "text": "Authorization, Bearer y Cookie.",
                "definition": "Incorrecto: cabeceras orientadas a autenticación y sesión."
            },
            {
                "text": "Accept-Language, Origin y Referer.",
                "definition": "Incorrecto: cabeceras de negociación de contenido y procedencia."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 8: 'En HTTP esto se apoya con encabezados como Cache-Control, ETag o Last-Modified'."
    },
    {
        "id": 51,
        "category": "Restricciones RESTful",
        "type": "multiple_choice",
        "question": "¿En cuáles 4 aspectos se refleja la 'INTERFAZ UNIFORME' en REST?",
        "options": [
            {
                "text": "Métodos HTTP, URLs de recursos, códigos de estado y datos predecibles.",
                "definition": "Correcto: los 4 pilares exactos explicados en la página 8 del documento."
            },
            {
                "text": "Mismo color, misma tipografía, mismo icono y mismo tamaño.",
                "definition": "Incorrecto: principios de diseño gráfico / UI de pantalla, no de la API."
            },
            {
                "text": "Un único endpoint, solo método GET, sin errores y texto plano.",
                "definition": "Incorrecto: diseño pésimo que contradice totalmente el estándar REST."
            },
            {
                "text": "Mismo sistema operativo, misma CPU, misma marca y misma IP.",
                "definition": "Incorrecto: restricciones de hardware incompatibles con la portabilidad."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 8: Uso correcto de métodos HTTP, uso de recursos identificados por URL, respuestas con códigos de estado claros y formatos predecibles (JSON)."
    },
    {
        "id": 52,
        "category": "Restricciones RESTful",
        "type": "multiple_choice",
        "question": "¿Qué principio fundamental rige la restricción de 'SISTEMA EN CAPAS'?",
        "options": [
            {
                "text": "El cliente no necesita saber si interactúa con proxy, balanceador o base.",
                "definition": "Correcto: cada capa intermedia cumple una función concreta sin alterar la interfaz visible."
            },
            {
                "text": "El cliente debe conectarse por separado a cada capa física de la red.",
                "definition": "Incorrecto: el cliente solo conoce el endpoint unificado al que realiza su petición."
            },
            {
                "text": "Se prohíbe el uso de balanceadores de carga y proxies intermedios.",
                "definition": "Incorrecto: al contrario, la arquitectura en capas promueve su inserción transparente."
            },
            {
                "text": "El código debe organizarse en exactamente diez carpetas en el disco.",
                "definition": "Incorrecto: no se refiere a la estructura de archivos en la máquina del programador."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 8: 'el cliente no necesita saber si el servidor accede directamente a la base de datos, si usa un servicio intermedio o si pasa por un balanceador'."
    },
    {
        "id": 53,
        "category": "Restricciones RESTful",
        "type": "true_false",
        "question": "La restricción de 'Código bajo demanda' (Code on Demand) es opcional en una arquitectura RESTful.",
        "options": [
            {
                "text": "Verdadero",
                "definition": "Correcto: el documento especifica expresamente: 'Código bajo demanda (opcional)'."
            },
            {
                "text": "Falso",
                "definition": "Incorrecto: es la única restricción de Fielding formalmente declarada como opcional."
            }
        ],
        "correct_answer": 0,
        "explanation": "Páginas 6 y 8: 'Código bajo demanda (opcional)... pero no una característica esencial de una API REST'."
    },
    {
        "id": 54,
        "category": "Restricciones RESTful",
        "type": "multiple_choice",
        "question": "¿Qué permite la restricción opcional de 'Código bajo demanda'?",
        "options": [
            {
                "text": "El servidor puede enviar código ejecutable para extender al cliente.",
                "definition": "Correcto: por ejemplo, scripts que el navegador descarga para enriquecer la interfaz."
            },
            {
                "text": "El programador debe escribir código solo cuando un cliente lo pida.",
                "definition": "Incorrecto: interpretación literal humorística."
            },
            {
                "text": "Descargar la base de datos completa en cada petición del usuario.",
                "definition": "Incorrecto: vulnerabilidad extrema sin relación técnica."
            },
            {
                "text": "Compilar el servidor desde cero cada vez que recibe un visitante.",
                "definition": "Incorrecto: generaría una lentitud inaceptable."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 8: 'Indica que el servidor puede enviar código ejecutable al cliente para extender su comportamiento (como scripts que el navegador descarga)'."
    },
    {
        "id": 55,
        "category": "Restricciones RESTful",
        "type": "fill_in_the_blank",
        "question": "Completar: En una arquitectura en capas, se pueden intercalar capas de seguridad, caché, monitoreo o ______ sin alterar la interfaz visible para el cliente.",
        "correct_answer": "proxy",
        "accepted_answers": ["proxy", "balanceador", "balanceo", "autenticacion", "autenticación"],
        "explanation": "Página 8: 'Esto permite agregar capas de seguridad, caché, monitoreo o proxy sin cambiar la interfaz visible para el cliente'."
    },
    {
        "id": 56,
        "category": "Restricciones RESTful",
        "type": "true_false",
        "question": "En una API sin estados, si un cliente hace dos peticiones iguales, el servidor puede responder igual sin necesidad de recordar la primera.",
        "options": [
            {
                "text": "Verdadero",
                "definition": "Correcto: concepto fundamental de stateless descripto en la página 7."
            },
            {
                "text": "Falso",
                "definition": "Incorrecto: en stateless cada petición es auto-contenida e independiente."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 7: 'si un cliente hace dos peticiones iguales, el servidor puede responder igual sin recordar la primera'."
    },

    # ==========================================
    # BLOQUE 5: RECURSOS, REPRESENTACIONES E IDENTIFICADORES (12 preguntas)
    # ==========================================
    {
        "id": 57,
        "category": "Recursos y URLs",
        "type": "multiple_choice",
        "question": "¿Qué es un RECURSO en la arquitectura REST?",
        "options": [
            {
                "text": "El bloque principal y la abstracción de lo que pueda ser nombrado.",
                "definition": "Correcto: definición clave en la página 9: una entidad con significado en el dominio del problema."
            },
            {
                "text": "Únicamente una tabla dentro de una base de datos MySQL.",
                "definition": "Incorrecto: el texto aclara que un recurso NO es solamente un dato guardado en base de datos."
            },
            {
                "text": "La memoria RAM disponible en el hardware del servidor.",
                "definition": "Incorrecto: eso es un recurso físico del equipo, no el concepto arquitectónico REST."
            },
            {
                "text": "Un archivo comprimido descargable en el navegador.",
                "definition": "Incorrecto: es un tipo de archivo estático específico, no la abstracción de recurso."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 9: 'Son los bloques principales de una arquitectura REST. Todo lo que pueda ser nombrado puede ser un recurso... Es la abstracción de cualquier cosa que pueda ser conceptualizada'."
    },
    {
        "id": 58,
        "category": "Recursos y URLs",
        "type": "multiple_choice",
        "question": "¿Cuáles son las 4 partes que componen la estructura de un recurso REST?",
        "options": [
            {
                "text": "Representación, Identificador, Metadatos y Datos de control.",
                "definition": "Correcto: la estructura cuatripartita formal explicada en la página 9 del texto."
            },
            {
                "text": "Frontend, Backend, Base de datos y Servidor web.",
                "definition": "Incorrecto: capas de infraestructura de una aplicación."
            },
            {
                "text": "Título, Autor, Editorial y Año de publicación.",
                "definition": "Incorrecto: campos de un modelo de datos particular de un libro."
            },
            {
                "text": "GET, POST, PUT y DELETE.",
                "definition": "Incorrecto: verbos o métodos HTTP, no partes estructurales del recurso."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 9: 'Estructura: 1. La representación, 2. El identificador, 3. Los metadatos, 4. Los datos de control'."
    },
    {
        "id": 59,
        "category": "Recursos y URLs",
        "type": "multiple_choice",
        "question": "¿Cuál es la función de los 'DATOS DE CONTROL' en un recurso REST?",
        "options": [
            {
                "text": "Controlar los ventiladores y temperatura del servidor.",
                "definition": "Incorrecto: no tiene relación con el hardware físico."
            },
            {
                "text": "Ayudar a manejar caché, modificaciones condicionales o permisos.",
                "definition": "Correcto: definición textual de datos de control dada en la página 9."
            },
            {
                "text": "Eliminar la cuenta del usuario si tarda en contestar.",
                "definition": "Incorrecto: acción arbitraria sin sentido técnico."
            },
            {
                "text": "Cambiar el estilo visual de las fuentes en pantalla.",
                "definition": "Incorrecto: función de CSS en la capa de presentación."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 9: '4. Los datos de control, que ayudan a manejar caché, modificaciones condicionales o permisos'."
    },
    {
        "id": 60,
        "category": "Recursos y URLs",
        "type": "multiple_choice",
        "question": "¿Qué es la REPRESENTACIÓN de un recurso según la página 10?",
        "options": [
            {
                "text": "La copia en crudo de los sectores del disco duro.",
                "definition": "Incorrecto: los datos del disco nunca se transmiten directamente en crudo."
            },
            {
                "text": "Bytes y metadatos con la forma en que el recurso viaja por la red.",
                "definition": "Correcto: formato concreto (JSON, XML, texto) en el que viaja el recurso entre sistemas."
            },
            {
                "text": "El nombre de la variable asignada en el código backend.",
                "definition": "Incorrecto: las variables locales del servidor son invisibles al cliente."
            },
            {
                "text": "Una foto de la pantalla del servidor enviada por correo.",
                "definition": "Incorrecto: formato inadecuado para la interacción entre aplicaciones."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 10: 'Un conjunto de bytes y algún metadata que describen estos bytes. La representación es la forma concreta en la que un recurso viaja por la red'."
    },
    {
        "id": 61,
        "category": "Recursos y URLs",
        "type": "true_false",
        "question": "En REST, un mismo recurso puede tener más de una representación (por ejemplo JSON y XML).",
        "options": [
            {
                "text": "Verdadero",
                "definition": "Correcto: el recurso es el mismo; lo que cambia es su representación según el cliente."
            },
            {
                "text": "Falso",
                "definition": "Incorrecto: REST promueve explícitamente múltiples representaciones negociables."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 10: 'Un recurso puede tener más de una representación... Por ejemplo, un libro puede representarse como JSON para una app web, como XML para una integración antigua'."
    },
    {
        "id": 62,
        "category": "Recursos y URLs",
        "type": "multiple_choice",
        "question": "¿Cuáles son las 4 características que debe tener un BUEN IDENTIFICADOR?",
        "options": [
            {
                "text": "Único, Estable, Legible y Predecible.",
                "definition": "Correcto: las 4 propiedades indispensables explicadas en la página 11 del documento."
            },
            {
                "text": "Dinámico, Efímero, Cifrado y Oculto.",
                "definition": "Incorrecto: atentan contra la legibilidad y estabilidad requeridas en REST."
            },
            {
                "text": "Numérico, Aleatorio, Largo y Temporal.",
                "definition": "Incorrecto: un identificador no debe depender de lógicas temporales cambiantes."
            },
            {
                "text": "Privado, Local, Bloqueado y Secreto.",
                "definition": "Incorrecto: las URLs públicas deben ser accesibles y seguir convenciones claras."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 11: Un buen identificador debe ser: Único (no apuntar a más de uno), Estable (no cambiar todo el tiempo), Legible (expresar qué representa) y Predecible (convención clara)."
    },
    {
        "id": 63,
        "category": "Recursos y URLs",
        "type": "multiple_choice",
        "question": "¿Por qué la ruta `GET /api/v1/libros/ultimo` es considerada un ejemplo ERRÓNEO en el PDF?",
        "options": [
            {
                "text": "Porque el idioma español está prohibido en las URLs.",
                "definition": "Incorrecto: el idioma no condiciona la validez arquitectónica de la ruta."
            },
            {
                "text": "Porque depende de una lógica temporal ambigua que cambia con el tiempo.",
                "definition": "Correcto: no identifica un recurso único y estable; lo que es 'último' hoy no lo será mañana."
            },
            {
                "text": "Porque contiene más de tres barras diagonales en la ruta.",
                "definition": "Incorrecto: la profundidad de rutas no invalida la semántica REST."
            },
            {
                "text": "Porque el método GET no permite solicitar libros.",
                "definition": "Incorrecto: GET es precisamente el método para obtener información."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 11: Se prefieren rutas como `/libros/12` antes que `/ultimo-libro` porque la segunda depende de una lógica temporal y no identifica de forma única ni estable al recurso."
    },
    {
        "id": 64,
        "category": "Recursos y URLs",
        "type": "multiple_choice",
        "question": "¿Cuál es la forma correcta según el PDF para obtener el último libro mediante parámetros?",
        "options": [
            {
                "text": "GET /api/v1/libros?limit=1&sort=created_at",
                "definition": "Correcto: ejemplo textual de buena práctica en la página 11 usando query parameters."
            },
            {
                "text": "POST /api/v1/libros/dame-el-mas-nuevo",
                "definition": "Incorrecto: utiliza un verbo en la URL y usa POST indebidamente para lectura."
            },
            {
                "text": "DELETE /api/v1/libros/ultimo",
                "definition": "Incorrecto: DELETE eliminaría el recurso en lugar de consultarlo."
            },
            {
                "text": "GET /api/v1/obtenerUltimoLibro",
                "definition": "Incorrecto: antipatrón que incluye el verbo de la acción en la ruta."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 11: Ejemplo correcto: `GET /api/v1/libros?limit=1&sort=created_at`."
    },
    {
        "id": 65,
        "category": "Recursos y URLs",
        "type": "multiple_choice",
        "question": "En una API REST, ¿con qué clase de palabras suelen construirse las URLs?",
        "options": [
            {
                "text": "Con verbos de acción en imperativo (/crearLibro).",
                "definition": "Incorrecto: es un antipatrón propio de RPC, no de la arquitectura REST."
            },
            {
                "text": "Con sustantivos, no con verbos.",
                "definition": "Correcto: ayuda a pensar en términos de recursos y no en operaciones internas del servidor."
            },
            {
                "text": "Únicamente con adjetivos calificativos.",
                "definition": "Incorrecto: carece de sentido conceptual en el diseño de APIs."
            },
            {
                "text": "Con cadenas de texto aleatorias e ilegibles.",
                "definition": "Incorrecto: atenta contra la legibilidad y predictibilidad."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 11: 'En una API REST, las URLs suelen construirse con sustantivos, no con verbos. Eso ayuda a pensar en términos de recursos y no en términos de operaciones internas del servidor'."
    },
    {
        "id": 66,
        "category": "Recursos y URLs",
        "type": "multiple_choice",
        "question": "¿Cuál de las siguientes URLs representa una mala práctica (ejemplo menos recomendable citado)?",
        "options": [
            {
                "text": "GET /api/v1/libros/12",
                "definition": "Buena práctica: sustantivo en plural seguido del identificador único del recurso."
            },
            {
                "text": "/getLibros",
                "definition": "Mala práctica citada en la página 12: coloca el verbo 'get' en la URL en lugar de usar métodos HTTP."
            },
            {
                "text": "POST /api/v1/libros",
                "definition": "Buena práctica: verbo POST hacia la colección de recursos sustantivados."
            },
            {
                "text": "DELETE /api/v1/libros/12",
                "definition": "Buena práctica: método DELETE aplicado directamente sobre el identificador."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 12: Ejemplos menos recomendables: `/getLibros`, `/createLibro`, `/deleteLibro/12`."
    },
    {
        "id": 67,
        "category": "Recursos y URLs",
        "type": "fill_in_the_blank",
        "question": "Completar: En la estructura de un recurso REST, la parte que describe la respuesta o el recurso corresponde a los ______.",
        "correct_answer": "metadatos",
        "accepted_answers": ["metadatos", "metadata"],
        "explanation": "Página 9: '3. Los metadatos, que describen la respuesta o el recurso'."
    },
    {
        "id": 68,
        "category": "Recursos y URLs",
        "type": "true_false",
        "question": "La estructura de un recurso REST obliga a almacenar los datos de una forma específica dentro de la base de datos.",
        "options": [
            {
                "text": "Verdadero",
                "definition": "Incorrecto: el texto aclara que NO obliga a guardarlo de forma específica en la BD."
            },
            {
                "text": "Falso",
                "definition": "Correcto: la página 10 dice: 'Esta estructura no obliga a guardar el recurso de una forma específica en la base de datos. Solo indica cómo se expone desde la API'."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 10: 'Esta estructura no obliga a guardar el recurso de una forma específica en la base de datos. Solo indica cómo se expone desde la API'."
    },

    # ==========================================
    # BLOQUE 6: VERBOS HTTP Y CÓDIGOS DE ESTADO (12 preguntas)
    # ==========================================
    {
        "id": 69,
        "category": "Verbos y Códigos de Estado",
        "type": "multiple_choice",
        "question": "¿Cuál es la diferencia de alcance entre los métodos HTTP PUT y PATCH?",
        "options": [
            {
                "text": "PUT crea usuarios nuevos y PATCH los elimina.",
                "definition": "Incorrecto: crear corresponde a POST y eliminar a DELETE."
            },
            {
                "text": "PUT reemplaza el recurso completo; PATCH actualiza solo una parte.",
                "definition": "Correcto: distinción semántica fundamental de la página 12 (sustituir estado vs cambio parcial)."
            },
            {
                "text": "PUT funciona solo en Windows y PATCH solo en Linux.",
                "definition": "Incorrecto: los métodos HTTP son independientes del sistema operativo."
            },
            {
                "text": "Son exactamente sinónimos sin ninguna diferencia.",
                "definition": "Incorrecto: PUT exige el recurso completo mientras PATCH admite modificaciones parciales."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 12: PUT: 'Reemplazar o actualizar un recurso completo / Sustituir el estado'. PATCH: 'Actualizar una parte del recurso / Cambio parcial'."
    },
    {
        "id": 70,
        "category": "Verbos y Códigos de Estado",
        "type": "multiple_choice",
        "question": "¿Cuál es el propósito y la idea asociada al método HTTP HEAD?",
        "options": [
            {
                "text": "Consultar metadatos sin cuerpo para verificar existencia o estado.",
                "definition": "Correcto: definición textual en la página 12: comprueba cabeceras sin descargar el payload."
            },
            {
                "text": "Consultar las capacidades y verbos disponibles que soporta la API.",
                "definition": "Incorrecto: esa es la función de OPTIONS."
            },
            {
                "text": "Borrar la cabecera principal de la base de datos del servidor.",
                "definition": "Incorrecto: HEAD es un método de solo lectura y no borra nada."
            },
            {
                "text": "Subir archivos adjuntos pesados en el cuerpo del request.",
                "definition": "Incorrecto: HEAD precisamente nunca devuelve ni procesa cuerpo de mensaje."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 12: HEAD: 'Consultar metadatos sin cuerpo' / 'Verificar existencia o estado'."
    },
    {
        "id": 71,
        "category": "Verbos y Códigos de Estado",
        "type": "multiple_choice",
        "question": "¿Para qué se utiliza el método HTTP OPTIONS según la página 12?",
        "options": [
            {
                "text": "Consultar capacidades disponibles para saber qué puede hacer el cliente.",
                "definition": "Correcto: definición exacta en la tabla de acciones del PDF."
            },
            {
                "text": "Configurar las opciones de brillo y color de la interfaz de usuario.",
                "definition": "Incorrecto: no tiene relación con configuraciones de pantalla."
            },
            {
                "text": "Modificar parcialmente una propiedad específica de un recurso.",
                "definition": "Incorrecto: esa es la función de PATCH."
            },
            {
                "text": "Crear un nuevo recurso enviando datos en el cuerpo.",
                "definition": "Incorrecto: esa es la función de POST."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 12: OPTIONS: 'Consultar capacidades disponibles' / 'Saber que puede hacer el cliente'."
    },
    {
        "id": 72,
        "category": "Verbos y Códigos de Estado",
        "type": "multiple_choice",
        "question": "¿Qué indica la familia de códigos de estado HTTP 4xx?",
        "options": [
            {
                "text": "Errores generados por los clientes.",
                "definition": "Correcto: indica solicitudes mal formadas, sin autenticación o con recursos inexistentes."
            },
            {
                "text": "Errores internos de los servidores.",
                "definition": "Incorrecto: los errores de servidor pertenecen a la familia 5xx."
            },
            {
                "text": "Respuestas informativas bajo HTTP 1.1.",
                "definition": "Incorrecto: las respuestas informativas corresponden a 1xx."
            },
            {
                "text": "Redirecciones a otra URL destino.",
                "definition": "Incorrecto: las redirecciones corresponden a 3xx."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 12: '4xx: Errores de los clientes'."
    },
    {
        "id": 73,
        "category": "Verbos y Códigos de Estado",
        "type": "multiple_choice",
        "question": "¿Qué significa específicamente el código de estado HTTP 201 Created?",
        "options": [
            {
                "text": "La solicitud se resolvió pero no se creó nada.",
                "definition": "Incorrecto: ese caso suele ser 200 OK."
            },
            {
                "text": "Se creó un recurso nuevo en el servidor.",
                "definition": "Correcto: respuesta estándar tras un POST exitoso que crea un nuevo recurso."
            },
            {
                "text": "La petición tenía un formato inválido.",
                "definition": "Incorrecto: eso corresponde a 400 Bad Request."
            },
            {
                "text": "Ocurrió un error interno en el servidor.",
                "definition": "Incorrecto: eso corresponde a 500 Internal Server Error."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 13: '201 Created: se creó un recurso nuevo'."
    },
    {
        "id": 74,
        "category": "Verbos y Códigos de Estado",
        "type": "multiple_choice",
        "question": "¿Cuándo se devuelve típicamente el código de estado 204 No Content?",
        "options": [
            {
                "text": "Cuando la base de datos colapsó y se perdieron datos.",
                "definition": "Incorrecto: 204 indica éxito, no una pérdida o falla de base de datos."
            },
            {
                "text": "Acción exitosa donde no hace falta devolver cuerpo.",
                "definition": "Correcto: respuesta típica de un DELETE exitoso donde la operación se cumplió."
            },
            {
                "text": "Cuando el cliente omitió las credenciales de acceso.",
                "definition": "Incorrecto: la falta de credenciales devuelve 401 Unauthorized."
            },
            {
                "text": "Cuando el servidor no encuentra el archivo pedido.",
                "definition": "Incorrecto: recurso no encontrado devuelve 404 Not Found."
            }
        ],
        "correct_answer": 1,
        "explanation": "Página 13: '204 No Content: la acción fue exitosa pero no hace falta devolver cuerpo'."
    },
    {
        "id": 75,
        "category": "Verbos y Códigos de Estado",
        "type": "multiple_choice",
        "question": "¿Qué representa el código de estado HTTP 400 Bad Request?",
        "options": [
            {
                "text": "La petición del cliente tiene un formato inválido.",
                "definition": "Correcto: datos mal estructurados o parámetros incorrectos que el backend no puede procesar."
            },
            {
                "text": "El servidor se apagó por una sobrecarga eléctrica.",
                "definition": "Incorrecto: fallas de infraestructura generan 5xx o desconexión TCP."
            },
            {
                "text": "La operación se completó de manera satisfactoria.",
                "definition": "Incorrecto: 400 es un código de error de cliente."
            },
            {
                "text": "El recurso fue trasladado permanentemente de lugar.",
                "definition": "Incorrecto: redirección permanente corresponde a 301 Moved Permanently."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 13: '400 Bad Request: la petición tiene un formato inválido'."
    },
    {
        "id": 76,
        "category": "Verbos y Códigos de Estado",
        "type": "multiple_choice",
        "question": "¿Cuál es la causa de una respuesta con código de estado 401 Unauthorized?",
        "options": [
            {
                "text": "Falta autenticación o las credenciales son inválidas.",
                "definition": "Correcto: definición textual en la página 13 del PDF."
            },
            {
                "text": "El recurso solicitado no existe en el servidor.",
                "definition": "Incorrecto: recurso inexistente devuelve 404 Not Found."
            },
            {
                "text": "La solicitud fue procesada correctamente sin cuerpo.",
                "definition": "Incorrecto: eso corresponde a 204 No Content."
            },
            {
                "text": "El servidor demoró demasiado tiempo en responder.",
                "definition": "Incorrecto: demora excesiva devuelve 504 Gateway Timeout o 408."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 13: '401 Unauthorized: falta autenticación o es inválida'."
    },
    {
        "id": 77,
        "category": "Verbos y Códigos de Estado",
        "type": "multiple_choice",
        "question": "¿Qué significan los códigos de estado 404 y 500 según el PDF?",
        "options": [
            {
                "text": "404: recurso no existe; 500: problema en el servidor.",
                "definition": "Correcto: definiciones textuales de 404 Not Found y 500 Internal Server Error."
            },
            {
                "text": "404: éxito completo; 500: redirección obligatoria.",
                "definition": "Incorrecto: invierte y distorsiona el significado de los códigos."
            },
            {
                "text": "404: falta autenticación; 500: petición inválida.",
                "definition": "Incorrecto: confunde 404/500 con 401 y 400."
            },
            {
                "text": "404: error de servidor; 500: error del cliente.",
                "definition": "Incorrecto: invierte las familias 4xx (cliente) y 5xx (servidor)."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 13: '404 Not Found: el recurso no existe. 500 Internal Server Error: ocurrió un problema en el servidor'."
    },
    {
        "id": 78,
        "category": "Verbos y Códigos de Estado",
        "type": "true_false",
        "question": "Los códigos de estado permiten entender rápidamente el resultado sin necesidad de leer toda la respuesta.",
        "options": [
            {
                "text": "Verdadero",
                "definition": "Correcto: cualidad clave de visibilidad descripta en la página 13."
            },
            {
                "text": "Falso",
                "definition": "Incorrecto: precisamente los códigos de estado evitan parsear el body para saber el resultado general."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 13: 'Los códigos de estado permiten entender rápidamente qué pasó con una petición sin leer toda la respuesta. Son una parte clave de REST porque hacen visible el resultado de cada acción'."
    },
    {
        "id": 79,
        "category": "Verbos y Códigos de Estado",
        "type": "fill_in_the_blank",
        "question": "Completar: Cuando una solicitud se resolvió correctamente con éxito, el código 200 lleva el nombre estándar ______.",
        "correct_answer": "OK",
        "accepted_answers": ["OK", "ok"],
        "explanation": "200 OK es el código estándar de éxito en el protocolo HTTP."
    },
    {
        "id": 80,
        "category": "Verbos y Códigos de Estado",
        "type": "multiple_choice",
        "question": "¿Por qué es tan valioso que la API devuelva los códigos de estado correctos?",
        "options": [
            {
                "text": "Permite al cliente reaccionar mejor: mostrar mensajes o reintentar.",
                "definition": "Correcto: conclusión del PDF: facilita informar al usuario, pedir credenciales o reintentar."
            },
            {
                "text": "Evita tener que escribir sentencias de control en el servidor.",
                "definition": "Incorrecto: el servidor debe escribir la lógica que determina el código adecuado."
            },
            {
                "text": "Garantiza que el cliente no consuma memoria RAM en el móvil.",
                "definition": "Incorrecto: la gestión de memoria no depende del código de estado HTTP."
            },
            {
                "text": "Fuerza a que todos los requests se completen en cero segundos.",
                "definition": "Incorrecto: el tiempo de respuesta depende del procesamiento y la red."
            }
        ],
        "correct_answer": 0,
        "explanation": "Página 13: 'Cuando la API devuelve el código correcto, el cliente puede reaccionar mejor: mostrar mensajes, reintentar, pedir credenciales o informar un error al usuario'."
    }
]

output_path = "/Users/jimy/.gemini/antigravity/scratch/simulador-examen-git-rest/questions_data.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"80 preguntas optimizadas con opciones breves y equilibradas guardadas en {output_path}")
