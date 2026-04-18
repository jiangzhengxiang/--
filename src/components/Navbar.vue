<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { useRouter } from 'vue-router';

const props = defineProps(['isDarkMode']);
const emit = defineEmits(['toggle-theme']);
const router = useRouter();

const isScrolled = ref(false);

const handleScroll = () => {
  isScrolled.value = window.scrollY > 20;
};

onMounted(() => {
  window.addEventListener('scroll', handleScroll);
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
});

const navigateTo = (tabId) => {
  router.push({ path: '/dashboard', query: { tab: tabId } });
};
</script>

<template>
  <nav 
    class="fixed top-0 left-0 right-0 z-50 transition-all duration-500"
    :class="[isScrolled ? 'py-4 bg-white/80 dark:bg-slate-950/80 backdrop-blur-xl border-b border-slate-200/60 dark:border-slate-800 shadow-sm' : 'py-6 bg-transparent']"
  >
    <div class="container px-6 mx-auto max-w-7xl flex items-center justify-between">
      <!-- Logo -->
      <router-link to="/" class="flex items-center gap-2 group">
        <div class="w-10 h-10 bg-emerald-600 rounded-xl flex items-center justify-center text-white shadow-lg shadow-emerald-600/20 group-hover:rotate-12 transition-transform duration-500">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2.5" stroke="currentColor" class="w-6 h-6">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 22V12m0 0l-5 5m5-5l5 5M12 12l-4-4m4 4l4-4M12 7V2" />
          </svg>
        </div>
        <span class="text-xl font-serif font-bold tracking-tighter dark:text-white">今日<span class="text-emerald-600 italic">无事</span></span>
      </router-link>

      <!-- PC Nav -->
      <div class="hidden md:flex items-center gap-10">
        <router-link to="/" class="text-sm font-bold text-slate-500 hover:text-emerald-600 transition-colors uppercase tracking-widest">首页</router-link>
        <button @click="navigateTo('llm')" class="text-sm font-bold text-slate-500 hover:text-emerald-600 transition-colors uppercase tracking-widest">大模型</button>
        <button @click="navigateTo('kb')" class="text-sm font-bold text-slate-500 hover:text-emerald-600 transition-colors uppercase tracking-widest">知识库</button>
        
        <div class="w-px h-4 bg-slate-200 dark:bg-slate-800"></div>
        
        <!-- Theme Toggle -->
        <button @click="emit('toggle-theme')" class="p-2 text-slate-400 hover:text-emerald-600 transition-colors">
          <svg v-if="isDarkMode" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2.25m6.364.386-1.591 1.591M21 12h-2.25m-.386 6.364-1.591-1.591M12 18.75V21m-4.773-4.227-1.591 1.591M3 12h2.25m.386-6.364 1.591-1.591M16.5 12a4.5 4.5 0 1 1-9 0 4.5 4.5 0 0 1 9 0Z" />
          </svg>
          <svg v-else xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21.752 15.002A9.72 9.72 0 0 1 18 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 0 0 3 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 0 0 9.002-5.998Z" />
          </svg>
        </button>

        <button 
          @click="navigateTo('release')"
          class="px-8 py-3 bg-emerald-600 text-white rounded-2xl text-xs font-bold hover:bg-emerald-700 transition-all shadow-xl shadow-emerald-600/20 active:scale-95"
        >
          立刻开始
        </button>
      </div>

      <!-- Mobile Menu Toggle -->
      <button class="md:hidden p-2 text-slate-600 dark:text-slate-300">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
          <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 9h16.5m-16.5 6.75h16.5" />
        </svg>
      </button>
    </div>
  </nav>
</template>
