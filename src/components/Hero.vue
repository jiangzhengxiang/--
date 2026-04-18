<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

const navigateTo = (tabId) => {
  router.push({ path: '/dashboard', query: { tab: tabId } });
};
</script>

<template>
  <div class="container px-6 mx-auto max-w-7xl">
    <div class="flex flex-col lg:flex-row items-center justify-between gap-12 min-h-[60vh] pt-12">
      
      <!-- 左侧内容区 -->
      <div class="lg:w-3/5 space-y-12">
        <div>
          <span class="inline-block px-3 py-1 bg-emerald-50 dark:bg-emerald-900/20 text-emerald-600 text-[10px] font-bold uppercase tracking-[0.2em] rounded-lg mb-8">自在 (Freedom)</span>
          <h1 class="text-4xl md:text-6xl font-serif font-light tracking-tighter text-slate-800 dark:text-white leading-[1.1]">
            通过彻底的释放<br/>
            让情绪像水一般<br/>
            <span class="text-emerald-600 italic">随境而生 自然流动</span>
          </h1>
        </div>

        <div class="max-w-md space-y-4 opacity-70">
          <p class="text-base text-slate-500 dark:text-slate-400 font-light leading-relaxed">
            情绪之所以抓着你不放 是因为你潜意识里在抓它
          </p>
          <p class="text-base text-slate-500 dark:text-slate-400 font-light leading-relaxed">
            当你不再试图拥有 控制 或排斥某种情绪时 它自然就会流走
          </p>
        </div>

        <!-- 主操作按钮 -->
        <div class="flex items-center gap-6 pt-4">
          <button 
            @click="navigateTo('release')"
            class="px-12 py-4 bg-emerald-800 hover:bg-emerald-900 text-white rounded-full text-base font-bold transition-all active:scale-95 shadow-2xl shadow-emerald-900/20"
          >
            开始探索 →
          </button>
          <button 
            @click="navigateTo('kb')"
            class="px-10 py-4 bg-white dark:bg-slate-900 text-slate-400 border border-slate-200 dark:border-slate-800 rounded-full text-base font-medium hover:border-emerald-600 hover:text-emerald-600 transition-all active:scale-95"
          >
            浏览知识库
          </button>
        </div>
      </div>

      <!-- 右侧装饰排版（纵向文字） -->
      <div class="hidden lg:flex items-start gap-12 select-none opacity-80">
        <div class="text-4xl md:text-5xl font-serif font-light text-slate-800 dark:text-white [writing-mode:vertical-rl] tracking-[0.5em] pt-24">
          故能胜物而不伤
        </div>
        <div class="text-4xl md:text-5xl font-serif font-light text-slate-400 dark:text-slate-600 [writing-mode:vertical-rl] tracking-[0.5em] pt-12">
          应而不藏
        </div>
        <div class="text-4xl md:text-5xl font-serif font-light text-slate-400 dark:text-slate-600 [writing-mode:vertical-rl] tracking-[0.5em]">
          不将不迎
        </div>
        <div class="text-4xl md:text-5xl font-serif font-light text-slate-800 dark:text-white [writing-mode:vertical-rl] tracking-[0.5em] pt-8 border-l-2 border-emerald-100 dark:border-emerald-900/30 pl-12">
          用心若镜
        </div>
      </div>

    </div>
  </div>
</template>

<style scoped>
.container {
  animation: fade-in 1.5s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes fade-in {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
