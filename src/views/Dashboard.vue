<script setup>
import { ref, onMounted, watch } from 'vue';
import { useRoute } from 'vue-router';
import ReleaseGuide from '../components/ReleaseGuide.vue';
import BreathingGuide from '../components/BreathingGuide.vue';

const route = useRoute();

const tabs = [
  { id: 'llm', name: '大模型', icon: 'M12 21a9.004 9.004 0 0 0 8.716-6.747M12 21a9.004 9.004 0 0 1-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 0 1 7.843 4.582M12 3a8.997 8.997 0 0 0-7.843 4.582m15.686 0A11.953 11.953 0 0 1 21 12c0 1.059-.137 2.085-.393 3.063M5.157 7.582A11.957 11.957 0 0 0 3 12c0 1.059.137 2.085.393 3.063' },
  { id: 'kb', name: '知识库', icon: 'M12 6.042A8.967 8.967 0 0 0 6 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 0 1 6 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 0 1 6-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0 0 18 18a8.967 8.967 0 0 0-6 2.292m0-14.25v14.25' },
  { id: 'release', name: '释放引导', icon: 'M15.19 8.683a5.877 5.877 0 0 1 2.232-.433c3.245 0 5.875 2.63 5.875 5.875s-2.63 5.875-5.875 5.875a5.877 5.877 0 0 1-2.232-.433A5.16 5.16 0 0 1 12 18.25a5.16 5.16 0 0 1-3.19-1.133 5.877 5.877 0 0 1-2.232.433c-3.245 0-5.875-2.63-5.875-5.875s2.63-5.875 5.875-5.875c.801 0 1.555.16 2.232.443A5.16 5.16 0 0 1 12 5.133a5.16 5.16 0 0 1 3.19 3.55Z' },
  { id: 'breathing', name: '呼吸引导', icon: 'M12 18.75a6 6 0 0 0 6-6v-1.5m-6 7.5a6 6 0 0 1-6-6v-1.5m6 7.5v3.75m-3.75 0h7.5M12 15.75a3 3 0 0 1-3-3V4.5a3 3 0 1 1 6 0v8.25a3 3 0 0 1-3 3Z' }
];

const activeTab = ref('llm');
const llmSubTab = ref('chat'); 
const selectedArticle = ref(null);

watch(() => route.query.tab, (newTab) => {
  if (newTab && tabs.some(t => t.id === newTab)) {
    activeTab.value = newTab;
    selectedArticle.value = null;
  }
}, { immediate: true });

// --- 知识库数据（完全按照提供内容修改） ---
const kbArticles = [
  {
    id: 'emotion',
    title: '情绪：停止对抗，让一切流动',
    tag: '释放核心',
    description: '谈到情绪释放，一定绕不开莱斯特·利文森的释放理论，它是“圣多纳释放法”的核心基础。',
    sections: [
      { type: 'text', content: '谈到情绪释放，一定绕不开莱斯特·利文森（Lester Levenson）的释放理论，是后来广为人知的“圣多纳释放法”（The Sedona Method）的核心基础。大卫·霍金斯早年曾与莱斯特共事，他的“放下”机制深受莱斯特启发。\n莱斯特认为，人类最大的误区在于将自己与情绪等同起来（比如认为“我是愤怒的”，而不是“我感觉到了愤怒”）。情绪只是一种受限的能量程序，并不属于你真正的本质。' },
      { type: 'quote', content: '他提出了一个极其经典的隐喻：就像你手里紧紧握着一支笔。 是你主动在消耗能量去“抓着”这支笔不放，久了你的手会酸痛。只要你意识到这一点，并且愿意松开手指，笔自然会掉落。情绪也是如此，是我们潜意识里死死抓着它们，只要我们愿意，随时可以“松手”。' },
      { type: 'list', title: '人类通常用三种低效或有害的方式来处理情绪，这些方式本质上都是在制造阻力：', items: [
        { label: '压抑（Suppression/Repression）', detail: '将情绪强行压入潜意识。这些被压抑的能量不会消失，而是会转化为焦虑、身体紧绷或失控的行为。' },
        { label: '表达（Expression）', detail: '将情绪发泄出来。霍金斯认为，单纯的发泄（如愤怒地咆哮或抱怨）不仅不能释放底层能量，反而会赋予情绪更多能量，使其被进一步固化。' },
        { label: '逃避（Escape）', detail: '通过娱乐、工作、转移注意力或无意识的消遣来避免感受内心的波动。' }
      ]},
      { type: 'text', title: '真正的释放：零阻力的“臣服”', content: '释放机制，是一种极度纯粹的觉知状态：' },
      { type: 'list', items: [
        { label: '允许其存在', detail: '当一种情绪升起时，不抗拒它、不评判它、不试图改变它，也不试图推开它。' },
        { label: '抽离故事，只感受能量', detail: '情绪总是伴随着无数的“念头”和情境“故事”。霍金斯强调，必须放下所有的念头，把注意力完全收回到感受情绪在身体里的“能量涌动”上。 念头是由底层的情绪能量驱动的；一旦这股纯粹的能量被允许流淌并释放，成千上万个由其衍生出的念头就会瞬间消散。' },
        { label: '能量的耗尽', detail: '情绪本身就像是一股被压缩的能量。当你对它保持“零阻力”的观察时，这股能量就会自然释放并耗尽。就像水流自然地漫过河床，没有刻意的摩擦和停滞，情绪也就流走了。' }
      ]},
      { type: 'text', content: '这一点在古代中国有也有所表现，如《庄子·内篇·应帝王》用心若镜，不将不迎，应而不藏，故能胜物而不伤。\n佛陀教导要“观受如受”。当愤怒、悲伤升起时，修行者不是去压抑它，也不是被它带着走（即发泄），而是像一个旁观者一样观察它的生起、停留和消失。\n老子推崇的“柔弱”和莱斯特推崇的“释放”，指的都是“无阻力状态”也就是无为。天下莫柔弱于水，而攻坚强者莫之能胜。水没有固定的形状，它不与任何东西硬碰硬，而是顺势而为。所以老子提出了上善若水，像水一样生活。\n《登出键》的作者莫子在他的yuotube频道中也分享过对待情绪的办法，就是放下头脑的解释，安住覺察 （不解釋），看著情緒生滅起落，知道自己不是那個情緒。情绪就会被觉察消融。\n从霍金斯的“臣服”、莱斯特的“放手”、庄子的“用心若镜”，再到禅宗的“狂心顿歇”，莫子的“不解释”，你会发现人类顶级的智慧在处理内在冲突时，最终都指向了同一个动作——停止对抗。' },
      { type: 'quote', content: '没错，处理情绪最核心的方法不是对情绪做什么，而是对情绪什么都不做。放手，让情绪自然流动。' },
      { type: 'text', content: '但是我们经过常年累月的压抑，以至于我们太擅长压抑了，负面情绪一出现，通常还没有反应过来，就已经压抑下去了。扭转常年累积的“压抑习性”，本质上是在重塑你的神经回路。你的潜意识之所以在零点几秒内把情绪按下去，是因为它在过去几十年里形成了一个根深蒂固的认知：“我想要这些感受赶快离开，我不想要感受这些感受”\n因此，扭转这个习性的核心，不是用更大的力气去把情绪“挖”出来（那是一种暴力），而是通过不断地接受情绪出现，把注意力从“大脑故事”转移到“身体雷达”。情绪来的时候单纯体会这个感觉，不加以分析。通过这样持续不断的做，来让压抑的习性被扭转。这一切的过程中不需要大脑的参与。相反，你需要放下头脑。' }
    ]
  },
  {
    id: 'desire',
    title: '欲望：匮乏的表达与能量机制',
    tag: '底层动力',
    description: '人类所有表层的负面情绪，都可以向下追溯到三个最核心的匮乏性欲望。',
    sections: [
      { type: 'text', content: '在莱斯特的释放法中谈到：人类所有表层的负面情绪，都可以向下追溯到三个最核心的匮乏性欲望。这与东方智慧中的“三毒”完美契合：' },
      { type: 'list', items: [
        { label: '想要控制 (Wanting to Control)', detail: '等于 嗔 (愤怒、抗拒)' },
        { label: '想要被认同/爱 (Wanting Approval)', detail: '等于 贪 (无餍足的抓取)' },
        { label: '想要安全 (Wanting Security)', detail: '等于 痴 (无明、恐惧)' }
      ]},
      { type: 'quote', content: '欲望是什么？你特别想要，想要的得不行，但是得不到。因为欲望这个感受在不断地阻止你得到。' },
      { type: 'text', title: '这背后的心理和能量机制在于：', content: '“欲求”是匮乏的表达： 当你极其强烈地“想要（Want）”某样东西时，你向潜意识发出的核心指令其实是——“我现在没有（Lack）”。\n阻力的诞生： “想要”会产生一种紧绷的能量（霍金斯称之为 Force/用力）。这种紧绷感会扭曲你的动作，让你在做事时患得患失、动作变形，反而把目标推得更远。\n举一个例子：我们总想做好一件事，却怎么都做不好。然后说：‘算了，反正干不好，无所谓了。’ 结果反而很轻松地做好了。这里的“算了”，并不是放弃了做这件事本身，而是放下了“想要完美控制结果的欲望”。' },
      { type: 'quote', content: '零阻力状态： 当你说出“无所谓”的那一刻，你松开了紧紧攥着的手。匮乏感消失了，紧绷的阻力卸下了。此时，你不再用“小我”的焦虑去死磕，而是进入了如流水般自然的“心流”状态。事情还是那件事，但驱动你做事的能量从“恐惧/控制”变成了“纯粹的行动”，结果自然水到渠成。\n任何你紧抓不放的“想要”，都在不断确认你的“匮乏”。松开对结果的控制，接纳当下的发生，你才能从“阻力”切换到“毫不费力”。' },
      { type: 'text', title: '那要怎么释放欲望呢？', content: '如同前面情绪所讲的，欲望也是一种感受。\n当你在用一种求生般的绝望去死磕一件事时，你发现自己是被欲望这种感受所驱动着，这时候我们放下头脑，单纯的回到这个感受上。可能是死死抓取的紧绷感，也可能是一种揪心、紧缩、或者像有爪子在心里挠的感觉。不管是什么感觉，不要去分析它。只是轻松的看着它，体会它，没一会他就会消散。' },
      { type: 'quote', content: '你可以把释放欲望想象成你手里紧紧攥着的一把沙子，你越是用力（想要），沙子越离不开手掌；当你放松手掌，沙子会轻松快速的离开。' }
    ]
  },
  {
    id: 'relaxation',
    title: '放松的重要性：生理层面的开关',
    tag: '生理开关',
    description: '没有生理上的放松，就不可能有真正的情绪释放。',
    sections: [
      { type: 'text', content: '当你受制于“想要控制、想要安全”等匮乏性欲望时，你的大脑会判定你正处于威胁之中。这会强制激活你的交感神经系统你的肌肉僵硬，呼吸变浅，大量的能量被用于维持这种“防御姿态”。\n只有当你真正放松下来（哪怕只是做几次深长的腹式呼吸），你的副交感神经系统（休息与消化模式）才会被激活。在这个模式下，你自动化压抑的“盖子”才会被安全地掀开，那些淤堵的情绪能量才能像冰块融化一样，通过身体的代谢自然流走。没有生理上的放松，就不可能有真正的情绪释放。' },
      { type: 'text', title: '杨定一博士的方法：舌抵上腭', content: '杨定一博士有谈到一个可以帮助我们激活副交感神经系统的方法，那就是舌抵上腭。\n当你舌抵上腭时，你的嘴唇会自然闭合，迫使身体采用鼻腔呼吸。舌头根部与迷走神经有着紧密的连结。当你把舌头轻轻抵在上腭（门牙后方的齿龈隆起处）时，会向大脑发送一个极其强烈的“安全信号”，直接激活迷走神经，从而唤醒副交感神经系统。' },
      { type: 'text', title: '道家智慧：搭鹊桥', content: '在道家和中医理论中，这个动作被称为“搭鹊桥”。人体有两大核心经络：督脉（主阳气，沿后背上升，终于上唇系带）和任脉（主阴血，沿前胸下降，起于下唇承浆穴）。口部是这两条经络断开的“缺口”。当你将舌尖轻轻抵在门牙后方的上腭（天池穴附近）时，就像是闭合了一个电路开关。它能让原本容易郁结在大脑（导致思虑过载、焦虑）的能量，顺着任脉顺畅地降下来，形成“小周天”的循环。这就是生理层面的“不堵塞、零阻力”。\n杨博士常提到，保持这个姿势一段时间后，口腔内会自然分泌出大量的唾液。在古代修行中这被称为“甘露”或“玉液”。从现代医学看，这些唾液中含有大量的消化酶和免疫球蛋白，不仅能促进消化，本身就是身体进入极度放松和自我疗愈状态的标志。' },
      { type: 'quote', title: '操作要领', content: '做这个动作时千万不要用力。不需要用舌头死死顶住上腭。正确的做法是：毫不费力地、轻轻地触碰，就像一片羽毛落在水面上一样。' }
    ]
  }
];

// --- 大模型 API 逻辑 ---
const deepseekApiKey = ref('');
const deepseekSelectedModel = ref('deepseek-chat');
const selectedKbIds = ref(['emotion', 'desire', 'relaxation']); 
const chatInput = ref('');
const chatMessages = ref([]);
const isSending = ref(false);

const dsModelOptions = [
  { id: 'deepseek-chat', name: '通用对话 (V3)', desc: '平衡速度与质量' },
  { id: 'deepseek-reasoner', name: '深度思考 (R1)', desc: '复杂推理与拆解' }
];

onMounted(() => {
  const savedKey = localStorage.getItem('deepseek_api_key');
  if (savedKey) deepseekApiKey.value = savedKey;
  const savedModel = localStorage.getItem('deepseek_selected_model');
  if (savedModel) deepseekSelectedModel.value = savedModel;
  const savedKb = localStorage.getItem('deepseek_selected_kb');
  if (savedKb) selectedKbIds.value = JSON.parse(savedKb);
  const savedHistory = localStorage.getItem('deepseek_chat_history');
  if (savedHistory) chatMessages.value = JSON.parse(savedHistory);
});

watch(chatMessages, (newVal) => localStorage.setItem('deepseek_chat_history', JSON.stringify(newVal)), { deep: true });
watch(deepseekSelectedModel, (newVal) => localStorage.setItem('deepseek_selected_model', newVal));
watch(selectedKbIds, (newVal) => localStorage.setItem('deepseek_selected_kb', JSON.stringify(newVal)), { deep: true });

const saveDsApiKey = () => { localStorage.setItem('deepseek_api_key', deepseekApiKey.value); alert('DeepSeek API 密钥已保存'); };
const toggleKbSelection = (id) => { const index = selectedKbIds.value.indexOf(id); if (index > -1) { selectedKbIds.value.splice(index, 1); } else { selectedKbIds.value.push(id); } };
const getSelectedKbContent = () => { return kbArticles.filter(article => selectedKbIds.value.includes(article.id)).map(article => { let content = `标题: ${article.title}\n`; article.sections.forEach(s => { if (s.title) content += `## ${s.title}\n`; content += `${s.content}\n`; }); return content; }).join('\n---\n'); };

const sendMessage = async () => {
  if (!chatInput.value.trim() || isSending.value) return;
  if (!deepseekApiKey.value) { alert('请在设置中配置 DeepSeek API 密钥'); llmSubTab.value = 'settings'; return; }
  const userMsg = chatInput.value;
  chatMessages.value.push({ role: 'user', content: userMsg });
  chatInput.value = '';
  isSending.value = true;
  try {
    const kbContext = getSelectedKbContent();
    const systemPrompt = `你是一个温柔的情绪释放助手。你精通利文森释放法、霍金斯臣服实验和杨定一放松理论。\n${kbContext ? `以下是用户为你挑选的参考知识库内容，请结合这些内容进行引导：\n\n${kbContext}` : '请以温柔专业的姿态引导用户面对情绪。'}`;
    const response = await fetch('https://api.deepseek.com/chat/completions', { method: 'POST', headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${deepseekApiKey.value}` }, body: JSON.stringify({ model: deepseekSelectedModel.value, messages: [{ role: 'system', content: systemPrompt }, ...chatMessages.value], temperature: 0.7 }) });
    const data = await response.json();
    if (data.choices && data.choices[0]) { chatMessages.value.push({ role: 'assistant', content: data.choices[0].message.content }); } else { throw new Error(data.error?.message || '请求失败'); }
  } catch (error) { chatMessages.value.push({ role: 'system', content: `错误: ${error.message}` }); } finally { isSending.value = false; setTimeout(() => { const container = document.getElementById('chat-container'); if (container) container.scrollTop = container.scrollHeight; }, 100); }
};

const clearChat = () => { if (confirm('确定要清空聊天记录吗？')) { chatMessages.value = []; localStorage.removeItem('deepseek_chat_history'); } };
const changeTab = (id) => { activeTab.value = id; selectedArticle.value = null; };
const openArticle = (article) => { selectedArticle.value = article; window.scrollTo({ top: 0, behavior: 'smooth' }); };
</script>

<template>
  <div class="relative pt-32 pb-20 min-h-[calc(100vh-80px)]">
    <div class="absolute top-0 left-1/2 -translate-x-1/2 w-[800px] h-[500px] bg-gradient-to-b from-emerald-100/20 dark:from-emerald-900/10 to-transparent rounded-full blur-3xl -z-10"></div>
    <div class="container px-6 mx-auto max-w-7xl">
      <div v-if="!selectedArticle" class="mb-12 text-center md:text-left animate-in fade-in duration-700">
        <h2 class="text-3xl font-serif font-light md:text-4xl dark:text-white">深呼吸，<span class="text-emerald-600 italic">开启</span>内在之旅。</h2>
        <p class="mt-4 text-slate-500 dark:text-slate-400">选择您需要的工具，开始与内心的对话。</p>
      </div>
      <div class="flex flex-wrap items-center gap-2 mb-8 p-1.5 bg-slate-100/50 dark:bg-slate-800/50 backdrop-blur-sm rounded-2xl w-fit">
        <button v-for="tab in tabs" :key="tab.id" @click="changeTab(tab.id)" :class="[activeTab === tab.id ? 'bg-white dark:bg-slate-700 text-emerald-600 dark:text-white shadow-md' : 'text-slate-500 dark:text-slate-400 hover:text-emerald-600']" class="flex items-center gap-2 px-6 py-2.5 text-sm font-medium transition-all rounded-xl">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5"><path stroke-linecap="round" stroke-linejoin="round" :d="tab.icon" /></svg>
          {{ tab.name }}
        </button>
      </div>
      <div class="transition-all duration-500">
        <div v-if="activeTab === 'llm'" class="space-y-6">
          <div class="flex items-center gap-8 border-b border-slate-200 dark:border-slate-800 pb-4 mb-8">
            <button @click="llmSubTab = 'chat'" :class="[llmSubTab === 'chat' ? 'text-emerald-600 border-b-2 border-emerald-600' : 'text-slate-400']" class="pb-2 text-sm font-bold tracking-widest uppercase transition-all">对话 (Chat)</button>
            <button @click="llmSubTab = 'settings'" :class="[llmSubTab === 'settings' ? 'text-emerald-600 border-b-2 border-emerald-600' : 'text-slate-400']" class="pb-2 text-sm font-bold tracking-widest uppercase transition-all">配置 (Settings)</button>
          </div>
          <div v-if="llmSubTab === 'chat'" class="grid grid-cols-1 lg:grid-cols-4 gap-8 animate-in fade-in slide-in-from-left-4 duration-500">
            <div class="lg:col-span-1 space-y-6">
              <div class="p-6 bg-white/70 dark:bg-slate-900/50 border border-slate-100 dark:border-slate-800 rounded-[2rem] shadow-sm backdrop-blur-md">
                <h3 class="text-xs font-bold text-slate-400 uppercase tracking-widest mb-4">知识库关联</h3>
                <div class="space-y-2">
                  <button v-for="article in kbArticles" :key="article.id" @click="toggleKbSelection(article.id)" :class="[selectedKbIds.includes(article.id) ? 'border-emerald-500 bg-emerald-50/30 dark:bg-emerald-900/20' : 'border-slate-100 dark:border-slate-800 opacity-60']" class="w-full flex items-center justify-between p-3 border-2 rounded-xl transition-all">
                    <span class="text-xs font-medium dark:text-white">{{ article.title.split('：')[0] }}</span>
                    <div v-if="selectedKbIds.includes(article.id)" class="w-2 h-2 bg-emerald-500 rounded-full"></div>
                  </button>
                </div>
              </div>
            </div>
            <div class="lg:col-span-3 flex flex-col h-[700px] bg-white/70 dark:bg-slate-900/50 border border-slate-100 dark:border-slate-800 rounded-[2.5rem] shadow-2xl overflow-hidden backdrop-blur-md">
              <div class="px-8 py-4 border-b border-slate-100 dark:border-slate-800 flex justify-between items-center bg-white/30 dark:bg-slate-800/30">
                <div class="flex items-center gap-3"><div class="w-2 h-2 bg-emerald-500 rounded-full animate-pulse"></div><span class="text-sm font-medium dark:text-white">情绪释放助手</span></div>
                <button @click="clearChat" class="text-xs text-slate-400 hover:text-red-500 transition-colors">清空记录</button>
              </div>
              <div id="chat-container" class="flex-1 overflow-y-auto p-8 space-y-6">
                <div v-if="chatMessages.length === 0" class="h-full flex flex-col items-center justify-center text-center opacity-30">
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1" stroke="currentColor" class="w-16 h-16 mb-4"><path stroke-linecap="round" stroke-linejoin="round" d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 0 1-.923 1.785c-.442.496.057 1.285.693 1.066a4.713 4.713 0 0 0 2.43-1.442c.495-.442 1.104-.613 1.7-.586 1.107.051 2.253.085 3.421.085Z" /></svg>
                  <p class="font-serif italic text-lg tracking-widest">说出此刻的感受...</p>
                </div>
                <div v-for="(msg, idx) in chatMessages" :key="idx" :class="[msg.role === 'user' ? 'justify-end' : 'justify-start']" class="flex animate-in fade-in duration-300">
                  <div :class="[msg.role === 'user' ? 'bg-emerald-600 text-white rounded-t-2xl rounded-bl-2xl shadow-emerald-600/10' : 'bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-200 border border-slate-100 dark:border-slate-700 rounded-t-2xl rounded-br-2xl shadow-sm']" class="max-w-[85%] px-5 py-3 text-sm leading-relaxed whitespace-pre-wrap">{{ msg.content }}</div>
                </div>
                <div v-if="isSending" class="flex justify-start"><div class="bg-white dark:bg-slate-800 border border-slate-100 dark:border-slate-800 px-5 py-3 rounded-2xl flex gap-1"><div class="w-1.5 h-1.5 bg-emerald-500 rounded-full animate-bounce"></div><div class="w-1.5 h-1.5 bg-emerald-500 rounded-full animate-bounce [animation-delay:0.2s]"></div><div class="w-1.5 h-1.5 bg-emerald-500 rounded-full animate-bounce [animation-delay:0.4s]"></div></div></div>
              </div>
              <div class="p-6 bg-white/30 dark:bg-slate-800/30 border-t border-slate-100 dark:border-slate-800">
                <div class="flex gap-3">
                  <input v-model="chatInput" @keyup.enter="sendMessage" placeholder="此刻有什么念头或感觉升起？" class="flex-1 px-5 py-3 bg-white dark:bg-slate-800 border border-slate-100 dark:border-slate-700 rounded-2xl text-sm outline-none transition-all dark:text-white focus:ring-2 focus:ring-emerald-500" />
                  <button @click="sendMessage" :disabled="isSending" class="px-6 py-3 bg-emerald-600 hover:bg-emerald-700 disabled:opacity-50 text-white rounded-2xl transition-all shadow-lg shadow-emerald-600/20">发送</button>
                </div>
              </div>
            </div>
          </div>
          <div v-if="llmSubTab === 'settings'" class="grid grid-cols-1 lg:grid-cols-4 gap-8 animate-in fade-in slide-in-from-right-4 duration-500">
            <div class="lg:col-span-1 space-y-4">
              <button class="w-full flex items-center gap-4 p-4 bg-emerald-50 dark:bg-emerald-900/20 border-2 border-emerald-500 rounded-2xl transition-all text-left">
                <div class="w-8 h-8 bg-emerald-500 rounded-lg flex items-center justify-center text-white font-bold text-xs italic">DS</div>
                <div><p class="text-sm font-bold dark:text-white leading-none mb-1">DeepSeek</p><p class="text-[10px] text-emerald-600/60 uppercase font-bold tracking-tighter">API Provider</p></div>
              </button>
            </div>
            <div class="lg:col-span-3 space-y-8 p-10 bg-white/70 dark:bg-slate-900/50 border border-slate-100 dark:border-slate-800 rounded-[2.5rem] shadow-xl backdrop-blur-md">
              <div><h3 class="text-xl font-serif dark:text-white mb-2">DeepSeek 开放平台</h3><p class="text-xs text-slate-400">配置您的 API 密钥以启用智能对话服务。</p></div>
              <div class="max-w-xl space-y-10">
                <div class="space-y-4"><label class="block text-xs font-bold text-slate-500 uppercase tracking-widest">API 密钥</label><div class="flex gap-4"><input v-model="deepseekApiKey" type="password" placeholder="sk-..." class="flex-1 px-5 py-3 bg-slate-50 dark:bg-slate-800 border border-slate-100 dark:border-slate-700 rounded-xl text-sm outline-none focus:ring-2 focus:ring-emerald-500 transition-all dark:text-white" /><button @click="saveDsApiKey" class="px-8 py-3 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-sm font-bold transition-all shadow-lg shadow-emerald-600/20">保存</button></div></div>
                <div class="space-y-4"><label class="block text-xs font-bold text-slate-500 uppercase tracking-widest">模型切换</label><div class="grid grid-cols-1 md:grid-cols-2 gap-4"><button v-for="model in dsModelOptions" :key="model.id" @click="deepseekSelectedModel = model.id" :class="[deepseekSelectedModel === model.id ? 'border-emerald-500 bg-emerald-50/50 dark:bg-emerald-900/20' : 'border-slate-100 dark:border-slate-800 opacity-60']" class="flex flex-col items-start p-5 border-2 rounded-[1.5rem] transition-all text-left"><span class="text-sm font-bold" :class="[deepseekSelectedModel === model.id ? 'text-emerald-600 dark:text-emerald-400' : 'text-slate-700 dark:text-slate-300']">{{ model.name }}</span><span class="text-[10px] opacity-60 mt-1 leading-relaxed">{{ model.desc }}</span></button></div></div>
              </div>
            </div>
          </div>
        </div>
        <div v-if="activeTab === 'kb'">
          <div v-if="!selectedArticle" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 animate-in fade-in slide-in-from-bottom-4">
            <div v-for="article in kbArticles" :key="article.id" @click="openArticle(article)" class="p-8 bg-white dark:bg-slate-900/50 border border-slate-100 dark:border-slate-800 rounded-3xl hover:shadow-xl transition-all cursor-pointer group">
              <span class="inline-block px-3 py-1 mb-4 text-[10px] font-bold tracking-widest uppercase bg-emerald-50 dark:bg-emerald-900/30 text-emerald-600 dark:text-emerald-400 rounded-lg">{{ article.tag }}</span>
              <h4 class="text-xl font-serif mb-3 dark:text-white group-hover:text-emerald-600 transition-colors">{{ article.title }}</h4>
              <p class="text-sm text-slate-500 dark:text-slate-400 leading-relaxed line-clamp-3">{{ article.description }}</p>
            </div>
          </div>
          <div v-else class="max-w-4xl mx-auto animate-in fade-in slide-in-from-bottom-8">
            <button @click="selectedArticle = null" class="mb-8 flex items-center gap-2 text-slate-400 hover:text-emerald-600 transition-colors group"><svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 group-hover:-translate-x-1 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" /></svg>返回列表</button>
            <article class="bg-white/80 dark:bg-slate-900/70 backdrop-blur-xl border border-slate-100 dark:border-slate-800 rounded-[3rem] p-8 md:p-16 shadow-2xl">
              <header class="mb-12 border-b border-slate-100 dark:border-slate-800 pb-12"><span class="text-xs font-bold tracking-[0.3em] uppercase text-emerald-500 mb-4 block">{{ selectedArticle.tag }}</span><h1 class="text-3xl md:text-5xl font-serif dark:text-white leading-tight">{{ selectedArticle.title }}</h1></header>
              <div class="space-y-10 text-justify">
                <div v-for="(section, idx) in selectedArticle.sections" :key="idx">
                  <blockquote v-if="section.type === 'quote'" class="relative py-6 pl-8">
                    <div class="absolute top-0 left-0 text-6xl text-emerald-100 dark:text-emerald-900/20 font-serif">“</div>
                    <p class="text-xl md:text-2xl font-serif italic text-slate-700 dark:text-slate-300 leading-relaxed whitespace-pre-wrap">{{ section.content }}</p>
                  </blockquote>
                  <div v-if="section.type === 'text'">
                    <h3 v-if="section.title" class="text-lg font-bold mb-4 flex items-center gap-3 dark:text-white"><span class="w-8 h-px bg-emerald-200 dark:bg-emerald-800"></span>{{ section.title }}</h3>
                    <p class="text-slate-600 dark:text-slate-300 leading-[1.8] text-lg whitespace-pre-wrap">{{ section.content }}</p>
                  </div>
                  <div v-if="section.type === 'list'">
                    <h3 v-if="section.title" class="text-lg font-bold mb-6 dark:text-white">{{ section.title }}</h3>
                    <div class="grid gap-4">
                      <div v-for="item in section.items" :key="item.label" class="p-6 bg-emerald-50/30 dark:bg-emerald-900/10 rounded-2xl border border-emerald-100/50 dark:border-emerald-800/50"><span class="font-bold text-emerald-600 dark:text-emerald-400 block mb-2">{{ item.label }}</span><p class="text-slate-500 dark:text-slate-400 text-sm leading-relaxed">{{ item.detail }}</p></div>
                    </div>
                  </div>
                </div>
              </div>
              <footer class="mt-20 pt-12 border-t border-slate-100 dark:border-slate-800 text-center"><p class="text-slate-400 text-sm italic font-serif">放手，让一切自然流动。</p></footer>
            </article>
          </div>
        </div>
        <div v-if="activeTab === 'release'" class="animate-in fade-in slide-in-from-bottom-4 duration-500"><ReleaseGuide /></div>
        <div v-if="activeTab === 'breathing'" class="animate-in fade-in slide-in-from-bottom-4 duration-500"><BreathingGuide /></div>
      </div>
    </div>
  </div>
</template>

<style scoped>
article p { text-align: justify; }
#chat-container::-webkit-scrollbar { width: 4px; }
#chat-container::-webkit-scrollbar-track { background: transparent; }
#chat-container::-webkit-scrollbar-thumb { background: #10b98120; border-radius: 10px; }
</style>
