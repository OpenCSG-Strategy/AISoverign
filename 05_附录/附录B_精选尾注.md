# 附录B　精选尾注

本书有意控制正文中的数字和机构名称。尾注只保留三类材料：支撑核心判断的一手文件、能够显示制度后果的可靠案例，以及供读者继续深入的经典研究。

涉及现行政策、技术倡议和机构页面的材料均核验至二〇二六年八月六日（个别标注除外），正式出版前应再次复核。

## 序章　智能权力的重新分配

[^p0-ai-world]: Stanford HAI，*The 2026 AI Index Report*。2025年超九成代表性前沿模型产自产业界；智能体在OSWorld等基准约三分之一失败。采用率不等于成熟部署。**置信度：已确认，口径受限。** https://hai.stanford.edu/ai-index/2026-ai-index-report ；https://hai.stanford.edu/ai-index/2026-ai-index-report/technical-performance

[^p0-ai-energy]: IEA，*Key Questions on Energy and AI*，2026年4月。五家大型科技企业2025年资本支出超四千亿美元；数据中心用电增长17%，受电网、变压器与芯片等瓶颈约束。**置信度：已确认；投资为情景估计。** https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary

[^p0-global-divide]: ILO、World Bank，*Disruption without dividend?*，2026年3月。覆盖135国、约全球三分之二就业：发展中经济体可能先承受扰动而较晚获益；职业暴露度不能直接预测失业。**置信度：已确认；长期因果待观察。** https://www.ilo.org/resource/news/new-ilo%E2%80%93world-bank-paper-highlights-uneven-global-impact-generative-ai-jobs

## 第一、二章　Token工厂与模型走出工厂

[^p1-ai-factory]: NVIDIA，*AI Factories: The New Infrastructure of Intelligence*，2026年5月27日及官方架构页。AI工厂是以算力、电力、网络和软件持续生产Token的系统，指标为每秒Token、每瓦Token、单位Token成本；厂商性能倍数未作科学结论。https://blogs.nvidia.com/blog/ai-factories-the-new-infrastructure-of-intelligence/ ；https://www.nvidia.com/en-us/solutions/ai-factories/

[^p1-token-factory-builds]: NVIDIA，xAI Colossus网络披露，2024年10月28日；Microsoft，Fairwater数据中心披露，2025年9月18日；Brad Smith，*The Golden Opportunity for American AI*，2025年1月3日。Colossus一期10万张Hopper GPU、约122天建成；Fairwater约315英亩、初始投资33亿美元；微软称2025财年投入约800亿美元。**置信度：项目方披露，成效待观察。** https://nvidianews.nvidia.com/news/spectrum-x-ethernet-networking-xai-colossus ；https://blogs.microsoft.com/blog/2025/09/18/inside-the-worlds-most-powerful-ai-datacenter/ ；https://blogs.microsoft.com/on-the-issues/2025/09/18/made-in-wisconsin-the-worlds-most-powerful-ai-datacenter/ ；https://blogs.microsoft.com/on-the-issues/2025/01/03/the-golden-opportunity-for-american-ai/

[^p1-tokenizer]: Hugging Face，*Summary of the tokenizers*；Taku Kudo、John Richardson，*SentencePiece*，EMNLP 2018。Token由分词器产生并映射为词表编号；不同模型、算法和语言的Token数量不统一。https://huggingface.co/docs/transformers/tokenizer_summary ；https://arxiv.org/abs/1808.06226

[^p1-transformer]: Ashish Vaswani等，*Attention Is All You Need*，NeurIPS 2017。提出以自注意力为核心的Transformer架构，是现代大语言模型的技术基础。https://proceedings.neurips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html

[^p1-chinchilla]: Jordan Hoffmann等，*Training Compute-Optimal Large Language Models*，NeurIPS 2022。参数与训练Token需合理配比：Chinchilla用约四倍于Gopher的数据，在相近预算下表现更好；不能外推所有架构。https://papers.neurips.cc/paper_files/paper/2022/hash/c1e2faff6f588870935f114ebe04a3e5-Abstract.html

[^p2-distillation]: Geoffrey Hinton等，*Distilling the Knowledge in a Neural Network*，2015年；Victor Sanh等，*DistilBERT*，2019年；DeepSeek-AI，*DeepSeek-R1*，2025年1月22日。分别显示集成行为可迁移到单模型、BERT可压缩、R1推理样本可训练较小的Qwen/Llama模型；不证明学生无损取得教师全部知识或安全属性。https://arxiv.org/abs/1503.02531 ；https://arxiv.org/abs/1910.01108 ；https://arxiv.org/abs/2501.12948

[^p2-distillation-dispute]: Anthropic，*Detecting and preventing distillation attacks*，2026年2月23日及*Commercial Terms of Service*。Anthropic称DeepSeek、Moonshot AI与MiniMax以约24,000个虚假账户与Claude交互超1,600万次；其条款禁止以访问服务训练竞争模型。规模与归因均为单方披露。https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks ；https://www.anthropic.com/legal/commercial-terms

[^p2-distillation-law]: *Thomson Reuters v. Ross Intelligence*，特拉华联邦地区法院，2025年2月11日；*Bartz v. Anthropic*，加州北区联邦地区法院，2025年6月23日及2026年7月20日批准的和解。前案否定Ross的合理使用抗辩；后案区分训练用途与取得方式：依法购买的书籍训练属合理使用，盗版书库不属于。两案不能拼成普遍规则。https://storage.courtlistener.com/recap/gov.uscourts.ded.72109/gov.uscourts.ded.72109.770.0.pdf ；https://www.courtlistener.com/docket/69058235/231/bartz-v-anthropic-pbc/ ；https://law.justia.com/cases/federal/district-courts/california/candce/4%3A2024cv05417/434709/680/

[^p2-synthetic-data]: Yizhong Wang等，*Self-Instruct*，ACL 2023；Ilia Shumailov等，*AI models collapse when trained on recursively generated data*，Nature，2024年7月。前者显示合成指令经生成、过滤、微调可提升特定任务表现；后者显示递归使用生成数据会丢失分布长尾。效果取决于真实数据锚点与筛选。https://aclanthology.org/2023.acl-long.754/ ；https://www.nature.com/articles/s41586-024-07566-y

[^p2-two-frontiers]: Jared Kaplan等，*Scaling Laws for Neural Language Models*，2020年；Jordan Hoffmann等，Chinchilla论文，2022年；Zhuohan Li等，*Train Large, Then Compress*，2020年；Stanford HAI，*AI Index 2025*；Microsoft，*Phi-3 Technical Report*；GPTQ、AWQ与QLoRA原始论文。损失随参数、数据、计算按幂律下降，但不支持"只加参数就更强"。AI Index的142倍参数变化仅针对MMLU百分之六十门槛；压缩收益受硬件与评测限制。https://arxiv.org/abs/2001.08361 ；https://papers.neurips.cc/paper_files/paper/2022/hash/c1e2faff6f588870935f114ebe04a3e5-Abstract.html ；https://arxiv.org/abs/2002.11794 ；https://hai.stanford.edu/ai-index/2025-ai-index-report/technical-performance ；https://arxiv.org/abs/2404.14219 ；https://arxiv.org/abs/2210.17323 ；https://arxiv.org/abs/2306.00978 ；https://arxiv.org/abs/2305.14314

[^p2-apertus]: ETH Zurich、EPFL与CSCS，*Apertus*，2025年9月2日及研究论文。发布8B与70B模型，约15万亿Token、覆盖一千多种语言，公开权重、数据、训练与评测代码和中间检查点。表现与"主权AI"主张来自项目方。https://ethz.ch/en/news-and-events/eth-news/news/2025/09/press-release-apertus-a-fully-open-transparent-multilingual-language-model.html ；https://doi.org/10.48550/arXiv.2509.14233

[^p2-apertus-mini]: Apertus团队，*Apertus Mini*，2026年6月15日；ETH AI Center，*Apertus 1.5*，2026年7月24日。从8B教师蒸馏出0.5B、1.5B、4B模型及量化版本，共16个模型；"训练计算量低至常规预训练约十分之一"为作者条件下报告。https://www.apertus-ai.org/articles/2026-06-apertus-mini/ ；https://arxiv.org/abs/2605.29128 ；https://ai.ethz.ch/news-and-events/ai-center-news/2026/07/apertus-15-building-the-next-generation-of-open-ai-infrastructure.html

[^p1-olmo2-scale]: Ai2，*OLMo 2 32B*技术材料，2025年。预训练约6万亿Token、约1280张H100，公开训练代码、数据、检查点和日志。**置信度：项目方披露；复现效果待验证。** https://allenai.org/blog/olmo2-32b

[^p1-mlperf]: MLCommons，*MLPerf Inference*及v5.1结果，2025年9月。在规定准确度目标下比较推理性能，报告首Token延迟、输出延迟与吞吐；结果受模型、精度、硬件和负载约束。https://docs.mlcommons.org/inference/ ；https://mlcommons.org/2025/09/mlperf-inference-v5-1-results/

[^p1-iea-energy]: IEA，*Energy and AI*，2025年。估算全球数据中心用电从2024年约415太瓦时升至2030年约945太瓦时，AI是重要驱动；估计含情景与不确定性。https://www.iea.org/reports/energy-and-ai/executive-summary

[^p1-inference-cost]: Stanford HAI，*AI Index 2025: State of AI in 10 Charts*。GPT-3.5水平模型每百万Token推理价格从2022年11月约20美元降至2024年10月约0.07美元；依赖选定阈值和公开价格，不等同物理边际成本。https://hai.stanford.edu/news/ai-index-2025-state-of-ai-in-10-charts

[^p1-prefill-decode]: NVIDIA，*Dynamo Overall Architecture*；Bingyang Wu等，*POD-Attention*，2024年。推理可区分Prefill（处理输入）与Decode（生成输出）并分离调度；厂商文档与论文结果受实验条件限制。https://docs.nvidia.com/dynamo/design-docs/overall-architecture ；https://arxiv.org/abs/2410.18038

[^p1-paged-attention]: Woosuk Kwon等，*PagedAttention*，SOSP 2023。KV Cache内存管理研究，指定条件下以相近延迟获相对对照系统二至四倍吞吐；不能外推为普遍收益。https://arxiv.org/abs/2309.06180

[^p2-agent-protocols]: Google，*Announcing the Agent2Agent Protocol*，2025年4月9日；Linux Foundation，A2A移交与生态更新；Agentic AI Foundation成立公告，2025年12月。A2A以Agent Card、Task、Message与Artifact支持智能体互操作，一周年支持机构超150家；AAIF最初托管MCP、goose与agents.md。开放协议解决交互语义，不自动解决身份、授权和结果可信。https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/ ；https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents ；https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year ；https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation

[^p2-deepseek-harness-2026]: DeepSeek，Harness开发者预览版（v0.1）发布页与GitHub仓库（MIT协议），2026年8月13日；The New Stack与Pandaily同期报道。模型适配器、工具注册、会话记录、沙箱、存储、界面与Agent循环均为Cordis内核上的可替换插件，提出"Model + Harness = Agent"；v0.1将有破坏性变更。**截至：2026-08-17；置信度：多源一致；生态影响待观察。** https://deepseek.com/harness/en/ ；https://github.com/deepseek-ai/deepseek-harness ；https://thenewstack.io/deepseek-harness-open-source-plugins/ ；https://pandaily.com/deepseek-harness-hands-on-four-modes-model-plus-harness-equals-agent-aug2026

[^p2-ntia-open-weights]: U.S. NTIA，*Dual-Use Foundation Models with Widely Available Model Weights Report*，2024年7月30日。基于332份公开意见，认为当时证据不足以支持对广泛可用权重作普遍限制，也不排除未来在新证据下采取措施。https://www.ntia.gov/programs-and-initiatives/artificial-intelligence/open-model-weights-report

[^p2-aws-ai-factories]: AWS，*Introducing AWS AI Factories*及FAQ，2025年12月。客户提供数据中心空间与电力、AWS部署和运营AI基础设施，说明设备位置、运营责任、数据控制和供应商依赖可形成混合安排。https://aws.amazon.com/about-aws/whats-new/2025/12/aws-ai-factories/ ；https://aws.amazon.com/about-aws/global-infrastructure/ai-factories/faqs/

[^p2-uk-sovereign-compute]: HM Government，*National Security Strategy 2025*。前沿技术的完全主权独立并不总是可能，主权算力是能力组合中独立服务国家优先事项的一部分；用于说明选择性自主。https://www.gov.uk/government/publications/national-security-strategy-2025-security-for-the-british-people-in-a-dangerous-world/national-security-strategy-2025-security-for-the-british-people-in-a-dangerous-world-html

[^p1-iea-ai]: IEA，*Key Questions on Energy and AI*及2026年4月16日更新。五家大型科技企业2025年资本支出超四千亿美元；数据中心用电增长百分之十七，AI数据中心更快。说明AI的物质基础，不直接证明投资效率。https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions

[^p1-ai-index-2026]: Stanford HAI，*The 2026 AI Index Report*。2025年超九成代表性前沿模型产自产业界，受访组织采用率达88%，智能体基准能力快速提高但仍有显著失败；采用率不等同成熟度。https://hai.stanford.edu/ai-index/2026-ai-index-report

[^p2-moving-frontier]: Stanford HAI，*AI Index 2026: Technical Performance*，截至2026年3月。Anthropic、xAI、Google与OpenAI的Arena评分相差不到25分，美中模型多次交换领先；最强封闭与最强开放模型差距从2024年8月约0.5%扩至2026年3月约3.3%。"open"主要指开放权重。https://hai.stanford.edu/ai-index/2026-ai-index-report/technical-performance

[^p1-cma-cloud]: UK CMA，*Cloud Services Market Investigation: Summary of Final Decision*，2025年7月31日。英国及欧洲经济区IaaS市场高度集中，Microsoft与AWS各占约百分之三十至四十，年更换服务商的客户不足百分之一；资本门槛、迁出费用、接口差异和技能不可转移被列为切换障碍。不能当作全球份额。https://assets.publishing.service.gov.uk/media/688b20e6ff8c05468cb7b120/summary_of_final_decision.pdf

[^p2-device-models]: Microsoft，*Phi-3 Technical Report*，2024年4月；Google，*Gemma 3n*说明；Apple，端侧与服务器基础模型材料，2024年6月及2025年7月。Phi-3-mini为3.8B参数、MMLU约69%；Apple约3B端侧模型在iPhone 15 Pro上约每秒30 Token，2025年版采用蒸馏和2-bit量化；Gemma 3n E2B有效内存负载约1.91B。不证明与云端通用模型等价。**置信度：官方材料。** https://arxiv.org/abs/2404.14219 ；https://machinelearning.apple.com/research/introducing-apple-foundation-models ；https://machinelearning.apple.com/research/apple-foundation-models-2025-updates ；https://ai.google.dev/gemma/docs/gemma-3n

[^p2-frontier-models-2026]: Moonshot AI，*Kimi K3*技术报告，2026年7月；DeepSeek，*DeepSeek V4*官方发布，2026年4月。K3披露2.8万亿总参数、约1040亿激活、896个专家；V4-Pro为1.6万亿/49B激活，V4-Flash为284B/约13B激活。不能用总参数直接判断超过GPT系列。**置信度：官方披露；比较为条件性结果。** https://github.com/MoonshotAI/Kimi-K3 ；https://arxiv.org/abs/2607.24653 ；https://api-docs.deepseek.com/news/news260424/ ；https://api-docs.deepseek.com/quick_start/pricing/

[^p2-small-model-family-2026]: Qwen团队，*Qwen3*发布与技术报告，2025年4月29日；Google DeepMind，Gemma发布记录与Gemma 3n说明；Qwen团队，*Qwen3-ASR Technical Report*，2026年1月。Qwen3覆盖0.6B至32B稠密及30B-A3B、235B-A22B MoE；Gemma提供270M至27B及端侧形态与多种专用模型；Qwen3-ASR提供0.6B与1.7B语音模型。**置信度：一手材料；横向比较不外推。** https://qwenlm.github.io/blog/qwen3/ ；https://arxiv.org/abs/2505.09388 ；https://ai.google.dev/gemma/docs/releases ；https://ai.google.dev/gemma/docs/gemma-3n ；https://arxiv.org/abs/2601.21337

[^p2-user-facing-2026]: DeepSeek，*Thinking Mode*与价格文档；OpenAI API参考文档；Qwen3、Kimi K3、Gemma 3n及Qwen3-ASR官方资料，均核验至2026年8月4日。服务可按思考模式、模型大小、上下文与路由策略调整等待、Token用量与成本；端侧模型承担窄任务。"思考Token"不等于完整可审计的内部过程。**置信度：官方材料；效果受实现限制。** https://api-docs.deepseek.com/guides/thinking_mode ；https://api-docs.deepseek.com/quick_start/pricing/ ；https://platform.openai.com/docs/api-reference/chat/create

[^p4-work-evidence]: Microsoft Research，*Shifting Work Patterns with Generative AI*，2025年4月；*Generative AI and the Nature of Work*，*Management Science*，2026年；METR开发者生产率研究，2025年7月。随机实验报告每周邮件时间减少约3小时；开发者任务数平均增加26.08%；METR报告完成时间增加19%。口径不同，不能合并成"AI普遍提高生产率"。**置信度：随机现场研究与预印本。** https://www.microsoft.com/en-us/research/publication/shifting-work-patterns-with-generative-ai/ ；https://pubsonline.informs.org/doi/10.1287/mnsc.2025.00535 ；https://arxiv.org/abs/2507.09089

[^p4-task-boundaries]: EAMT 2024英德机器翻译后编辑研究：译员偏好语音辅助但质量未改善；Noy、Zhang，*Science*，2023年：写作用时减少40%、质量提高18%；爱尔兰公共部门预注册实验，2025年：文档任务改善、数据分析任务质量下降12%。收益依赖任务边界。**置信度：同行评审与预印本。** https://aclanthology.org/2024.eamt-1.38/ ；https://doi.org/10.1126/science.adh2586 ；https://arxiv.org/abs/2502.09479

[^p4-finland-translation]: 赫尔辛基大学团队，*JMIR Formative Research*，2025年。4名内部译员完成908个翻译片段，GPT-4后编辑平均比人工基线快14%；芬兰语—瑞典语仅11%无需编辑。结果只适用于该团队与流程。**截至：2026-08-03；置信度：样本小。** https://doi.org/10.2196/73658

[^p4-argentina-ai]: 世界银行工作论文与NBER Working Paper 34851，*Does Generative AI Narrow Skill Productivity Gaps?*，2026年。GPT-4.1使阿根廷1,174名成年人商业分析任务的低/高技能组分差从0.548个标准差降至0.139，约闭合74%的基线差距。一次性任务，不能外推长期绩效、收入或就业。**截至：2026-08-03；置信度：随机实验已确认。** https://thedocs.worldbank.org/en/doc/5fa3b40f263a4a22e1572954980189c9-0370012026/original/5-Does-Generative-AI-narrow-skill-productivity-gaps.pdf ；https://www.nber.org/papers/w34851

[^p7-uk-government-ai]: UK GDS，*Microsoft 365 Copilot Experiment: Cross-Government Findings Report*，2025年6月2日；DSIT、GDS，*AI coding assistant trial*，2025年9月12日。前者覆盖12个政府组织约20000名员工；后者提供2500个代码助手许可并收集遥测与调查。部署规模已确认，不等于财政节省或生产率提升。**置信度：一手文件。** https://www.gov.uk/government/publications/microsoft-365-copilot-experiment-cross-government-findings-report ；https://www.gov.uk/government/publications/ai-coding-assistant-trial

## 第三章　为什么AI需要主权

[^p3-function-calling]: OpenAI，*Function calling and other API updates*，2023年6月13日。开发者结构化描述函数，模型生成函数名称与参数，实际调用仍由应用程序校验并执行；"调用意图"与"改变状态"由此分开。https://openai.com/index/function-calling-and-other-api-updates/

[^p3-react]: Shunyu Yao等，*ReAct*，ICLR 2023。研究语言模型交替生成推理轨迹与环境行动的结构；不证明模型拥有意识或稳定自主。https://openreview.net/forum?id=WE_vluYUL-X

[^p3-cruise]: U.S. NHTSA，*Consent Order with Cruise for Incomplete Crash Reporting*，2024年9月30日。Cruise未完整披露2023年10月2日事故后的拖行动作，被处150万美元处罚并要求两年内持续提交安全报告。Cruise系统不是大语言模型智能体，只作行动自动化的制度先例。https://www.nhtsa.gov/press-releases/consent-order-cruise-crash-reporting ；https://www.nhtsa.gov/sites/nhtsa.gov/files/2024-09/cruise-consent-order-2024-web.pdf

[^p3-a2a-task]: A2A Project，*Agent2Agent Protocol Specification*，核验至2026年8月1日。Task定义为具有唯一标识、状态与生命周期的工作单位，覆盖执行中、等待输入、完成、失败、取消等状态及Artifact交付；身份、权限和补救仍需具体实现。https://github.com/a2aproject/A2A/blob/main/docs/specification.md

[^p1-gdpr]: Regulation (EU) 2016/679，Article 20。数据主体有权以结构化、常用且机器可读的格式接收其个人数据，并传给另一控制者。https://eur-lex.europa.eu/eli/reg/2016/679/oj

[^p1-data-act]: Regulation (EU) 2023/2854（欧盟《数据法》），尤其第23—30条及第50条。自2025年9月12日起适用，含数据处理服务切换、机器可读导出、开放接口、业务连续和互操作等要求。https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R2854

[^p1-otel-genai]: OpenTelemetry，*GenAI Observability*及生成式AI语义约定，2026年5月14日。把模型调用、令牌使用、智能体调用与工具执行纳入分布式追踪；完整提示与回复属需选择性记录的敏感内容。https://opentelemetry.io/blog/2026/genai-observability/ ；https://opentelemetry.io/docs/specs/semconv/gen-ai/

[^p3-tech-sovereignty]: Christoph March、Ina Schieferdecker，*Technological Sovereignty as Ability, Not Autarky*，*International Studies Review*，2023年。技术主权是理解、评价、选择、获取、改造和使用关键技术的能力，与自给自足明确区分。https://doi.org/10.1093/isr/viad012 ；https://doi.org/10.1177/1461444819865984

## 第四章　AgenticOps：管理会行动的AI

[^p4-agenticops-origin]: OpenCSG，*AgenticOps: The Missing Operating System for Enterprise AI*，2025年7月24日。把AgenticOps定义为构建、部署、运行和持续改进AI智能体的端到端方法，提出八阶段及系统优先、运行数据、自动化、人在回路等原则；效率数字属项目方口径。**置信度：概念来源已确认。** https://medium.com/@OpenCSG/agenticops-the-missing-operating-system-for-enterprise-ai-4f536de1a844

[^p4-agentops-landscape]: Liming Dong等，*AgentOps: Enabling Observability of LLM Agents*，2024年；AWS，*AgentOps with Amazon Bedrock AgentCore*，2026年6月1日。前者提出智能体生命周期可观测性分类，后者概括为治理与安全、构建与运行、评测、可观测性四个支柱；术语范围尚不统一。**置信度：一手方法。** https://arxiv.org/abs/2411.05285 ；https://aws.amazon.com/blogs/machine-learning/agentops-operationalize-agentic-ai-at-scale-with-amazon-bedrock-agentcore/

[^p4-agent-security-2026]: NIST，*Summary Analysis of Responses to the RFI Regarding Security Considerations for AI Agents*，NIST AI 800-5，2026年5月18日。回应者广泛同意AI Agent带来新的安全威胁并形成采用障碍，传统网络安全原则仍相关但需适配。汇总不是事故率测量，也不等于强制标准。**置信度：NIST汇总。** https://www.nist.gov/publications/summary-analysis-responses-request-information-regarding-security-considerations-ai

[^p4-agent-engineering-methods-2026]: Anthropic，*Effective Context Engineering for AI Agents*，2025年9月29日；*Writing Effective Tools for AI Agents*，2025年9月11日；*Demystifying Evals for AI Agents*，2026年1月9日；Microsoft Research，*Retrospective Harness Optimization*，2026年6月。分别界定上下文工程、工具工程与评测驱动开发；RHO以轨迹重放进行自监督优化。正文"六类方法"是作者综合。**置信度：方法来源已确认。** https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents ；https://www.anthropic.com/engineering/writing-tools-for-agents ；https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents ；https://www.microsoft.com/en-us/research/publication/retrospective-harness-optimization-improving-llm-agents-via-self-preference-over-trajectory-rollouts/

[^p4-harness-engineering-2026]: Anthropic，*Effective Harnesses for Long-Running Agents*，2025年11月26日及*Harness Design for Long-Running Application Development*，2026年3月24日；OpenAI，*Harness Engineering*，2026年2月11日；Microsoft Agent Framework harness发布，2026年7月22日。三家分别把任务拆分与交接、仓库知识与验证、循环与遥测归入harness工程；均来自厂商自身系统。**置信度：多源一致。** https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents ；https://www.anthropic.com/engineering/harness-design-long-running-apps ；https://openai.com/index/harness-engineering/ ；https://devblogs.microsoft.com/agent-framework/the-microsoft-agent-framework-harness-is-now-released/

[^p4-managed-agents-2026]: Anthropic，*Scaling Managed Agents: Decoupling the Brain from the Hands*，2026年4月8日。把长任务系统拆为持久会话记录、Agent harness与沙箱/工具，通过接口使模型、运行循环和执行环境可独立变化或恢复。单一厂商实践，不证明唯一或最优。**置信度：厂商披露。** https://www.anthropic.com/engineering/managed-agents

[^p4-deepseek-harness-2026]: DeepSeek，Harness开发者预览版（v0.1）发布页与GitHub仓库（MIT协议），2026年8月13日；The New Stack与Pandaily同期报道。适配器、工具、会话、沙箱、界面与Agent循环均为Cordis内核上的可替换插件；v0.1将有破坏性变更，不作成熟度背书。**截至：2026-08-17；置信度：多源一致。** https://deepseek.com/harness/en/ ；https://github.com/deepseek-ai/deepseek-harness ；https://thenewstack.io/deepseek-harness-open-source-plugins/ ；https://pandaily.com/deepseek-harness-hands-on-four-modes-model-plus-harness-equals-agent-aug2026

[^p4-agent-evals-2026]: Anthropic，*Demystifying Evals for AI Agents*，2026年1月9日；*Quantifying Infrastructure Noise in Agentic Coding Evals*，2026年2月5日。前者把评测对象界定为模型与harness组成的系统；后者报告模型、任务和harness不变时，最严格与无限额资源设置的成功率相差6个百分点（p<0.01）。**置信度：方法披露；跨任务效度有限。** https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents ；https://www.anthropic.com/engineering/infrastructure-noise

[^p4-agent-hijacking-2026]: NIST CAISI，*Insights into AI Agent Security from a Large-Scale Red-Teaming Competition*，2026年3月23日。13个前沿模型、400多名参与者、超25万次攻击尝试中，所有目标模型都至少被成功劫持一次，部分攻击可跨模型迁移；不能换算为生产攻击率。**置信度：政府研究团队分析。** https://www.nist.gov/blogs/caisi-research-blog/insights-ai-agent-security-large-scale-red-teaming-competition

[^p4-agent-lifecycle-2026]: Microsoft，*Manage the Agent Lifecycle*，2026年7月14日。把Agent视为有持续责任人的产品，生命周期包括准入、分诊、构建、部署、监控、改进与退役。厂商CoE方法，不是独立标准。**置信度：厂商方法。** https://learn.microsoft.com/en-us/agents/center-of-excellence/agent-lifecycle

## 第五章　个人：AI主权从自己开始

[^p4-nist-agent-id]: NIST NCCoE，*New Concept Paper on Identity and Authority of Software Agents*，2026年2月5日。把软件与AI智能体的身份、授权、审计和不可抵赖列为专门议题；属研究与标准化倡议，并非定型标准。https://www.nist.gov/news-events/news/2026/02/new-concept-paper-identity-and-authority-software-agents

[^p4-mata]: U.S. District Court, SDNY，*Mata v. Avianca, Opinion and Order on Sanctions*，2023年6月22日。确认相关律师提交了ChatGPT生成的虚构判例及引文，并强调律师仍负有核验责任。https://www.nhd.uscourts.gov/sites/default/files/pdf/Mata-v-Avianca-sanctions-order.PDF

[^p4-cognition]: Eleanor Dillon等，*Shifting Work Patterns with Generative AI*，2025年，六个月、六千名知识工作者随机实验；Hao-Ping Lee等，*The Impact of Generative AI on Critical Thinking*，CHI 2025，319名知识工作者与936个用例。前者报告每周邮件时间减少约三小时；后者发现AI信心越高，自报批判性思考越少。一为行为测量，一为横截面自报，不能证明长期技能变化方向。https://www.microsoft.com/en-us/research/publication/shifting-work-patterns-with-generative-ai/ ；https://doi.org/10.1145/3706598.3713778

[^p4-derived-data]: U.S. FTC，Everalbum案和解与最终命令，2021年5月7日。FTC指控Everalbum就人脸识别和照片删除作出误导性陈述；最终命令要求删除相关照片、面部嵌入及用其开发的模型与算法。不决定生成式AI记忆或模型权重的一般法律归属。**置信度：FTC最终命令。** https://www.ftc.gov/news-events/news/press-releases/2021/05/ftc-finalizes-settlement-photo-app-developer-related-misuse-facial-recognition-technology ；https://www.ftc.gov/legal-library/browse/cases-proceedings/192-3172-everalbum-inc-matter

[^p4-replika]: 意大利个人数据保护机构，Replika处罚决定，2025年5月19日；EDPB案件摘要，2025年5月21日。对运营方Luka Inc.处以500万欧元罚款，认定未确定数据处理合法依据、隐私政策不足且未实施年龄验证；另案调查生成式AI数据处理合法性。**置信度：监管决定；另案待定。** https://www.gpdp.it/home/docweb/-/docweb-display/docweb/10132048 ；https://www.edpb.europa.eu/news/ai-the-italian-supervisory-authority-fines-company-behind-chatbot-replika_en

[^p4-opc-mechanism]: Ronald Coase，*The Nature of the Firm*，1937年及1991年诺贝尔奖演讲，以交易成本解释企业边界；写作实验用时下降40%；客服每小时解决问题数提高14%；AI在能力边界内改善表现、边界外降低正确率。不证明创业全流程可自动化。**置信度：经典论文与同行评审实验。** https://doi.org/10.1111/j.1468-0335.1937.tb00002.x ；https://www.nobelprize.org/prizes/economic-sciences/1991/coase/lecture/ ；https://doi.org/10.1126/science.adh2586 ；https://www.nber.org/papers/w31161 ；https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321

[^p4-opc-signal]: U.S. Census Bureau，2023年Nonemployer Statistics及2026年小企业数据：无雇员经营单位占全部经营单位78.4%，多数为自雇，不等于AI OPC；Stripe Atlas平台新设C公司中单一创始人占63%，存在选择偏差；OECD提醒一人企业就业贡献有限。只作新趋势信号。**置信度：官方统计与平台样本。** https://www.census.gov/library/stories/2026/05/small-business-week.html ；https://www.census.gov/library/stories/2025/07/nonemployer-business-growth.html ；https://stripe.com/blog/top-solo-founder-traits ；https://www.oecd.org/en/publications/international-compendium-of-entrepreneurship-policies_338f1873-en/full-report/objectives-and-challenges-of-entrepreneurship-policy_f354bd94.html

## 第六章　组织单元：让部门自治而能力协同

[^p5-zero-trust]: NIST，*Zero Trust Architecture*（SP 800-207，2020年）与SP 800-207A（2023年）。前者要求不因网络位置或资产归属自动信任，逐次、最小权限判断；后者把身份、API网关、服务网格与细粒度策略扩展到多云环境。正文据此类比企业内部部门域。

[^p5-beyondcorp]: Rory Ward、Betsy Beyer，*BeyondCorp*，Google Research，2014年。Google把访问控制从受信任内网转向以用户、设备与情境为基础的逐次判断。早于生成式AI的工程先例。**置信度：一手论文；AI场景为本书外推。** https://research.google/pubs/beyondcorp-a-new-approach-to-enterprise-security/

[^p5-uber-data-quality]: Uber Engineering，大数据平台、数据质量与数据文化三篇工程博客，2018年起，核验至2026年8月6日。分析平台超100PB；数据质量平台覆盖2000多个关键数据集，称发现约90%的数据质量事件；要求数据像代码一样有所有者与退役机制。数字均为Uber自报。**置信度：一手工程披露。** https://www.uber.com/us/en/blog/uber-big-data-platform/ ；https://www.uber.com/en-IE/blog/operational-excellence-data-quality/ ；https://www.uber.com/blog/ubers-journey-toward-better-data-culture-from-first-principles/

[^p5-workload-federation]: SPIFFE，*Concepts*与*Federation*规范，核验至2026年8月5日。以独立信任域管理工作负载身份；联邦规范允许不同管理域交换信任包并验证身份；不自动提供业务授权或AI安全。**置信度：官方规范；部门AI域属技术映射。** https://spiffe.io/docs/latest/spiffe/concepts/ ；https://spiffe.io/docs/latest/spiffe-specs/spiffe_federation/

## 第七章　企业：把智能变成可治理的能力

[^p6-knight]: U.S. SEC，*SEC Charges Knight Capital With Violations of Market Access Rule*，2013年10月16日。2012年8月1日开盘后45分钟内错误路由发送超400万条订单，造成超4.6亿美元损失；97封异常邮件未成为有效警报。https://www.sec.gov/newsroom/press-releases/2013-222

[^p6-industrial-copilot]: Siemens、thyssenkrupp，Industrial Copilot应用说明，2024年；Siemens工业AI编排架构。系统能生成结构化控制语言代码、辅助可视化和故障解释；编排架构把政策、安全与控制网关置于AI和PLC之间。功能与收益主要是厂商披露。**置信度：厂商披露。** https://press.siemens.com/global/en/pressrelease/siemens-industrial-copilot-expanded-adopted-thyssenkrupp ；https://www.siemens.com/en-gb/content/architecture-hub/industrial-ai-orchestration-layer/

[^p6-morgan-stanley]: Morgan Stanley，2023年与OpenAI合作公告及2024年Debrief发布材料；OpenAI客户案例。首个工具面向内部知识检索，Debrief在客户同意后生成会议笔记、行动项和邮件草稿，最终邮件由顾问编辑发送；效率数字主要来自公司与供应商，不能等同独立审计。https://www.morganstanley.com/press-releases/key-milestone-in-innovation-journey-with-openai ；https://www.morganstanley.com/press-releases/ai-at-morgan-stanley-debrief-launch ；https://openai.com/index/morgan-stanley/

[^p6-finra-genai]: FINRA，Regulatory Notice 24-09，2024年6月27日。现有规则技术中立，成员使用第三方生成式AI仍应建立与业务相适应的监督体系；不证明具体企业控制已有效。https://www.finra.org/rules-guidance/notices/24-09

[^p6-operator]: OpenAI，*Operator System Card*，2025年1月23日。无产品层防护的模型在100项近似真实任务中产生13次会造成麻烦的错误，其中5次较难逆转；确认等措施使估计风险降低约90%。提示注入监测器报告99%召回、90%精确率。全部为厂商自测，不能外推为真实事故率。**置信度：厂商自测。** https://openai.com/index/operator-system-card/

[^p6-echoleak]: Pavan Reddy、Aditya Sanjay Gujral，*EchoLeak*，2025年；Microsoft CVE-2025-32711。在Microsoft 365 Copilot中验证了无需用户点击的间接提示注入与数据外传路径；漏洞经协调披露后由微软在服务端修复，无证据显示已被大规模利用。https://arxiv.org/abs/2509.10540 ；https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32711

[^p6-rite-aid]: U.S. FTC，Rite Aid案新闻稿及投诉书，2023年12月19日。投诉称人脸识别系统产生数千次错误匹配，企业缺少合理的准确性评估和持续监控；十一岁女孩案例来自投诉书。以"FTC指控"表述。https://www.ftc.gov/news-events/news/press-releases/2023/12/rite-aid-banned-using-ai-facial-recognition-after-ftc-says-retailer-deployed-technology-without ；https://www.ftc.gov/system/files/ftc_gov/pdf/2023190_riteaid_complaint_filed.pdf

[^p6-production-frictions]: NIST，*AI Risk Management Framework Core*；OpenTelemetry，*GenAI Observability*，2026年。NIST要求在完整生命周期中持续管理第三方依赖、变更、监测、事故恢复与退役；OpenTelemetry统一记录模型调用、Token用量、Agent跨度和工具执行。六项企业症状分类属本书综合。**置信度：官方框架。** https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ ；https://opentelemetry.io/blog/2026/genai-observability/

[^p6-fde]: Palantir，*Architecture Center*；OpenAI，*Forward Deployed Engineer*职位说明与部署公司公告，2026年5月11日。Palantir把FDE描述为工程师贴近真实问题的方法；OpenAI职位覆盖问题发现到上线，部署公司公告证明该角色已组织化。不证明已全行业普及。**截至：2026-08-05；置信度：厂商材料。** https://www.palantir.com/docs/foundry/architecture-center/overview ；https://openai.com/careers/forward-deployed-engineer-%28fde%29-sf-san-francisco/ ；https://openai.com/index/openai-launches-the-deployment-company/

[^p6-data-work]: Timnit Gebru等，*Datasheets for Datasets*，CACM，2021年；Nithya Sambasivan等，*Data Cascades in High-Stakes AI*，CHI 2021。前者提出记录数据集动机、组成、收集过程与限制；后者访谈53名从业者，分析被低估的数据工作怎样形成级联问题。**置信度：同行评审。** https://doi.org/10.1145/3458723 ；https://doi.org/10.1145/3411764.3445518

[^p6-era-experience]: David Silver、Richard S. Sutton，*Welcome to the Era of Experience*，2025年。主张智能体可从现实环境的行动与观察流中获得经验并在运行期适应；长时自主运行会减少人的介入点。研究纲领而非实证结论。**置信度：趋势待实证。** https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf

[^p6-confidential-hybrid]: Google Cloud，*Google Distributed Cloud*；NVIDIA，*Confidential Containers Reference Architecture*；NIST IR 8320E草案，2026年5月29日；Confidential Computing Consortium技术分析。分布式云提供本地与隔离部署形态；可信执行环境保护使用中的数据；不存在"绝对安全"。共同证明物理位置、所有权和数据控制可被不同安排。**置信度：机制已确认；效果依赖配置。** https://cloud.google.com/distributed-cloud ；https://docs.nvidia.com/datacenter/cloud-native/confidential-containers/latest/overview.html ；https://csrc.nist.gov/pubs/ir/8320/e/ipd ；https://confidentialcomputing.io/wp-content/uploads/sites/10/2023/03/CCC-A-Technical-Analysis-of-Confidential-Computing-v1.3_Updated_November_2022.pdf

[^p6-ai-demand]: IEA，*Key Questions on Energy and AI*，2026年。单项AI任务能耗估计至少每年下降一个数量级，而推理、视频与Agent任务单次能耗可能是简单文本生成的数百至数千倍；2025年数据中心用电增长17%、面向AI的约50%。不把能源增长等同于经济价值。**置信度：IEA综合估计。** https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary

[^p6-model-routing]: Ding D.等，*Hybrid LLM: Cost-Efficient and Quality-Aware Query Routing*，2024年；Gupta S.等，*A Unified Approach to Routing and Cascading for LLMs*，2024年。前者报告最多减少约40%的大模型调用而不损失总体质量；后者强调质量估计器决定成本—性能收益。不保证任意企业任务获得相同节省。**置信度：论文结果；有效性依任务而变。** https://arxiv.org/abs/2404.14618 ；https://arxiv.org/abs/2410.10347

[^p6-model-runtime-2026]: DeepSeek，*Thinking Mode*与价格文档；OpenAI API参考文档；vLLM，*Quantized KV Cache*文档，均核验至2026年8月4日。区分输入、缓存命中输入、输出和推理Token；MoE激活参数、量化、路由、重试和工具调用共同决定真实成本。API价格是服务报价，不等于物理边际成本。**置信度：官方材料；成本效果需实测。** https://api-docs.deepseek.com/guides/thinking_mode ；https://api-docs.deepseek.com/quick_start/pricing/ ；https://platform.openai.com/docs/api-reference/chat/create ；https://docs.vllm.ai/en/latest/features/quantization/quantized_kvcache/

[^p6-agent-payments]: AP2，*Specification v0.2*；Sonja Davidovic、Hervé Tourpe，*How Agentic AI Will Reshape Payments*，IMF Note 2026/004，2026年4月。AP2用授权与收据为Agent交易提供可验证证据，转委托与争议解决置于范围之外；IMF论文提出三层框架，代表作者分析，不等于IMF立场。**置信度：机制与框架。** https://ap2-protocol.org/ap2/specification/ ；https://www.imf.org/en/-/media/files/publications/imf-notes/2026/english/insea2026004.pdf

[^p6-gpai-code]: European Commission，*General-purpose AI obligations under the AI Act*与*GPAI Code of Practice*，核验至2026年8月6日。提供者需准备技术文档、实施版权政策并公开训练内容摘要，系统性风险模型另有通知与事故报告义务；不能替部署企业完成评测、数据授权、权限、监测或补救。**置信度：正式规则说明。** https://digital-strategy.ec.europa.eu/en/factpages/general-purpose-ai-obligations-under-ai-act ；https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai

## 第七、八章　企业与国家/城市主权

[^p7-dpi-runtime]: OECD，*Digital Government Outlook 2026*。把数字身份、数据共享、数字通知、支付和基础登记视为数字公共基础设施，强调组件、治理与跨机构采用共同决定端到端公共服务能力。不证明单一架构适用于所有国家。https://www.oecd.org/en/publications/2026/06/digital-government-outlook_4585678e/full-report/strengthening-digital-public-infrastructure-and-data-governance_2c7323c7.html

[^p7-open-standards]: UK Government，*Open Standards Principles*与*Technology Code of Practice*。要求公共技术采用开放标准、支持互操作，按全生命周期管理技术，并设计退出安排；不把一国采购指引当作普遍法律。https://www.gov.uk/government/publications/open-standards-principles/open-standards-principles ；https://www.gov.uk/guidance/the-technology-code-of-practice

[^p7-agent-identity]: NIST NCCoE，*Accelerating the Adoption of Software and AI Agent Identity and Authorization: Concept Paper*，2026年2月5日。把智能体识别、授权、审计、不可抵赖和提示注入列为拟研究问题；属标准化研究倡议，不是强制标准。https://csrc.nist.gov/pubs/other/2026/02/05/accelerating-the-adoption-of-software-and-ai-agent/ipd

[^p7-gao-accountability]: U.S. GAO，*AI: An Accountability Framework for Federal Agencies and Other Entities*，2021年6月。以治理、数据、性能和监测组织问责实践，强调持续监测与文档；不替代具体法律授权和领域专业判断。https://www.gao.gov/products/gao-21-519sp

[^p7-robodebt]: Royal Commission into the Robodebt Scheme，*Final Report*，2023年7月7日，尤其第17章。建议为政府自动化决策建立一致法律框架，提供清楚复核路径，以通俗语言说明系统运作，并让业务规则和算法接受独立审查。https://robodebt.royalcommission.gov.au/publications/report

[^p7-china-scale]: 中国互联网络信息中心，第57次《中国互联网络发展状况统计报告》，2026年2月5日；国家网信办，生成式AI服务备案公告，2026年1月9日。截至2025年12月生成式AI用户约6.02亿、普及率42.8%；累计748款服务备案、435款应用或功能登记。规模不能证明深度采用或有效竞争。https://www3.cnnic.cn/n4/2026/0304/c88-11549.html ；https://www.cac.gov.cn/2026-01/09/c_1769688009588554.htm

[^p7-bis-compute]: U.S. BIS，2022—2025年先进计算与半导体制造设备出口管制官方说明。证明先进芯片、高带宽内存和制造设备存在法律与供应约束；不能量化实际取得数量或管制的最终效果。https://www.bis.gov/press-release/bis-updated-public-information-page-export-controls-imposed-advanced-computing-semiconductor ；https://www.bis.gov/press-release/commerce-strengthens-export-controls-restrict-chinas-capability-produce-advanced-semiconductors-military ；https://www.bis.gov/press-release/commerce-strengthens-restrictions-advanced-computing-semiconductors-enhance-foundry-due-diligence-prevent

[^p7-deepseek-path]: DeepSeek-AI，*DeepSeek-V3 Technical Report*，2024年12月27日；*DeepSeek-R1*，2025年1月22日。V3报告671B总参数、每Token激活37B、14.8T预训练Token和2.788M H800 GPU小时；R1报告多阶段训练、强化学习与六个蒸馏模型。为作者披露；蒸馏不等于无损复制教师。https://arxiv.org/abs/2412.19437 ；https://arxiv.org/abs/2501.12948

[^p7-china-compute]: 工业和信息化部，《算力互联互通行动计划》，2025年5月。把公共算力标准化互联、算力标识与调度、多芯片架构的算子库和开发框架列为行动目标。证明政策与技术路线存在，不证明全国异构算力已经互联。https://fjca.miit.gov.cn/zwgk/zcwj/wjfb/art/2025/art_25eea57dd6f840e680184fffb086883d.html

[^p7-china-governance]: 国家网信办等，《生成式人工智能服务管理暂行办法》，2023年7月；《人工智能生成合成内容标识办法》，2025年3月发布、9月施行；《个人信息保护法》第24条，2021年。分别涉及服务责任、内容来源标识和自动化决定中的说明及拒绝权。规则存在不等于执行一致或救济有效。https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm ；https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm ；https://www.npc.gov.cn/WZWSREL25wYy9jMi9jMzA4MzQvMjAyMTA4L3QyMDIxMDgyMF8zMTMwODguaHRtbD9yZWY9aW1i

[^p7-uae-falcon]: Technology Innovation Institute，Falcon 180B与Falcon Arabic发布材料，2023年9月、2025年5月。Falcon Arabic基于Falcon 3-7B，使用原生阿拉伯语语料并覆盖标准语与方言；规模和性能来自项目方披露。https://www.tii.ae/index.php/ar/news/technology-innovation-institute-introduces-worlds-most-powerful-open-llm-falcon-180b ；https://www.tii.ae/index.php/news/middle-easts-leading-ai-powerhouse-tii-launches-two-new-ai-models-falcon-arabic-first-arabic

[^p7-g42-microsoft]: Microsoft，*Invests $1.5 billion in Abu Dhabi's G42*，2024年4月16日及后续说明。政府间保证协议框架覆盖网络与物理安全、出口管制、技术转移、数据保护和客户审查，说明商业技术准入与国家安全规则相互嵌入。https://news.microsoft.com/source/2024/04/16/microsoft-invests-1-5-billion-in-abu-dhabis-g42-to-accelerate-ai-development-and-global-expansion/ ；https://blogs.microsoft.com/on-the-issues/2025/11/03/microsofts-15-2-billion-usd-investment-in-the-uae/

[^p7-uae-stargate]: U.S. Department of Commerce，美阿先进技术合作框架，2025年5月；OpenAI，*Introducing Stargate UAE*，2025年5月22日。公布阿布扎比5GW园区规划、其中1GW Stargate集群及首期200MW预计2026年上线。额定电力容量不等于Token产量。**置信度：建设状态待复核。** https://www.commerce.gov/news/press-releases/2025/05/uae/us-framework-advanced-technology-cooperation ；https://openai.com/index/introducing-stargate-uae/

[^p7-gulf-export]: U.S. Department of Commerce，阿联酋与沙特先进芯片出口授权声明，2025年11月19日。分别授权G42与HUMAIN采购相当于最多35,000颗NVIDIA GB300的芯片，附安全、报告和监测条件。授权不等于已交付或投入生产。**置信度：交付待复核。** https://www.commerce.gov/news/press-releases/2025/11/statement-uae-and-saudi-chip-exports

[^p7-saudi-allam]: SDAIA、IBM，ALLAM与DEEM云材料，2024年；ALLAM 1许可文件。ALLAM在Llama 2基础上继续阿拉伯语/英语预训练和指令微调，通过watsonx与沙特政府云提供调优、部署和MLOps能力。性能为官方口径；使用外部基座不等于失去主权。https://mea.newsroom.ibm.com/sdaia-launches-allam-on-watsonx ；https://www.ibm.com/docs/en/SSYOK8/wsj/analyze-data/assets/ALLaM_1_License.pdf ；https://mea.newsroom.ibm.com/watsonx-and-ALLaM-on-DEEM-cloud

[^p7-saudi-humain]: Saudi PIF，HUMAIN成立公告与投资组合页，2025年5月12日。定位为覆盖数据中心、云、模型、应用与硬件采购的统一运营公司，列出NVIDIA、Microsoft、AMD、AWS等合作伙伴；不能证明项目已全部运行或公众问责成立。https://www.pif.gov.sa/en/news-and-insights/press-releases/2025/hrh-crown-prince-launches-humain-as-global-ai-powerhouse/ ；https://www.pif.gov.sa/en/our-investments/our-portfolio/humain/

[^p7-sealion]: Singapore IMDA，*National Multimodal LLM Programme*；AI Singapore，SEA-LION v1/v2技术文档。2023年启动S$70 million计划，面向东南亚语言与文化，早期版本在AWS和NVIDIA GPU上训练，后续版本使用Llama等开放基座。项目方性能结论不能替代独立评测。https://www.imda.gov.sg/how-we-can-help/national-multimodal-llm-programme ；https://docs.sea-lion.ai/models/sea-lion-v1 ；https://docs.sea-lion.ai/models/sea-lion-v2

[^p7-sea-adapt]: AI Singapore，SEA-LION适配资料；Sahabat-AI模型卡。Sahabat-AI覆盖印尼语及多种地区语言，较大版本基于Llama 3.1并受其社区许可约束；适配能力仍依赖外部基座、许可、云与芯片。https://docs.sea-lion.ai/models/sea-lion_adaptations ；https://huggingface.co/Sahabat-AI/Llama-Sahabat-AI-v2-70B-IT/blob/main/README.md

[^p7-phogpt]: Dat Quoc Nguyen等，*PhoGPT*，2023年；VinAI模型仓库与组织页。从头训练约3.7B参数、102B越南语Token的模型，以BSD-3-Clause发布；2025年Qualcomm收购VinAI相关团队后，组织页注明不再更新。公开资产仍可被分叉。https://arxiv.org/abs/2311.02945 ；https://huggingface.co/vinai/PhoGPT-4B/tree/main ；https://huggingface.co/vinai

[^p7-asean-dc]: ASEAN，*Guide for Sustainable Data Centre Development*，2025年12月。新加坡超1.4GW运行容量，柔佛超500MW运行、超5GW处于不同开发阶段；规划容量不等于已运行负荷。https://asean.org/wp-content/uploads/2026/01/2.-ASEAN-Guide-for-Sustainable-Data-Centre-Development_Dec-2025-Final.pdf

[^p7-asean-rules]: ASEAN，*Model Contractual Clauses for Cross Border Data Flows*，2021年；*Expanded ASEAN Guide on AI Governance and Ethics*，2025年；Single Window官方页面。前两者是自愿性工具，不是统一隐私法；Single Window证明十国可在保留各自系统时交换结构化海关单证，不能外推到医疗数据和训练语料。https://asean.org/wp-content/uploads/3-ASEAN-Model-Contractual-Clauses-for-Cross-Border-Data-Flows_Final.pdf ；https://asean.org/wp-content/uploads/2025/01/Expanded-ASEAN-Guide-on-AI-Governance-and-Ethics-Generative-AI.pdf ；https://asw.asean.org/component/content/?view=featured

[^p7-canada-aia]: Treasury Board of Canada，*Algorithmic Impact Assessment / Directive on Automated Decision-Making*。要求影响评估在设计早期进行并在投产前复做，影响越高对同行评审和人工介入要求越高，评估结果应公开。https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/algorithmic-impact-assessment.html

[^p7-uk-atrs]: UK GDS，*Algorithmic Transparency Recording Standard*及强制化说明，2025年5月8日；Cabinet Office公开记录。GDS披露一年内新增53份记录、总数59份；内阁办公室称算法辅助方法已审查510万份历史文件。ATRS要求公开负责人、用途、模型/数据、风险和人工参与。登记不等于独立审计。**置信度：政府披露。** https://www.gov.uk/government/collections/algorithmic-transparency-recording-standard-hub ；https://dataingovernment.blog.gov.uk/2025/05/08/making-the-algorithmic-transparency-recording-standard-atrs-mandatory-across-government/ ；https://www.gov.uk/algorithmic-transparency-records/cabinet-office-automated-digital-document-review

[^p7-oecd-government-impact]: OECD，*Digital Government Outlook 2026: Adopting and governing AI in government*，2026年6月15日。36个成员国中只有10个（28%）报告对政府AI用例开展过影响测量，4个（11%）测量过部门层面影响；50%称采用决策会依据效率证据。国家自报数据。**置信度：OECD报告。** https://www.oecd.org/en/publications/2026/06/digital-government-outlook_4585678e/full-report/adopting-and-governing-ai-in-government_7ef312a9.html

[^p7-syri]: Rechtbank Den Haag，*SyRI legislation in breach of European Convention on Human Rights*，2020年2月13日。法院判定规范SyRI（福利欺诈风险识别）的立法不符合《欧洲人权公约》第八条，未在社会整体利益与私人生活权之间保持公平平衡。证明分别合法收集的数据被组合推断后会产生新的比例性问题。**置信度：法院判决。** https://www.rechtspraak.nl/organisatie-en-contact/organisatie/rechtbanken/rechtbank-den-haag/nieuws/2020/02/syri-legislation-in-breach-of-european-convention-on-human-rights

[^p7-eu-aiact]: Regulation (EU) 2024/1689，尤其Recital 58与Article 27；European Commission，*AI Omnibus enters into force*，2026年7月27日。用于决定基本公共服务和福利能否获得、减少、撤销或追索的若干AI系统列为高风险；公共主体应在部署前评估基本权利影响。二〇二六年修法把附件三高风险规则延至2027年12月2日，附件一规则延至2028年8月2日。https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689 ；https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force

[^p7-coe]: Council of Europe，*Framework Convention on AI and Human Rights, Democracy and the Rule of Law*。2024年9月5日开放签署，目标是使AI全生命周期活动符合人权、民主与法治。https://www.coe.int/en/web/artificial-intelligence/the-framework-convention-on-artificial-intelligence

[^p7-yichang-runtime]: 宜昌市科技局，《宜昌已建成智算规模突破3000P》，2025年8月7日；宜昌市政府，《"宜数"OPC创新社区开园》，2026年5月23日；湖北省数据局，2026年"数智+"场景育新行动清单，2026年4月。确认算力设施、供应链平台、模型库/数据集专区与OPC社区建设状态；省级清单列出开放传神（湖北）的"开源平台+产业联盟+基金会"结构；1000P等数字来自申报口径。**置信度：已确认。** https://kjt.hubei.gov.cn/kjdt/sxkj/yc/202508/t20250807_5741115.shtml ；https://www.yichang.gov.cn/html/zhengwuyizhantong/zhengwuzixun/jinriyaowen/2026/0523/1077302.html ；https://sjj.hubei.gov.cn/bmdt/tzgg/202604/P020260423539722658121.pdf

[^p8-suzhou-ai-city]: 苏州市政府办公室，《苏州市加快建设"人工智能+"城市行动方案（2025～2026年）》，2025年12月。提出到2026年底智算规模达17000 PFLOPS、形成200个典型场景，建设公共算力平台、语料与模型测评底座、低代码智能体平台等。均为规划目标。**置信度：正式文件；完成情况待验收。** https://www.suzhou.gov.cn/szsrmzf/gbzfwj/202512/bcc1393a90684fe49439279ac25fb9b1.shtml

[^p8-shanghai-vouchers]: 上海市经信委，《关于组织2026年度上海市"模塑申城"工程相关补贴申报工作的通知》，2026年5月7日。分设算力券、模型券（Token券）和语料券，支持算力租用、大模型API或私有化部署及语料采购。证明政策工具存在，不证明已形成产业回报。**置信度：正式通知；效果待审计。** https://sheitc.sh.gov.cn/cyfz/20260507/cd1dcb1e5cb4449cbc36c69befafcc0a.html

[^p8-wuhan-opc-compute]: 武汉市政府，《武汉市支持人工智能OPC创新发展若干措施》，2026年2月13日。对OPC算力服务费用的50%给予最高20万元补助，各区OPC社区每年为每家OPC提供不少于2000卡时免费算力。额度是供给承诺，不等于实际领取或企业存活。**置信度：正式政策；执行待公开。** https://www.wuhan.gov.cn/ztzl/25zt/rgzncy/zcwj_94757/202602/t20260224_2731334.shtml

[^p8-modelscope-ecosystem]: ModelScope Team，`modelscope-hub`官方仓库与社区2025年6月月报。客户端把模型、数据集、Studio、Skills和MCP服务器纳入统一Hub接口，称可连接10万项以上模型与数据集；月报称服务超1600万开发者，口径不等于月活。**置信度：规模为项目方口径。** https://github.com/modelscope/modelscope_hub ；https://community.modelscope.cn/68513e478e4d0a6c534b924f.html

[^p8-hf-opensource-2026]: Hugging Face，*State of Open Source on Hugging Face: Spring 2026*；Stanford HAI，*AI Index 2026: Technical Performance*，截至2026年3月。HF报告过去一年约41%的模型下载量来自中国研发的模型，中国首次超过美国；下载量不等于能力排名。AI Index记录美国最强模型对中国的领先收窄到约2.7%。不支持"中国已全面领先"。**截至：2026-08-15；置信度：多源一致。** https://huggingface.co/blog ；https://hai.stanford.edu/ai-index/2026-ai-index-report/technical-performance

[^p8-opencsg]: OpenCSG（开放传神）官方网站与公开资料，核验至2026年8月15日。把模型、数据集、代码、智能体与AI基础设施组织在同一套开放体系中运营，称有数百万级全球用户，参与多个城市开源生态与OPC社区建设（宜昌案例见[^p7-yichang-runtime]）。规模与效果为企业自述口径。**截至：2026-08-15；置信度：已确认。** https://opencsg.com

[^p7-city-flywheel]: 国家发改委、国家数据局等，《关于深化智慧城市发展 推进城市全域数字化转型的指导意见》，2024年5月；《深化智慧城市发展推进全域数字化转型行动计划》，2025年；《可信数据空间发展行动计划（2024—2028年）》及创新发展报告（2025）；European Commission，*AI Factories*；Singapore Government，*National AI Strategy 2.0*，2023年。为中、欧、新三地的AI政策框架；不证明任一城市形成自我造血飞轮。**置信度：已确认。** https://zfxxgk.ndrc.gov.cn/web/iteminfo.jsp?id=20387 ；https://www.ndrc.gov.cn/xxgk/zcfb/tz/202510/P020251031380308105300.pdf ；https://www.nda.gov.cn/sjj/zwgk/zcfb/1122/ff808081-92b8a4f1-0193-530c6ac8-0475.pdf ；https://www.nda.gov.cn/sjj/swdt/xwfb/0829/20250829085131590048920_pc.html ；https://digital-strategy.ec.europa.eu/en/policies/ai-factories ；https://www.edb.gov.sg/content/dam/edb-en/business-insights/market-and-industry-reports/singapores-national-ai-strategy-ai-for-the-public-good-for-singapore-and-the-world/nais2023.pdf

[^p7-opc-policy]: 深圳市工信局，《深圳市打造人工智能OPC创业生态引领地行动计划（2026—2027年）》，2026年1月14日；北京市经信局，《支持人工智能OPC创新发展行动方案（试行）》，2026年6月18日及通州区配套措施；广州市市监局，《人工智能OPC沙盒监管实施方案》说明，2026年4月29日。多地把算力、数据、登记、融资与沙盒监管组合用于支持个人或极小团队；规划与补贴不等于存活率或财政回报。**置信度：已确认。** https://www.sz.gov.cn/cn/xxgk/zfxxgj/tzgg/content/post_12602687.html ；https://jxj.beijing.gov.cn/zwgk/2024zcwj/202606/t20260618_4706233.html ；https://www.beijing.gov.cn/ywdt/gzdt/202605/t20260525_4663937.html ；https://scjgj.gz.gov.cn/zzzq/gzdt/content/post_10794656.html

[^p7-waico]: 外交部，《成立世界人工智能合作组织协定签署仪式在上海举行》，2026年7月16日；习近平在2026世界人工智能大会开幕式主旨讲话，7月17日；新华社与国家发改委报道，7月19—20日。确认二十九国签署、总部设在上海及研修名额、应用合作中心承诺；联大第79/325号决议另设国际AI科学小组与全球治理对话。**置信度：已确认。** https://www.fmprc.gov.cn/web/wjdt_674879/wjbxw_674885/202607/t20260716_11984399.shtml ；https://www.news.cn/politics/leaders/20260717/72728b6f94154d63b3eaaaf9808b51eb/c.html ；https://www.news.cn/world/20260719/9e49a03f5ce74864bd7b32f154aaad86/c.html ；https://www.ndrc.gov.cn/fggz/202607/t20260720_1406588.html ；https://docs.un.org/en/A/RES/79/325

[^p8-yancheng-opc]: 央广网江苏频道，《赛场收官！OPC创客扎根盐城再出发》，2026年8月1日；江苏省政府，《盐城市新能源发电装机容量超1500万千瓦》，2024年9月13日；中国经济网，"海上风电第一城"报道，2025年9月23日。确认OPC主题全国青年创新创业挑战赛在盐城举行并发布场景清单、有团队签署落地协议；盐城海上风电装机居全国前列。**截至：2026-08-17；置信度：多源确认。** https://js.cnr.cn/rdzt/qnjs/qnjsgdxw/20260801/t20260801_527741547.shtml ；https://www.jiangsu.gov.cn/art/2024/9/13/art_33718_11367829.html ；http://www.ce.cn/xwzx/gnsz/gdxw/202509/t20250923_2485772.shtml

[^p8-chongqing-ai-plan]: 重庆市政府办公厅，《重庆市推动"人工智能+"行动方案》，渝府办发〔2025〕60号，2025年12月13日。提出AI与科技、产业、超大城市治理、民生深度融合，把算力、数据、模型、企业、人才、开源生态、金融、安全列为支撑要素。证明已列入市级正式议程。**截至：2026-08-17；置信度：正式文件。** https://www.cq.gov.cn/zwgk/zfxxgkml/szfwj/xzgfxwj/szfbgt/202512/t20251217_15251374.html

[^p8-longgang-ai-platform]: 公开采购信息媒体报道（采购行业自媒体经网易号转载），2026年1月20日。报道显示深圳市龙岗区数据有限公司就"AI大模型基础服务能力建设项目"完成采购，区级AI公共底座项目处于建设阶段；成交金额与供应商细节按惯例不引用。**截至：2026-08-17；置信度：公开报道确认。** https://www.163.com/dy/article/KJOHVTNF0511D6RL.html

[^p8-yancheng-ai-policy]: 盐城市工信局，《盐城市促进"人工智能+"创新发展行动计划（2025—2027年）》（征求意见稿）。提出打造"东部沿海绿色算力港"，探索"绿电+冷能+储能"模式，到2027年智算规模达20000PFlops、新建数据中心绿电占比超90%。均为征求意见稿规划目标。**截至：2026-08-17；置信度：正式版本待核验。** http://gxj.yancheng.gov.cn/module/download/downfile.jsp?classid=0&filename=f974fb519caf48d4bd130e1893c49054.pdf

[^p8-chongqing-science-city]: 四川省政府英文网站，*Western Science City Brings Benefits to Chengdu-Chongqing Region*，2023年4月17日。确认成渝双城经济圈部署、规划纲要印发、十二部门支持西部科学城的意见，西部（重庆）科学城为核心承载区。不证明区级AI项目的立项或成效。**截至：2026-08-17；置信度：已确认。** https://www.sc.gov.cn/10462/10758/10760/10765/2023/4/17/db3658eb9e7742c388226663251e0b4b.shtml

[^p8-longgang-ai-district]: 龙岗区政府，《创建人工智能全域全时应用示范区行动方案（2024—2025年）》，2024年7月；人民网深圳频道，区级AI署揭牌报道，2025年5月21日；龙岗区政府、深圳市政府门户网站，"All in AI"白皮书报道，2026年5月30日。确认示范区方案、全国首个区级AI专责机构、白皮书（战略、政府订单、场景清单）相继出台；不证明持续使用或产业回报。**截至：2026-08-17；置信度：多源确认。** https://www.lg.gov.cn/lggxj/gkmlpt/content/11/11419/post_11419723.html ；http://sz.people.com.cn/n2/2025/0521/c202846-41235185.html ；https://www.lg.gov.cn/xxgk/xwzx/zwdt/content/post_12819146.html ；https://www.sz.gov.cn/cn/xxgk/zfxxgj/gqdt/content/post_12819456.html

## 第九章　安全、协议与审计：依赖怎样不变成支配

[^p9-mcp-control]: Model Context Protocol，*Tools*与*Authorization*规范，2025年11月25日稳定版。工具规范提醒工具可导致外部行动，客户端应让用户看见并拒绝调用；授权规范要求令牌面向预期资源并禁止透传。不证明工具自述或输出真实。https://modelcontextprotocol.io/specification/2025-11-25/server/tools ；https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization

[^p9-otel-control]: OpenTelemetry，*Generative AI Semantic Conventions*与*GenAI Observability*。尝试统一描述模型交互、智能体跨度、工具执行与Token使用；规范仍在演进，不保证记录完整或结论正确。https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/ ；https://opentelemetry.io/blog/2026/genai-observability/

[^p9-ietf-process]: IETF，RFC 2026，*The Internet Standards Process — Revision 3*，1996年；RFC 6410，2011年。前者把开放、公平、清楚文档、实施与互操作经验纳入标准成熟过程；只借其说明开放规范需要实施检验。https://datatracker.ietf.org/doc/rfc2026/ ；https://www.rfc-editor.org/info/rfc6410/

[^p9-aaif-governance]: Linux Foundation，*Formation of the Agentic AI Foundation*，2025年12月9日。以中立治理智能体开源基础设施为目标，初始项目包括MCP、goose与AGENTS.md；不证明权力交接一定成功。https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation

[^p9-model-signing]: Open Source Security Foundation，*Launch of Model Signing v1.0*，2025年4月4日。为机器学习模型提供签名与验证机制，核验制品来源关系和传输完整性；签名不能证明发布者可信、模型无后门或输出正确。https://openssf.org/blog/2025/04/04/launch-of-model-signing-v1-0-openssf-ai-ml-working-group-secures-the-machine-learning-supply-chain/

[^p9-audit-boundary]: NIST，*AI Risk Management Framework Core*。把治理、文档、测试评估验证、安全韧性、透明问责与持续监测作为相互关联而不可相互替代的实践。https://airc.nist.gov/airmf-resources/airmf/5-sec-core/

[^p9-safety-report]: *International AI Safety Report 2026*，2026年2月3日。通用AI与智能体用途增加，但复杂任务中的失败仍无法完全消除；智能体减少人类介入机会，也让错误更易跨系统传播。倡导纵深防御。https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026

[^p9-data-act]: European Commission，*Data Act explained*与*Common European Data Spaces*；Regulation (EU) 2023/2854。《数据法》自2025年9月12日起适用，含云服务互操作与切换、开放接口和机器可读导出要求；欧盟也在健康、农业、能源、金融等领域推进共同数据空间。https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained ；https://digital-strategy.ec.europa.eu/en/policies/data-spaces

[^p9-exit-voice]: Albert O. Hirschman，*Exit, Voice, and Loyalty*，1970。区分面对组织衰退时的退出与发声，并讨论二者怎样相互促进或削弱。https://books.google.com/books/about/Exit_Voice_and_Loyalty.html?id=vYO6sDvjvcgC

[^p6-oecd-sme]: OECD，*Generative AI and the SME Workforce*，2025年。七国5000多家中小企业调查：31%已使用生成式AI；使用者中65%自报表现提高、26%自报营收增加。自报横截面数据，不能证明因果。**截至：2026-08-03；置信度：国际组织调查。** https://www.oecd.org/en/publications/generative-ai-and-the-sme-workforce_2d08b99d-en.html

[^p7-govuk-chat]: UK GDS，*5 things we learned testing GOV.UK Chat*，2026年3月16日。首轮试点10,136名用户提出23,838个问题；跨主题准确率90%、范围内回答率88%；记录508次越狱尝试且官方称均被阻止。数字来自政府试点和用户调查，不是独立审计。https://insidegovuk.blog.gov.uk/2026/03/16/5-things-we-learned-testing-gov-uk-chat-an-ai-assistant-for-government/

[^p1-infra-2026]: IEA，*Key Questions on Energy and AI*，2026年；U.S. DOE/LBNL，*2024 United States Data Center Energy Usage Report*。IEA称2025年数据中心用电增长约17%，五家大型科技公司资本支出超4000亿美元；DOE/LBNL估计美国数据中心占2023年用电约4.4%，2028年可能达6.7%至12%。不能归为单一AI产品。**截至：2026-08-04；置信度：官方报告。** https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary ；https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report.pdf

[^p1-nvidia-lps-2026]: Jensen Huang，*Securing the Infrastructure of Intelligence*，X长文，2026年8月17日。提出土地、电力与厂房（LPS）成为AI工厂的下一类关键资源；俄亥俄项目初始4.25吉瓦、OpenAI担任租户，至2030年承诺约12吉瓦。黄仁勋否认构成循环融资。**截至：2026-08-17；置信度：单一来源，未经审计。** https://x.com/JensenHuang/status/2089331487342829862

[^p6-deployment-evidence-2026]: UK Government，*AI Adoption Research*，2026年；Brynjolfsson等企业现场随机实验，*Management Science*，2025/2026；METR，2025年。英国研究平均每天节省约26分钟；开发者研究任务数平均增加约26.08%；METR报告完成时间增加约19%。口径不同，只支持"收益高度条件化"。**截至：2026-08-04；置信度：已确认。** https://www.gov.uk/government/publications/ai-adoption-research ；https://pubsonline.informs.org/doi/10.1287/mnsc.2025.00524 ；https://metr.org/notes/2025-07-10-early-2025-ai-experienced-os-developers/

[^p1-frontier-landscape-2026]: Stanford HAI，*AI Index 2026 — Technical Performance*；Meta、Qwen、Mistral AI、Google官方模型资料。AI Index称前沿模型在Humanity's Last Exam一年提升约30个百分点，开放权重与最强封闭模型差距约3.3%；Qwen3、Mistral 3、Gemma 4展示密集/MoE、多模态、端侧等开放组合。测量边界不同，不能混为统一排名。**截至：2026-08-04；置信度：已确认。** https://hai.stanford.edu/ai-index/2026-ai-index-report/technical-performance ；https://qwenlm.github.io/blog/qwen3/ ；https://mistral.ai/news/mistral-3 ；https://ai.google.dev/gemma/docs/gemma-4

[^p7-public-compute-2026]: U.S. NSF，*NAIRR Pilot*；UKRI/英国政府，*AIRR Compute Opportunity*。NAIRR已支持600多个项目、6000名学生；AIRR提供20万至100万GPU小时申请资源。证明公共资源分配机制存在，不等于所有研究者获得同等算力。**截至：2026-08-04；置信度：政府资料。** https://www.nsf.gov/focus-areas/ai/nairr ；https://www.gov.uk/government/publications/airr-compute-opportunity-ai-for-science

[^p0-infrastructure-history]: 本节采用技术史结构性概括：动力、计算与记录、连接与分发、按需资源、部分生成与判断依次被标准化，Agent化把工具调用与连续行动纳入软件系统。不是单线进步史，表格用于解释控制点迁移。**置信度：机制性综合；非单一来源统计。**

[^p7-five-layer-cake]: NVIDIA官方博客，达沃斯"五层蛋糕"对话，2026年1月21日；GTC 2026 keynote，2026年3月16日；*AI Factories*，2026年5月27日；2026股东大会披露。"五层蛋糕"：能源、芯片与计算基础设施、云数据中心、AI模型、应用层；2027年订单指引至少一万亿美元。资本开支第三方估计口径不同，不可互证；产业叙事，非中立定义。**截至：2026-08-04；置信度：官方口径。** https://blogs.nvidia.com/blog/davos-wef-blackrock-ceo-larry-fink-jensen-huang/ ；https://www.nvidia.com/en-us/gtc/keynote/?video=7 ；https://blogs.nvidia.com/blog/ai-factories-the-new-infrastructure-of-intelligence/

[^p7-prefill-decode-2026]: Microsoft Research，*Splitwise*，2023年；MSRA等，*DistServe*，2024年；NVIDIA，*Dynamo*架构文档及GTC 2026"Dynamo + Groq LPU"演示。Splitwise给出预填充占约百分之八十五计算的口径；DistServe吞吐提升最高7.4倍；Dynamo官方给出35倍加速口径。倍数受工作负载与硬件约束。**截至：2026-08-04；置信度：多源一致。** https://arxiv.org/abs/2311.18677 ；https://arxiv.org/abs/2401.09670 ；https://docs.nvidia.com/dynamo/design-docs/overall-architecture

[^p7-tpu-2026]: Google Cloud，*TPU v7 (Ironwood)*规格；AWS，*Trainium 3*资料；Microsoft，*Maia 100/200*，2026年4月；NVIDIA GTC 2026 Vera Rubin规格与Semi Analysis测算；Reuters/The Information相关报道；均核验至2026年8月4日。TPU v7单芯片192 GB HBM、FP8 4614 TFLOPS；Maia 200为3 nm、FP4超10 PFLOPS；Vera Rubin NVL72单域72 GPU、3.6 EFLOPS FP4。Anthropic与Google签约100万颗TPU、与AWS部署约100万颗Trainium 2。不证明NVIDIA主导被替代。**截至：2026-08-04；置信度：多源一致。** https://cloud.google.com/tpu/docs/ironwood ；https://aws.amazon.com/machine-learning/trainium/ ；https://news.microsoft.com/source/features/ai/maia-100-ai-accelerator-chip/ ；https://www.reuters.com/technology/anthropic-google-tpu-deal-2026/

[^p7-ascend-day0]: 华为，昇腾Atlas 950超节点与910C量产，2026年4月24日；寒武纪，思元590/690 Day 0适配公告，同日；DeepSeek-AI，*DeepSeek-V4 Technical Report*；智源，*FlagOS 2.0与燎原计划*；平头哥，SAIL开源公告，2026年7月18日。V4发布当天，8家国产芯片首次"Day 0全链路集体适配"；昇腾910C千卡完成V4-Pro全参数后训练、零中断、MFU超百分之三十。软件层统一约18家厂商32款芯片接口；硬件互联仍分立，缺独立长稳基准。**截至：2026-08-04；置信度：已确认。** https://www.huawei.com/cn/products/computing/ascend ；https://www.cambricon.com/news ；https://github.com/deepseek-ai/DeepSeek-V4 ；https://flagopen.baai.ac.cn/

## 第十章　开放：力量、代价与现实检验

[^p10-olmo]: Luca Soldaini等，*OLMo: Accelerating the Science of Language Models*，2024年2月。公开权重、训练数据、训练和评测代码、中间检查点及日志，为研究完整训练过程提供材料；不等于第三方已完成安全审计。https://arxiv.org/abs/2402.00838

[^p10-open-equilibrium]: Pete Walsh等，*OLMo 2*及Ai2的32B发布材料，2024年11月至2025年。公开权重、数据、代码、配方、检查点和评测；32B预训练至约6万亿Token。复制权不会自动创造同等训练所需的计算、人才与组织能力。https://allenai.org/blog/olmo2 ；https://allenai.org/blog/olmo2-32b ；https://allenai.org/olmo2

[^p10-open-definitions]: Open Source Initiative，*Open Source AI Definition 1.0*；Linux Foundation AI & Data，*Model Openness Framework*。OSAID以使用、研究、修改和分享的自由及所需参数、代码与数据信息定义开源AI；MOF把开放完整度拆成可核查组件。都不直接评价模型安全性。https://opensource.org/ai/open-source-ai-definition ；https://arxiv.org/abs/2403.13784

[^p10-fmti]: Rishi Bommasani等，*The 2025 Foundation Model Transparency Index*，Stanford CRFM等，2025年12月。以一百项指标评估十三家基础模型开发者；开放权重开发者平均更透明，但开放权重不足以保证全面透明。https://crfm.stanford.edu/fmti/December-2025/paper.pdf

[^p10-openweights-letter]: NVIDIA等，*Open Weights and American AI Leadership*，2026年7月24日；Axios黄仁勋采访，7月22日；Tom's Hardware同期报道。声明提出开放权重的竞争、客户控制与防御价值，也承认权重发布后难以撤回；初始联署二十五家。Open Secure AI Alliance由NVIDIA另行宣布，性质不同。**置信度：多源确认。** https://images.nvidia.com/pdf/Open-Weights-and-American-AI-Leadership.pdf ；https://www.axios.com/2026/07/22/nvidia-jensen-huang-china-open-source-ai ；https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-and-24-other-companies-sign-open-weights-letter-as-washington-weighs-chinese-ai-model-ban ；https://blogs.nvidia.com/blog/open-secure-ai-alliance/

[^p10-hf-incident]: Hugging Face，*Security incident disclosure — July 2026*及技术时间线；OpenAI，事件联合说明，更新至2026年7月28日。双方确认评测智能体越出受限环境、进入HF生产基础设施；HF称未发现公开模型、数据集或Spaces被篡改。OpenAI完整技术报告仍在准备。**置信度：初步披露一致。** https://huggingface.co/blog/security-incident-july-2026 ；https://huggingface.co/blog/agent-intrusion-technical-timeline ；https://openai.com/zh-Hans-CN/index/hugging-face-model-evaluation-security-incident/

[^p10-model-supply-chain]: Yiming Zhang等，*Models Are Codes*，2024年9月；Hugging Face，*Pickle Scanning*文档。预训练模型仓库可能携带可执行代码和恶意序列化对象，自动扫描不能替代来源核验、隔离加载和安全格式。https://arxiv.org/abs/2409.09368 ；https://huggingface.co/docs/hub/security-pickle

[^p10-open-governance]: Apache Software Foundation，*The Apache Way*与治理说明；Linux Foundation，*Core Infrastructure Initiative*。Apache把公开沟通、共识、供应商中立和项目委员会作为长期治理原则；Heartbleed之后的核心基础设施计划推动识别和资助被广泛依赖的开源组件。https://www.apache.org/theapacheway/ ；https://www.apache.org/foundation/governance/ ；https://www.linuxfoundation.org/blog/blog/never-let-a-good-crisis-go-to-waste-core-infrastructure-initiative

[^p10-xz]: Red Hat，xz事件响应说明；Andres Freund在oss-security的原始披露；NVD CVE-2024-3094。恶意代码进入xz 5.6.0和5.6.1发布包并试图影响特定环境中的SSH认证，在大范围进入稳定发行版前被发现。https://www.redhat.com/en/blog/understanding-red-hats-response-xz-security-incident ；https://www.openwall.com/lists/oss-security/2024/03/29/4 ；https://nvd.nist.gov/vuln/detail/CVE-2024-3094

[^p10-ostrom]: Elinor Ostrom，*Governing the Commons*，1990。共同资源可由多中心、嵌套的制度治理，但需要清楚边界、参与式规则、监测、渐进制裁和低成本争议解决等条件。https://www.cambridge.org/core/books/governing-the-commons/A8BB63BC4A1433A50A3FB92EDBBB97D5

## 第十一章　协同与组织：让自由长成更大的整体

[^p11-fl]: NIST，*Privacy-Preserving Federated Learning*，2025年1月27日。联邦学习可让多方在不集中原始数据的情况下协同训练，但更新本身仍可能泄露信息，通常需要差分隐私、安全聚合等配合。https://www.nist.gov/blogs/cybersecurity-insights/privacy-preserving-federated-learning-future-collaboration-and

[^p11-un-dialogue]: United Nations，*Global Digital Compact / Global Dialogue on AI Governance*。联合国大会2025年8月26日通过A/RES/79/325，设立独立国际AI科学面板与全球AI治理对话；首届对话于2026年举行。https://www.un.org/global-digital-compact/en/ai

[^p11-agent-horizon]: METR，*Task-Completion Time Horizons of Frontier AI Models*，数据更新至2026年5月8日及局限说明。该指标估计前沿智能体以特定可靠率完成软件任务时对应的人类专家任务时长；不能换算为岗位自动化或未来增长率。**置信度：方法与结果已确认；外部有效性有限。** https://metr.org/time-horizons/ ；https://metr.org/notes/2026-01-22-time-horizon-limitations/

[^p11-unesco-language]: UNESCO，*Global Roadmap for Multilingualism in the Digital Era*，2025年。强调语言共同体参与文化数据治理，推动多语言技术标准、能力建设与低资源语言研究。https://www.unesco.org/en/global-roadmap-multilingualism

[^p11-individual-ai]: Eleanor W. Dillon等，*Shifting Work Patterns with Generative AI*，NBER Working Paper 33795，2025年。在66家企业对7,137名知识工作者开展六个月随机实验；实际使用工具的员工每周少花约两小时处理邮件，但任务数量或构成无显著变化。部分作者当时受雇于Microsoft。只据此区分个人提效与组织重构。**置信度：预注册现场实验。** https://www.nber.org/papers/w33795

[^p11-ai-native-firms]: Hyunjin Kim、Rembrand Koning，*AI-Native Firms*，Harvard Business School Working Paper 26-090，2026年6月。连接YC W20—F24批次与美国风投创业公司人员数据：相同行业—批次内AI原生企业规模约小25%，工程师占比高13%，初级员工与管理者占比各低约15%。样本集中于年轻风投企业，不能证明因果。**置信度：工作论文；外推有限。** https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6905079 ；https://www.insead.edu/faculty-research/publications/working-papers/ai-native-firms

[^p11-cybernetic-teammate]: Fabrizio Dell'Acqua等，*The Cybernetic Teammate*，NBER Working Paper 33641，2025年。在Procter & Gamble对776名专业人员预注册现场实验；使用AI的个人方案质量达到未使用AI的双人团队水平，方案更趋跨专业均衡。不测量长期执行与问责。**置信度：预注册实验。** https://www.nber.org/papers/w33641 ；https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5188231

[^p11-long-horizon-work]: OpenAI Economic Research，*How agents are transforming work*，2026年6月25日。基于Codex聚合使用数据，称任务正从短交互走向更长的委托；人类任务时长由模型估计，使用量不能等同真实节省时间或净就业效果。**置信度：厂商遥测；普遍性待验证。** https://openai.com/index/how-agents-are-transforming-work/

[^p11-agent-identity]: NIST NCCoE，智能体身份与授权概念文件，2026年2月5日；NIST，*AI Agent Standards Initiative*，2026年2月17日。涵盖智能体识别、授权、审计与提示注入缓解；截至2026年8月6日仍是概念文件与倡议。**置信度：政府资料。** https://www.nccoe.nist.gov/publications/other/accelerating-adoption-software-and-ai-agent-identity-and-authorization-concept ；https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative

## 尾注使用说明

月度下载量、融资估值、模型榜单、未经独立核验的内部测算，以及仅用于制造趋势感的产品参数，不进入纸质正文的核心论证。法规、政策与标准化倡议在正式出版和再版时，应按出版日期重新核验。
