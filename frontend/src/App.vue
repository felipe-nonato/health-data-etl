<script setup>
import Search from './components/Search.vue'
import { ref, computed } from 'vue'
import axios from 'axios'

const searchResults = ref([]) // Inicializado como array vazio
const currentPage = ref(1)
const resultsPerPage = 3

// Computed para calcular os resultados da página atual
const paginatedResults = computed(() => {
  if (!Array.isArray(searchResults.value)) {
    return []; // Garante que sempre retornamos um array
  }
  const start = (currentPage.value - 1) * resultsPerPage;
  const end = start + resultsPerPage;
  return searchResults.value.slice(start, end);
});

async function fetchSearchResults(query) {
  try {
    const response = await axios.get(`https://etl-api.felipenonato.com:5000/operadoras?query=${encodeURIComponent(query)}`);

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
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />
    <div class="links">
      <a target="_blank" href="https://github.com/felipe-nonato/health-data-etl">Github</a>
      <a target="_blank" href="https://www.linkedin.com/in/lu%C3%ADs-felipe-nonato-840400203/">Linkedin</a>
    </div>
  </header>

  <main>
    <Search @input="fetchSearchResults($event.target.value)" />
    <div class="table-container">
      <table v-if="Array.isArray(paginatedResults) && paginatedResults.length" class="results-table">
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

    <!-- Botões de paginação -->
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
      <p>Um projeto de ETL para dados de saúde.</p>
    </div>

    <div style="display: flex; justify-content: space-between;">
      <p>Desenvolvido por Luís Felipe Nonato</p>
      <p>2025</p>
    </div>
  </footer>
</template>

<style scoped>
/* Garante que a página inteira permaneça fixa */
body {
  overflow: hidden;
  /* Impede rolagem da página */
}

main {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}


.table-container {
  max-width: 100%;
  overflow-x: auto;
  /* Permite rolagem horizontal apenas na tabela */
  margin: 1rem;
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
  line-height: 1.5;
}

.links {
  display: flex;
  gap: 1rem;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

footer {
  width: 100%;
  color: gray;
}

footer hr {
  margin: 2px 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
