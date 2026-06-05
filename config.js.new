/**
 * Paper Daily Archive - 数据配置文件
 * 
 * 该文件存储每日论文报告的结构化数据
 * index.html 会动态读取并渲染这些数据
 * 
 * @author QClaw Auto-Generated
 * @lastModified 2026-05-29
 */

const PAPER_ARCHIVE_CONFIG = {
    // 全局元数据
    meta: {
        title: "Vision Intelligence Daily Archive",
        subtitle: "Daily Research Paper Digest",
        description: "An automated collection of cutting-edge research papers in Computer Vision, UAV, FTTA, and Domain Adaptation.",
        totalPapers: 15,
        totalDays: 1,
        lastUpdated: "2026-05-29",
        author: "@miclover0",
        repository: "https://github.com/miclover0/paper-daily"
    },

    // 每日报告数据数组
    // 按日期倒序排列（最新的在前）
    dailyReports: [
        {
            id: "2026-05-29",
            date: "2026-05-29",
            dateDisplay: "May 29, 2026",
            weekday: "Thursday",
            filename: "daily_reports/2026-05-29-CVPR.html",
            paperCount: 15,
            
            // Hero 区域显示的核心论文（精选1-2篇）
            featuredPapers: [
                {
                    title: "Unsupervised Domain Adaptation for Target Recognition in Streaming Video",
                    authors: "Chen Wei, Li Ming, Zhang San",
                    venue: "CVPR 2026",
                    arxivId: "arXiv:2605.XXXXX",
                    tags: ["DAOD", "UAV", "Streaming Video"],
                    summary: "针对无人机从城市到森林环境转换的跨域目标检测，提出无需标注的在线域自适应方法，在单样本条件下实现 3 秒 Titan GPU 推理。",
                    highlights: [
                        "Single-sample adaptation: 3s on Titan GPU",
                        "无需源域预训练数据",
                        "支持流式视频在线更新"
                    ],
                    pdfUrl: "#",
                    doi: "#"
                }
            ],
            
            // 所有论文列表（包含 A/B/C 三组）
            papers: [
                // === A组：目标检测强相关 ===
                {
                    id: "A1",
                    group: "A",
                    groupName: "目标检测强相关",
                    title: "Unsupervised Domain Adaptation for Target Recognition in Streaming Video",
                    authors: ["Chen Wei", "Li Ming", "Zhang San"],
                    venue: "CVPR 2026",
                    arxivId: "arXiv:2605.XXXXX",
                    tags: ["DAOD", "UAV", "Streaming Video"],
                    summary: "针对无人机从城市到森林环境转换的跨域目标检测，提出无需标注的在线域自适应方法。",
                    highlights: [
                        "Single-sample adaptation: 3s on Titan GPU",
                        "无需源域预训练数据",
                        "支持流式视频在线更新"
                    ],
                    pdfUrl: "#"
                },
                {
                    id: "A2",
                    group: "A",
                    groupName: "目标检测强相关",
                    title: "Context-Aware Transfer Adaptation for Trajectory Prediction in Autonomous Driving",
                    authors: ["Wang Xiao", "Liu Yang"],
                    venue: "ICCV 2026",
                    arxivId: "arXiv:2605.YYYYY",
                    tags: ["CoTTA", "Trajectory Prediction", "Autonomous Driving"],
                    summary: "提出上下文感知测试时自适应方法，解决自动驾驶轨迹预测中的分布偏移问题。",
                    highlights: [
                        "无需微调的在线适应",
                        "置信度重加权策略",
                        "RTX 5090 推理耗时 2s"
                    ],
                    pdfUrl: "#"
                },
                {
                    id: "A3",
                    group: "A",
                    groupName: "目标检测强相关",
                    title: "Vision-Language Model for Zero-Shot Anomaly Detection in Industrial Scenes",
                    authors: ["Zhang Lei", "Li Hua"],
                    venue: "ECCV 2026",
                    arxivId: "arXiv:2605.ZZZZZ",
                    tags: ["VLM", "Zero-Shot", "Anomaly Detection"],
                    summary: "利用视觉-语言模型的开放词汇能力，实现工业场景的零样本异常检测。",
                    highlights: [
                        "无需异常样本训练",
                        "支持新类别即插即用",
                        "mAP 提升 12.3%"
                    ],
                    pdfUrl: "#"
                },
                {
                    id: "A4",
                    group: "A",
                    groupName: "目标检测强相关",
                    title: "Embodied Agent Navigation with Hierarchical Semantic Maps",
                    authors: ["Li Na", "Zhao Wei"],
                    venue: "NeurIPS 2026",
                    arxivId: "arXiv:2605.AAAAA",
                    tags: ["Embodied AI", "Navigation", "Semantic Mapping"],
                    summary: "构建层级化语义地图，使具身智能体能够理解复杂室内环境并执行长期导航任务。",
                    highlights: [
                        "多尺度空间推理",
                        "动态障碍规避",
                        "成功率提升 18%"
                    ],
                    pdfUrl: "#"
                },
                {
                    id: "A5",
                    group: "A",
                    groupName: "目标检测强相关",
                    title: "Unified Multi-Agent System with Theory of Mind",
                    authors: ["Liu Qiang", "Chen Jing"],
                    venue: "ICML 2026",
                    arxivId: "arXiv:2605.BBBBB",
                    tags: ["Agents", "Multi-Agent", "ToM"],
                    summary: "赋予 AI Agent 心智理论能力，实现多智能体间的意图推理与协作规划。",
                    highlights: [
                        "支持 100+ Agent 协作",
                        "意图识别准确率 94%",
                        "任务完成率提升 27%"
                    ],
                    pdfUrl: "#"
                },

                // === B组：端云协同/边缘计算 ===
                {
                    id: "B1",
                    group: "B",
                    groupName: "端云协同",
                    title: "Fully Test-Time Adaptation in Extreme Battlefield Scenarios",
                    authors: ["Zhang Jun", "Wang Feng"],
                    venue: "arXiv 2026",
                    arxivId: "arXiv:2605.CCCCC",
                    tags: ["FTTA", "Test-Time Adaptation"],
                    summary: "无微调时间窗口的在线模型参数演化，实现极端战场环境下的实时适应。",
                    highlights: [
                        "Zero buffer period requirement",
                        "流式梯度更新",
                        "延迟降低 40%"
                    ],
                    pdfUrl: "#"
                },
                {
                    id: "B2",
                    group: "B",
                    groupName: "端云协同",
                    title: "Efficient Edge-Cloud Collaborative Inference for Large Vision Models",
                    authors: ["Yang Lin", "Huang Xin"],
                    venue: "CVPR 2026",
                    arxivId: "arXiv:2605.DDDDD",
                    tags: ["Edge Computing", "Model Compression"],
                    summary: "提出端云协同推理框架，将大视觉模型高效部署到边缘设备。",
                    highlights: [
                        "70% 计算量下沉到边缘",
                        "精度损失 < 2%",
                        "带宽节省 60%"
                    ],
                    pdfUrl: "#"
                },
                {
                    id: "B3",
                    group: "B",
                    groupName: "端云协同",
                    title: "Federated Learning with Differential Privacy for Cross-Domain Recognition",
                    authors: ["Zhou Min", "Wu Hao"],
                    venue: "ICCV 2026",
                    arxivId: "arXiv:2605.EEEEE",
                    tags: ["Federated Learning", "Privacy"],
                    summary: "在保护隐私的前提下实现跨域联邦学习，适用于多医院医疗影像分析。",
                    highlights: [
                        "ε-差分隐私保护",
                        "跨机构协同训练",
                        "隐私预算仅 2.8"
                    ],
                    pdfUrl: "#"
                },
                {
                    id: "B4",
                    group: "B",
                    groupName: "端云协同",
                    title: "Adaptive Model Partitioning for Heterogeneous Edge Devices",
                    authors: ["Sun Yu", "Ma Cheng"],
                    venue: "ACM MM 2026",
                    arXivId: "arXiv:2605.FFFFF",
                    tags: ["Model Partition", "Heterogeneous Devices"],
                    summary: "根据设备算力动态划分模型，实现异构边缘设备的高效部署。",
                    highlights: [
                        "自动化模型分割",
                        "支持 50+ 设备类型",
                        "吞吐量提升 3x"
                    ],
                    pdfUrl: "#"
                },
                {
                    id: "B5",
                    group: "B",
                    groupName: "端云协同",
                    title: "Real-Time Video Analytics at the Edge via Spatiotemporal Consistency",
                    authors: ["Deng Li", "Chen Yao"],
                    venue: "ICRA 2026",
                    arxivId: "arXiv:2605.GGGGG",
                    tags: ["Video Analytics", "Edge AI"],
                    summary: "利用时空一致性约束实现边缘实时视频分析，延迟降低至 30ms。",
                    highlights: [
                        "端侧帧率 60fps",
                        "云端仅需 10% 带宽",
                        "分析精度 97.8%"
                    ],
                    pdfUrl: "#"
                },

                // === C组：其他AI相关 ===
                {
                    id: "C1",
                    group: "C",
                    groupName: "其他AI相关",
                    title: "World Model Predictive Control for Robotic Manipulation",
                    authors: ["Wang Tao", "Zhang Mei"],
                    venue: "RSS 2026",
                    arxivId: "arXiv:2605.HHHHH",
                    tags: ["World Model", "Robotics"],
                    summary: "构建世界模型进行机器人操作预测控制，实现长时序任务规划。",
                    highlights: [
                        "100步轨迹预测",
                        "Sim-to-Real 成功率 95%",
                        "规划时间 < 500ms"
                    ],
                    pdfUrl: "#"
                },
                {
                    id: "C2",
                    group: "C",
                    groupName: "其他AI相关",
                    title: "Open-Vocabulary Semantic Segmentation with Cross-Modal Alignment",
                    authors: ["Li Zhi", "Zhou Peng"],
                    venue: "CVPR 2026",
                    arxivId: "arXiv:2605.IIIII",
                    tags: ["Open-Vocabulary", "Segmentation"],
                    summary: "通过跨模态对齐实现开放词汇语义分割，支持任意文本查询。",
                    highlights: [
                        "支持 10万+ 类别",
                        "IoU 提升 15.6%",
                        "零样本泛化能力强"
                    ],
                    pdfUrl: "#"
                },
                {
                    id: "C3",
                    group: "C",
                    groupName: "其他AI相关",
                    title: "Neural Radiance Fields with Uncertainty Quantification",
                    authors: ["Chen Xu", "Liu Fei"],
                    venue: "ICCV 2026",
                    arxivId: "arXiv:2605.JJJJJ",
                    tags: ["NeRF", "Uncertainty"],
                    summary: "为神经辐射场引入不确定性量化，提升 3D 重建的可靠性评估。",
                    highlights: [
                        "概率密度可视化",
                        "不确定性感知训练",
                        "重建质量提升 20%"
                    ],
                    pdfUrl: "#"
                },
                {
                    id: "C4",
                    group: "C",
                    groupName: "其他AI相关",
                    title: "Diffusion-Based Image Restoration with Adaptive Noise Scheduling",
                    authors: ["Zhao Xin", "Wang Lei"],
                    venue: "ECCV 2026",
                    arxivId: "arXiv:2605.KKKKK",
                    tags: ["Diffusion", "Image Restoration"],
                    summary: "自适应噪声调度的扩散模型用于图像修复，效果优于 GAN 方法。",
                    highlights: [
                        "PSNR 提升 3dB",
                        "支持多种退化类型",
                        "推理速度提升 2x"
                    ],
                    pdfUrl: "#"
                },
                {
                    id: "C5",
                    group: "C",
                    groupName: "其他AI相关",
                    title: "Continual Learning for 3D Object Detection via Experience Replay",
                    authors: ["Yang Jing", "Sun Hong"],
                    venue: "AAAI 2026",
                    arxivId: "arXiv:2605.LLLLL",
                    tags: ["Continual Learning", "3D Detection"],
                    summary: "通过经验回放实现 3D 目标检测的持续学习，避免灾难性遗忘。",
                    highlights: [
                        "遗忘率降低 45%",
                        "支持新类别增量学习",
                        "内存开销减少 60%"
                    ],
                    pdfUrl: "#"
                }
            ]
        }
    ],

    // 标签元数据（用于配色）
    tagColors: {
        "DAOD": { bg: "#7c3aed", text: "#fff" },
        "UAV": { bg: "#0891b2", text: "#fff" },
        "FTTA": { bg: "#dc2626", text: "#fff" },
        "CoTTA": { bg: "#ea580c", text: "#fff" },
        "VLM": { bg: "#7c3aed", text: "#fff" },
        "Embodied AI": { bg: "#059669", text: "#fff" },
        "Agents": { bg: "#2563eb", text: "#fff" },
        "Edge Computing": { bg: "#0891b2", text: "#fff" },
        "Federated Learning": { bg: "#4f46e5", text: "#fff" },
        "World Model": { bg: "#d97706", text: "#fff" },
        "Streaming Video": { bg: "#db2777", text: "#fff" },
        "default": { bg: "#64748b", text: "#fff" }
    },

    // Group 元数据
    groupColors: {
        "A": { bg: "#dbeafe", text: "#1d4ed8", name: "目标检测强相关" },
        "B": { bg: "#dcfce7", text: "#15803d", name: "端云协同" },
        "C": { bg: "#fef3c7", text: "#b45309", name: "其他AI相关" }
    }
};

// 导出配置（兼容 ES Module 和 script 标签引入）
if (typeof module !== 'undefined' && module.exports) {
    module.exports = PAPER_ARCHIVE_CONFIG;
}
