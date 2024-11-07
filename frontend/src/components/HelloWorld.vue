<script setup lang="ts">
import { ref, onMounted } from 'vue'
import axios from 'axios'

const message = ref('not loaded yet..a.') // sets the message to not loaded yet while waiting for the response
const message_2 = ref('ok')

onMounted(async () => { // when the component is mounted
  try {
    const response = await axios.get('http://localhost:8000/') // gets data from fastapi port 8000
    message.value = response.data.message['message_1'] // sets the message to the response data
    message_2.value = response.data.message['message_2']

  } catch (error) {
    console.error(error)
  }
})
</script>

<template>
  <div>
    <h1>{{ message }}</h1>
    <h1> {{message_2}}</h1>
  </div>
</template>

<style scoped>
</style>