<script setup>
import { ref, onMounted } from 'vue';
import Navbar from '../components/Navbar.vue';
import Hero from '../components/Hero.vue';
import AppPreview from '../components/AppPreview.vue';

const props = defineProps(['isDarkMode']);
const emit = defineEmits(['toggle-theme']);

const toggleTheme = () => {
  emit('toggle-theme');
};
</script>

<template>
  <div class="relative pt-32 pb-20 md:pt-48">
    <Hero />
    <AppPreview />
  </div>
</template>
