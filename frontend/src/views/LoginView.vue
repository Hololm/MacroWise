<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'

const formData = ref({
  name: '',
  first: '',
  last: '',
  height: '',
  weight: '',
  age: '',
  gender: '',
})

const errors = ref({
  first: '',
  last: '',
  height: '',
  weight: '',
  age: '',
  gender: ''
})

const result = ref(null)

function validateForm() {
  let isValid = true

  // Reset all errors
  Object.keys(errors.value).forEach(key => errors.value[key] = '')

  // Validate each field
  if (!formData.value.first.trim()) {
    errors.value.first = 'Please enter your first name'
    isValid = false
  }

  if (!formData.value.last.trim()) {
    errors.value.last = 'Please enter your last name'
    isValid = false
  }

  if (!formData.value.height) {
    errors.value.height = 'Please enter your height'
    isValid = false
  }

  if (!formData.value.weight) {
    errors.value.weight = 'Please enter your weight'
    isValid = false
  }

  if (!formData.value.age) {
    errors.value.age = 'Please enter your age'
    isValid = false
  }

  if (!formData.value.gender) {
    errors.value.gender = 'Please select your gender'
    isValid = false
  }

  return isValid
}

async function calculateBMI() {
  if (!validateForm()) return

  try {
    const response = await axios.post('http://localhost:8000/login', formData.value)
    result.value = response.data
  } catch (error) {
    console.error('Error calculating BMI:', error)
  }
}
</script>

<template>
  <div class="card-container">
    <div class="card">
      <p class="text-4xl text-left pb-2">Let's Get Aligned With Your Goals</p>
      <p class="text-2xl text-left mb-6">It won't take more than a couple of seconds.</p>
      <div class="border-b mb-8"></div>
      <form @submit.prevent="calculateBMI" class="form">
        <div class="input-row">
          <div class="form-group">
            <label for="firstName">First Name</label>
            <input
              id="firstName"
              v-model="formData.first"
              type="text"
              class="border-2"
            >
            <span class="error-text" :class="{ 'error-visible': errors.first }">
      {{ errors.first || 'placeholder' }}
    </span>
          </div>
          <div class="form-group">
            <label for="lastName">Last Name</label>
            <input
              id="lastName"
              v-model="formData.last"
              type="text"
              class="border-2"
            >
            <span class="error-text" :class="{ 'error-visible': errors.first }">
      {{ errors.first || 'placeholder' }}
    </span>
          </div>
        </div>

        <div class="input-row">
          <div class="form-group">
            <label for="height">Height (inches)</label>
            <input
              id="height"
              v-model.number="formData.height"
              type="number"
            >
            <span class="error-text" v-if="errors.height">{{ errors.height }}</span>
          </div>
          <div class="form-group">
            <label for="weight">Weight (lbs)</label>
            <input
              id="weight"
              v-model.number="formData.weight"
              type="number"
            >
            <span class="error-text" :class="{ 'error-visible': errors.first }">
      {{ errors.first || 'placeholder' }}
    </span>
          </div>
        </div>

        <div class="input-row">
          <div class="form-group">
            <label for="age">Age</label>
            <input
              id="age"
              v-model.number="formData.age"
              type="number"
            >
            <span class="error-text" :class="{ 'error-visible': errors.first }">
      {{ errors.first || 'placeholder' }}
    </span>
          </div>
          <div class="form-group">
            <label for="gender">Gender</label>
            <select id="gender" v-model="formData.gender">
              <option value="Male">Male</option>
              <option value="Female">Female</option>
            </select>
            <span class="error-text" :class="{ 'error-visible': errors.first }">
      {{ errors.first || 'placeholder' }}
    </span>
          </div>
        </div>

        <button type="submit">Next</button>
      </form>
    </div>
  </div>
</template>

<style scoped>
.card-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: clamp(1rem, 5vw, 2rem);
}

.card {
  width: 100%;
  max-width: clamp(300px, 90%, 600px);
  background: #ffffff;
  padding: clamp(1rem, 3vw, 2rem);
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.input-wrapper {
  position: relative;
}

.input-row {
  display: flex;
  gap: 1rem;
}

.error-text {
  color: #dc2626;
  font-size: 0.75rem;
  opacity: 0;
  visibility: hidden;
  height: 1rem;
  display: block;
}

.error-visible {
  opacity: 1;
  visibility: visible;
}

/* Remove the min-height from form-group if you had added it */
.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  flex: 1;
}

select {
  cursor: pointer;
}

input, select {
  padding: 0.5rem;
  border: none;
  border-bottom: #5d1cda 2px solid;
  width: 100%;
  background-color: #fafafa;
}

input:hover, select:hover {
  border-bottom: #a783f1 2px solid;
}

button {
  padding: 8px 16px;
  color: #ffffff;
  background-color: #5d1cda;
  border: 2px solid #f3f4f6;
  border-radius: 16px;
  cursor: pointer;
  margin-top: 1rem;
  box-shadow: 0 3px 5px rgba(0, 0, 0, 0.03);
  max-width: 100px;
}

button:hover {
}

input::-webkit-outer-spin-button,
      input::-webkit-inner-spin-button {
         -webkit-appearance: none;
      }
</style>