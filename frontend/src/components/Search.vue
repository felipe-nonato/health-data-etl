<script setup>
import IconSearch from './icons/IconSearch.vue'
</script>

<template>
  <div class="search-bar">
    <IconSearch class="icon" />
    <input type="text" placeholder="Pesquise por nome, cidade ou estado..." />
  </div>
</template>

<style scoped>
.icon {
  width: 2rem;
  height: 2rem;
  margin-right: 1rem;
}

.search-bar {
  border: 1px solid #ccc;
  border-radius: 0.375rem;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 0.5rem;
  width: 30vw;
}

.search-bar input {
  all: unset;
  width: 100%;
  padding: 0.5rem 2rem;
  font-size: 1rem;
}

@media (max-width: 768px) {
  .search-bar {
    width: 90vw;
  }
}
</style>