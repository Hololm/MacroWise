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
  <div class="page-container">
  <div class="image-side"></div>
  <div class="divider"></div>
  <div class="content-side">
  <div class="card-container">
    <div class="card">
      <div class="header-container">
      <p class="text-4xl text-center pb-2">Welcome to MacroWise</p>
      <p class="text-xl text-center mb-6">Just a few more details and you're set.</p>
      <div class="border-b mb-8"></div>
      </div>
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
            <span class="error-text" :class="{ 'error-visible': errors.last }">
      {{ errors.last || 'placeholder' }}
    </span>
          </div>
        </div>

        <div class="input-row">
          <div class="form-group">
            <label for="height">Height (in.)</label>
            <input
              id="height"
              v-model.number="formData.height"
              type="number"
            >
                        <span class="error-text" :class="{ 'error-visible': errors.height }">
      {{ errors.height || 'placeholder' }}</span>
          </div>
          <div class="form-group">
            <label for="weight">Weight (lbs.)</label>
            <input
              id="weight"
              v-model.number="formData.weight"
              type="number"
            >
            <span class="error-text" :class="{ 'error-visible': errors.weight }">
      {{ errors.weight || 'placeholder' }}
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
            <span class="error-text" :class="{ 'error-visible': errors.age }">
      {{ errors.age || 'placeholder' }}
    </span>
          </div>
          <div class="form-group">
            <label for="gender">Gender</label>
            <select id="gender" v-model="formData.gender">
              <option value="Male">Male</option>
              <option value="Female">Female</option>
            </select>
            <span class="error-text" :class="{ 'error-visible': errors.gender }">
      {{ errors.gender || 'placeholder' }}
    </span>
          </div>
        </div>

        <button type="submit">Next</button>
      </form>
    </div>
  </div>
  </div>
  </div>
</template>

<style scoped>

.card-container {
}

.header-container {
  font-family: "Gilroy Bold", sans-serif;
  color: #191753FF;
}

.page-container {
  display: flex;
  min-height: 100vh;
  width: 100%;
  background-color: #f8f8f8;
}

.image-side {
  flex: 0.76;
  background: url('https://d327mhnbii227g.cloudfront.net/images/left-banner.jpg') no-repeat center center;
  background-size: cover;
}

.divider {
  width: 2px;
  height: 100vh;
}

.content-side {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 2rem;
}

.card {
  width: 100%;
  max-width: 900px;
  background: #ffffff;
  padding: clamp(1rem, 3vw, 2rem);
  border-radius: 16px;
  box-shadow: 0 3px 5px rgba(0, 0, 0, 0.03);
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
  font-family: "Gilroy Medium", sans-serif;
}

.error-text {
  color: #dc2626;
  font-size: 0.75rem;
  opacity: 0;
  visibility: hidden;
  height: 1rem;
  display: block;
  font-family: "Gilroy Regular", sans-serif;
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
  border-bottom: #325694 2px solid;
  width: 100%;
  background-color: #fcfcfc;
}

input:hover, select:hover {
  border-bottom: #7393B3 2px solid;
}

input:focus, select:focus {
  outline: none;
}

button {
  padding: 8px 16px;
  color: #ffffff;
  background-color: #5b9de1;
  border: 2px solid #f3f4f6;
  border-radius: 16px;
  cursor: pointer;
  margin-top: 1rem;
  box-shadow: 0 3px 5px rgba(0, 0, 0, 0.03);
  max-width: 100px;
  font-family: "Gilroy Bold", sans-serif;
  transition: all 0.15s ease;
}

button:hover {
  background-color: #325694;
  transition: background-color 0.15s ease;
}

input::-webkit-outer-spin-button,
      input::-webkit-inner-spin-button {
         -webkit-appearance: none;
      }
</style>