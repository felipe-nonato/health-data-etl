<script setup>
import Search from './components/Search.vue'
import { ref, computed, onMounted, onUnmounted } from 'vue'



const windowWidth = ref(window.innerWidth);

function updateWindowWidth() {
  windowWidth.value = window.innerWidth;
}

onMounted(() => {
  window.addEventListener('resize', updateWindowWidth);
});

onUnmounted(() => {
  window.removeEventListener('resize', updateWindowWidth);
});
import axios from 'axios'

const searchResults = ref([]) // Inicializado como array vazio
const currentPage = ref(1)
let resultsPerPage = 4

// Computed para calcular os resultados da página atual
const paginatedResults = computed(() => {
  if (!Array.isArray(searchResults.value)) {
    return []; // Garante que sempre retornamos um array
  }
  const start = (currentPage.value - 1) * resultsPerPage;
  const end = start + resultsPerPage;
  return searchResults.value.slice(start, end);
});

// Computed para verificar se é dispositivo móvel
const isMobile = computed(() => windowWidth.value <= 768);

async function fetchSearchResults(query) {
  try {
    const response = await axios.get(`https://etl-api.felipenonato.com/operadoras?query=${encodeURIComponent(query)}`);

    // Manipula diretamente o JSON retornado
    if (Array.isArray(response.data)) {
      searchResults.value = response.data.map(item => ({
        ...item,
        complemento: item.complemento || 'N/A',
        ddd: item.ddd || 'N/A',
        telefone: item.telefone || 'N/A',
        fax: item.fax || 'N/A'
      }));
    } else {
      console.error('Response data is not an array:', response.data);
      searchResults.value = []; // Garante que searchResults seja um array vazio
    }

    currentPage.value = 1; // Reseta para a primeira página ao buscar novos resultados
  } catch (error) {
    console.error('Error fetching search results:', error);
    searchResults.value = []; // Garante que searchResults seja um array vazio em caso de erro
  }
}

// Funções para navegação entre páginas
function nextPage() {
  if (currentPage.value * resultsPerPage < searchResults.value.length) {
    currentPage.value++
  }
}

function previousPage() {
  if (currentPage.value > 1) {
    currentPage.value--
  }
}
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="100" height="100" />
    <div class="links">
      <a target="_blank" href="https://github.com/felipe-nonato/health-data-etl">Github</a>
      <a target="_blank" href="https://www.linkedin.com/in/lu%C3%ADs-felipe-nonato-840400203/">Linkedin</a>
    </div>
  </header>

  <main>
    <Search @input="fetchSearchResults($event.target.value)" />
    <div class="table-container">
      <!-- Layout para dispositivos móveis -->
      <div v-if="isMobile && paginatedResults.length" class="mobile-results">
        <div v-for="result in paginatedResults" :key="result.registro_ans" class="mobile-result">
          <div v-for="(value, key) in result" :key="key" class="mobile-row">
            <strong>{{ key }}:</strong> <span>{{ value }}</span>
          </div>
        </div>
      </div>

      <!-- Layout para dispositivos maiores -->
      <table v-else-if="Array.isArray(paginatedResults) && paginatedResults.length" class="results-table">
        <thead>
          <tr>
            <th>Registro ANS</th>
            <th>CNPJ</th>
            <th>Razão Social</th>
            <th>Nome Fantasia</th>
            <th>Modalidade</th>
            <th>Logradouro</th>
            <th>Número</th>
            <th>Complemento</th>
            <th>Bairro</th>
            <th>Cidade</th>
            <th>UF</th>
            <th>CEP</th>
            <th>DDD</th>
            <th>Telefone</th>
            <th>Fax</th>
            <th>Endereço Eletrônico</th>
            <th>Representante</th>
            <th>Cargo Representante</th>
            <th>Região de Comercialização</th>
            <th>Data Registro ANS</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="result in paginatedResults" :key="result.registro_ans">
            <td>{{ result.registro_ans }}</td>
            <td>{{ result.cnpj }}</td>
            <td>{{ result.razao_social }}</td>
            <td>{{ result.nome_fantasia }}</td>
            <td>{{ result.modalidade }}</td>
            <td>{{ result.logradouro }}</td>
            <td>{{ result.numero }}</td>
            <td>{{ result.complemento }}</td>
            <td>{{ result.bairro }}</td>
            <td>{{ result.cidade }}</td>
            <td>{{ result.uf }}</td>
            <td>{{ result.cep }}</td>
            <td>{{ result.ddd }}</td>
            <td>{{ result.telefone }}</td>
            <td>{{ result.fax }}</td>
            <td>{{ result.endereco_eletronico }}</td>
            <td>{{ result.representante }}</td>
            <td>{{ result.cargo_representante }}</td>
            <td>{{ result.regiao_de_comercializacao }}</td>
            <td>{{ result.data_registro_ans }}</td>
          </tr>
        </tbody>
      </table>
      <p v-else>Nenhum resultado encontrado.</p>
    </div>

    <!-- Botões de paginação fora do scroll -->
    <div v-if="searchResults.length" class="pagination">
      <button @click="previousPage" :disabled="currentPage === 1">Anterior</button>
      <span>Página {{ currentPage }}</span>
      <button @click="nextPage" :disabled="currentPage * resultsPerPage >= searchResults.length">Próxima</button>
    </div>
  </main>

  <footer>
    <hr />
    <div style="display: flex; justify-content: space-between;margin-top: 15px;">
      <p>Health Data ETL</p>
      <p v-if="windowWidth > 768">Um projeto de ETL para dados de saúde.</p>
    </div>

    <div style="display: flex; justify-content: space-between;">
      <p>Desenvolvido por Luís Felipe Nonato</p>
      <p v-if="windowWidth > 768">2025</p>
    </div>
  </footer>
</template>

<style scoped>
/* Garante que a página inteira permaneça fixa */
body {
  margin: 0;
  padding: 0;
}

main {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  flex-grow: 1;
  /* Permite que o conteúdo principal ocupe o espaço disponível */
}

.table-container {
  max-width: 100%;
  overflow-x: auto;
  /* Permite rolagem horizontal apenas na tabela */
  margin: 1rem 0;
}

.results-table {
  color: black;
  width: 100%;
  border-collapse: collapse;
}

.results-table th,
.results-table td {
  border: 1px solid #ccc;
  padding: 0.5rem;
  text-align: left;
}

.results-table th {
  background-color: #f9f9f9;
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 1rem;
  gap: 1rem;
}

.pagination button {
  padding: 0.5rem 1rem;
  border: 1px solid #ccc;
  background-color: #f9f9f9;
  cursor: pointer;
}

.pagination button:disabled {
  background-color: #e0e0e0;
  cursor: not-allowed;
}

header {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  line-height: 1.5;
  flex-wrap: wrap;
}

.links {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.logo {
  display: block;
  margin: 0 2rem;
}

footer {
  width: 100%;
  color: gray;
  margin-top: auto;
  /* Garante que o footer fique no final da página */
  text-align: center;
}

footer hr {
  margin: 2px 0;
}

/* Estilos para dispositivos móveis */
@media (max-width: 768px) {
  header {
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .table-container {
    margin: 0.5rem;
  }

  .results-table th,
  .results-table td {
    font-size: 0.8rem;
    padding: 0.3rem;
  }

  .pagination {
    flex-direction: column;
    gap: 0.5rem;
  }

  .pagination button {
    width: 100%;
    padding: 0.5rem;
  }

  footer {
    font-size: 0.8rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    bottom: 2px;
  }
}

@media (max-width: 480px) {

  .results-table th,
  .results-table td {
    font-size: 0.7rem;
    padding: 0.2rem;
  }

  .pagination button {
    font-size: 0.8rem;
    padding: 0.4rem;
  }

  .links a {
    font-size: 0.9rem;
  }
}

.mobile-results {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.mobile-result {
  border: 1px solid #ccc;
  border-radius: 0.375rem;
  padding: 1rem;
  background-color: #f9f9f9;
}

.mobile-row {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}

.mobile-row strong {
  font-weight: bold;
}
</style>
