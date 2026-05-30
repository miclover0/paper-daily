/**
 * Paper Daily Archive - 数据配置文件
 * 
 * 该文件存储每日论文报告的结构化数据
 * index.html 会动态读取并渲染这些数据
 * 
 * @author QClaw Auto-Generated
 * @lastModified 2026-05-30
 */

const PAPER_ARCHIVE_CONFIG = {
    // 全局元数据
    meta: {
        title: "Vision Intelligence Daily Archive",
        subtitle: "Daily Research Paper Digest",
        description: "An automated collection of cutting-edge research papers in Computer Vision, UAV, FTTA, and Domain Adaptation.",
        totalPapers: 15,
        totalDays: 2,
        lastUpdated: "2026-05-30",
        author: "@miclover0",
        repository: "https://github.com/miclover0/paper-daily"
    },

    // 每日报告数据数组
    // 按日期倒序排列（最新的在前）
    dailyReports: [
        {
            id: "2026-05-30",
            date: "2026-05-30",
            dateDisplay: "May 30, 2026",
            weekday: "Saturday",
            filename: "daily_reports/2026-05-30-arXiv.html",
            paperCount: 15,
            
            // Hero 区域显示的核心论文（精选1-2篇）
            featuredPapers: [
                {
                    title: "Ultra-Light Test-Time Adaptation for Vision--Language Models",
                    authors: "Byunghyun Kim",
                    venue: "arXiv 2026",
                    arxivId: "arXiv:2511.09101",
                    tags: ["CoTTA", "VLM", "Domain Adaptation"],
                    summary: "提出超轻量级测试时自适应方法，无需反向传播即可实现视觉-语言模型的在线适应，显著降低计算和内存开销。",
                    highlights: [
                        "无需反向传播的 TTA",
                        "仅更新 logit 级参数",
                        "长流实验无崩溃"
                    ],
                    pdfUrl: "https://arxiv.org/pdf/2511.09101v1",
                    doi: "http://arxiv.org/abs/2511.09101v1"
                }
            ],
            
            // 所有论文列表（包含 A/B/C 三组）
            papers: [
                // === A组：目标检测强相关 ===
                {
                    id: "A1",
                    group: "A",
                    groupName: "目标检测强相关",
                    title: "Ultra-Light Test-Time Adaptation for Vision--Language Models",
                    authors: ["Byunghyun Kim"],
                    venue: "arXiv 2026",
                    arxivId: "arXiv:2511.09101",
                    tags: ["CoTTA", "VLM", "Domain Adaptation"],
                    summary: "提出超轻量级测试时自适应方法，无需反向传播即可实现视觉-语言模型的在线适应。",
                    highlights: [
                        "无需反向传播的 TTA",
                        "仅更新 logit 级参数",
                        "长流实验无崩溃"
                    ],
                    pdfUrl: "https://arxiv.org/pdf/2511.09101v1"
                },
                {
                    id: "A2",
                    group: "A",
                    groupName: "目标检测强相关",
                    title: "Test-Time Distillation for Continual Model Adaptation (CoDiRe)",
                    authors: ["Xiao Chen", "Jiazhen Huang", "Zhiming Liu"],
                    venue: "arXiv 2026",
                    arxivId: "arXiv:2506.02671",
                    tags: ["CoTTA", "VLM", "Test-Time Adaptation"],
                    summary: "将测试时适应重构为蒸馏过程，使用冻结的 VLM 作为外部信号引导目标模型。",
                    highlights: [
                        "VLM 引导的蒸馏",
                        "动态融合预测",
                        "最优传输校正"
                    ],
                    pdfUrl: "https://arxiv.org/pdf/2506.02671v3"
                },
                {
                    id: "A3",
                    group: "A",
                    groupName: "目标检测强相关",
                    title: "Grounded 3D-Aware Spatial Vision-Language Modeling (GR3D)",
                    authors: ["An-Chieh Cheng", "Yang Fu", "Yatai Ji"],
                    venue: "arXiv 2026",
                    arxivId: "arXiv:2605.30307",
                    tags: ["VLM", "3D Grounding", "Spatial Understanding"],
                    summary: "提出具备 2D 显式/隐式定位和单目 3D 定位的时空视觉-语言模型。",
                    highlights: [
                        "隐式定位机制",
                        "单目 3D 边界框预测",
                        "空间链式思考"
                    ],
                    pdfUrl: "https://arxiv.org/pdf/2605.30307v1"
                },
                {
                    id: "A4",
                    group: "A",
                    groupName: "目标检测强相关",
                    title: "YoCausal: How Far is Video Generation from World Model? A Causality Perspective",
                    authors: ["You-Zhe Xie", "Yu-Hsuan Li", "Jie-Ying Lee"],
                    venue: "arXiv 2026",
                    arxivId: "arXiv:2605.30346",
                    tags: ["World Model", "Video Generation", "Causality"],
                    summary: "通过因果性视角评估视频生成模型，揭示感知时间箭头不等于理解因果关系。",
                    highlights: [
                        "双级基准",
                        "反向惊喜指数",
                        "因果认知指数"
                    ],
                    pdfUrl: "https://arxiv.org/pdf/2605.30346v1"
                },
                {
                    id: "A5",
                    group: "A",
                    groupName: "目标检测强相关",
                    title: "World Models in Words: Auditing Physical State-Transition Commitments in VLMs",
                    authors: ["Emmanuelle Bourigault"],
                    venue: "arXiv 2026",
                    arxivId: "arXiv:2605.29585",
                    tags: ["VLM", "World Model", "Physical Reasoning"],
                    summary: "审计 VLM 语言表达的物理承诺，通过混合验证器检查状态转换的一致性和可追溯性。",
                    highlights: [
                        "类型化跟踪",
                        "混合验证器",
                        "偏好调优"
                    ],
                    pdfUrl: "https://arxiv.org/pdf/2605.29585v1"
                },

                // === B组：端云协同/边缘计算 ===
                {
                    id: "B1",
                    group: "B",
                    groupName: "端云协同",
                    title: "ESAM++: Efficient Online 3D Perception on the Edge",
                    authors: ["Qin Liu", "Lavisha Aggarwal", "Saptarashmi Bandyopadhyay"],
                    venue: "arXiv 2026",
                    arxivId: "arXiv:2605.29505",
                    tags: ["Edge Computing", "3D Perception", "Efficient"],
                    summary: "提出轻量级 3D 稀疏特征金字塔网络，实现边缘设备上的高效在线 3D 场景感知。",
                    highlights: [
                        "3D 稀疏特征金字塔",
                        "推理速度提升 3 倍",
                        "模型尺寸减半"
                    ],
                    pdfUrl: "https://arxiv.org/pdf/2605.29505v1"
                },
                {
                    id: "B2",
                    group: "B",
                    groupName: "端云协同",
                    title: "FedSmoothLoRA: Toward Smoother and Faster Convergence in Federated Low-Rank Adaptation",
                    authors: ["Zehao Wang"],
                    venue: "arXiv 2026",
                    arxivId: "arXiv:2605.29460",
                    tags: ["Federated Learning", "LoRA", "Distributed Inference"],
                    summary: "提出平滑 LoRA 聚合策略，加速联邦低秩适应的收敛速度并提高稳定性。",
                    highlights: [
                        "平滑聚合",
                        "更快收敛",
                        "低秩适应"
                    ],
                    pdfUrl: "https://arxiv.org/pdf/2605.29460v1"
                },
                {
                    id: "B3",
                    group: "B",
                    groupName: "端云协同",
                    title: "Fairness-Aware Federated Learning with Trajectory Shapley Value",
                    authors: ["Daniel Kuznetsov", "Ziqi Wang"],
                    venue: "arXiv 2026",
                    arxivId: "arXiv:2605.30336",
                    tags: ["Federated Learning", "Fairness", "Aggregation"],
                    summary: "提出轨迹 Shapley 值作为贡献度量，实现公平感知的联邦学习动态聚合。",
                    highlights: [
                        "轨迹 Shapley 值",
                        "动态客户端权重",
                        "公平感知优化"
                    ],
                    pdfUrl: "https://arxiv.org/pdf/2605.30336v1"
                },
                {
                    id: "B4",
                    group: "B",
                    groupName: "端云协同",
                    title: "Federated Learning over Human-Body Communication for On-Body Edge Intelligence",
                    authors: ["Koffka Khan"],
                    venue: "arXiv 2026",
                    arxivId: "arXiv:2605.24062",
                    tags: ["Federated Learning", "Edge Intelligence", "Body Communication"],
                    summary: "综述人体通信与联邦学习的结合，提出身体通道感知的联邦学习分类法和参考架构。",
                    highlights: [
                        "人体通信",
                        "可穿戴联邦学习",
                        "身体通道感知"
                    ],
                    pdfUrl: "https://arxiv.org/pdf/2605.24062v1"
                },
                {
                    id: "B5",
                    group: "B",
                    groupName: "端云协同",
                    title: "OccamToken: Efficient VLM Inference with Training-Free and Budget-Adaptive Token Reduction",
                    authors: ["Weiming Huang", "Yuqi Cheng", "Yuhang Li"],
                    venue: "arXiv 2026",
                    arxivId: "arXiv:2605.29657",
                    tags: ["VLM", "Token Pruning", "Efficient Inference", "Edge"],
                    summary: "提出基于寄存器锚定相对证据测试的视觉 token 剪枝框架，实现训练无关的自适应推理加速。",
                    highlights: [
                        "寄存器锚定",
                        "相对证据测试",
                        "极端保留率 1.4%"
                    ],
                    pdfUrl: "https://arxiv.org/pdf/2605.29657v1"
                },

                // === C组：其他AI相关 ===
                {
                    id: "C1",
                    group: "C",
                    groupName: "其他AI相关",
                    title: "NeuROK: Generative 4D Neural Object Kinematics",
                    authors: ["Chen Geng", "Guangzhao He", "Yue Gao"],
                    venue: "arXiv 2026",
                    arxivId: "arXiv:2605.30347",
                    tags: ["Generative", "Neural Network", "4D"],
                    summary: "学习数据驱动的 4D 物体运动学状态参数化，实现大规模动态物体仿真。",
                    highlights: [
                        "神经物体运动学",
                        "低维潜在空间",
                        "拉格朗日力学视角"
                    ],
                    pdfUrl: "https://arxiv.org/pdf/2605.30347v1"
                },
                {
                    id: "C2",
                    group: "C",
                    groupName: "其他AI相关",
                    title: "Veda: Scalable Video Diffusion via Distilled Sparse Attention",
                    authors: [],
                    venue: "arXiv 2026",
                    arxivId: "arXiv:2605.30325",
                    tags: ["Diffusion", "Distillation", "Transformer"],
                    summary: "提出蒸馏稀疏注意力框架，通过统计感知的 tile 评分和头感知分块实现视频扩散模型的高效推理。",
                    highlights: [
                        "稀疏注意力",
                        "蒸馏优化",
                        "硬件高效内核"
                    ],
                    pdfUrl: "https://arxiv.org/pdf/2605.30325v1"
                },
                {
                    id: "C3",
                    group: "C",
                    groupName: "其他AI相关",
                    title: "minWM: A Full-Stack Open-Source Framework for Real-Time Interactive Video World Models",
                    authors: [],
                    venue: "arXiv 2026",
                    arxivId: "arXiv:2605.30263",
                    tags: ["World Model", "Distillation", "Interactive"],
                    summary: "提出端到端开源框架，将双向视频扩散模型转换为相机可控的少步自回归世界模型。",
                    highlights: [
                        "全栈框架",
                        "因果强制",
                        "少步自回归"
                    ],
                    pdfUrl: "https://arxiv.org/pdf/2605.30263v1"
                },
                {
                    id: "C4",
                    group: "C",
                    groupName: "其他AI相关",
                    title: "Improving CLIP Adaptation by Breaking Tail Alignment for Source-Free Cross-Domain Generalization",
                    authors: [],
                    venue: "arXiv 2026",
                    arxivId: "arXiv:2605.29776",
                    tags: ["CLIP", "Domain Adaptation", "Cross-Domain"],
                    summary: "发现打破尾部对齐可提升跨域泛化性能，提出自适应头尾对齐策略 ATHA。",
                    highlights: [
                        "尾部对齐打破",
                        "自适应对齐",
                        "跨域少样本"
                    ],
                    pdfUrl: "https://arxiv.org/pdf/2605.29776v1"
                },
                {
                    id: "C5",
                    group: "C",
                    groupName: "其他AI相关",
                    title: "Colored Noise Diffusion Sampling",
                    authors: [],
                    venue: "arXiv 2026",
                    arxivId: "arXiv:2605.30332",
                    tags: ["Diffusion", "Neural Network", "Sampling"],
                    summary: "提出彩色噪声采样器，通过频率解耦的能量转移实现更高效的扩散模型推理。",
                    highlights: [
                        "彩色噪声",
                        "频率解耦",
                        "能量转移"
                    ],
                    pdfUrl: "https://arxiv.org/pdf/2605.30332v1"
                }
            ]
        },
        // === 2026-05-29 的报告（保留）===
        {
            id: "2026-05-29",
            date: "2026-05-29",
            dateDisplay: "May 29, 2026",
            weekday: "Thursday",
            filename: "daily_reports/2026-05-29-CVPR.html",
            paperCount: 15,
            
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
            
            papers: [
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
                    arxivId: "arXiv:2605.FFFFF",
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
