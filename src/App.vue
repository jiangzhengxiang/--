<script setup>
import { ref, onMounted } from 'vue';
import Navbar from './components/Navbar.vue';

const isDarkMode = ref(false);

const toggleTheme = () => {
  isDarkMode.value = !isDarkMode.value;
  updateTheme();
};

const updateTheme = () => {
  if (isDarkMode.value) {
    document.documentElement.classList.add('dark');
    localStorage.setItem('theme', 'dark');
  } else {
    document.documentElement.classList.remove('dark');
    localStorage.setItem('theme', 'light');
  }
};

onMounted(() => {
  const saved = localStorage.getItem('theme');
  if (saved === 'dark' || (!saved && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    isDarkMode.value = true;
    updateTheme();
  }
});
</script>

<template>
  <div class="min-h-screen transition-colors duration-1000 bg-[#fdfbf7] dark:bg-slate-950 text-slate-800 dark:text-slate-100 font-sans selection:bg-emerald-100">
    <!-- 背景装饰：柔和的呼吸圆球 -->
    <div class="fixed inset-0 overflow-hidden pointer-events-none">
      <div class="absolute -top-[10%] -left-[10%] w-[40%] h-[40%] bg-emerald-100/40 dark:bg-emerald-900/10 rounded-full blur-[120px] animate-pulse"></div>
      <div class="absolute top-[20%] -right-[5%] w-[30%] h-[30%] bg-orange-100/30 dark:bg-orange-900/10 rounded-full blur-[100px]" style="animation: float 20s infinite"></div>
    </div>

    <Navbar :isDarkMode="isDarkMode" @toggle-theme="toggleTheme" />

    <router-view :isDarkMode="isDarkMode" @toggle-theme="toggleTheme"></router-view>

    <footer class="py-16 border-t border-slate-200/60 dark:border-slate-800">
      <div class="container px-6 mx-auto text-center max-w-7xl opacity-40 text-sm tracking-widest font-light">
        &copy; 2026 今日无事 (NO AFFAIRS). Breathe in, breathe out.
      </div>
    </footer>
  </div>
</template>

<style>
@keyframes float {
  0%, 100% { transform: translate(0, 0); }
  50% { transform: translate(-20px, 30px); }
}
</style>
