const PAPER_ARCHIVE_CONFIG = {
  "meta": {
    "title": "Agent & LLM Research Daily",
    "subtitle": "Daily arXiv Digest — Agents · RSI · Agentic RL · Frontier LLMs",
    "description": "Automated collection of cutting-edge research papers on AI Agents, Recursive Self-Improvement (RSI), Agentic RL, and releases from leading LLM labs (OpenAI, Anthropic, Google, Meta, Zhipu, DeepSeek, Qwen, Kimi, Hunyuan, Xiaomi, ByteDance, Baidu, etc.).",
    "totalPapers": 50,
    "totalDays": 1,
    "lastUpdated": "2026-10-02",
    "author": "@miclover0",
    "repository": "https://github.com/miclover0/paper-daily"
  },
  "dailyReports": [
    {
      "id": "2026-10-02",
      "date": "2026-10-02",
      "dateDisplay": "October 02, 2026",
      "weekday": "Friday",
      "filename": "daily_reports/2026-10-02-arXiv.html",
      "paperCount": 50,
      "groups": {
        "A": 28,
        "B": 22,
        "C": 0
      },
      "featuredPapers": [
        {
          "title": "REVEAL: Robust Evolution of Vision-Language Models for Explainable AI-Video Detection",
          "authors": "Yun-Yun Tsai, Qingyuan Liu, Ruijian Zha",
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2502.14994",
          "tags": [
            "OpenAI",
            "Google",
            "Qwen"
          ],
          "summary": "【研究背景】该论文聚焦OpenAI领域。\nThe rapid advancement of AI-generated video poses challenges to digital authenticity and security.。\n【核心方法】We introduce a framework leveraging Vision Language Models (VLMs) for robust AI-generated video detection.。\n【实验结果】Experiments show that REVEAL improves F1 scores by 9.1% to 30.。",
          "highlights": [
            "introduce a framework leveraging Vision Language Model",
            "first benchmark VidForensic containing 1",
            "The rapid advancement of AI-generated video poses challenges to digital authenticity and security."
          ],
          "pdfUrl": "https://arxiv.org/pdf/2502.14994",
          "readReason": "来自 OpenAI 团队的最新研究工作，值得重点关注其技术路线；来自 Google 团队的最新研究工作，值得重点关注其技术路线"
        },
        {
          "title": "SHARPO: Segment-Level Credit Assignment for Agentic Reinforcement Learning",
          "authors": "Xinchen Du, Zhengze Zhou, Wenhui Zhu",
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.00838",
          "tags": [
            "Qwen",
            "Agentic RL",
            "Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nTo address this limitation, we introduce Segment-level Hindsight Advantage Reweighting for Policy Optimization (SHARPO), a credit-assignment mechanism that refines Group Relative Policy Optimization...。\n【核心方法】we introduce Segment-level Hindsight Advantage Reweighting for Policy Optimization (SHARPO), a credit-assignment mechanism that refines Group Relative Policy Optimization (GRPO) at the level of environment-facing segments.。",
          "highlights": [
            "outperforms existing baselines on the ALFWorld and WebShop benchmarks",
            "SHARPO",
            "隶属于 cs.LG, cs.AI"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.00838",
          "readReason": "AI Agent 是当前研究热点，本文可能包含创新性的设计思路；Agentic 强化学习将决策与语言模型结合，是智能体研究的前沿方向"
        },
        {
          "title": "GUI-HARVEST: Self-Improving GUI Agents through Evidence-Driven Harness Evolution",
          "authors": "Geyi Yang, Zikun Qu, Xiang Li",
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.00948",
          "tags": [
            "OpenAI",
            "Qwen",
            "RSI"
          ],
          "summary": "【研究背景】该论文聚焦递归自改进（RSI）领域。\nWith the same backbone and initial harness, GUI-HARVEST outperforms Self-Harness and Meta-Harness, suggesting that GUI-specific diagnosis and validation help harness improvements generalize to...。\n【核心方法】We introduce GUI-HARVEST, an automatic harness optimizer that enables self-improving GUI agents with frozen backbone models.。\n【实验结果】Frozen-harness transfer improves GPT-5 by 13.87 percentage points on WindowsAgentArena at 50 steps without further optimization.。",
          "highlights": [
            "outperforms Self-Harness and Meta-Harness",
            "GUI",
            "隶属于 cs.LG, cs.AI"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.00948",
          "readReason": "递归自改进（RSI）是智能体自我进化的关键方向，本文具有一定的探索价值；来自 OpenAI 团队的最新研究工作，值得重点关注其技术路线"
        },
        {
          "title": "Do Your Own Research: Learning to Forecast by Learning to Search",
          "authors": "Yusuf Afifi, Artur Kiulian, Anton Polishko",
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.01955",
          "tags": [
            "Anthropic",
            "Qwen",
            "Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nOutcome-based reinforcement learning can train language models to forecast real-world events, but prior forecasting work either freezes research context before training or deploys agentic research...。\n【实验结果】Training changes how the agent interacts with information: calibration improves 30-40%, and search attempts fall from 3.。",
          "highlights": [
            "Do Your Own Research",
            "隶属于 cs.LG",
            "0.256, n=265), at about 5% of the inference cost, and its margin is widest on the hardest questions, the ones the crowd "
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.01955",
          "readReason": "AI Agent 是当前研究热点，本文可能包含创新性的设计思路；来自 Anthropic 团队的最新研究工作，值得重点关注其技术路线"
        },
        {
          "title": "Detecting Multi-Agent Collusion Through Multi-Agent Interpretability",
          "authors": "Aaron Rose, Carissa Cullen, Sahar Abdelnabi",
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2604.01151",
          "tags": [
            "Meta",
            "DeepSeek",
            "Qwen"
          ],
          "summary": "【研究背景】该论文聚焦Meta领域。\nWhile linear probes on model activations have shown promise for detecting deception in single-agent settings, collusion is inherently a multi-agent phenomenon, and the use of internal...。\n【核心方法】We introduce NARCBench, a benchmark for evaluating collusion detection under environment distribution shift, and propose five probing techniques that aggregate per-agent deception scores to classify scenarios at the group level, evaluated across...。",
          "highlights": [
            "propose five probing technique",
            "Detecting Multi",
            "隶属于 cs.AI, cs.LG"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2604.01151",
          "readReason": "来自 Meta 团队的最新研究工作，值得重点关注其技术路线；来自 DeepSeek 团队的最新研究工作，值得重点关注其技术路线"
        },
        {
          "title": "Kernel-Managed Shared Memory for System-Wide Personalization",
          "authors": "Ryan Lum, Yongfeng Zhang",
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2609.10144",
          "tags": [
            "OpenAI",
            "Meta",
            "Qwen"
          ],
          "summary": "【研究背景】该论文聚焦OpenAI领域。\nAI systems become more useful when they can adapt to the people using them, but in multi-agent systems, useful context learned by one agent often remains unavailable to others.。\n【核心方法】We present kernel-managed shared memory, a system-level abstraction in which specialized agents write structured, tagged memories while the agent-system kernel, not individual agents, governs retrieval, privacy enforcement, and prompt injection.。\n【实验结果】Against an unmanaged external memory backend (Mem0) using identical underlying storage, kernel-managed retrieval and injection improve personalization scores by 2.4-4.。",
          "highlights": [
            "Kernel",
            "隶属于 cs.AI, cs.LG",
            "Against standard retrieval-augmented injection, gains are similarly large and consistent across all three models."
          ],
          "pdfUrl": "https://arxiv.org/pdf/2609.10144",
          "readReason": "来自 OpenAI 团队的最新研究工作，值得重点关注其技术路线；来自 Meta 团队的最新研究工作，值得重点关注其技术路线"
        },
        {
          "title": "iARCS: Iterative Agentic RL for Controllable 3D Scene Generation",
          "authors": "Saugat Adhikari, Ashok Prasad Neupane, Pramish Paudel",
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2608.06161",
          "tags": [
            "Agentic RL",
            "Agent",
            "Embodied AI"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nSynthetic 3D scene generation is increasingly used as a data source for computer vision and embodied AI, but existing generators often optimize perceptual realism without reliably satisfying...。\n【核心方法】We present iARCS, an iterative agentic reinforcement learning framework that adapts a pretrained scene generator to naturallanguage task requirements.。",
          "highlights": [
            "iARCS",
            "隶属于 cs.AI"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2608.06161",
          "readReason": "AI Agent 是当前研究热点，本文可能包含创新性的设计思路；Agentic 强化学习将决策与语言模型结合，是智能体研究的前沿方向"
        },
        {
          "title": "Verbal tics in frontier language models: A critical review of current releases, research evidence, and public discussion",
          "authors": "Shuai Wu, Xue Li, Zhijun Wang",
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2604.19139",
          "tags": [
            "OpenAI",
            "Anthropic",
            "Google"
          ],
          "summary": "【研究背景】该论文聚焦OpenAI领域。\nRepeated praise, canned reassurance, familiar contrasts, and conspicuous vocabulary are recurring subjects in discussions of large language models.。\n【核心方法】We propose separate measures of recurrence, contextual appropriateness, and belief distortion, with precise service records and language-specific annotation.。",
          "highlights": [
            "Verbal tics in frontier language models",
            "隶属于 cs.CL, cs.AI",
            "Repeated praise, canned reassurance, familiar contrasts, and conspicuous vocabulary are recurring subjects in discussion"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2604.19139",
          "readReason": "来自 OpenAI 团队的最新研究工作，值得重点关注其技术路线；来自 Anthropic 团队的最新研究工作，值得重点关注其技术路线"
        },
        {
          "title": "The Next Challenge for Agentic Cybersecurity: A Realistic, Contamination-Free Reverse Engineering Benchmark",
          "authors": "Jeremy Spence, Nicholas Assaderaghi, Feng Xiao",
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2608.11469",
          "tags": [
            "OpenAI",
            "Anthropic",
            "Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nEvaluating agentic RE poses a fundamental challenge: realistic benchmark instances must (1) be absent from LLMs' training data to prevent shortcuts by memorization, and (2) reflect the scale and...。\n【核心方法】We introduce SRE-Bench, the first realistic, contamination-free RE benchmark.。",
          "highlights": [
            "first realistic",
            "The Next Challenge for Agentic Cybersecurity",
            "隶属于 cs.CR, cs.AI"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2608.11469",
          "readReason": "AI Agent 是当前研究热点，本文可能包含创新性的设计思路；来自 OpenAI 团队的最新研究工作，值得重点关注其技术路线"
        },
        {
          "title": "EmbodiRSI: Recursive Self-Improvement for Data-Efficient Robot Adaptation",
          "authors": "Haoran Lang, Haotao Lu, Shiyu Sang",
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2609.38905",
          "tags": [
            "RSI",
            "Agent",
            "Embodied AI"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nAdapting robot manipulation policies to new tasks and environments remains highly data-intensive, while the data needed for further improvement depends on the policy's current capabilities and...。\n【实验结果】With 400 adaptive simulated trajectories and only ten real-world refinement trajectories per subtask, EmbodiRSI achieves 83.1% scene-balanced autonomous real-world success, compared with 75.。",
          "highlights": [
            "EmbodiRSI",
            "隶属于 cs.RO",
            "EmbodiRSI uses policy execution feedback to guide subsequent experience acquisition and policy updates."
          ],
          "pdfUrl": "https://arxiv.org/pdf/2609.38905",
          "readReason": "AI Agent 是当前研究热点，本文可能包含创新性的设计思路；递归自改进（RSI）是智能体自我进化的关键方向，本文具有一定的探索价值"
        },
        {
          "title": "Cross-Benchmark Transfer from RL on Agentic Coding Tasks",
          "authors": "Sushant Mehta, Logan Ritchie, Edwin Chen",
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.00890",
          "tags": [
            "Kimi",
            "Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\n001), and it remains significant on the three sets released after the training data was collected (p = 0.。\nWe ask whether reinforcement learning (RL) on expert-built agentic coding tasks closes this gap, and whether what the agent learns transfers beyond the training distribution.。\nThe reward is the fraction of target checks passed and drops to zero if any pass-to-pass test fails.。",
          "highlights": [
            "Cross",
            "隶属于 cs.LG, cs.AI",
            "The reward is the fraction of target checks passed and drops to zero if any pass-to-pass test fails."
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.00890",
          "readReason": "AI Agent 是当前研究热点，本文可能包含创新性的设计思路；来自 Kimi 团队的最新研究工作，值得重点关注其技术路线"
        },
        {
          "title": "False Prophets: On the Security of World Models in Agentic Systems",
          "authors": "Erik Imgrund, Anna Wimbauer, Klim Kireev",
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2607.23147",
          "tags": [
            "Agent",
            "World Model",
            "LLM"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nRecent research proposes to enhance predictive capabilities via specially trained environment simulators-world models.。\n【核心方法】we introduce a security benchmark dataset designed for text-based world models.。",
          "highlights": [
            "introduce a security benchmark dataset designed for text-based world model",
            "False Prophets",
            "隶属于 cs.CR, cs.AI"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2607.23147",
          "readReason": "AI Agent 是当前研究热点，本文可能包含创新性的设计思路；世界模型是提升模型泛化与规划能力的前沿方向，本文具有一定的探索价值"
        },
        {
          "title": "Global Coherence: When Every Agent Is Right and the Team Is Still Wrong - A Local-to-Global Semantic Foundation for Multi-Agent Collaboration",
          "authors": "Xin Heng",
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.02036",
          "tags": [
            "Agent",
            "Multi-Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nWe call this the global coherence problem: a failure of shared state, not merely of model intelligence.。\nAI agents can each make locally valid decisions yet jointly produce an invalid result.。\nOur Observation-Aliasing Impossibility Theorem gives the exact boundary.。\nA policy can guarantee a valid action exactly when all worlds producing the same observation share an admissible action.。",
          "highlights": [
            "exceed a shared budget in 5/5 runs",
            "Global Coherence",
            "隶属于 cs.AI"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.02036",
          "readReason": "AI Agent 是当前研究热点，本文可能包含创新性的设计思路；多智能体协作是复杂任务求解的重要范式，本文值得关注"
        },
        {
          "title": "How Much Can Language Models Gain from Test-Time Computation?",
          "authors": "Bangji Yang, Jingyuan Li, Jiajun Fan",
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.01110",
          "tags": [
            "Anthropic",
            "Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nHow much can test-time computation improve a language model, and at what cost?。\n【核心方法】We introduce SELF-POT, a benchmark and evaluation framework that measures the test-time potential of a model across competition mathematics, competitive programming, and agentic workflows.。",
          "highlights": [
            "How Much Can Language Models Gain from Test",
            "隶属于 cs.LG",
            "How much can test-time computation improve a language model, and at what cost?"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.01110",
          "readReason": "AI Agent 是当前研究热点，本文可能包含创新性的设计思路；来自 Anthropic 团队的最新研究工作，值得重点关注其技术路线"
        },
        {
          "title": "ROGUE: Evaluating Corrigibility Failures in Frontier Computer-Use Agents",
          "authors": "Jeremy Tien, Abishek Anand, Yu-Rou Tuan",
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2606.00341",
          "tags": [
            "Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nAlthough much work has focused on agent safety in the presence of an adversary, we study corrigibility: whether agents remain amenable to human correction, interruption, or shutdown while pursuing...。\n【核心方法】We introduce ROGUE, a benchmark in which agents are asked to complete realistic computer-use tasks but encounter controlled conflicts with human control, shutdown, or explicit resource restrictions.。",
          "highlights": [
            "ROGUE",
            "隶属于 cs.LG, cs.AI",
            "Further, independent task capability does not by itself imply greater corrigibility."
          ],
          "pdfUrl": "https://arxiv.org/pdf/2606.00341",
          "readReason": "AI Agent 是当前研究热点，本文可能包含创新性的设计思路；论文建立了新的基准评测，对后续研究有参考价值"
        },
        {
          "title": "VERITYGATE: A Four-Gate Schema-Level Faithfulness Framework and Paired Benchmark for Grounded LLM Narrations over Structured Evidence",
          "authors": "Sachin Gupta",
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.00833",
          "tags": [
            "OpenAI",
            "Anthropic",
            "Meta"
          ],
          "summary": "【研究背景】该论文聚焦OpenAI领域。\nFluent LLM explanations may not follow the evidence from a structured system.。\n【核心方法】We present VERITYGATE, a four-gate checker for declared evidence IDs, entities, numbers, and claim types.。",
          "highlights": [
            "VERITYGATE",
            "隶属于 cs.CL, cs.LG",
            "Fluent LLM explanations may not follow the evidence from a structured system."
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.00833",
          "readReason": "来自 OpenAI 团队的最新研究工作，值得重点关注其技术路线；来自 Anthropic 团队的最新研究工作，值得重点关注其技术路线"
        },
        {
          "title": "Measuring the Microtask Eligibility Gap: When Is an Off-the-Shelf SLM Enough for an Agent Harness?",
          "authors": "Jundong Hu, Shekar Ramachandran",
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.00025",
          "tags": [
            "Meta",
            "Qwen",
            "Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nAgent harnesses increasingly want to run small language models (SLMs) on the microtasks around a frontier large language model (LLM) planner: auto-approving shell commands, writing memory, selecting...。\nWe ask whether off-the-shelf SLMs meet practitioner-defined thresholds and, when they fail, why, and whether quantization changes the answer.。",
          "highlights": [
            "Measuring the Microtask Eligibility Gap",
            "隶属于 cs.AI, cs.LG",
            "We ask whether off-the-shelf SLMs meet practitioner-defined thresholds and, when they fail, why, and whether quantizatio"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.00025",
          "readReason": "AI Agent 是当前研究热点，本文可能包含创新性的设计思路；来自 Meta 团队的最新研究工作，值得重点关注其技术路线"
        },
        {
          "title": "Kepler: Auditable World Models for ARC-AGI-3",
          "authors": "Wensen Wu",
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.00834",
          "tags": [
            "OpenAI",
            "Anthropic",
            "Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nARC-AGI-3 evaluates agents in interactive environments whose rules and objectives must be inferred from observation.。\n【核心方法】We present Kepler, an open-source harness that represents hypotheses as executable world models and validates them through retrospective transition checks and conditional prediction checks.。",
          "highlights": [
            "Kepler",
            "隶属于 cs.AI, cs.MA",
            "ARC-AGI-3 evaluates agents in interactive environments whose rules and objectives must be inferred from observation."
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.00834",
          "readReason": "AI Agent 是当前研究热点，本文可能包含创新性的设计思路；来自 OpenAI 团队的最新研究工作，值得重点关注其技术路线"
        },
        {
          "title": "Agent Error Dataset: Scaling 50,000 Error--Diagnosis Pairs for Failure Analysis and Error-Aware Post-Training",
          "authors": "Kunlun Zhu, Xuyan Ye, Yibo Li",
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2609.40111",
          "tags": [
            "Qwen",
            "Agent",
            "LLM"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nAn unsuccessful LLM agent rollout contains more information than its final reward: the observations available to the agent, the actions it chose, and the environment's responses.。\n【核心方法】We introduce the Agent Error Dataset (AED), comprising 50,228 error-diagnosis pairs from 9,961 source tasks across 33 environments, 19 harness families, and 23 policy models in text-based agent systems.。",
          "highlights": [
            "Agent Error Dataset",
            "隶属于 cs.AI, cs.CL",
            "Reusing this experience for learning requires identifying a decision to revise and testing a concrete alternative."
          ],
          "pdfUrl": "https://arxiv.org/pdf/2609.40111",
          "readReason": "AI Agent 是当前研究热点，本文可能包含创新性的设计思路；大语言模型是当代 AI 的核心基座，本文对相关方向有参考价值"
        },
        {
          "title": "T2SPO: Trajectory-to-Step Policy Optimization for Agentic Reinforcement Learning",
          "authors": "Bo-Wen Zhang, Junwei He, Maoqi Liu",
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.00388",
          "tags": [
            "Agentic RL",
            "Agent",
            "LLM"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nT2SPO derives remaining-distance targets from successful trajectories and pairs them with representations of the states visited along the way.。\n【核心方法】We introduce Trajectory-to-Step Policy Optimization (T2SPO), a method that uses past interaction trajectories to provide step-level feedback for policy learning.。\n【主要贡献】5B and 7B language models on ALFWorld and WebShop show that T2SPO consistently improves overall task success over GRPO.。",
          "highlights": [
            "T2SPO",
            "隶属于 cs.LG, cs.AI",
            "Reinforcement learning enables large language model (LLM) agents to learn multi-step behaviors through interaction with "
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.00388",
          "readReason": "AI Agent 是当前研究热点，本文可能包含创新性的设计思路；Agentic 强化学习将决策与语言模型结合，是智能体研究的前沿方向"
        }
      ],
      "papers": [
        {
          "id": "A1",
          "anchorId": "A1",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "REVEAL: Robust Evolution of Vision-Language Models for Explainable AI-Video Detection",
          "authors": [
            "Yun-Yun Tsai",
            "Qingyuan Liu",
            "Ruijian Zha",
            "Victoria Li",
            "Pengyuan Shi",
            "Chengzhi Mao",
            "Junfeng Yang"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2502.14994",
          "tags": [
            "OpenAI",
            "Google",
            "Qwen"
          ],
          "summary": "【研究背景】该论文聚焦OpenAI领域。\nThe rapid advancement of AI-generated video poses challenges to digital authenticity and security.。\n【核心方法】We introduce a framework leveraging Vision Language Models (VLMs) for robust AI-generated video detection.。\n【实验结果】Experiments show that REVEAL improves F1 scores by 9.1% to 30.。",
          "highlights": [
            "introduce a framework leveraging Vision Language Model",
            "first benchmark VidForensic containing 1",
            "The rapid advancement of AI-generated video poses challenges to digital authenticity and security."
          ],
          "pdfUrl": "https://arxiv.org/pdf/2502.14994",
          "worthReading": true
        },
        {
          "id": "A2",
          "anchorId": "A2",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "SHARPO: Segment-Level Credit Assignment for Agentic Reinforcement Learning",
          "authors": [
            "Xinchen Du",
            "Zhengze Zhou",
            "Wenhui Zhu",
            "Han Yu",
            "Sen Na",
            "Rohit Jain",
            "Alborz Geramifard"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.00838",
          "tags": [
            "Qwen",
            "Agentic RL",
            "Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nTo address this limitation, we introduce Segment-level Hindsight Advantage Reweighting for Policy Optimization (SHARPO), a credit-assignment mechanism that refines Group Relative Policy Optimization...。\n【核心方法】we introduce Segment-level Hindsight Advantage Reweighting for Policy Optimization (SHARPO), a credit-assignment mechanism that refines Group Relative Policy Optimization (GRPO) at the level of environment-facing segments.。",
          "highlights": [
            "outperforms existing baselines on the ALFWorld and WebShop benchmarks",
            "SHARPO",
            "隶属于 cs.LG, cs.AI"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.00838",
          "worthReading": true
        },
        {
          "id": "A3",
          "anchorId": "A3",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "GUI-HARVEST: Self-Improving GUI Agents through Evidence-Driven Harness Evolution",
          "authors": [
            "Geyi Yang",
            "Zikun Qu",
            "Xiang Li",
            "Zhiyong Wang",
            "Min Zhang",
            "Shipei Zeng",
            "Zhongxiang Dai"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.00948",
          "tags": [
            "OpenAI",
            "Qwen",
            "RSI"
          ],
          "summary": "【研究背景】该论文聚焦递归自改进（RSI）领域。\nWith the same backbone and initial harness, GUI-HARVEST outperforms Self-Harness and Meta-Harness, suggesting that GUI-specific diagnosis and validation help harness improvements generalize to...。\n【核心方法】We introduce GUI-HARVEST, an automatic harness optimizer that enables self-improving GUI agents with frozen backbone models.。\n【实验结果】Frozen-harness transfer improves GPT-5 by 13.87 percentage points on WindowsAgentArena at 50 steps without further optimization.。",
          "highlights": [
            "outperforms Self-Harness and Meta-Harness",
            "GUI",
            "隶属于 cs.LG, cs.AI"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.00948",
          "worthReading": true
        },
        {
          "id": "A4",
          "anchorId": "A4",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "Do Your Own Research: Learning to Forecast by Learning to Search",
          "authors": [
            "Yusuf Afifi",
            "Artur Kiulian",
            "Anton Polishko",
            "Mykola Khandoga",
            "Hamudi Naanaa",
            "Alina Krasnobrizha"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.01955",
          "tags": [
            "Anthropic",
            "Qwen",
            "Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nOutcome-based reinforcement learning can train language models to forecast real-world events, but prior forecasting work either freezes research context before training or deploys agentic research...。\n【实验结果】Training changes how the agent interacts with information: calibration improves 30-40%, and search attempts fall from 3.。",
          "highlights": [
            "Do Your Own Research",
            "隶属于 cs.LG",
            "0.256, n=265), at about 5% of the inference cost, and its margin is widest on the hardest questions, the ones the crowd "
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.01955",
          "worthReading": true
        },
        {
          "id": "A5",
          "anchorId": "A5",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "Detecting Multi-Agent Collusion Through Multi-Agent Interpretability",
          "authors": [
            "Aaron Rose",
            "Carissa Cullen",
            "Sahar Abdelnabi",
            "Philip Torr",
            "Brandon Gary Kaplowitz",
            "Christian Schroeder de Witt"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2604.01151",
          "tags": [
            "Meta",
            "DeepSeek",
            "Qwen"
          ],
          "summary": "【研究背景】该论文聚焦Meta领域。\nWhile linear probes on model activations have shown promise for detecting deception in single-agent settings, collusion is inherently a multi-agent phenomenon, and the use of internal...。\n【核心方法】We introduce NARCBench, a benchmark for evaluating collusion detection under environment distribution shift, and propose five probing techniques that aggregate per-agent deception scores to classify scenarios at the group level, evaluated across...。",
          "highlights": [
            "propose five probing technique",
            "Detecting Multi",
            "隶属于 cs.AI, cs.LG"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2604.01151",
          "worthReading": true
        },
        {
          "id": "A6",
          "anchorId": "A6",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "Kernel-Managed Shared Memory for System-Wide Personalization",
          "authors": [
            "Ryan Lum",
            "Yongfeng Zhang"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2609.10144",
          "tags": [
            "OpenAI",
            "Meta",
            "Qwen"
          ],
          "summary": "【研究背景】该论文聚焦OpenAI领域。\nAI systems become more useful when they can adapt to the people using them, but in multi-agent systems, useful context learned by one agent often remains unavailable to others.。\n【核心方法】We present kernel-managed shared memory, a system-level abstraction in which specialized agents write structured, tagged memories while the agent-system kernel, not individual agents, governs retrieval, privacy enforcement, and prompt injection.。\n【实验结果】Against an unmanaged external memory backend (Mem0) using identical underlying storage, kernel-managed retrieval and injection improve personalization scores by 2.4-4.。",
          "highlights": [
            "Kernel",
            "隶属于 cs.AI, cs.LG",
            "Against standard retrieval-augmented injection, gains are similarly large and consistent across all three models."
          ],
          "pdfUrl": "https://arxiv.org/pdf/2609.10144",
          "worthReading": true
        },
        {
          "id": "A7",
          "anchorId": "A7",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "Verbal tics in frontier language models: A critical review of current releases, research evidence, and public discussion",
          "authors": [
            "Shuai Wu",
            "Xue Li",
            "Zhijun Wang",
            "Bolun Liu",
            "Weilin Cai",
            "Zihao Su",
            "Ran Wang"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2604.19139",
          "tags": [
            "OpenAI",
            "Anthropic",
            "Google"
          ],
          "summary": "【研究背景】该论文聚焦OpenAI领域。\nRepeated praise, canned reassurance, familiar contrasts, and conspicuous vocabulary are recurring subjects in discussions of large language models.。\n【核心方法】We propose separate measures of recurrence, contextual appropriateness, and belief distortion, with precise service records and language-specific annotation.。",
          "highlights": [
            "Verbal tics in frontier language models",
            "隶属于 cs.CL, cs.AI",
            "Repeated praise, canned reassurance, familiar contrasts, and conspicuous vocabulary are recurring subjects in discussion"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2604.19139",
          "worthReading": true
        },
        {
          "id": "A8",
          "anchorId": "A8",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "The Next Challenge for Agentic Cybersecurity: A Realistic, Contamination-Free Reverse Engineering Benchmark",
          "authors": [
            "Jeremy Spence",
            "Nicholas Assaderaghi",
            "Feng Xiao",
            "Jinhao Zhu",
            "Nikil Ravi",
            "Xiangyu Qi",
            "Matthew Jagielski",
            "Raluca Ada Popa",
            "Eric Wallace",
            "Guannan Wei",
            "Yangruibo Ding",
            "Zhuo Zhang"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2608.11469",
          "tags": [
            "OpenAI",
            "Anthropic",
            "Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nEvaluating agentic RE poses a fundamental challenge: realistic benchmark instances must (1) be absent from LLMs' training data to prevent shortcuts by memorization, and (2) reflect the scale and...。\n【核心方法】We introduce SRE-Bench, the first realistic, contamination-free RE benchmark.。",
          "highlights": [
            "first realistic",
            "The Next Challenge for Agentic Cybersecurity",
            "隶属于 cs.CR, cs.AI"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2608.11469",
          "worthReading": true
        },
        {
          "id": "A9",
          "anchorId": "A9",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "Cross-Benchmark Transfer from RL on Agentic Coding Tasks",
          "authors": [
            "Sushant Mehta",
            "Logan Ritchie",
            "Edwin Chen"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.00890",
          "tags": [
            "Kimi",
            "Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\n001), and it remains significant on the three sets released after the training data was collected (p = 0.。\nWe ask whether reinforcement learning (RL) on expert-built agentic coding tasks closes this gap, and whether what the agent learns transfers beyond the training distribution.。\nThe reward is the fraction of target checks passed and drops to zero if any pass-to-pass test fails.。",
          "highlights": [
            "Cross",
            "隶属于 cs.LG, cs.AI",
            "The reward is the fraction of target checks passed and drops to zero if any pass-to-pass test fails."
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.00890",
          "worthReading": true
        },
        {
          "id": "A10",
          "anchorId": "A10",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "How Much Can Language Models Gain from Test-Time Computation?",
          "authors": [
            "Bangji Yang",
            "Jingyuan Li",
            "Jiajun Fan",
            "Yi Evie Zhang",
            "Ruihan Guo",
            "Hongba Ma",
            "Neil He",
            "Chumeng Liang",
            "Qinglong Zheng",
            "Zhanghan Ni",
            "Ge Liu"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.01110",
          "tags": [
            "Anthropic",
            "Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nHow much can test-time computation improve a language model, and at what cost?。\n【核心方法】We introduce SELF-POT, a benchmark and evaluation framework that measures the test-time potential of a model across competition mathematics, competitive programming, and agentic workflows.。",
          "highlights": [
            "How Much Can Language Models Gain from Test",
            "隶属于 cs.LG",
            "How much can test-time computation improve a language model, and at what cost?"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.01110",
          "worthReading": true
        },
        {
          "id": "A11",
          "anchorId": "A11",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "VERITYGATE: A Four-Gate Schema-Level Faithfulness Framework and Paired Benchmark for Grounded LLM Narrations over Structured Evidence",
          "authors": [
            "Sachin Gupta"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.00833",
          "tags": [
            "OpenAI",
            "Anthropic",
            "Meta"
          ],
          "summary": "【研究背景】该论文聚焦OpenAI领域。\nFluent LLM explanations may not follow the evidence from a structured system.。\n【核心方法】We present VERITYGATE, a four-gate checker for declared evidence IDs, entities, numbers, and claim types.。",
          "highlights": [
            "VERITYGATE",
            "隶属于 cs.CL, cs.LG",
            "Fluent LLM explanations may not follow the evidence from a structured system."
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.00833",
          "worthReading": true
        },
        {
          "id": "A12",
          "anchorId": "A12",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "Measuring the Microtask Eligibility Gap: When Is an Off-the-Shelf SLM Enough for an Agent Harness?",
          "authors": [
            "Jundong Hu",
            "Shekar Ramachandran"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.00025",
          "tags": [
            "Meta",
            "Qwen",
            "Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nAgent harnesses increasingly want to run small language models (SLMs) on the microtasks around a frontier large language model (LLM) planner: auto-approving shell commands, writing memory, selecting...。\nWe ask whether off-the-shelf SLMs meet practitioner-defined thresholds and, when they fail, why, and whether quantization changes the answer.。",
          "highlights": [
            "Measuring the Microtask Eligibility Gap",
            "隶属于 cs.AI, cs.LG",
            "We ask whether off-the-shelf SLMs meet practitioner-defined thresholds and, when they fail, why, and whether quantizatio"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.00025",
          "worthReading": true
        },
        {
          "id": "A13",
          "anchorId": "A13",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "Kepler: Auditable World Models for ARC-AGI-3",
          "authors": [
            "Wensen Wu"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.00834",
          "tags": [
            "OpenAI",
            "Anthropic",
            "Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nARC-AGI-3 evaluates agents in interactive environments whose rules and objectives must be inferred from observation.。\n【核心方法】We present Kepler, an open-source harness that represents hypotheses as executable world models and validates them through retrospective transition checks and conditional prediction checks.。",
          "highlights": [
            "Kepler",
            "隶属于 cs.AI, cs.MA",
            "ARC-AGI-3 evaluates agents in interactive environments whose rules and objectives must be inferred from observation."
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.00834",
          "worthReading": true
        },
        {
          "id": "A14",
          "anchorId": "A14",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "Agent Error Dataset: Scaling 50,000 Error--Diagnosis Pairs for Failure Analysis and Error-Aware Post-Training",
          "authors": [
            "Kunlun Zhu",
            "Xuyan Ye",
            "Yibo Li",
            "Cheng Qian",
            "Beibin Li",
            "Heng Ji"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2609.40111",
          "tags": [
            "Qwen",
            "Agent",
            "LLM"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nAn unsuccessful LLM agent rollout contains more information than its final reward: the observations available to the agent, the actions it chose, and the environment's responses.。\n【核心方法】We introduce the Agent Error Dataset (AED), comprising 50,228 error-diagnosis pairs from 9,961 source tasks across 33 environments, 19 harness families, and 23 policy models in text-based agent systems.。",
          "highlights": [
            "Agent Error Dataset",
            "隶属于 cs.AI, cs.CL",
            "Reusing this experience for learning requires identifying a decision to revise and testing a concrete alternative."
          ],
          "pdfUrl": "https://arxiv.org/pdf/2609.40111",
          "worthReading": true
        },
        {
          "id": "A15",
          "anchorId": "A15",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "On-Device Named-Entity Recognition: A Deployability Study of Accuracy, Cost, Reliability, and Confidence",
          "authors": [
            "Vinay Kumar Chaganti"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.00007",
          "tags": [
            "DeepSeek",
            "Qwen",
            "Edge Computing"
          ],
          "summary": "【研究背景】该论文聚焦边缘计算与端云协同领域。\nNamed-entity recognition (NER) is increasingly wanted on-device (no API, low latency, data kept local).。\nThe practitioner's question is not the leaderboard but which model is deployable, how to evaluate it without human annotation, and whether its confidence can be trusted.。",
          "highlights": [
            "without human annotation",
            "On",
            "隶属于 cs.CL, cs.AI"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.00007",
          "worthReading": false
        },
        {
          "id": "A16",
          "anchorId": "A16",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "CompactionRL: Reinforcement Learning with Context Compaction for Long-Horizon Agents",
          "authors": [
            "Yujiang Li",
            "Zhenyu Hou",
            "Yi Jing",
            "Jie Tang",
            "Yuxiao Dong"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2607.05378",
          "tags": [
            "Agent",
            "LLM"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nContext compaction offers a natural solution by summarizing previous interaction states and continuing the rollout under a compressed context, but incorporating compaction into reinforcement...。\n【核心方法】We propose CompactionRL, a reinforcement learning strategy to train long-horizon agentic LLMs with context compaction.。\n【实验结果】5-Air model (106B-A12B) to achieve Pass@1 scores of 66.4% on SWE-bench Verified and 26.。",
          "highlights": [
            "exceed the maximum context length before a task is completed",
            "CompactionRL",
            "隶属于 cs.LG"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2607.05378",
          "worthReading": false
        },
        {
          "id": "A17",
          "anchorId": "A17",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "The Delegation Danger Band: Why Mid-Capability Sub-Agents Over-Trust Inherited Stale State",
          "authors": [
            "Jundong Hu",
            "Shekar Ramachandran"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.00041",
          "tags": [
            "Qwen",
            "Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nAgent frameworks increasingly delegate work by forking sub-agents; a common default makes the child inherit the parent's full working context.。\nWe measure how the effect of inherited state changes with capability, where $C_m$ denotes clean fork-fresh accuracy.。\nEvery task is solvable from the base evidence, so performance loss can be attributed to reliance on stale state.。",
          "highlights": [
            "The Delegation Danger Band",
            "隶属于 cs.MA, cs.AI",
            "Agent frameworks increasingly delegate work by forking sub-agents; a common default makes the child inherit the parent's"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.00041",
          "worthReading": false
        },
        {
          "id": "A18",
          "anchorId": "A18",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "MGSM-Pro: A Simple Strategy for Robust Multilingual Mathematical Reasoning Evaluation",
          "authors": [
            "Tianyi Xu",
            "Kosei Uemura",
            "Alfred Malengo Kondoro",
            "Tadesse Destaw Belay",
            "Catherine Nana Nyaah Essuman",
            "Ifeoma Okoh",
            "Ganiyat Afolabi",
            "Ayodele Awokoya",
            "David Ifeoluwa Adelani"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2601.21225",
          "tags": [
            "OpenAI",
            "Google",
            "DeepSeek"
          ],
          "summary": "【研究背景】该论文聚焦OpenAI领域。\nEvaluations across nine languages reveal that many low-resource languages suffer large performance drops when tested on digit instantiations different from those in the original test set.。\n【核心方法】we introduce MGSM-Pro, an extension of MGSM dataset with GSM-Symbolic approach.。",
          "highlights": [
            "MGSM",
            "隶属于 cs.CL, cs.AI",
            "Large language models have made substantial progress in mathematical reasoning."
          ],
          "pdfUrl": "https://arxiv.org/pdf/2601.21225",
          "worthReading": false
        },
        {
          "id": "A19",
          "anchorId": "A19",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "No Model Required: Text Entropy Rate Filtering Mitigates Iterative Fine-Tuning Collapse",
          "authors": [
            "Lewis Mitchell"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.01493",
          "tags": [
            "Meta",
            "Agent",
            "Multi-Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nIterative fine-tuning on synthetic data causes \\emph{model collapse}: output diversity narrows as rare patterns are progressively lost, a signature most visible as phrase-level repetition.。\n【核心方法】we develop a new approach grounded in mathematical information theory: the non-parametric Kontoyiannis entropy rate estimator $h_k$, computed entirely from raw text via match-length statistics, with no model of any kind.。\n【主要贡献】We show that this is in fact a \\emph{superior} training-data filter on text-diversity metrics in a fully-synthetic, single-lineage fine-tuning setting.。",
          "highlights": [
            "No Model Required",
            "隶属于 cs.CL, cs.AI",
            "Existing mitigations either require model log-probabilities, an external oracle, or continued access to real human data."
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.01493",
          "worthReading": false
        },
        {
          "id": "A20",
          "anchorId": "A20",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "Decentralized Multi-Agent Systems with Shared Context",
          "authors": [
            "Yuzhen Mao",
            "Jerry Gu",
            "Aadi Chauhan",
            "Qizheng Zhang",
            "Hangoo Kang",
            "Azalia Mirhoseini"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2606.10662",
          "tags": [
            "Anthropic",
            "Agent",
            "Multi-Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nMulti-agent systems (MAS) can scale large language model agents on long-horizon tasks by running them in parallel, yet existing designs waste much of this parallelism in bubbles: agent time spent...。\n【核心方法】We propose Decentralized Language Models (DeLM), a MAS framework on top of existing agent harnesses that squeezes out these bubbles by replacing the main agent with a shared context and a task queue.。",
          "highlights": [
            "propose Decentralized Language Model",
            "Decentralized Multi",
            "隶属于 cs.MA, cs.AI"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2606.10662",
          "worthReading": false
        },
        {
          "id": "A21",
          "anchorId": "A21",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "Finding the Right Fit: Model-Harness Interactions across Agent Tasks",
          "authors": [
            "Yixuan Li",
            "Yiyun Zhou",
            "Yao Long Teng",
            "Fuchao Yang",
            "Yanchen Deng",
            "Zhiyi Lyu",
            "Xuyu Dong",
            "Feng Chen",
            "Bo An"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.00917",
          "tags": [
            "Anthropic",
            "DeepSeek",
            "Kimi"
          ],
          "summary": "【研究背景】该论文聚焦Anthropic领域。\nGPT does best with PI's lean scaffold, while Kimi, which often issues malformed tool calls, does best in openJiuwen.。\nChoosing an agent system means choosing both a language model and the harness through which it acts.。\nWe ask whether a strong model, harness, or pairing stays strong when the setting changes.。",
          "highlights": [
            "Finding the Right Fit",
            "隶属于 cs.AI, cs.SE",
            "Choosing an agent system means choosing both a language model and the harness through which it acts."
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.00917",
          "worthReading": false
        },
        {
          "id": "A22",
          "anchorId": "A22",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "VeriHarness: Scaling Agentic Verification for Long-Horizon Tasks",
          "authors": [
            "Caiqi Zhang",
            "Rujun Han",
            "Zifeng Wang",
            "Zoey CuiZhu",
            "Nigel Collier",
            "Tomas Pfister",
            "Chen-Yu Lee"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.00972",
          "tags": [
            "Anthropic",
            "Google",
            "Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nA disagreement resolver checks competing claims against environmental evidence, while a consensus challenger tests shared claims and searches for omitted requirements.。\n【核心方法】We study how verification capability can be strengthened with a fixed base model, without access to reference answers or grading rubrics at test time.。\n【实验结果】Evidence-backed revision further improves average performance, bringing gains over a single rollout to 6.2 points with Gemini 3.。",
          "highlights": [
            "first find that disagreement often exposes correct alternatives",
            "VeriHarness",
            "隶属于 cs.AI, cs.MA"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.00972",
          "worthReading": false
        },
        {
          "id": "A23",
          "anchorId": "A23",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "FinEvo-Bench: A Longitudinal Benchmark for Self-Evolving Agents in Professional Financial Workflows",
          "authors": [
            "Bo Deng (Beihang University",
            "Qwen DianJin Team",
            "Alibaba Cloud Computing)",
            "Kang Zhou (Qwen DianJin Team",
            "Alibaba Cloud Computing)",
            "Lifan Guo (Qwen DianJin Team",
            "Alibaba Cloud Computing)",
            "Chongyang Tao (Beihang University)",
            "Xuanren Chen (Beihang University)",
            "Chenggang Xie (Beihang University)",
            "Renzhao Liang (Beihang University)",
            "Feng Chen (Qwen DianJin Team",
            "Alibaba Cloud Computing)",
            "Chi Zhang (Qwen DianJin Team",
            "Alibaba Cloud Computing)"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2608.06144",
          "tags": [
            "Anthropic",
            "Qwen",
            "RSI"
          ],
          "summary": "【研究背景】该论文聚焦递归自改进（RSI）领域。\n44 fewer compliance issues per task than their paired controls.。\n【核心方法】We introduce FinEvo-Bench, a longitudinal benchmark designed around this structure.。\n【实验结果】Paired score gains at within-scene ranks~4--6 exceed those at ranks~1--3 by 6.10--8.。",
          "highlights": [
            "exceed those at ranks~1--3 by 6",
            "FinEvo",
            "隶属于 cs.AI"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2608.06144",
          "worthReading": false
        },
        {
          "id": "A24",
          "anchorId": "A24",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "Scientific Agents: Evaluating Profession-Specific System Prompts on Scientific Tasks",
          "authors": [
            "Timothy Kassis"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.00084",
          "tags": [
            "Google",
            "Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nOn 60 tool-using BioMysteryBench bioinformatics problems (three runs each for baseline and profile), mean solve rates were 46.。\nDetailed profession-specific system prompts raise token use and estimated cost per response without a consistent accuracy gain.。\nWe evaluate Scientific Agents, an open-source corpus of 503 profession-specific AGENTS.md profiles, with Gemini 3.8 Flash via OpenRouter in the Pi agent harness.。",
          "highlights": [
            "Scientific Agents",
            "隶属于 cs.AI, cs.CL",
            "Detailed profession-specific system prompts raise token use and estimated cost per response without a consistent accurac"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.00084",
          "worthReading": false
        },
        {
          "id": "A25",
          "anchorId": "A25",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "Reputation, Strategy, and Emotion Effects on Generative AI Cooperation: A Comparison Across Reasoning and Non-Reasoning Models",
          "authors": [
            "Celso de Melo",
            "Zishan Feng",
            "James Hale",
            "Kazunori Terada",
            "Giorgio Coricelli",
            "Jonathan Gratch"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.01222",
          "tags": [
            "OpenAI",
            "Anthropic",
            "Google"
          ],
          "summary": "【研究背景】该论文聚焦OpenAI领域。\nAs generative AI (Gen AI) systems take on increasingly autonomous roles in economically and socially consequential interactions, understanding their propensity to cooperate -- and the signals that...。\nWe examine cooperative behavior in frontier Gen AI models using the iterated prisoner's dilemma, manipulating counterpart reputation (positive, unknown, negative), strategy (extortion vs.。\ngenerosity), and non-verbal emotional signaling (facial expressions conveying competitive or cooperative appraisals).。",
          "highlights": [
            "first study with non-reasoning models (Claude 3",
            "Reputation, Strategy, and Emotion Effects on Generative AI Cooperation",
            "隶属于 cs.AI"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.01222",
          "worthReading": false
        },
        {
          "id": "A26",
          "anchorId": "A26",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "Beyond Linear Concepts: Discovering and Aligning Non-Linear Concept Manifolds in Large Language Models",
          "authors": [
            "Tido Specht",
            "Elias Benedict Krey",
            "Nils Neukirch",
            "Nils Strodthoff"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.01821",
          "tags": [
            "Meta",
            "Qwen",
            "Agentic RL"
          ],
          "summary": "【研究背景】该论文聚焦Agentic 强化学习领域。\nWhile existing mechanistic interpretability (MI) methods seek to extract concepts, they are constrained by a strong linearity assumption challenged by evidence of non-linear feature manifolds.。\n【核心方法】we introduce a concept-based alignment (CBA) score, a generalized Rand index that measures geometric proximity without explicit feature matching.。",
          "highlights": [
            "Beyond Linear Concepts",
            "隶属于 cs.LG, cs.CL"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.01821",
          "worthReading": false
        },
        {
          "id": "A27",
          "anchorId": "A27",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "Your Language Model is Its Own Critic: Reinforcement Learning with Value Estimation from Actor's Internal States",
          "authors": [
            "Yunho Choi",
            "Jongwon Lim",
            "Woojin Ahn",
            "Minjae Oh",
            "Jeonghoon Shim",
            "Yohan Jo"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2605.07579",
          "tags": [
            "OpenAI",
            "Qwen",
            "Agentic RL"
          ],
          "summary": "【研究背景】该论文聚焦Agentic 强化学习领域。\nMoreover, the probe matches a separate LLM-scale value model, generalizes to various tasks, and remains accurate as the policy scales.。\n【核心方法】We introduce POISE (Policy Optimization with Internal State Value Estimation), a reinforcement learning algorithm that turns the model's internal states into a value model.。",
          "highlights": [
            "outperforms other RLVR baselines while achieving more stable training",
            "Your Language Model is Its Own Critic",
            "隶属于 cs.LG, cs.AI"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2605.07579",
          "worthReading": false
        },
        {
          "id": "A28",
          "anchorId": "A28",
          "group": "A",
          "groupName": "重点跟进（产业界 / 端云结合）",
          "title": "Characterizing a Configuration Where Inference-Time PRM-Pruned Fragment Grafting Is Inert: Evidence from Three Reasoning LMs",
          "authors": [
            "Khawaja Murad ul Hassan",
            "Mehran Ebrahimi"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.00047",
          "tags": [
            "Meta",
            "Qwen"
          ],
          "summary": "【研究背景】该论文聚焦Meta领域。\nA hindsight oracle bounds any per-problem gain from choosing PPFG over independent at +0.。\n该论文涉及Meta、Qwen等关键技术方向。",
          "highlights": [
            "Characterizing a Configuration Where Inference",
            "隶属于 cs.AI, cs.CL",
            "A hindsight oracle bounds any per-problem gain from choosing PPFG over independent at +0.13 pp."
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.00047",
          "worthReading": false
        },
        {
          "id": "B1",
          "anchorId": "B1",
          "group": "B",
          "groupName": "Agent / RSI / Agentic RL 主题",
          "title": "iARCS: Iterative Agentic RL for Controllable 3D Scene Generation",
          "authors": [
            "Saugat Adhikari",
            "Ashok Prasad Neupane",
            "Pramish Paudel",
            "Ajad Chhatkuli",
            "Danda Pani Paudel"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2608.06161",
          "tags": [
            "Agentic RL",
            "Agent",
            "Embodied AI"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nSynthetic 3D scene generation is increasingly used as a data source for computer vision and embodied AI, but existing generators often optimize perceptual realism without reliably satisfying...。\n【核心方法】We present iARCS, an iterative agentic reinforcement learning framework that adapts a pretrained scene generator to naturallanguage task requirements.。",
          "highlights": [
            "iARCS",
            "隶属于 cs.AI"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2608.06161",
          "worthReading": true
        },
        {
          "id": "B2",
          "anchorId": "B2",
          "group": "B",
          "groupName": "Agent / RSI / Agentic RL 主题",
          "title": "EmbodiRSI: Recursive Self-Improvement for Data-Efficient Robot Adaptation",
          "authors": [
            "Haoran Lang",
            "Haotao Lu",
            "Shiyu Sang",
            "Haoyang Luo",
            "Guo Chen",
            "Qun Li",
            "Jingyi Yu",
            "Ye Shi",
            "Jingya Wang"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2609.38905",
          "tags": [
            "RSI",
            "Agent",
            "Embodied AI"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nAdapting robot manipulation policies to new tasks and environments remains highly data-intensive, while the data needed for further improvement depends on the policy's current capabilities and...。\n【实验结果】With 400 adaptive simulated trajectories and only ten real-world refinement trajectories per subtask, EmbodiRSI achieves 83.1% scene-balanced autonomous real-world success, compared with 75.。",
          "highlights": [
            "EmbodiRSI",
            "隶属于 cs.RO",
            "EmbodiRSI uses policy execution feedback to guide subsequent experience acquisition and policy updates."
          ],
          "pdfUrl": "https://arxiv.org/pdf/2609.38905",
          "worthReading": true
        },
        {
          "id": "B3",
          "anchorId": "B3",
          "group": "B",
          "groupName": "Agent / RSI / Agentic RL 主题",
          "title": "False Prophets: On the Security of World Models in Agentic Systems",
          "authors": [
            "Erik Imgrund",
            "Anna Wimbauer",
            "Klim Kireev",
            "Konrad Rieck"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2607.23147",
          "tags": [
            "Agent",
            "World Model",
            "LLM"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nRecent research proposes to enhance predictive capabilities via specially trained environment simulators-world models.。\n【核心方法】we introduce a security benchmark dataset designed for text-based world models.。",
          "highlights": [
            "introduce a security benchmark dataset designed for text-based world model",
            "False Prophets",
            "隶属于 cs.CR, cs.AI"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2607.23147",
          "worthReading": true
        },
        {
          "id": "B4",
          "anchorId": "B4",
          "group": "B",
          "groupName": "Agent / RSI / Agentic RL 主题",
          "title": "Global Coherence: When Every Agent Is Right and the Team Is Still Wrong - A Local-to-Global Semantic Foundation for Multi-Agent Collaboration",
          "authors": [
            "Xin Heng"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.02036",
          "tags": [
            "Agent",
            "Multi-Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nWe call this the global coherence problem: a failure of shared state, not merely of model intelligence.。\nAI agents can each make locally valid decisions yet jointly produce an invalid result.。\nOur Observation-Aliasing Impossibility Theorem gives the exact boundary.。\nA policy can guarantee a valid action exactly when all worlds producing the same observation share an admissible action.。",
          "highlights": [
            "exceed a shared budget in 5/5 runs",
            "Global Coherence",
            "隶属于 cs.AI"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.02036",
          "worthReading": true
        },
        {
          "id": "B5",
          "anchorId": "B5",
          "group": "B",
          "groupName": "Agent / RSI / Agentic RL 主题",
          "title": "ROGUE: Evaluating Corrigibility Failures in Frontier Computer-Use Agents",
          "authors": [
            "Jeremy Tien",
            "Abishek Anand",
            "Yu-Rou Tuan",
            "Yuchen Shen",
            "J. Zico Kolter",
            "Aran Nayebi"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2606.00341",
          "tags": [
            "Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nAlthough much work has focused on agent safety in the presence of an adversary, we study corrigibility: whether agents remain amenable to human correction, interruption, or shutdown while pursuing...。\n【核心方法】We introduce ROGUE, a benchmark in which agents are asked to complete realistic computer-use tasks but encounter controlled conflicts with human control, shutdown, or explicit resource restrictions.。",
          "highlights": [
            "ROGUE",
            "隶属于 cs.LG, cs.AI",
            "Further, independent task capability does not by itself imply greater corrigibility."
          ],
          "pdfUrl": "https://arxiv.org/pdf/2606.00341",
          "worthReading": true
        },
        {
          "id": "B6",
          "anchorId": "B6",
          "group": "B",
          "groupName": "Agent / RSI / Agentic RL 主题",
          "title": "T2SPO: Trajectory-to-Step Policy Optimization for Agentic Reinforcement Learning",
          "authors": [
            "Bo-Wen Zhang",
            "Junwei He",
            "Maoqi Liu",
            "Feiran Li",
            "Song-Lin Lv",
            "Wentao Ma",
            "Rongyi Lin",
            "Shuhan Zhong",
            "Lan-Zhe Guo"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.00388",
          "tags": [
            "Agentic RL",
            "Agent",
            "LLM"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nT2SPO derives remaining-distance targets from successful trajectories and pairs them with representations of the states visited along the way.。\n【核心方法】We introduce Trajectory-to-Step Policy Optimization (T2SPO), a method that uses past interaction trajectories to provide step-level feedback for policy learning.。\n【主要贡献】5B and 7B language models on ALFWorld and WebShop show that T2SPO consistently improves overall task success over GRPO.。",
          "highlights": [
            "T2SPO",
            "隶属于 cs.LG, cs.AI",
            "Reinforcement learning enables large language model (LLM) agents to learn multi-step behaviors through interaction with "
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.00388",
          "worthReading": true
        },
        {
          "id": "B7",
          "anchorId": "B7",
          "group": "B",
          "groupName": "Agent / RSI / Agentic RL 主题",
          "title": "Learning Meta-Skills for Agent Harness Design in Test-Time AI4AI",
          "authors": [
            "Cheng Qian",
            "Kunlun Zhu",
            "Beibin Li",
            "Zhenhailong Wang",
            "Heng Ji"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2609.38143",
          "tags": [
            "RSI",
            "Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nWe study test-time AI-for-AI, asking how a Builder can learn to construct better execution environments for a Target while both models' weights remain fixed.。\n【核心方法】we introduce Meta-Skill: principles specifying when support is needed and what resources to provide.。\n【实验结果】Across Harness-Bench and NewtonBench, full-bank meta-skills improve macro-average performance by 8.95 percentage points over no-skill construction, and 12.。",
          "highlights": [
            "Learning Meta",
            "隶属于 cs.AI, cs.CL",
            "Agent performance depends on both reasoning ability and the environment in which it acts."
          ],
          "pdfUrl": "https://arxiv.org/pdf/2609.38143",
          "worthReading": false
        },
        {
          "id": "B8",
          "anchorId": "B8",
          "group": "B",
          "groupName": "Agent / RSI / Agentic RL 主题",
          "title": "Worse Together: How Performance Breaks Down in Multi-User Multi-Agent Teams",
          "authors": [
            "Sahan Paliskara",
            "Nattaput Namchittai",
            "Andrew Lampinen"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.00583",
          "tags": [
            "Agent",
            "Multi-Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nPeople are increasingly delegating tasks to AI agents, and those agents are increasingly encountering other people's agents over shared resources such as a codebase, a calendar, or a budget.。\nWhen each agent acts for a different user with different goals, coordination often fails, and the group ends up worse off than if a single agent had acted for everyone.。\nIn each scenario, we compare a single agent that serves every user (a coordinator) to a team in which each agent serves one user, with and without a communication channel between the agents.。",
          "highlights": [
            "Worse Together",
            "隶属于 cs.AI",
            "For example, in the personal assistant environment, the coordinator fulfills a targeted user request about twice as ofte"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.00583",
          "worthReading": false
        },
        {
          "id": "B9",
          "anchorId": "B9",
          "group": "B",
          "groupName": "Agent / RSI / Agentic RL 主题",
          "title": "Dependency-Aware Reward Shaping for Agentic Reinforcement Learning",
          "authors": [
            "Ziyi Chen",
            "Yan Zhang",
            "Jianhui Wei",
            "Daoan Zhang",
            "Zuozhu Liu"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.01207",
          "tags": [
            "Agentic RL",
            "Agent",
            "LLM"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nCommon methods for assigning step credit overlook that work built on uncorrected mistakes is wasted while independent work remains valid.。\n【核心方法】We propose Dependency-Aware Reward Shaping (DARS), which represents task progress as predicates linked by prerequisite relations and assigns step-level credit over the dependency graph.。",
          "highlights": [
            "exceeds OmniOPD in controlled tool-free reasoning comparisons at 1",
            "Dependency",
            "隶属于 cs.AI"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.01207",
          "worthReading": false
        },
        {
          "id": "B10",
          "anchorId": "B10",
          "group": "B",
          "groupName": "Agent / RSI / Agentic RL 主题",
          "title": "Self-Evolving Coding Rules for AI Coding Agents",
          "authors": [
            "Zhengyuan Jiang",
            "Reachal Wang",
            "Yuepeng Hu",
            "Yupu Wang",
            "Yuqi Jia",
            "Neil Zhenqiang Gong"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.00650",
          "tags": [
            "RSI",
            "Agent",
            "LLM"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nIn each iteration, it employs an LLM-powered mutator module to generate variants from existing candidates, and then uses a judge module to evaluate these variants and update the pool with the...。\n【核心方法】we propose RuleEvolve, a self-evolving framework for coding rules.。",
          "highlights": [
            "outperforms both manual engineering and existing prompt optimization baselines in terms of functional correctness of the",
            "Self",
            "隶属于 cs.CL, cs.AI"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.00650",
          "worthReading": false
        },
        {
          "id": "B11",
          "anchorId": "B11",
          "group": "B",
          "groupName": "Agent / RSI / Agentic RL 主题",
          "title": "CompMat-Bench: Benchmarking AI Agents for Computational Materials Science",
          "authors": [
            "Chenmu Zhang",
            "Levi Felix",
            "Jun-Jie Zhang",
            "Xingfu Li",
            "Xuelian Jiang",
            "Tao Jiang",
            "Subhendu Mishra",
            "Xixi Qin",
            "Boris Yakobson"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.00636",
          "tags": [
            "Agent",
            "LLM"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nWe introduce CompMat-Bench, a benchmark of 94 tasks derived from recently published computational materials studies, each asking agents to complete a step toward achieving the study's scientific goal.。\n【核心方法】We introduce CompMat-Bench, a benchmark of 94 tasks derived from recently published computational materials studies, each asking agents to complete a step toward achieving the study's scientific goal.。",
          "highlights": [
            "CompMat",
            "隶属于 cs.AI, cond-mat.mtrl-sci",
            "Evaluating AI agents on scientific research tasks is constrained by the time and resources required for the underlying e"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.00636",
          "worthReading": false
        },
        {
          "id": "B12",
          "anchorId": "B12",
          "group": "B",
          "groupName": "Agent / RSI / Agentic RL 主题",
          "title": "SWE-chat: Coding Agent Interactions From Real Users in the Wild",
          "authors": [
            "Joachim Baumann",
            "Vishakh Padmakumar",
            "Xiang Li",
            "John Yang",
            "Diyi Yang",
            "Sanmi Koyejo"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2604.20779",
          "tags": [
            "Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nAI coding agents are being adopted at scale, yet we lack empirical evidence on how people actually use them and how much of their output is useful in practice.。\n【核心方法】We present SWE-chat, the first large-scale dataset of real coding agent sessions collected from open-source developers in the wild.。",
          "highlights": [
            "first large-scale dataset of real coding agent sessions collected from open-source developers in the wild",
            "SWE",
            "隶属于 cs.AI, cs.CY"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2604.20779",
          "worthReading": false
        },
        {
          "id": "B13",
          "anchorId": "B13",
          "group": "B",
          "groupName": "Agent / RSI / Agentic RL 主题",
          "title": "Crossing the Cyber Divide: Sim-to-Sim and Sim-to-Real Transfer for RL Agents",
          "authors": [
            "Sabrina Saika",
            "Yinuo Du",
            "Aritran Piplai"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.00759",
          "tags": [
            "Agentic RL",
            "Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nThis limitation hinders both deployment and fair comparison, as cyber simulators differ substantially in their state representations, observation models, and action spaces.。\n【核心方法】We propose a framework that separates state alignment from action translation, enabling a policy trained in one environment to operate in another without retraining.。\n【实验结果】Our experiments show that zero-shot transfer is feasible, fully preserving source-policy performance in closely aligned environments and achieving 45.2% win rates when transferring policies whose...。",
          "highlights": [
            "propose a framework",
            "without retraining",
            "We evaluate transfer across four cyber platforms, CyberBattleSim, NetSecGame, CyberWheel, and NASim, including emulated "
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.00759",
          "worthReading": false
        },
        {
          "id": "B14",
          "anchorId": "B14",
          "group": "B",
          "groupName": "Agent / RSI / Agentic RL 主题",
          "title": "A Channel-Boosted Multi-Agent System with Iterative Consultation for Document Sensitivity Classification",
          "authors": [
            "Aleesha Zainab",
            "Asifullah Khan",
            "Muhammad Ahmed Khalid",
            "Faheem Ullah Khan"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2609.22212",
          "tags": [
            "Agent",
            "Multi-Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nHowever, transformer baselines suffer from a structural limitation: fixed input length truncation discards evidence beyond the retained window-precisely where sensitive cables tend to be longest.。\n【核心方法】We present Channel-Boosted MAS (CB-MAS) and instantiate it as IC-MAS (Iterative Consultation Multi-Agent System) to solve this without long-context computational costs.。\n【实验结果】Critic-Controlled Gated Channel Boosting with Max-Pool fusion and Blackboard Adaptive Consultation achieves 90.72% accuracy, 91.。",
          "highlights": [
            "A Channel",
            "隶属于 cs.CL, cs.LG",
            "Organizations in critical national infrastructure sectors must assess heterogeneous documents for sensitivity before rou"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2609.22212",
          "worthReading": false
        },
        {
          "id": "B15",
          "anchorId": "B15",
          "group": "B",
          "groupName": "Agent / RSI / Agentic RL 主题",
          "title": "Incident-Arena: Getting agents to the last nine of reliability",
          "authors": [
            "Andre Fu",
            "Malik Drabla",
            "Leon Liu",
            "Meji Abidoye",
            "Marek Suppa",
            "Lata Mishra",
            "Adnan El Assadi",
            "Yiyuan Li"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.00648",
          "tags": [
            "Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nAI coding agents are ubiquitous in engineering workflows amongst industry and academia.。\n【核心方法】We introduce Incident-Arena, a human-built benchmark of 20 carefully selected tasks grounded in real-world deployed open source software.。",
          "highlights": [
            "present a novel verification method",
            "Incident",
            "隶属于 cs.AI"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.00648",
          "worthReading": false
        },
        {
          "id": "B16",
          "anchorId": "B16",
          "group": "B",
          "groupName": "Agent / RSI / Agentic RL 主题",
          "title": "KaliBench: A Fine-Grained Benchmark for Cybersecurity Tool Use on Kali Linux with Runtime-Free Verifiable Rewards",
          "authors": [
            "Pengfei Li",
            "Naufal Suryanto",
            "Sicheng Zhang",
            "Muzammal Naseer"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.02206",
          "tags": [
            "Agent",
            "LLM"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nLLMs are increasingly applied to cybersecurity workflows, where they are expected to translate analysts' intent into tool invocations.。\n【核心方法】We introduce KaliBench, a fine-grained benchmark and dataset for natural-language--to--CLI translation on Kali Linux, comprising 8,504 query--command pairs spanning 1,642 tools across 23 capability dimensions and 5 security phases.。\n【实验结果】Across three evaluation modes and 24 configurations of general-purpose and security-focused open-weight models, no open-weight model exceeds 42% exact-command accuracy in the unrestricted setting,...。",
          "highlights": [
            "exceeds 42% exact-command accuracy in the unrestricted setting",
            "KaliBench",
            "隶属于 cs.CL, cs.AI"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.02206",
          "worthReading": false
        },
        {
          "id": "B17",
          "anchorId": "B17",
          "group": "B",
          "groupName": "Agent / RSI / Agentic RL 主题",
          "title": "Safety of Latent Communication in Multi-Agent Systems",
          "authors": [
            "Muhammad Huzaifa",
            "Sina Mavali",
            "Thorsten Eisenhofer"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2609.39788",
          "tags": [
            "Agent",
            "Multi-Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nIn this work, we show that even benign link training can increase harmful compliance relative to text-based communication while the underlying safety-aligned agents remain unchanged.。\n【主要贡献】In this work, we show that even benign link training can increase harmful compliance relative to text-based communication while the underlying safety-aligned agents remain unchanged.。",
          "highlights": [
            "Safety of Latent Communication in Multi",
            "隶属于 cs.AI, cs.LG",
            "To this end, lightweight trainable links are introduced to map the sender's representations into the receiver's input sp"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2609.39788",
          "worthReading": false
        },
        {
          "id": "B18",
          "anchorId": "B18",
          "group": "B",
          "groupName": "Agent / RSI / Agentic RL 主题",
          "title": "Sapien: A Stateful Policy Engine for Autonomous AI Agents",
          "authors": [
            "Corinn Tiffany",
            "Wen Zhang",
            "Eugene Bagdasarian",
            "Lillian Tsai"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.00797",
          "tags": [
            "Agent"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nContextual security defenses prevent AI agents from taking rogue actions by synthesizing a task-specific policy and enforcing it on the agent's tool calls.。\n【核心方法】We present Sapien, a policy engine for enforcing stateful contextual policies.。\n【主要贡献】We show that Sapien stays within a few percent of an unconstrained agent's utility.。",
          "highlights": [
            "Sapien",
            "隶属于 cs.AI, cs.CL",
            "In multi-step tasks, however, which actions are valid often depends on what the agent has already done and learned."
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.00797",
          "worthReading": false
        },
        {
          "id": "B19",
          "anchorId": "B19",
          "group": "B",
          "groupName": "Agent / RSI / Agentic RL 主题",
          "title": "Pay for the Fault, Not the Flow: Label-Free In-Flow Multi-Agent Workflow Optimization",
          "authors": [
            "Xuehang Guo",
            "Haoyu Wang",
            "Shengyu Chen",
            "Zach Chen",
            "Wei Cheng",
            "Qingyun Wang",
            "Haifeng Chen"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.01017",
          "tags": [
            "Agent",
            "Multi-Agent",
            "LLM"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nHowever, building such a workflow well remains challenging: how finely to divide the task, which agent to trust with each subtask, and when to create a new specialist are all critical decisions a...。\n【核心方法】We propose InFlowOp, which prices every decision in one label-free cost that weighs how well an agent's competence meets what a subtask demands against how much that agent takes to run.。",
          "highlights": [
            "outperforms single agent baselines by up to $+11",
            "Pay for the Fault, Not the Flow",
            "隶属于 cs.AI, cs.CL"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.01017",
          "worthReading": false
        },
        {
          "id": "B20",
          "anchorId": "B20",
          "group": "B",
          "groupName": "Agent / RSI / Agentic RL 主题",
          "title": "Beyond Final Accuracy: Auditing Communication in LLM Multi-Agent Systems",
          "authors": [
            "Shixuan Li",
            "Wei Yang",
            "Peiyu Zhang",
            "Anzhe Cheng",
            "Heng Ping",
            "Paul Bogdan"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.01042",
          "tags": [
            "Agent",
            "Multi-Agent",
            "LLM"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nThese findings challenge treating communication quality as an intrinsic property of a channel.。\n【核心方法】We introduce Independent--Communicate--Revise (ICR), a controlled framework that evaluates communication as answer revision following independent reasoning.。",
          "highlights": [
            "Beyond Final Accuracy",
            "隶属于 cs.AI, cs.CL",
            "Multi-agent communication aims to help agents benefit from one another's information."
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.01042",
          "worthReading": false
        },
        {
          "id": "B21",
          "anchorId": "B21",
          "group": "B",
          "groupName": "Agent / RSI / Agentic RL 主题",
          "title": "Counting Moves, Weighing Voices: Bayesian Dialectical Argumentation for Calibrated Multi-LLM Councils under Persistent Adversaries",
          "authors": [
            "Ionel Eduard Stan",
            "Paolo Napoletano"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.02005",
          "tags": [
            "Agent",
            "Multi-Agent",
            "LLM"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nAs these systems become increasingly used for reasoning, that confidence should represent a calibrated \\emph{probability of being correct}, and the decision should remain robust when some agents are...。\n【核心方法】We introduce Bayesian Dialectical Argumentation (BDA), which treats the council's \\emph{typed} moves---who proposed, challenged, or conceded which answer---as observations of a classical annotator model with \\emph{per-agent} reliabilities.。",
          "highlights": [
            "Counting Moves, Weighing Voices",
            "隶属于 cs.AI"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.02005",
          "worthReading": false
        },
        {
          "id": "B22",
          "anchorId": "B22",
          "group": "B",
          "groupName": "Agent / RSI / Agentic RL 主题",
          "title": "Mimir: Physics-Grounded LLM Agents for Long-Horizon Irrigation Control",
          "authors": [
            "Yimeng Liu",
            "Mi Zhang",
            "Younsuk Dong",
            "Zhichao Cao"
          ],
          "venue": "arXiv 2026",
          "arxivId": "arXiv:2610.02038",
          "tags": [
            "RSI",
            "Agent",
            "LLM"
          ],
          "summary": "【研究背景】该论文聚焦AI智能体（Agent）领域。\nAt the slow timescale, recurrent failure patterns are consolidated into persistent contextual principles that condition future proposals, while the physical model, evaluator, and execution...。\n【核心方法】We present Mimir, a physics-grounded LLM agent organized around two repair timescales.。\n【实验结果】Under a common retrospective evaluator across multiple sites, crops, and years, Mimir attains the lowest reported aggregate control cost among the evaluated references and uses about 51% less...。",
          "highlights": [
            "Mimir",
            "隶属于 cs.AI",
            "We study this regime through irrigation, where daily decisions interact with soil-water dynamics over entire growing sea"
          ],
          "pdfUrl": "https://arxiv.org/pdf/2610.02038",
          "worthReading": false
        }
      ]
    }
  ]
};
