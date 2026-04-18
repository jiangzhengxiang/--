<script setup>
import { ref, computed } from 'vue';
import releaseLogic from '../release-logic.json';

const currentNodeId = ref(releaseLogic.startNode || 'node_1');
const history = ref([]);

const currentNode = computed(() => {
  const node = releaseLogic.nodes[currentNodeId.value];
  return {
    id: currentNodeId.value,
    text: node?.text || '流程结束',
    isEnd: node?.isEnd || false
  };
});

// 计算进度
const progress = computed(() => {
  const totalNodes = Object.keys(releaseLogic.nodes).length;
  const visited = new Set(history.value).size + 1;
  return Math.min(Math.round((visited / 15) * 100), 100);
});

const options = computed(() => {
  const node = releaseLogic.nodes[currentNodeId.value];
  if (!node || node.isEnd) return [];
  
  const res = [];
  if (node.yes) res.push({ label: '是 (Yes)', nextId: node.yes, type: 'yes' });
  if (node.no) res.push({ label: '否 (No)', nextId: node.no, type: 'no' });
  if (node.next) res.push({ label: '继续', nextId: node.next, type: 'next' });
  
  return res;
});

const handleNavigate = (nextId) => {
  history.value.push(currentNodeId.value);
  currentNodeId.value = nextId;
};

const reset = () => {
  currentNodeId.value = releaseLogic.startNode || 'node_1';
  history.value = [];
};

const goBack = () => {
  if (history.value.length > 0) {
    currentNodeId.value = history.value.pop();
  }
};
</script>

<template>
  <div class="max-w-4xl mx-auto py-12 px-6">
    <div class="relative group">
      <!-- 背景光晕 -->
      <div class="absolute -inset-1 bg-gradient-to-r from-emerald-100/30 to-indigo-100/30 dark:from-emerald-900/10 dark:to-indigo-900/10 rounded-[4rem] blur-2xl opacity-50 group-hover:opacity-100 transition duration-1000"></div>

      <!-- 主卡片 -->
      <div class="relative bg-white/70 dark:bg-slate-900/70 backdrop-blur-3xl border border-white/50 dark:border-slate-800/50 shadow-[0_32px_64px_-16px_rgba(0,0,0,0.08)] rounded-[3.5rem] p-10 md:p-20 min-h-[600px] flex flex-col items-center justify-between overflow-hidden">
        
        <div class="absolute inset-0 opacity-[0.03] dark:opacity-[0.05] pointer-events-none bg-[url('https://grainy-gradients.vercel.app/noise.svg')]"></div>

        <!-- 顶部 -->
        <div class="w-full flex justify-between items-center z-10">
          <div class="flex flex-col gap-2">
            <div class="flex items-center gap-2">
              <div class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></div>
              <span class="text-[10px] font-bold tracking-[0.3em] uppercase text-slate-400 dark:text-slate-500">Mindfulness Guidance</span>
            </div>
            <div class="w-32 h-1 bg-slate-100 dark:bg-slate-800 rounded-full overflow-hidden">
              <div class="h-full bg-gradient-to-r from-emerald-400 to-indigo-500 transition-all duration-1000" :style="{ width: progress + '%' }"></div>
            </div>
          </div>

          <div class="flex items-center gap-2">
            <button @click="reset" class="p-3 text-slate-300 hover:text-indigo-500 hover:bg-white dark:hover:bg-slate-800 rounded-2xl transition-all active:scale-90">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M16.023 9.348h4.992v-.001M2.985 19.644v-4.992m0 0h4.992m-4.993 0 3.181 3.183a8.25 8.25 0 0 0 13.803-3.7M4.031 9.865a8.25 8.25 0 0 1 13.803-3.7l3.181 3.182m0-4.991v4.99" />
              </svg>
            </button>
            <button :disabled="history.length === 0" @click="goBack" :class="[history.length === 0 ? 'opacity-10' : 'hover:text-indigo-500 hover:bg-white dark:hover:bg-slate-800']" class="p-3 text-slate-300 rounded-2xl transition-all active:scale-90">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 15 3 9m0 0 6-6M3 9h12a6 6 0 0 1 0 12h-3" />
              </svg>
            </button>
          </div>
        </div>

        <!-- 核心内容 -->
        <div class="flex-1 flex flex-col items-center justify-center w-full max-w-2xl py-8 z-10 text-center">
          
          <!-- 前置建议语 (仅在第一步显示) -->
          <div v-if="history.length === 0" class="mb-8 animate-in fade-in slide-in-from-top-4 duration-1000">
            <span class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-emerald-50 dark:bg-emerald-900/20 text-emerald-600 dark:text-emerald-400 text-xs font-medium border border-emerald-100 dark:border-emerald-800/50">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-4 h-4">
                <path fill-rule="evenodd" d="M18 10a8 8 0 1 1-16 0 8 8 0 0 1 16 0Zm-7-4a1 1 0 1 1-2 0 1 1 0 0 1 2 0ZM9 9a.75.75 0 0 0 0 1.5h.253a.25.25 0 0 1 .244.304l-.459 2.066A1.75 1.75 0 0 0 10.747 15H11a.75.75 0 0 0 0-1.5h-.253a.25.25 0 0 1-.244-.304l.459-2.066A1.75 1.75 0 0 0 9.253 9H9Z" clip-rule="evenodd" />
              </svg>
              释放情绪前最好进行一次呼吸引导，让身体放松
            </span>
          </div>

          <!-- 禅意符号 -->
          <div class="mb-10 opacity-10">
            <div class="w-10 h-10 border-2 border-slate-900 dark:border-white rounded-full flex items-center justify-center">
              <div class="w-1.5 h-1.5 bg-slate-900 dark:bg-white rounded-full"></div>
            </div>
          </div>

          <transition name="zen-fade" mode="out-in">
            <div :key="currentNode.id">
              <h2 class="text-3xl md:text-4xl font-serif font-light text-slate-800 dark:text-slate-100 leading-[1.6] tracking-tight">
                {{ currentNode.text }}
              </h2>
              
              <!-- 停顿建议语 (对每个问题显示) -->
              <p v-if="!currentNode.isEnd" class="mt-8 text-sm text-slate-400 dark:text-slate-500 font-light tracking-widest italic animate-pulse">
                阅读完问题，请尝试停顿 30 秒左右，放松地感受当下
              </p>
            </div>
          </transition>
        </div>

        <!-- 操作区 -->
        <div class="w-full flex flex-col sm:flex-row gap-6 justify-center items-center z-10">
          <template v-if="options.length > 0">
            <button 
              v-for="option in options" 
              :key="option.nextId"
              @click="handleNavigate(option.nextId)"
              :class="[
                option.type === 'yes' ? 'bg-emerald-600 dark:bg-emerald-500 text-white shadow-xl shadow-emerald-600/20' : '',
                option.type === 'no' ? 'bg-white/50 dark:bg-slate-800/50 text-slate-500 border border-slate-200 dark:border-slate-700' : '',
                option.type === 'next' ? 'bg-slate-900 dark:bg-white text-white dark:text-slate-900 shadow-xl shadow-slate-900/10' : ''
              ]"
              class="group relative px-16 py-5 rounded-3xl font-medium transition-all duration-700 hover:scale-105 active:scale-95 overflow-hidden min-w-[180px]"
            >
              <span class="relative z-10">{{ option.label }}</span>
              <div class="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
            </button>
          </template>
          
          <template v-else>
            <div class="text-center">
              <p v-if="currentNode.isEnd" class="text-slate-400 dark:text-slate-500 mb-10 font-serif italic text-lg tracking-wide opacity-60">
                “心如工画师，能画诸世间。”
              </p>
              <button @click="reset" class="px-16 py-5 bg-gradient-to-r from-emerald-500 to-indigo-600 text-white rounded-3xl font-bold tracking-widest hover:shadow-[0_20px_40px_-12px_rgba(79,70,229,0.4)] transition-all hover:scale-105 active:scale-95">
                再次开启内在之旅
              </button>
            </div>
          </template>
        </div>

        <!-- 底部 -->
        <div class="mt-12 text-[9px] uppercase tracking-[0.5em] text-slate-300 dark:text-slate-700 font-bold z-10">
          Pause &bull; Feel &bull; Release
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.zen-fade-enter-active,
.zen-fade-leave-active {
  transition: all 1.2s cubic-bezier(0.23, 1, 0.32, 1);
}

.zen-fade-enter-from {
  opacity: 0;
  filter: blur(10px);
  transform: translateY(15px);
}

.zen-fade-leave-to {
  opacity: 0;
  filter: blur(10px);
  transform: translateY(-15px);
}

button {
  -webkit-tap-highlight-color: transparent;
}

.backdrop-blur-3xl {
  animation: card-float 10s ease-in-out infinite;
}

@keyframes card-float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-8px); }
}
</style>
