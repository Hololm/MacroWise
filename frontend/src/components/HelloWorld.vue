<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

const message = ref('not loaded yet..a.') // sets the message to not loaded yet while waiting for the response

onMounted(async () => { // when the component is mounted
  try {
    const response = await axios.get('http://localhost:8000/') // gets data from fastapi port 8000
    message.value = response.data.message // sets the message to the response data
  } catch (error) {
    console.error(error)
  }
})
</script>

<template>
  <div>
    <h1>{{ message }}</h1>
  </div>
</template>

<style scoped>
</style>