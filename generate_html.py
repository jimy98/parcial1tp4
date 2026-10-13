import json

with open("/Users/jimy/.gemini/antigravity/scratch/simulador-examen-git-rest/questions_data.json", "r", encoding="utf-8") as f:
    questions_json = f.read()

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Simulador de Examen: Git Distribuido & APIs REST (80 Preguntas)</title>
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            primary: {{
              50: '#eef2ff',
              100: '#e0e7ff',
              500: '#6366f1',
              600: '#4f46e5',
              700: '#4338ca',
              800: '#3730a3',
              900: '#312e81',
            }}
          }}
        }}
      }}
    }}
  </script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    body {{
      font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }}
    .custom-scroll::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    .custom-scroll::-webkit-scrollbar-track {{
      background: rgba(0,0,0,0.05);
    }}
    .custom-scroll::-webkit-scrollbar-thumb {{
      background: rgba(100,116,139,0.3);
      border-radius: 9999px;
    }}
    .badge-git {{ background-color: #f97316; color: white; }}
    .badge-api {{ background-color: #06b6d4; color: white; }}
    .badge-beneficios {{ background-color: #10b981; color: white; }}
    .badge-restricciones {{ background-color: #8b5cf6; color: white; }}
    .badge-recursos {{ background-color: #ec4899; color: white; }}
    .badge-verbos {{ background-color: #3b82f6; color: white; }}
  </style>
</head>
<body class="bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100 min-h-screen flex flex-col antialiased">

  <!-- Header -->
  <header class="sticky top-0 z-40 bg-white/95 dark:bg-slate-900/95 backdrop-blur border-b border-slate-200 dark:border-slate-800 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5 flex flex-wrap items-center justify-between gap-3">
      <div class="flex items-center space-x-3">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-indigo-600 to-violet-500 flex items-center justify-center text-white shadow-md font-bold text-xl">
          80
        </div>
        <div>
          <h1 class="text-lg sm:text-xl font-bold tracking-tight text-slate-900 dark:text-white leading-tight">
            Simulador de Examen: Git & REST
          </h1>
          <p class="text-xs text-slate-500 dark:text-slate-400">
            80 Preguntas de Preparación Intensiva para el Viernes
          </p>
        </div>
      </div>

      <!-- Control Bar Right -->
      <div class="flex items-center gap-2 sm:gap-3 flex-wrap">
        <!-- Modo Switcher -->
        <div class="bg-slate-100 dark:bg-slate-800 p-1 rounded-xl flex items-center text-xs font-semibold">
          <button id="btn-mode-study" onclick="setMode('study')" class="px-3 py-1.5 rounded-lg transition-all shadow-sm bg-white dark:bg-slate-700 text-indigo-600 dark:text-indigo-300">
            Modo Estudio (Feedback Inmediato)
          </button>
          <button id="btn-mode-exam" onclick="setMode('exam')" class="px-3 py-1.5 rounded-lg transition-all text-slate-600 dark:text-slate-300 hover:text-slate-900">
            Modo Examen (Simulacro)
          </button>
        </div>

        <!-- Dark Mode Toggle -->
        <button onclick="toggleDarkMode()" class="p-2 rounded-xl bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 dark:hover:bg-slate-700 text-slate-600 dark:text-slate-300 transition-colors" title="Alternar tema">
          <svg id="theme-icon-sun" class="w-5 h-5 hidden dark:block text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
          <svg id="theme-icon-moon" class="w-5 h-5 block dark:hidden text-slate-700" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
        </button>

        <!-- Reset Button -->
        <button onclick="confirmReset()" class="px-3 py-1.5 text-xs font-medium text-rose-600 dark:text-rose-400 hover:bg-rose-50 dark:hover:bg-rose-950/40 rounded-lg transition-colors border border-rose-200 dark:border-rose-900/50">
          Reiniciar Todo
        </button>
      </div>
    </div>

    <!-- Barra de progreso superior -->
    <div class="w-full bg-slate-200 dark:bg-slate-800 h-1.5">
      <div id="top-progress-bar" class="h-1.5 bg-gradient-to-r from-indigo-500 via-purple-500 to-emerald-500 transition-all duration-300 w-0"></div>
    </div>
  </header>

  <!-- Main Container -->
  <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6 grid grid-cols-1 lg:grid-cols-12 gap-6">

    <!-- Left Column: Navigation, Stats & Filters (4 cols) -->
    <aside class="lg:col-span-4 space-y-5">

      <!-- Score Card / Progress Summary -->
      <div class="bg-white dark:bg-slate-900 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 shadow-sm">
        <div class="flex items-center justify-between mb-4">
          <h2 class="text-sm font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400">Progreso del Test</h2>
          <span id="answered-count-badge" class="px-2.5 py-1 text-xs font-bold rounded-full bg-indigo-50 dark:bg-indigo-950/60 text-indigo-600 dark:text-indigo-400">
            0 / 80 respondidas
          </span>
        </div>

        <div class="grid grid-cols-3 gap-3 text-center mb-4">
          <div class="bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-900/40 rounded-xl p-3">
            <div id="stat-correct" class="text-2xl font-extrabold text-emerald-600 dark:text-emerald-400">0</div>
            <div class="text-[11px] font-semibold text-emerald-700 dark:text-emerald-300">Correctas</div>
          </div>
          <div class="bg-rose-50 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-900/40 rounded-xl p-3">
            <div id="stat-incorrect" class="text-2xl font-extrabold text-rose-600 dark:text-rose-400">0</div>
            <div class="text-[11px] font-semibold text-rose-700 dark:text-rose-300">Incorrectas</div>
          </div>
          <div class="bg-indigo-50 dark:bg-indigo-950/30 border border-indigo-200 dark:border-indigo-900/40 rounded-xl p-3">
            <div id="stat-percentage" class="text-2xl font-extrabold text-indigo-600 dark:text-indigo-400">0%</div>
            <div class="text-[11px] font-semibold text-indigo-700 dark:text-indigo-300">Acierto</div>
          </div>
        </div>

        <!-- Botón de entrega para modo examen -->
        <div id="exam-finish-container" class="hidden mb-3">
          <button onclick="finishExam()" class="w-full py-2.5 px-4 bg-gradient-to-r from-indigo-600 to-violet-600 hover:from-indigo-700 hover:to-violet-700 text-white font-bold text-sm rounded-xl shadow-md transition-all">
            📝 Entregar Examen y Ver Calificación
          </button>
        </div>

        <!-- Diagnóstico Rápido -->
        <div id="diagnostic-banner" class="p-3 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-800 text-xs">
          <div class="font-semibold text-slate-700 dark:text-slate-300 mb-1 flex items-center gap-1.5">
            <span>🎯 Estado para el viernes:</span>
            <span id="diagnostic-text" class="font-bold text-indigo-600 dark:text-indigo-400">Comenzando test...</span>
          </div>
          <p id="diagnostic-subtext" class="text-slate-500 dark:text-slate-400 text-[11px]">
            Responde preguntas para evaluar tus fortalezas y debilidades.
          </p>
        </div>
      </div>

      <!-- Temas y Rendimiento por Categoría -->
      <div class="bg-white dark:bg-slate-900 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 shadow-sm">
        <h3 class="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-3">
          Temas Evaluados en el PDF
        </h3>
        <div class="space-y-2.5 text-xs" id="category-progress-list">
          <!-- Dinámico -->
        </div>
      </div>

      <!-- Filtros -->
      <div class="bg-white dark:bg-slate-900 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 shadow-sm space-y-4">
        <div class="flex items-center justify-between">
          <h3 class="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400">Filtros y Búsqueda</h3>
          <button onclick="resetFilters()" class="text-xs text-indigo-600 dark:text-indigo-400 hover:underline">Limpiar</button>
        </div>

        <!-- Filtro Categoría -->
        <div>
          <label class="block text-[11px] font-semibold text-slate-600 dark:text-slate-400 mb-1">Por Tema:</label>
          <select id="filter-category" onchange="applyFilters()" class="w-full text-xs rounded-xl bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 p-2 text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-2 focus:ring-indigo-500">
            <option value="all">Todos los temas (80)</option>
            <option value="Git Distribuido">Git Distribuido (16)</option>
            <option value="Fundamentos de API">Fundamentos de API (12)</option>
            <option value="Beneficios de REST">Beneficios de REST (14)</option>
            <option value="Restricciones RESTful">Restricciones RESTful (14)</option>
            <option value="Recursos y URLs">Recursos y URLs (12)</option>
            <option value="Verbos y Códigos de Estado">Verbos y Códigos de Estado (12)</option>
          </select>
        </div>

        <!-- Filtro Tipo -->
        <div>
          <label class="block text-[11px] font-semibold text-slate-600 dark:text-slate-400 mb-1">Por Tipo:</label>
          <select id="filter-type" onchange="applyFilters()" class="w-full text-xs rounded-xl bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 p-2 text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-2 focus:ring-indigo-500">
            <option value="all">Todos los tipos</option>
            <option value="multiple_choice">Múltiple Choice (61)</option>
            <option value="true_false">Verdadero / Falso (11)</option>
            <option value="fill_in_the_blank">Autocompletar (8)</option>
          </select>
        </div>

        <!-- Filtro Estado Respuesta -->
        <div>
          <label class="block text-[11px] font-semibold text-slate-600 dark:text-slate-400 mb-1">Por Estado:</label>
          <select id="filter-status" onchange="applyFilters()" class="w-full text-xs rounded-xl bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 p-2 text-slate-800 dark:text-slate-200 focus:outline-none focus:ring-2 focus:ring-indigo-500">
            <option value="all">Todas las preguntas</option>
            <option value="unanswered">Sin responder</option>
            <option value="answered">Respondidas</option>
            <option value="correct">Solo correctas</option>
            <option value="incorrect">Solo INCORRECTAS (Repasar)</option>
            <option value="bookmarked">Marcadas con estrella ★</option>
          </select>
        </div>
      </div>

      <!-- Grilla de navegación rápida 1 a 80 -->
      <div class="bg-white dark:bg-slate-900 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 shadow-sm">
        <div class="flex items-center justify-between mb-3">
          <h3 class="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400">Navegador 1 a 80</h3>
          <span class="text-[11px] text-slate-400">Clic para saltar</span>
        </div>
        <div id="quick-jump-grid" class="grid grid-cols-8 sm:grid-cols-10 gap-1.5 max-h-56 overflow-y-auto custom-scroll p-1">
          <!-- 80 badges dinámicos -->
        </div>
        <div class="mt-3 pt-3 border-t border-slate-100 dark:border-slate-800 flex flex-wrap gap-2 text-[10px] text-slate-500">
          <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-slate-200 dark:bg-slate-700"></span> Pendiente</span>
          <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span> Correcta</span>
          <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-rose-500"></span> Incorrecta</span>
          <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-amber-400"></span> Marcada ★</span>
        </div>
      </div>

    </aside>

    <!-- Right Column: Question View / Cards (8 cols) -->
    <section class="lg:col-span-8 space-y-6">

      <!-- Banner de Resumen de Resultados (Visible tras entregar en modo examen) -->
      <div id="exam-results-modal" class="hidden bg-white dark:bg-slate-900 rounded-2xl p-6 border-2 border-indigo-500 shadow-xl space-y-4">
        <div class="flex items-start justify-between">
          <div>
            <span class="text-xs font-bold px-2.5 py-1 rounded-full bg-indigo-100 dark:bg-indigo-900/60 text-indigo-700 dark:text-indigo-300">
              RESULTADO FINAL DEL SIMULACRO
            </span>
            <h2 id="modal-score-title" class="text-2xl sm:text-3xl font-extrabold text-slate-900 dark:text-white mt-2">
              Calificación: 0/80 (0%)
            </h2>
          </div>
          <div id="modal-grade-badge" class="px-4 py-2 rounded-xl text-lg font-black text-white bg-slate-600">
            --
          </div>
        </div>

        <p id="modal-feedback-desc" class="text-sm text-slate-600 dark:text-slate-300 leading-relaxed">
          Resumen detallado de tu desempeño.
        </p>

        <div class="p-4 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700 space-y-2">
          <h4 class="text-xs font-bold uppercase tracking-wider text-slate-500 dark:text-slate-400">Recomendaciones para el examen del viernes:</h4>
          <ul id="modal-recommendations" class="text-xs text-slate-600 dark:text-slate-300 space-y-1 list-disc list-inside">
          </ul>
        </div>

        <div class="flex flex-wrap gap-3 pt-2">
          <button onclick="filterOnlyIncorrect()" class="px-4 py-2 bg-rose-600 hover:bg-rose-700 text-white rounded-xl text-xs font-bold transition shadow-sm">
            🔍 Ver y Repasar Solo las Incorrectas
          </button>
          <button onclick="setMode('study')" class="px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl text-xs font-bold transition shadow-sm">
            📖 Ver Explicaciones de Todas
          </button>
          <button onclick="confirmReset()" class="px-4 py-2 bg-slate-200 dark:bg-slate-800 hover:bg-slate-300 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300 rounded-xl text-xs font-bold transition">
            🔄 Repetir Examen Completo
          </button>
        </div>
      </div>

      <!-- Controles de vista de preguntas -->
      <div class="flex items-center justify-between text-xs text-slate-500 dark:text-slate-400 px-1">
        <span id="filtered-count-text">Mostrando 80 preguntas</span>
        <div class="flex items-center gap-2">
          <button onclick="expandAllExplanations(true)" class="hover:text-indigo-600 dark:hover:text-indigo-400 underline">Desplegar explicaciones</button>
          <span>•</span>
          <button onclick="expandAllExplanations(false)" class="hover:text-indigo-600 dark:hover:text-indigo-400 underline">Contraer</button>
        </div>
      </div>

      <!-- Lista de Preguntas -->
      <div id="questions-container" class="space-y-6">
        <!-- Renderizado dinámico de las 80 preguntas -->
      </div>

    </section>

  </main>

  <!-- Footer -->
  <footer class="mt-auto border-t border-slate-200 dark:border-slate-800 py-6 bg-white dark:bg-slate-900 text-center text-xs text-slate-500 dark:text-slate-400">
    <div class="max-w-7xl mx-auto px-4">
      <p>Simulador de Examen creado con los contenidos exactos del PDF: Git Distribuido, APIs Web, Arquitectura RESTful, Verbos HTTP y Códigos de Estado.</p>
      <p class="mt-1 text-[11px] text-slate-400 dark:text-slate-500">Éxito en el examen del viernes. ¡A estudiar y repasar cada definición!</p>
    </div>
  </footer>

  <!-- DATA & APP LOGIC -->
  <script>
    const questionsData = {questions_json};

    // Estado de la aplicación
    let state = {{
      mode: 'study', // 'study' (feedback inmediato) o 'exam' (simulador con entrega)
      examFinished: false,
      userAnswers: {{}}, // id -> {{ answer, isCorrect, timestamp }}
      bookmarks: new Set(),
      filters: {{
        category: 'all',
        type: 'all',
        status: 'all'
      }}
    }};

    // Cargar de LocalStorage
    function loadState() {{
      try {{
        const saved = localStorage.getItem('simulador_git_rest_state');
        if (saved) {{
          const parsed = JSON.parse(saved);
          state.userAnswers = parsed.userAnswers || {{}};
          state.bookmarks = new Set(parsed.bookmarks || []);
          if (parsed.mode) state.mode = parsed.mode;
          state.examFinished = parsed.examFinished || false;
        }}
      }} catch (e) {{
        console.error("Error cargando estado:", e);
      }}
    }}

    function saveState() {{
      try {{
        const toSave = {{
          userAnswers: state.userAnswers,
          bookmarks: Array.from(state.bookmarks),
          mode: state.mode,
          examFinished: state.examFinished
        }};
        localStorage.setItem('simulador_git_rest_state', JSON.stringify(toSave));
      }} catch (e) {{
        console.error("Error guardando estado:", e);
      }}
    }}

    function confirmReset() {{
      if (confirm("¿Estás seguro de que deseas reiniciar todas tus respuestas y progreso?")) {{
        state.userAnswers = {{}};
        state.bookmarks.clear();
        state.examFinished = false;
        saveState();
        document.getElementById('exam-results-modal').classList.add('hidden');
        renderApp();
      }}
    }}

    function toggleDarkMode() {{
      document.documentElement.classList.toggle('dark');
      localStorage.setItem('theme', document.documentElement.classList.contains('dark') ? 'dark' : 'light');
    }}

    // Inicializar tema
    if (localStorage.getItem('theme') === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {{
      document.documentElement.classList.add('dark');
    }} else {{
      document.documentElement.classList.remove('dark');
    }}

    function setMode(newMode) {{
      state.mode = newMode;
      const btnStudy = document.getElementById('btn-mode-study');
      const btnExam = document.getElementById('btn-mode-exam');
      const examContainer = document.getElementById('exam-finish-container');

      if (newMode === 'study') {{
        btnStudy.className = "px-3 py-1.5 rounded-lg transition-all shadow-sm bg-white dark:bg-slate-700 text-indigo-600 dark:text-indigo-300 font-bold";
        btnExam.className = "px-3 py-1.5 rounded-lg transition-all text-slate-600 dark:text-slate-300 hover:text-slate-900";
        examContainer.classList.add('hidden');
      }} else {{
        btnExam.className = "px-3 py-1.5 rounded-lg transition-all shadow-sm bg-white dark:bg-slate-700 text-indigo-600 dark:text-indigo-300 font-bold";
        btnStudy.className = "px-3 py-1.5 rounded-lg transition-all text-slate-600 dark:text-slate-300 hover:text-slate-900";
        examContainer.classList.remove('hidden');
      }}
      saveState();
      renderQuestions();
      updateStats();
    }}

    function toggleBookmark(qId) {{
      if (state.bookmarks.has(qId)) {{
        state.bookmarks.delete(qId);
      }} else {{
        state.bookmarks.add(qId);
      }}
      saveState();
      renderBookmarkButton(qId);
      renderQuickGrid();
    }}

    function renderBookmarkButton(qId) {{
      const btn = document.getElementById(`bookmark-btn-${{qId}}`);
      if (btn) {{
        const isMarked = state.bookmarks.has(qId);
        btn.innerHTML = isMarked 
          ? '<span class="text-amber-500 font-black">★ Guardada</span>' 
          : '<span class="text-slate-400 hover:text-amber-500">☆ Marcar</span>';
      }}
    }}

    // Respuesta para Selección Múltiple y V/F
    function selectOption(qId, optionIndex) {{
      const q = questionsData.find(item => item.id === qId);
      if (!q) return;

      const isCorrect = (optionIndex === q.correct_answer);
      state.userAnswers[qId] = {{
        answer: optionIndex,
        isCorrect: isCorrect,
        timestamp: Date.now()
      }};
      saveState();

      // En modo estudio o si el examen ya fue entregado, mostramos de inmediato
      renderSingleQuestion(qId);
      updateStats();
      renderQuickGrid();
    }}

    // Respuesta para Autocompletar
    function checkFillBlank(qId) {{
      const input = document.getElementById(`blank-input-${{qId}}`);
      if (!input) return;
      const text = input.value.trim().toLowerCase();
      if (!text) return;

      const q = questionsData.find(item => item.id === qId);
      if (!q) return;

      const accepted = (q.accepted_answers || [q.correct_answer]).map(a => a.toLowerCase().trim());
      const isCorrect = accepted.some(acc => text === acc || text.includes(acc));

      state.userAnswers[qId] = {{
        answer: input.value.trim(),
        isCorrect: isCorrect,
        timestamp: Date.now()
      }};
      saveState();

      renderSingleQuestion(qId);
      updateStats();
      renderQuickGrid();
    }}

    function finishExam() {{
      const answeredCount = Object.keys(state.userAnswers).length;
      if (answeredCount < 80) {{
        const confirmDelivery = confirm(`Has respondido ${{answeredCount}} de 80 preguntas. ¿Seguro que deseas entregar el examen ahora?`);
        if (!confirmDelivery) return;
      }}
      state.examFinished = true;
      saveState();

      // Mostrar modal de resultados y explicaciones completas
      showExamResults();
      renderQuestions();
      updateStats();
      renderQuickGrid();
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function showExamResults() {{
      const modal = document.getElementById('exam-results-modal');
      modal.classList.remove('hidden');

      let correct = 0;
      let wrong = 0;
      const catStats = {{}};

      questionsData.forEach(q => {{
        if (!catStats[q.category]) catStats[q.category] = {{ total: 0, correct: 0 }};
        catStats[q.category].total++;

        const ans = state.userAnswers[q.id];
        if (ans && ans.isCorrect) {{
          correct++;
          catStats[q.category].correct++;
        }} else if (ans) {{
          wrong++;
        }}
      }});

      const pct = Math.round((correct / 80) * 100);
      document.getElementById('modal-score-title').textContent = `Puntaje: ${{correct}} / 80 (${{pct}}%)`;

      const badge = document.getElementById('modal-grade-badge');
      const desc = document.getElementById('modal-feedback-desc');
      const recList = document.getElementById('modal-recommendations');
      recList.innerHTML = '';

      if (pct >= 85) {{
        badge.className = "px-4 py-2 rounded-xl text-lg font-black text-white bg-emerald-600";
        badge.textContent = "SOBRESALIENTE";
        desc.textContent = "¡Excelente preparación! Tienes los conceptos de Git distribuido y la arquitectura REST muy claros para el examen del viernes.";
      }} else if (pct >= 70) {{
        badge.className = "px-4 py-2 rounded-xl text-lg font-black text-white bg-blue-600";
        badge.textContent = "APROBADO";
        desc.textContent = "Buen nivel. Estás aprobado, pero te recomendamos repasar los temas donde tuviste errores para asegurar una nota sobresaliente el viernes.";
      }} else if (pct >= 50) {{
        badge.className = "px-4 py-2 rounded-xl text-lg font-black text-white bg-amber-500";
        badge.textContent = "EN RIESGO";
        desc.textContent = "Has aprobado de manera justa o estás cerca del límite. Hay conceptos clave que debes afianzar con urgencia antes del viernes.";
      }} else {{
        badge.className = "px-4 py-2 rounded-xl text-lg font-black text-white bg-rose-600";
        badge.textContent = "NECESITA REPASO";
        desc.textContent = "No alcanzarías la aprobación todavía. No te preocupes: lee con atención las explicaciones y definiciones de cada opción errónea y vuelve a intentar.";
      }}

      // Desglose por categorías para recomendaciones
      for (const [cat, data] of Object.entries(catStats)) {{
        const catPct = Math.round((data.correct / data.total) * 100);
        const li = document.createElement('li');
        if (catPct < 70) {{
          li.innerHTML = `<strong class="text-rose-600 dark:text-rose-400">${{cat}}:</strong> ${{data.correct}}/${{data.total}} (${{catPct}}%) — <span class="text-slate-700 dark:text-slate-300">¡Prioridad alta de repaso!</span>`;
        }} else {{
          li.innerHTML = `<strong class="text-emerald-600 dark:text-emerald-400">${{cat}}:</strong> ${{data.correct}}/${{data.total}} (${{catPct}}%) — Buen dominio.`;
        }}
        recList.appendChild(li);
      }}
    }}

    function filterOnlyIncorrect() {{
      document.getElementById('filter-status').value = 'incorrect';
      state.filters.status = 'incorrect';
      document.getElementById('exam-results-modal').classList.add('hidden');
      renderQuestions();
      window.scrollTo({{ top: 300, behavior: 'smooth' }});
    }}

    function resetFilters() {{
      document.getElementById('filter-category').value = 'all';
      document.getElementById('filter-type').value = 'all';
      document.getElementById('filter-status').value = 'all';
      state.filters = {{ category: 'all', type: 'all', status: 'all' }};
      renderQuestions();
    }}

    function applyFilters() {{
      state.filters.category = document.getElementById('filter-category').value;
      state.filters.type = document.getElementById('filter-type').value;
      state.filters.status = document.getElementById('filter-status').value;
      renderQuestions();
    }}

    function getFilteredQuestions() {{
      return questionsData.filter(q => {{
        if (state.filters.category !== 'all' && q.category !== state.filters.category) return false;
        if (state.filters.type !== 'all' && q.type !== state.filters.type) return false;
        
        const ans = state.userAnswers[q.id];
        if (state.filters.status === 'unanswered' && ans !== undefined) return false;
        if (state.filters.status === 'answered' && ans === undefined) return false;
        if (state.filters.status === 'correct' && (!ans || !ans.isCorrect)) return false;
        if (state.filters.status === 'incorrect' && (!ans || ans.isCorrect)) return false;
        if (state.filters.status === 'bookmarked' && !state.bookmarks.has(q.id)) return false;
        
        return true;
      }});
    }}

    function getCategoryBadgeClass(category) {{
      switch (category) {{
        case 'Git Distribuido': return 'badge-git';
        case 'Fundamentos de API': return 'badge-api';
        case 'Beneficios de REST': return 'badge-beneficios';
        case 'Restricciones RESTful': return 'badge-restricciones';
        case 'Recursos y URLs': return 'badge-recursos';
        case 'Verbos y Códigos de Estado': return 'badge-verbos';
        default: return 'bg-slate-600 text-white';
      }}
    }}

    function getTypeLabel(type) {{
      switch (type) {{
        case 'multiple_choice': return 'Múltiple Choice';
        case 'true_false': return 'Verdadero o Falso';
        case 'fill_in_the_blank': return 'Autocompletar';
        default: return type;
      }}
    }}

    // Renderizado de una sola tarjeta de pregunta
    function renderQuestionHTML(q) {{
      const userAns = state.userAnswers[q.id];
      const isAnswered = (userAns !== undefined);
      // Revelamos el feedback si estamos en modo estudio O si el examen ya terminó
      const revealFeedback = (state.mode === 'study' && isAnswered) || (state.mode === 'exam' && state.examFinished && isAnswered);
      const isMarked = state.bookmarks.has(q.id);

      let cardBorder = "border-slate-200 dark:border-slate-800";
      if (revealFeedback) {{
        cardBorder = userAns.isCorrect 
          ? "border-emerald-300 dark:border-emerald-800/80 ring-1 ring-emerald-500/20" 
          : "border-rose-300 dark:border-rose-800/80 ring-1 ring-rose-500/20";
      }} else if (isAnswered) {{
        cardBorder = "border-indigo-300 dark:border-indigo-800";
      }}

      let optionsHTML = '';

      if (q.type === 'multiple_choice' || q.type === 'true_false') {{
        optionsHTML = `
          <div class="space-y-2.5 pt-1">
            ${{q.options.map((opt, idx) => {{
              const letter = String.fromCharCode(65 + idx); // A, B, C, D
              let btnClasses = "w-full text-left p-3.5 rounded-xl border transition-all text-xs sm:text-sm flex items-start gap-3 relative ";
              let badgeClasses = "w-6 h-6 rounded-lg font-bold text-xs flex items-center justify-center shrink-0 transition-colors ";
              let checkIcon = "";

              if (revealFeedback) {{
                const isThisSelected = (userAns.answer === idx);
                const isThisCorrect = (idx === q.correct_answer);

                if (isThisCorrect) {{
                  btnClasses += "bg-emerald-50/90 dark:bg-emerald-950/40 border-emerald-500 text-emerald-900 dark:text-emerald-100 font-medium ";
                  badgeClasses += "bg-emerald-600 text-white ";
                  checkIcon = `<span class="ml-auto text-emerald-600 dark:text-emerald-400 font-bold text-xs flex items-center gap-1">✓ Correcta</span>`;
                }} else if (isThisSelected && !isThisCorrect) {{
                  btnClasses += "bg-rose-50/90 dark:bg-rose-950/40 border-rose-500 text-rose-900 dark:text-rose-100 line-through ";
                  badgeClasses += "bg-rose-600 text-white ";
                  checkIcon = `<span class="ml-auto text-rose-600 dark:text-rose-400 font-bold text-xs flex items-center gap-1">✗ Tu elección</span>`;
                }} else {{
                  btnClasses += "bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-800 text-slate-500 dark:text-slate-400 opacity-60 ";
                  badgeClasses += "bg-slate-100 dark:bg-slate-800 text-slate-400 ";
                }}
              }} else if (isAnswered && userAns.answer === idx) {{
                btnClasses += "bg-indigo-50 dark:bg-indigo-950/40 border-indigo-500 text-indigo-900 dark:text-indigo-100 font-semibold shadow-sm ";
                badgeClasses += "bg-indigo-600 text-white ";
                checkIcon = `<span class="ml-auto text-indigo-600 dark:text-indigo-400 font-bold text-xs">Seleccionada</span>`;
              }} else {{
                btnClasses += "bg-white dark:bg-slate-900 border-slate-200 dark:border-slate-800 hover:border-indigo-300 dark:hover:border-indigo-700 hover:bg-slate-50 dark:hover:bg-slate-800/50 text-slate-800 dark:text-slate-200 ";
                badgeClasses += "bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 group-hover:bg-indigo-100 ";
              }}

              return `
                <button onclick="selectOption(${{q.id}}, ${{idx}})" class="${{btnClasses}}">
                  <span class="${{badgeClasses}}">${{letter}}</span>
                  <span class="flex-1">${{opt.text}}</span>
                  ${{checkIcon}}
                </button>
              `;
            }}).join('')}}
          </div>
        `;
      }} else if (q.type === 'fill_in_the_blank') {{
        const currentValue = userAns ? userAns.answer : '';
        optionsHTML = `
          <div class="space-y-3 pt-1">
            <div class="flex flex-col sm:flex-row gap-2">
              <input type="text" id="blank-input-${{q.id}}" value="${{currentValue}}" placeholder="Escribe tu respuesta aquí..." 
                class="flex-1 px-4 py-2.5 rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 text-slate-900 dark:text-white text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500"
                ${{revealFeedback ? 'disabled' : ''}}
                onkeydown="if(event.key==='Enter') checkFillBlank(${{q.id}})"
              />
              <button onclick="checkFillBlank(${{q.id}})" class="px-5 py-2.5 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl text-xs font-bold transition shadow-sm" ${{revealFeedback ? 'disabled' : ''}}>
                ${{revealFeedback ? 'Comprobado' : 'Comprobar'}}
              </button>
            </div>
            ${{revealFeedback ? `
              <div class="p-3 rounded-xl ${{userAns.isCorrect ? 'bg-emerald-50 dark:bg-emerald-950/30 text-emerald-800 dark:text-emerald-200 border border-emerald-300 dark:border-emerald-800' : 'bg-rose-50 dark:bg-rose-950/30 text-rose-800 dark:text-rose-200 border border-rose-300 dark:border-rose-800'}} text-xs">
                ${{userAns.isCorrect ? '✓ ¡Excelente! Respuesta exacta.' : `✗ Respuesta esperada: <strong class="underline font-mono text-emerald-600 dark:text-emerald-400">${{q.correct_answer}}</strong> (Tu respuesta fue: "${{userAns.answer}}")`}}
              </div>
            ` : ''}}
          </div>
        `;
      }}

      // Sección de Definiciones y Explicación Detallada (Requisito clave del usuario)
      let explanationSection = '';
      if (revealFeedback) {{
        explanationSection = `
          <div class="mt-4 pt-4 border-t border-slate-200 dark:border-slate-800 space-y-3">
            <div class="bg-indigo-50/70 dark:bg-indigo-950/40 p-4 rounded-xl border border-indigo-100 dark:border-indigo-900/50 text-xs text-slate-800 dark:text-slate-200">
              <div class="font-bold text-indigo-700 dark:text-indigo-300 text-xs uppercase tracking-wide flex items-center gap-1.5 mb-1.5">
                <span>💡 Fundamento Teórico y Definición</span>
              </div>
              <p class="leading-relaxed text-slate-700 dark:text-slate-300">
                ${{q.explanation}}
              </p>
            </div>

            ${{q.options ? `
              <div class="bg-slate-50 dark:bg-slate-800/50 p-4 rounded-xl border border-slate-200 dark:border-slate-800 text-xs space-y-2">
                <div class="font-bold text-slate-600 dark:text-slate-400 uppercase tracking-wide text-[11px]">
                  🔍 Análisis y Definición de Cada Opción (Para el Examen):
                </div>
                <div class="space-y-1.5 pt-1">
                  ${{q.options.map((opt, idx) => {{
                    const letter = String.fromCharCode(65 + idx);
                    const isRight = (idx === q.correct_answer);
                    return `
                      <div class="p-2 rounded-lg ${{isRight ? 'bg-emerald-100/60 dark:bg-emerald-950/50 border border-emerald-300 dark:border-emerald-800 text-emerald-900 dark:text-emerald-100' : 'bg-white dark:bg-slate-900/80 border border-slate-200 dark:border-slate-800/80 text-slate-600 dark:text-slate-400'}}">
                        <span class="font-bold mr-1">${{letter}})</span>
                        <span class="${{isRight ? 'font-semibold text-emerald-700 dark:text-emerald-300' : ''}}">${{opt.definition}}</span>
                      </div>
                    `;
                  }}).join('')}}
                </div>
              </div>
            ` : ''}}
          </div>
        `;
      }}

      return `
        <article id="question-card-${{q.id}}" class="bg-white dark:bg-slate-900 rounded-2xl p-5 sm:p-6 border ${{cardBorder}} shadow-sm transition-all">
          <div class="flex items-center justify-between gap-2 mb-3">
            <div class="flex items-center gap-2 flex-wrap">
              <span class="text-xs font-black px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300">
                #${{q.id}}
              </span>
              <span class="text-[11px] font-bold px-2.5 py-0.5 rounded-full ${{getCategoryBadgeClass(q.category)}}">
                ${{q.category}}
              </span>
              <span class="text-[11px] text-slate-400 font-medium">
                ${{getTypeLabel(q.type)}}
              </span>
            </div>

            <button id="bookmark-btn-${{q.id}}" onclick="toggleBookmark(${{q.id}})" class="text-xs font-semibold px-2 py-1 rounded-lg hover:bg-slate-100 dark:hover:bg-slate-800 transition">
              ${{isMarked ? '<span class="text-amber-500 font-black">★ Guardada</span>' : '<span class="text-slate-400 hover:text-amber-500">☆ Marcar</span>'}}
            </button>
          </div>

          <h3 class="text-sm sm:text-base font-semibold text-slate-900 dark:text-white leading-snug mb-3">
            ${{q.question}}
          </h3>

          ${{optionsHTML}}

          ${{explanationSection}}
        </article>
      `;
    }}

    function renderQuestions() {{
      const container = document.getElementById('questions-container');
      const filtered = getFilteredQuestions();

      document.getElementById('filtered-count-text').textContent = `Mostrando ${{filtered.length}} de 80 preguntas`;

      if (filtered.length === 0) {{
        container.innerHTML = `
          <div class="bg-white dark:bg-slate-900 rounded-2xl p-12 text-center border border-slate-200 dark:border-slate-800">
            <div class="text-4xl mb-3">🔎</div>
            <h4 class="text-base font-bold text-slate-800 dark:text-slate-200">No hay preguntas que coincidan</h4>
            <p class="text-xs text-slate-500 mt-1">Prueba cambiando o limpiando los filtros de categoría o estado.</p>
            <button onclick="resetFilters()" class="mt-4 px-4 py-2 bg-indigo-600 text-white rounded-xl text-xs font-bold">Limpiar Filtros</button>
          </div>
        `;
        return;
      }}

      container.innerHTML = filtered.map(q => renderQuestionHTML(q)).join('');
    }}

    function renderSingleQuestion(qId) {{
      const q = questionsData.find(item => item.id === qId);
      if (!q) return;
      const el = document.getElementById(`question-card-${{qId}}`);
      if (el) {{
        el.outerHTML = renderQuestionHTML(q);
      }}
    }}

    function renderQuickGrid() {{
      const grid = document.getElementById('quick-jump-grid');
      grid.innerHTML = questionsData.map(q => {{
        const ans = state.userAnswers[q.id];
        const isMarked = state.bookmarks.has(q.id);
        const reveal = (state.mode === 'study' && ans !== undefined) || (state.mode === 'exam' && state.examFinished && ans !== undefined);

        let bg = "bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200";
        if (reveal) {{
          bg = ans.isCorrect 
            ? "bg-emerald-500 text-white font-bold" 
            : "bg-rose-500 text-white font-bold";
        }} else if (ans !== undefined) {{
          bg = "bg-indigo-600 text-white font-bold";
        }}

        let starIndicator = isMarked ? '<span class="absolute -top-1 -right-1 text-[9px] text-amber-400 font-black">★</span>' : '';

        return `
          <a href="#question-card-${{q.id}}" class="relative h-7 text-[11px] rounded-lg flex items-center justify-center transition-all ${{bg}}">
            ${{q.id}}
            ${{starIndicator}}
          </a>
        `;
      }}).join('');
    }}

    function updateStats() {{
      const total = 80;
      let answered = 0;
      let correct = 0;
      let incorrect = 0;
      const catStats = {{}};

      questionsData.forEach(q => {{
        if (!catStats[q.category]) catStats[q.category] = {{ total: 0, answered: 0, correct: 0 }};
        catStats[q.category].total++;

        const a = state.userAnswers[q.id];
        if (a !== undefined) {{
          answered++;
          catStats[q.category].answered++;
          if (a.isCorrect) {{
            correct++;
            catStats[q.category].correct++;
          }} else {{
            incorrect++;
          }}
        }}
      }});

      document.getElementById('answered-count-badge').textContent = `${{answered}} / ${{total}} respondidas`;
      document.getElementById('stat-correct').textContent = correct;
      document.getElementById('stat-incorrect').textContent = incorrect;

      const pct = answered > 0 ? Math.round((correct / answered) * 100) : 0;
      document.getElementById('stat-percentage').textContent = `${{pct}}%`;

      const progressBar = document.getElementById('top-progress-bar');
      progressBar.style.width = `${{(answered / total) * 100}}%`;

      // Diagnóstico textual
      const diagText = document.getElementById('diagnostic-text');
      const diagSub = document.getElementById('diagnostic-subtext');
      if (answered < 10) {{
        diagText.textContent = "Comenzando test...";
        diagSub.textContent = "Responde al menos 10 preguntas para un primer diagnóstico.";
      }} else if (pct >= 85) {{
        diagText.textContent = "¡Muy bien preparado! 🎉";
        diagText.className = "font-bold text-emerald-600 dark:text-emerald-400";
        diagSub.textContent = `Llevas un ${{pct}}% de aciertos. Mantén este ritmo y asegurarás la máxima nota.`;
      }} else if (pct >= 70) {{
        diagText.textContent = "Aprobado - Buen nivel 👍";
        diagText.className = "font-bold text-blue-600 dark:text-blue-400";
        diagSub.textContent = `Acierto del ${{pct}}%. Revisa las definiciones de los errores para el viernes.`;
      }} else {{
        diagText.textContent = "Requiere Refuerzo ⚠️";
        diagText.className = "font-bold text-rose-600 dark:text-rose-400";
        diagSub.textContent = `Acierto del ${{pct}}%. Lee con atención las definiciones teóricas de cada opción.`;
      }}

      // Progreso por categorías
      const catContainer = document.getElementById('category-progress-list');
      catContainer.innerHTML = Object.entries(catStats).map(([cat, val]) => {{
        const cPct = val.answered > 0 ? Math.round((val.correct / val.answered) * 100) : 0;
        let color = "bg-slate-300 dark:bg-slate-700";
        if (val.answered > 0) {{
          color = cPct >= 80 ? "bg-emerald-500" : (cPct >= 60 ? "bg-indigo-500" : "bg-rose-500");
        }}
        return `
          <div>
            <div class="flex justify-between text-[11px] mb-1">
              <span class="font-medium truncate max-w-[170px]" title="${{cat}}">${{cat}}</span>
              <span class="font-bold text-slate-500">${{val.correct}}/${{val.total}} (${{cPct}}%)</span>
            </div>
            <div class="w-full bg-slate-100 dark:bg-slate-800 rounded-full h-1.5 overflow-hidden">
              <div class="h-1.5 ${{color}} transition-all" style="width: ${{val.total > 0 ? (val.correct / val.total) * 100 : 0}}%"></div>
            </div>
          </div>
        `;
      }}).join('');
    }}

    function expandAllExplanations(open) {{
      // Si el usuario quiere forzar apertura o estamos en modo estudio
      if (state.mode !== 'study' && !state.examFinished) {{
        alert("En el 'Modo Examen', las respuestas y explicaciones se revelan al pulsar 'Entregar Examen'. Puedes cambiar al 'Modo Estudio' arriba si deseas verlas inmediatamente.");
        return;
      }}
      renderQuestions();
    }}

    function renderApp() {{
      setMode(state.mode);
      renderQuestions();
      renderQuickGrid();
      updateStats();
      if (state.examFinished) {{
        showExamResults();
      }}
    }}

    // Iniciar
    loadState();
    renderApp();
  </script>
</body>
</html>
"""

with open("/Users/jimy/.gemini/antigravity/scratch/simulador-examen-git-rest/index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("index.html generado exitosamente.")
