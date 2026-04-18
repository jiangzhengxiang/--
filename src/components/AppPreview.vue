<template>
  <div class="container px-6 mx-auto max-w-7xl mt-32">
    <div class="relative p-12 bg-white dark:bg-slate-900 border border-slate-100 dark:border-slate-800 rounded-[3rem] shadow-2xl overflow-hidden group">
      <!-- 装饰背景 -->
      <div class="absolute -top-24 -right-24 w-96 h-96 bg-emerald-50 dark:bg-emerald-900/20 rounded-full blur-3xl opacity-50 group-hover:scale-110 transition-transform duration-1000"></div>
      
      <div class="relative z-10 grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
        <div class="space-y-8">
          <h2 class="text-4xl font-serif dark:text-white leading-tight">
            在平静中，<br/>
            发现<span class="text-emerald-600 italic">智慧</span>。
          </h2>
          <p class="text-slate-500 dark:text-slate-400 leading-relaxed text-lg font-light">
            通过科学的呼吸引导与情绪释放技术，帮助您在忙碌的生活中找回内在的平和。
          </p>
        </div>
        
        <div class="aspect-video bg-slate-100 dark:bg-slate-800 rounded-3xl overflow-hidden border-4 border-white dark:border-slate-700 shadow-inner flex flex-col items-center justify-center">
          <img 
            src="/hawkins-scale.jfif" 
            alt="能量层级预览" 
            class="w-full h-full object-cover"
          />
        </div>
      </div>
    </div>
  </div>
</template>
