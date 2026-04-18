<script setup>
import { ref, onUnmounted, computed } from 'vue';

// 模式定义
const modes = [
  { id: 'abdominal', name: '腹式呼吸', desc: '吸气鼓肚，呼气缩肚' },
  { id: 'hold', name: '闭气练习', desc: '吸满闭气，向腹部加压' }
];

const currentMode = ref('abdominal');
const isRunning = ref(false);
const phase = ref('准备'); // '吸气', '闭气', '呼气', '准备'
const counter = ref(0);
const cycleCount = ref(0);

// 时间调节参数 (单位：秒)
const inhaleDuration = ref(6);
const holdDuration = ref(5);
const exhaleDuration = ref(6);

// 当前运行中的闭气时间 (用于递增逻辑)
const activeHoldTime = ref(5);

let timer = null;

// 呼吸球缩放比例 - 动态计算
const scale = computed(() => {
  if (!isRunning.value) return 1;
  if (phase.value === '吸气') return 1 + (counter.value / inhaleDuration.value) * 0.5;
  if (phase.value === '闭气') return 1.5;
  if (phase.value === '呼气') return 1.5 - (counter.value / exhaleDuration.value) * 0.5;
  return 1;
});

const startBreathing = () => {
  isRunning.value = true;
  cycleCount.value = 0;
  activeHoldTime.value = holdDuration.value;
  runInhale();
};

const stopBreathing = () => {
  isRunning.value = false;
  phase.value = '准备';
  counter.value = 0;
  clearInterval(timer);
};

// 吸气逻辑
const runInhale = () => {
  phase.value = '吸气';
  counter.value = 0;
  timer = setInterval(() => {
    counter.value++;
    if (counter.value >= inhaleDuration.value) {
      clearInterval(timer);
      if (currentMode.value === 'hold') {
        runHold();
      } else {
        runExhale();
      }
    }
  }, 1000);
};

// 闭气逻辑
const runHold = () => {
  phase.value = '闭气';
  counter.value = 0;
  timer = setInterval(() => {
    counter.value++;
    if (counter.value >= activeHoldTime.value) {
      clearInterval(timer);
      runExhale();
    }
  }, 1000);
};

// 呼气逻辑
const runExhale = () => {
  phase.value = '呼气';
  counter.value = 0;
  timer = setInterval(() => {
    counter.value++;
    if (counter.value >= exhaleDuration.value) {
      clearInterval(timer);
      cycleCount.value++;
      // 闭气递增逻辑：每2个循环增加1秒，不再设置上限
      if (currentMode.value === 'hold' && cycleCount.value % 2 === 0) {
        activeHoldTime.value++;
      }
      runInhale();
    }
  }, 1000);
};

onUnmounted(() => {
  clearInterval(timer);
});
</script>

<template>
  <div class="max-w-4xl mx-auto py-12 px-6">
    <div class="relative bg-white/60 dark:bg-slate-900/60 backdrop-blur-3xl border border-white/50 dark:border-slate-800/50 shadow-2xl rounded-[3.5rem] p-8 md:p-16 min-h-[700px] flex flex-col items-center justify-between overflow-hidden">
      
      <!-- 模式与参数调节区 -->
      <div class="z-10 w-full flex flex-col items-center gap-8">
        <div class="flex gap-2 p-1.5 bg-slate-100 dark:bg-slate-800/50 rounded-2xl">
          <button 
            v-for="mode in modes" 
            :key="mode.id"
            @click="!isRunning && (currentMode = mode.id)"
            :class="[
              currentMode === mode.id 
                ? 'bg-white dark:bg-slate-700 text-emerald-600 dark:text-emerald-400 shadow-md' 
                : 'text-slate-400 hover:text-slate-600 cursor-pointer',
              isRunning ? 'opacity-50 cursor-not-allowed' : ''
            ]"
            class="px-6 py-2 text-sm font-medium rounded-xl transition-all"
          >
            {{ mode.name }}
          </button>
        </div>

        <!-- 滑动调节面板 (仅在未运行阶段显示) -->
        <transition name="fade">
          <div v-if="!isRunning" class="grid grid-cols-1 md:grid-cols-3 gap-8 w-full max-w-2xl bg-white/40 dark:bg-slate-800/20 p-6 rounded-[2rem] border border-white/40">
            <div class="flex flex-col gap-3">
              <label class="text-[10px] font-bold text-slate-400 uppercase tracking-widest flex justify-between">
                吸气时间 <span>{{ inhaleDuration }}s</span>
              </label>
              <input type="range" v-model.number="inhaleDuration" min="2" max="15" class="w-full h-1.5 bg-emerald-100 dark:bg-emerald-900/30 rounded-lg appearance-none cursor-pointer accent-emerald-500">
            </div>
            <div v-if="currentMode === 'hold'" class="flex flex-col gap-3">
              <label class="text-[10px] font-bold text-slate-400 uppercase tracking-widest flex justify-between">
                闭气时间 <span>{{ holdDuration }}s</span>
              </label>
              <input type="range" v-model.number="holdDuration" min="2" max="120" class="w-full h-1.5 bg-amber-100 dark:bg-amber-900/30 rounded-lg appearance-none cursor-pointer accent-amber-500">
            </div>
            <div class="flex flex-col gap-3">
              <label class="text-[10px] font-bold text-slate-400 uppercase tracking-widest flex justify-between">
                呼气时间 <span>{{ exhaleDuration }}s</span>
              </label>
              <input type="range" v-model.number="exhaleDuration" min="2" max="15" class="w-full h-1.5 bg-indigo-100 dark:bg-indigo-900/30 rounded-lg appearance-none cursor-pointer accent-indigo-500">
            </div>
          </div>
        </transition>
      </div>

      <!-- 呼吸核心区 -->
      <div class="flex-1 flex flex-col items-center justify-center py-8 z-10 w-full">
        <div class="relative w-72 h-72 flex items-center justify-center">
          <!-- 动态背景 -->
          <div 
            class="absolute inset-0 bg-emerald-400/10 dark:bg-emerald-500/5 rounded-full transition-all duration-1000 ease-in-out"
            :style="{ transform: `scale(${scale * 1.5})`, opacity: isRunning ? 1 : 0 }"
          ></div>
          
          <!-- 呼吸球 -->
          <div 
            class="w-48 h-48 bg-gradient-to-tr from-emerald-500 to-teal-400 rounded-full shadow-[0_0_60px_rgba(16,185,129,0.3)] flex items-center justify-center transition-transform duration-1000 ease-in-out relative z-10"
            :class="{ 'animate-vibrate': phase === '闭气' }"
            :style="{ transform: `scale(${scale})` }"
          >
            <div class="text-white text-5xl font-serif font-light">{{ counter || '' }}</div>
          </div>

          <!-- 装饰外环 -->
          <svg class="absolute inset-0 w-full h-full -rotate-90">
            <circle 
              cx="144" cy="144" r="130" 
              fill="none" 
              stroke="currentColor" 
              stroke-width="1" 
              class="text-slate-100 dark:text-slate-800 opacity-50"
            />
          </svg>
        </div>

        <!-- 动态引导文字 -->
        <div class="mt-16 text-center h-24">
          <transition name="fade" mode="out-in">
            <div :key="phase" class="space-y-3">
              <h3 class="text-4xl font-serif font-light dark:text-white">
                <span v-if="!isRunning">静心，准备</span>
                <span v-else-if="phase === '吸气'" class="text-emerald-600 dark:text-emerald-400">吸气，肚子鼓起来</span>
                <span v-else-if="phase === '闭气'" class="text-amber-500">闭气，把气往肚子压住</span>
                <span v-else-if="phase === '呼气'" class="text-indigo-500">吐气，肚子收缩</span>
              </h3>
              <p class="text-slate-400 text-sm font-light tracking-[0.3em] uppercase">
                {{ isRunning ? 'Breathe with awareness' : modes.find(m => m.id === currentMode).desc }}
              </p>
            </div>
          </transition>
        </div>
      </div>

      <!-- 控制按钮 -->
      <div class="z-10 pb-8">
        <button 
          v-if="!isRunning"
          @click="startBreathing"
          class="px-20 py-5 bg-slate-900 dark:bg-white text-white dark:text-slate-900 rounded-[2rem] font-bold tracking-widest hover:scale-105 active:scale-95 transition-all shadow-[0_20px_40px_rgba(0,0,0,0.1)]"
        >
          开始呼吸
        </button>
        <button 
          v-else
          @click="stopBreathing"
          class="px-20 py-5 border-2 border-slate-200 dark:border-slate-800 text-slate-500 dark:text-slate-400 rounded-[2rem] font-bold tracking-widest hover:bg-white dark:hover:bg-slate-800 transition-all"
        >
          结束练习
        </button>
      </div>

      <!-- 状态显示 -->
      <div v-if="isRunning" class="absolute bottom-10 left-0 w-full flex justify-center gap-12 text-[10px] font-bold tracking-[0.3em] text-slate-300 dark:text-slate-600 uppercase">
        <div class="flex flex-col items-center gap-1">
          <span class="text-slate-400">Cycles</span>
          <span class="text-lg font-serif">{{ cycleCount }}</span>
        </div>
        <div v-if="currentMode === 'hold'" class="flex flex-col items-center gap-1">
          <span class="text-slate-400">Next Hold</span>
          <span class="text-lg font-serif text-amber-500">{{ activeHoldTime }}s</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: all 0.8s cubic-bezier(0.2, 0.8, 0.2, 1);
}
.fade-enter-from, .fade-leave-to { opacity: 0; transform: translateY(10px); }

@keyframes vibrate {
  0%, 100% { transform: scale(1.5) translate(0); }
  25% { transform: scale(1.505) translate(0.5px, 0.5px); }
  50% { transform: scale(1.495) translate(-0.5px, 0.5px); }
  75% { transform: scale(1.5) translate(0.5px, -0.5px); }
}

.animate-vibrate {
  animation: vibrate 0.3s linear infinite;
}

/* 自定义 Range Slider 样式 */
input[type=range]::-webkit-slider-thumb {
  -webkit-appearance: none;
  height: 16px;
  width: 16px;
  border-radius: 50%;
  background: currentColor;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
  margin-top: -6px;
}

input[type=range]::-webkit-slider-runnable-track {
  width: 100%;
  height: 4px;
  cursor: pointer;
}
</style>
