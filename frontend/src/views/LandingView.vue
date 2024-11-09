<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'

const formData = ref({
  name: '',
  height: '',
  weight: '',
  age: '',
  gender: ''
})

const result = ref(null)

async function calculateBMI() {
  try {
    const response = await axios.post('http://localhost:8000/login', formData.value)
    result.value = response.data
  } catch (error) {
    console.error('Error calculating BMI:', error)
    alert('Error calculating BMI')
  }
}

</script>

<template>
  <div class="m-auto max-w-screen-sm p-2">
    <form @submit.prevent="calculateBMI" class="form">
      <div class="form-group">
        <label for="name">Name:</label>
        <input
          id="name"
          v-model="formData.name"
          type="text"
        >
      </div>

      <div class="form-group">
        <label for="height">Height (inches):</label>
        <input
          id="height"
          v-model.number="formData.height"
          type="number"
        >
      </div>

      <div class="form-group">
        <label for="weight">Weight (lbs):</label>
        <input
          id="weight"
          v-model.number="formData.weight"
          type="number"
        >
      </div>

      <div class="form-group">
        <label for="age">Age:</label>
        <input
          id="age"
          v-model.number="formData.age"
          type="number"
        >
      </div>

      <div class="form-group">
        <label for="gender">Gender:</label>
        <select id="gender" v-model="formData.gender" required>
          <option value="Male">Male</option>
          <option value="Female">Female</option>
        </select>
      </div>

      <button type="submit">Calculate BMI</button>
    </form>

    <div v-if="result" class="result">
      <h3>Results for {{ result.name }}</h3>
      <p><strong>BMI:</strong> {{ result.bmi }}</p>
      <p><strong>Body Fat Percentage:</strong> {{ result.body_fat_percentage }}%</p>
    </div>
  </div>
</template>

<style scoped>

</style>