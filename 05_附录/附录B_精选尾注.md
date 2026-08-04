# 附录B　精选尾注

本书有意控制正文中的数字和机构名称。尾注只保留三类材料：支撑核心判断的一手文件、能够显示制度后果的可靠案例，以及供读者继续深入的经典研究。

所有涉及现行政策、技术倡议和机构页面的材料，均核验至二〇二六年八月四日。法规时间表和进行中的标准工作仍可能变化，正式出版前应再次复核。

## 序章　智能权力的重新分配

[^p0-ai-world]: Stanford Institute for Human-Centered Artificial Intelligence，*The 2026 AI Index Report*，2026年。报告记录产业界生产了2025年超过九成的代表性前沿模型，生成式AI在三年内快速扩散，组织采用率继续上升；同时记录智能体在OSWorld等结构化任务基准上仍有约三分之一失败，以及模型在高难度数学与简单感知任务之间呈现锯齿状能力。报告汇总多种数据源、问卷与基准，采用率不等于成熟部署，基准表现也不能直接外推到开放世界可靠性。**置信度：综合研究报告已确认；社会采用与真实任务效果受口径限制。** https://hai.stanford.edu/ai-index/2026-ai-index-report ；https://hai.stanford.edu/ai-index/2026-ai-index-report/technical-performance

[^p0-ai-energy]: International Energy Agency，*Key Questions on Energy and AI*，2026年4月。IEA估计五家大型科技企业2025年资本支出超过四千亿美元，2026年仍可能显著增长；数据中心用电在2025年增长17%，AI数据中心增长更快，同时受到电网接入、变压器、燃气轮机、先进芯片等物理瓶颈约束。资本支出和用电证明AI具有不断扩大的物质基础，不证明每项投资有效，也不证明基础设施必然永久集中。**置信度：国际组织综合分析已确认；未来投资为情景估计。** https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary

[^p0-global-divide]: International Labour Organization、World Bank，*Disruption without dividend? How the digital divide and task differences split GenAI’s global impact*，2026年3月。研究覆盖135个国家、约全球三分之二就业，指出发展中经济体可能因数字基础设施、技能与任务构成差异，先面对工作扰动而较晚取得生产率收益。职业暴露度和任务模型不能直接预测实际失业或国家增长结果。**置信度：国际组织联合工作论文已确认；长期因果效果待观察。** https://www.ilo.org/resource/news/new-ilo%E2%80%93world-bank-paper-highlights-uneven-global-impact-generative-ai-jobs

## 第一章　Token工厂：AI怎样成为基础设施

[^p1-ai-factory]: NVIDIA，*AI Factories: The New Infrastructure of Intelligence*，2026年5月27日；以及NVIDIA AI Factory官方架构页面，核验至2026年7月31日。相关材料把AI工厂描述为以算力、电力、网络和软件持续生产Token的系统，并使用每秒Token、每瓦Token、单位Token成本、利用率和可用性等运营指标。正文将其视为产业工程框架与经济比喻，而非中立学术定义；厂商宣称的性能倍数未作为科学结论采用。https://blogs.nvidia.com/blog/ai-factories-the-new-infrastructure-of-intelligence/ ；https://www.nvidia.com/en-us/solutions/ai-factories/

[^p1-tokenizer]: Hugging Face，*Summary of the tokenizers*，Transformers文档，核验至2026年7月31日；Taku Kudo、John Richardson，*SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing*，EMNLP 2018。两份材料说明Token通常是由分词器产生并映射为词表编号的字符或子词片段；不同模型、分词算法和语言的Token数量并不统一。https://huggingface.co/docs/transformers/tokenizer_summary ；https://arxiv.org/abs/1808.06226

[^p1-transformer]: Ashish Vaswani等，*Attention Is All You Need*，NeurIPS 2017。论文提出以自注意力为核心的Transformer架构，是现代大语言模型的关键技术基础。论文不支持把大模型全部能力简化成单一注意力机制，也不证明生成内容天然真实。https://proceedings.neurips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html

[^p1-chinchilla]: Jordan Hoffmann等，*Training Compute-Optimal Large Language Models*，NeurIPS 2022。研究在其设定的计算预算和实验范围内表明，模型参数量与训练Token数需要合理配比；700亿参数的Chinchilla使用约四倍于Gopher的训练数据，并在相近训练计算预算下取得更好表现。该经验比例不能无条件外推到所有架构和训练方法。https://papers.neurips.cc/paper_files/paper/2022/hash/c1e2faff6f588870935f114ebe04a3e5-Abstract.html

[^p1-distillation]: Geoffrey Hinton、Oriol Vinyals、Jeff Dean，*Distilling the Knowledge in a Neural Network*，2015年；Victor Sanh等，*DistilBERT, a distilled version of BERT*，2019年；DeepSeek-AI，*DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning*，2025年1月22日。三组研究分别显示模型集成的行为可以迁移到单模型、BERT可以在特定基准上压缩，以及R1生成的推理样本可以训练基于Qwen与Llama的较小模型。它们不证明学生无损取得教师全部知识、权重、训练数据、长尾行为或安全属性；DeepSeek结果为作者技术报告中的基准数据。https://arxiv.org/abs/1503.02531 ；https://arxiv.org/abs/1910.01108 ；https://arxiv.org/abs/2501.12948

[^p1-synthetic-data]: Yizhong Wang等，*Self-Instruct: Aligning Language Models with Self-Generated Instructions*，ACL 2023；Ilia Shumailov等，*AI models collapse when trained on recursively generated data*，Nature 631，2024年7月24日。前者说明经过生成、过滤和微调的合成指令可以提升特定任务表现；后者显示，在其实验与理论设定中，无差别地用前代生成数据递归替代真实数据会逐渐丢失原分布长尾。两者共同说明合成数据的效果取决于真实数据锚点、筛选、任务设计和验证，不能概括为“合成数据必然有效”或“必然坍塌”。https://aclanthology.org/2023.acl-long.754/ ；https://www.nature.com/articles/s41586-024-07566-y

[^p1-two-frontiers]: Jared Kaplan等，*Scaling Laws for Neural Language Models*，2020年；Zhuohan Li等，*Train Large, Then Compress*，2020年；Stanford HAI，*AI Index 2025: Technical Performance*；Microsoft，*Phi-3 Technical Report*，2024年；GPTQ、AWQ与QLoRA原始论文。相关研究分别讨论扩大能力边界、训练后压缩、同一基准门槛所需模型规模下降、端侧小模型和低比特部署或高效微调。AI Index所述从5400亿到38亿参数的142倍变化只针对MMLU百分之六十门槛；各压缩论文的性能与速度也受模型、硬件和评测条件限制。https://arxiv.org/abs/2001.08361 ；https://arxiv.org/abs/2002.11794 ；https://hai.stanford.edu/ai-index/2025-ai-index-report/technical-performance ；https://arxiv.org/abs/2404.14219 ；https://arxiv.org/abs/2210.17323 ；https://arxiv.org/abs/2306.00978 ；https://arxiv.org/abs/2305.14314

[^p1-apertus]: ETH Zurich、EPFL与Swiss National Supercomputing Centre，*Apertus: a fully open, transparent, multilingual language model*，2025年9月2日；Apertus研究论文。项目发布8B与70B模型，使用约15万亿Token，覆盖一千多种语言并公开权重、数据准备材料、训练与评测代码和中间检查点。模型表现与“主权AI”价值主张主要来自项目方，正文只把它作为公共算力、完整开放和可追溯训练谱系的工程案例。https://ethz.ch/en/news-and-events/eth-news/news/2025/09/press-release-apertus-a-fully-open-transparent-multilingual-language-model.html ；https://doi.org/10.48550/arXiv.2509.14233

[^p1-apertus-mini]: Apertus团队，*Apertus Mini: LLM Family Expansion via Distillation and Quantization*，2026年6月15日；ETH AI Center，*Apertus 1.5: Building the next generation of open AI infrastructure*，2026年7月24日。项目从Apertus 8B教师蒸馏出0.5B、1.5B和4B基础及指令模型，并发布多个量化版本，共16个模型；“训练计算量低至常规预训练约十分之一”为作者在其方法与评测条件下的报告。https://www.apertus-ai.org/articles/2026-06-apertus-mini/ ；https://arxiv.org/abs/2605.29128 ；https://ai.ethz.ch/news-and-events/ai-center-news/2026/07/apertus-15-building-the-next-generation-of-open-ai-infrastructure.html

[^p1-olmo2-scale]: Ai2，*OLMo 2 32B*技术材料，2025年。OLMo 2 32B预训练约6万亿Token，使用160个节点、每节点8张H100，约1280张H100，并公开训练代码、数据处理材料、检查点和日志。公开材料用于说明开放提高检查和复现条件，但不等于第三方已经以同等成本复现，也不代表所有训练项目都需要相同资源。**置信度：项目方一手披露已确认；训练成本与外部复现效果需按具体配置验证。** https://allenai.org/blog/olmo2-32b

[^p1-mlperf]: MLCommons，*MLPerf Inference Benchmark Suite*及*MLPerf Inference v5.1 Results*，2025年9月。基准在规定准确度目标下比较推理性能，并针对大语言模型报告首Token延迟、输出Token间延迟与吞吐等指标。基准结果受模型、精度、硬件和负载约束，不能直接等同于真实业务价值。https://docs.mlcommons.org/inference/ ；https://mlcommons.org/2025/09/mlperf-inference-v5-1-results/

[^p1-iea-energy]: International Energy Agency，*Energy and AI*，2025年。IEA估算全球数据中心用电从2024年约415太瓦时上升到2030年约945太瓦时，AI是需求增长的重要驱动。估计包含情景与不确定性，正文不把全部增长归因于生成式AI。https://www.iea.org/reports/energy-and-ai/executive-summary

[^p1-inference-cost]: Stanford Institute for Human-Centered Artificial Intelligence，*AI Index 2025: State of AI in 10 Charts*，2025年。报告统计，达到相当于GPT-3.5能力水平的模型，其每百万Token推理价格从2022年11月约20美元下降到2024年10月约0.07美元，价格降至约原来的1/286，下降约99.65%。该比较依赖选定能力阈值和公开价格，不等同于服务商的物理边际成本。https://hai.stanford.edu/news/ai-index-2025-state-of-ai-in-10-charts

[^p1-prefill-decode]: NVIDIA，*Dynamo Overall Architecture*，核验至2026年7月31日；Bingyang Wu等，*POD-Attention: Unlocking Full Prefill-Decode Overlap for Faster LLM Inference*，2024年。两份材料说明大模型推理可区分处理输入上下文的Prefill阶段与逐步生成输出的Decode阶段，并可针对不同资源特征分离调度。NVIDIA材料属于厂商技术文档，论文结果受实验条件限制。https://docs.nvidia.com/dynamo/design-docs/overall-architecture ；https://arxiv.org/abs/2410.18038

[^p1-paged-attention]: Woosuk Kwon等，*Efficient Memory Management for Large Language Model Serving with PagedAttention*，SOSP 2023。论文研究KV Cache内存管理，并在指定模型、硬件与负载下以相近延迟获得相对当时对照系统二至四倍吞吐；该数值不能外推为所有系统的普遍收益。https://arxiv.org/abs/2309.06180

[^p1-agent-protocols]: Google，*Announcing the Agent2Agent Protocol*，2025年4月9日；Linux Foundation，A2A项目在2025年6月移交基金会及2026年4月生态更新；Linux Foundation，Agentic AI Foundation成立公告，2025年12月。相关材料说明A2A以Agent Card、Task、Message与Artifact等对象支持不同智能体互操作，支持机构在一周年时超过150家；AAIF最初托管MCP、goose与agents.md。开放协议解决交互语义，不自动解决身份、授权和任务结果可信问题。https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/ ；https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents ；https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year ；https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation

[^p1-ntia-open-weights]: U.S. National Telecommunications and Information Administration，*Dual-Use Foundation Models with Widely Available Model Weights Report*，2024年7月30日。报告基于332份公开意见，认为当时证据不足以支持对广泛可用模型权重作普遍限制，也不足以排除未来在新证据下采取措施。https://www.ntia.gov/programs-and-initiatives/artificial-intelligence/open-model-weights-report

[^p1-aws-ai-factories]: Amazon Web Services，*Introducing AWS AI Factories*及官方FAQ，2025年12月，核验至2026年7月31日。该方案由客户提供数据中心空间与电力，AWS部署和运营AI基础设施，说明设备位置、运营责任、数据控制和供应商依赖可以形成混合安排。正文不采用厂商性能宣传作为科学结论。https://aws.amazon.com/about-aws/whats-new/2025/12/aws-ai-factories/ ；https://aws.amazon.com/about-aws/global-infrastructure/ai-factories/faqs/

[^p1-uk-sovereign-compute]: HM Government，*National Security Strategy 2025: Security for the British People in a Dangerous World*，2025年。文件明确指出前沿技术的完全主权独立并不总是可能，并把主权算力描述为整体能力组合中用于独立服务国家优先事项的一部分。该材料用于说明选择性自主，不证明任何具体投资必然有效。https://www.gov.uk/government/publications/national-security-strategy-2025-security-for-the-british-people-in-a-dangerous-world/national-security-strategy-2025-security-for-the-british-people-in-a-dangerous-world-html

[^p1-iea-ai]: International Energy Agency，*Key Questions on Energy and AI*及2026年4月16日更新。IEA依据对能源与AI产业的持续跟踪指出，五家大型科技企业2025年资本支出超过四千亿美元，2026年预计继续大幅增加；数据中心用电在2025年增长百分之十七，AI数据中心增长更快。报告同时识别电网接入、燃气轮机、变压器、先进芯片与IT部件等现实瓶颈。资本支出与用电规模说明AI的物质基础，不直接证明投资效率或技术领先。https://www.iea.org/news/data-centre-electricity-use-surged-in-2025-even-with-tightening-bottlenecks-driving-a-scramble-for-solutions

[^p1-ai-index-2026]: Stanford Institute for Human-Centered Artificial Intelligence，*The 2026 AI Index Report*，2026年。报告统计，产业界生产了2025年超过九成的代表性前沿模型；受访组织的AI采用率达到88%；同时记录智能体基准能力快速提高但仍存在显著失败。AI Index汇总多种数据源、问卷与基准，适合说明产业结构与能力趋势，不应把采用率等同于成熟度，也不应把单项基准直接外推为真实世界可靠性。https://hai.stanford.edu/ai-index/2026-ai-index-report

[^p1-moving-frontier]: Stanford Institute for Human-Centered Artificial Intelligence，*The 2026 AI Index Report: Technical Performance*，截至2026年3月。报告记录Anthropic、xAI、Google与OpenAI的Arena评分相差不到25分，美国与中国模型自2025年以来多次交换领先位置；最强封闭模型相对最强开放模型的差距从2024年8月约0.5%扩大到2026年3月约3.3%。报告中的“open”主要指开放权重，Arena和综合基准受参与者偏好、模型适配和题目有效性限制，不能等同于真实世界的完整能力排名。https://hai.stanford.edu/ai-index/2026-ai-index-report/technical-performance

[^p1-cma-cloud]: UK Competition and Markets Authority，*Cloud Services Market Investigation: Summary of Final Decision*，2025年7月31日。CMA认定英国及欧洲经济区IaaS市场高度集中，Microsoft与AWS在2024年各占约百分之三十至四十；每年更换云服务商的客户不足百分之一。调查把资本门槛、规模经济、迁出费用、接口差异和技能不可转移等列为进入、切换与多云障碍，并指出云服务支撑AI模型开发和部署。数据针对英国及欧洲经济区云市场，不能直接当作全球市场份额。https://assets.publishing.service.gov.uk/media/688b20e6ff8c05468cb7b120/summary_of_final_decision.pdf

[^p1-device-models]: Microsoft，*Phi-3 Technical Report*，2024年4月；Google，*Gemma 3n*技术说明，核验至2026年8月3日；Apple，*Apple Intelligence Foundation Language Models*技术报告，2025年8月。Phi-3-mini报告3.8B参数、约3.3万亿训练Token、MMLU约69%，并讨论现代手机端运行；Gemma 3n E2B名义参数超过5B，但通过参数跳过和分层嵌入缓存使有效内存负载约1.91B；Apple端侧模型约3B参数，采用蒸馏、稀疏化和2-bit量化感知训练，定位于摘要、实体抽取、文本理解和短对话等任务。上述材料说明端侧扩散是任务型、压缩型能力扩散，不证明手机模型与云端通用模型等价。**置信度：项目方技术报告与官方文档已确认；性能和设备体验受作者评测、硬件与任务限制。** https://arxiv.org/abs/2404.14219 ；https://ai.google.dev/gemma/docs/gemma-3n ；https://arxiv.org/abs/2507.13575

[^p1-frontier-models-2026]: Moonshot AI，*Kimi K3*官方仓库与技术报告，2026年7月；DeepSeek，*DeepSeek V4*官方发布与产品文档，2026年4月，核验至2026年8月4日。Kimi K3项目方披露2.8万亿总参数、约1040亿激活参数、896个专家、每Token选择16个专家、约1,048,576上下文，并使用MXFP4权重与MXFP8激活；DeepSeek V4官方披露V4-Pro为1.6万亿总参数/49B激活、V4-Flash为284B总参数/约13B激活，并支持1M上下文。参数、架构、上下文和量化规格是项目方资料；基准、速度、价格和“领先”结论受模型、硬件、harness与推理强度影响，不能用公开总参数直接判断能力超过未公开参数的GPT系列。**置信度：规格为官方/作者一手披露已确认；跨模型能力比较为条件性结果。** https://github.com/MoonshotAI/Kimi-K3 ；https://arxiv.org/abs/2607.24653 ；https://api-docs.deepseek.com/news/news260424/ ；https://api-docs.deepseek.com/quick_start/pricing/

[^p1-small-model-family-2026]: Alibaba、Qwen团队，*Qwen3*官方发布与技术报告，2025年4月29日；Google DeepMind，Gemma官方发布记录与Gemma 3n说明，核验至2026年8月4日；Qwen团队，*Qwen3-ASR Technical Report*，2026年1月。Qwen3覆盖0.6B、1.7B、4B、8B、14B、32B稠密模型以及30B-A3B、235B-A22B MoE；Gemma系列提供270M、1B、4B、12B、27B及E2B/E4B端侧形态，并继续发布函数调用、翻译、医疗和语音等专用模型；Qwen3-ASR提供0.6B与1.7B语音识别模型。模型尺寸、架构与发布状态来自项目方；性能、内存、延迟和设备体验受作者评测、硬件、任务与许可证限制。**置信度：模型家族规格为一手材料已确认；能力横向比较不作普遍外推。** https://qwenlm.github.io/blog/qwen3/ ；https://arxiv.org/abs/2505.09388 ；https://ai.google.dev/gemma/docs/releases ；https://ai.google.dev/gemma/docs/gemma-3n ；https://arxiv.org/abs/2601.21337

[^p1-user-facing-2026]: DeepSeek，*Thinking Mode*与价格文档，核验至2026年8月4日；OpenAI API参考文档，核验至2026年8月4日；Qwen3、Kimi K3、Gemma 3n及Qwen3-ASR官方技术资料。相关材料显示，服务可按思考/非思考、模型大小、上下文长度、工具调用和路由策略调整等待、Token用量与成本；端侧模型可以承担语音、视觉、分类、函数调用和脱敏等窄任务。接口字段与产品规格是官方资料，不证明“思考Token”是完整可审计的内部过程，也不保证长上下文、路由或端侧体验在所有任务上可靠。**置信度：接口和规格为官方材料已确认；具体效果受实现、硬件和任务边界限制。** https://api-docs.deepseek.com/guides/thinking_mode ；https://api-docs.deepseek.com/quick_start/pricing/ ；https://platform.openai.com/docs/api-reference/chat/create

[^p3-work-evidence]: Microsoft Research，*Shifting Work Patterns with Generative AI*，2025年4月；Microsoft、Accenture等，*Generative AI and the Nature of Work*，*Management Science*，2026年；METR，*Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity*，2025年7月。Microsoft跨行业六个月随机现场实验约覆盖6000名知识工作者，实际使用者每周邮件时间减少约3小时，但会议时间未显著变化；企业开发现场研究合并4867名开发者，报告完成任务数平均增加26.08%，不同企业结果存在差异；METR对16名经验开发者和246项成熟开源项目任务的随机实验报告完成时间增加19%。这些结果分别回答邮件行为、任务数量和真实项目耗时，不应合并成“AI普遍提高生产率”，也不证明长期组织效果。**置信度：前两项为研究论文/随机现场研究，METR为预印本与公开实验报告；跨任务外部有效性有限。** https://www.microsoft.com/en-us/research/publication/shifting-work-patterns-with-generative-ai/ ；https://pubsonline.informs.org/doi/10.1287/mnsc.2025.00535 ；https://arxiv.org/abs/2507.09089

[^p3-task-boundaries]: EAMT 2024英语—德语机器翻译后编辑研究，21名专业译员中14人偏好文本转语音辅助，但质量与编辑距离没有改善、速度出现负面效果；Shakked Noy、Whitney Zhang，*Experimental Evidence on the Productivity Effects of Generative Artificial Intelligence*，*Science*，2023年，453名专业人士的写作实验报告平均用时减少40%、质量提高18%；爱尔兰公共部门预注册实验，*Generative AI in the Workplace: Evidence from a Field Experiment*，2025年，文档任务质量提高17%、耗时减少34%，数据分析任务质量下降12%、耗时差异不显著。三组结果支持“收益依赖任务边界”的判断，不证明AI普遍提高翻译、写作或数据分析生产率。**置信度：翻译研究与Science论文为同行评审材料；爱尔兰研究为预印本/现场实验，外部有效性有限。** https://aclanthology.org/2024.eamt-1.38/ ；https://doi.org/10.1126/science.adh2586 ；https://arxiv.org/abs/2502.09479

[^p3-finland-translation]: 芬兰赫尔辛基大学研究团队，*Evaluation of generative artificial intelligence implementation in a social and healthcare services translation team*，*JMIR Formative Research*，2025年，DOI 10.2196/73658。2024年3—6月，4名内部译员完成908个翻译片段，GPT-4后编辑平均速度比人工基线快14%；芬兰语—瑞典语仅141/1261（11%）、芬兰语—英语18/112（16%）无需编辑。结果只适用于该团队、语言对和Trados后编辑流程，不能外推为机器翻译可直接交付。**截至：2026-08-03；置信度：同行评审、真实团队过程数据已确认，但样本小。** https://doi.org/10.2196/73658

[^p3-argentina-ai]: 世界银行工作论文与NBER Working Paper 34851，*Does Generative AI Narrow Skill Productivity Gaps?*，2026年。阿根廷1,174名25—45岁成年人随机完成带激励的商业问题分析任务；GPT-4.1使低/高技能组分差从0.548个标准差降至0.139个标准差，低技能者处理效应比高技能者高0.408个标准差，约闭合74%的基线差距。任务为一次性自包含情境，工作论文的评分和长期外部有效性仍有限，不能直接外推到企业长期绩效、收入或就业。**截至：2026-08-03；置信度：随机实验和样本规模已确认，长期机制待验证。** https://thedocs.worldbank.org/en/doc/5fa3b40f263a4a22e1572954980189c9-0370012026/original/5-Does-Generative-AI-narrow-skill-productivity-gaps.pdf ；https://www.nber.org/papers/w34851

[^p3-ai-marketing]: *The power of generative marketing*，*International Journal of Research in Marketing*，2025年，DOI 10.1016/j.ijresmar.2024.09.002。研究比较10,320张AI合成营销图片、2,400张人工图片和254,400次人工评价，并观察超过173,000次现场广告曝光；特定横幅广告场景中，最佳AI图像点击率比人工图库图高50%。该结果只支持营销素材场景的点击差异，不等于品牌长期资产、销售利润或公共内容质量全面改善。**截至：2026-08-03；置信度：同行评审和现场曝光研究已确认，外部有效性受场景限制。** https://doi.org/10.1016/j.ijresmar.2024.09.002

[^p4-sierra-leone-ai]: Google，*Measuring the impact of AI on teaching and learning*，2026年5月19日。Google与当地教师合作，在塞拉利昂进行八周预注册随机试验，将48个数学课堂、近1800名七、八年级学生分为受引导的Gemini学习工具组和常规课堂组；项目方报告外部评估成绩提高0.26个标准差，达到建议使用量的学生提高0.38个标准差。材料来自项目方发布与技术报告，不能单独证明长期学习、跨学科或跨国家效果；它最适合说明教学设计、教师参与、使用剂量与模型共同决定结果。**置信度：项目方披露的随机试验已确认；独立复现和长期外部有效性待观察。** https://blog.google/products-and-platforms/products/education/measuring-the-impact-of-ai-on-teaching-and-learning/

[^p4-pnas-ai-learning]: *Generative AI Can Harm Learning: An RCT of AI Tutors in High School Mathematics*，*Proceedings of the National Academy of Sciences*，2025年，DOI:10.1073/pnas.2422633122。该现场实验比较普通学习、通用生成式AI与带教学护栏的AI辅导，报告即时表现与撤掉工具后的独立学习结果并不相同：未受约束的生成式AI可能提高当下解题表现，却损害后续独立表现，带护栏的辅导系统没有出现同样下降。**置信度：同行评审现场实验；具体效应受样本、课程、工具和测验设计限制，不应外推为所有教育AI必然有害。** https://doi.org/10.1073/pnas.2422633122

[^p4-kaiser-scribe]: Kaiser Permanente Division of Research，*AI-assisted notetaking gains steady support from Kaiser Permanente physicians*，2025年4月1日；相关NEJM Catalyst研究。2023年10月至2024年12月，AI记录助手被7260名医生用于2576627次就诊，机构分析称节省近16000小时记录时间；调查中88%的医生认为互动改善，患者调查中8%表示对使用技术有一定不适。该系统生成转录和摘要，不提供诊疗建议，医生可审阅、修改，患者被告知正在使用。数据来自单一医疗集团的部署与调查，不能外推为临床结局改善。**置信度：机构研究与官方披露已确认；效果和患者体验存在选择偏差，临床安全与长期经济性仍需独立验证。** https://divisionofresearch.kp.org/news/ai-assisted-notetaking-gains-steady-support-from-kaiser-permanente-physicians/

[^p6-uk-government-ai]: UK Government Digital Service，*Microsoft 365 Copilot Experiment: Cross-Government Findings Report*，2025年6月2日；Department for Science, Innovation and Technology、Government Digital Service，*AI coding assistant trial*，2025年9月12日。前者在2024年9月至12月覆盖12个政府组织、约20000名员工，评估文档、邮件、表格、演示和会议中的效率、质量与满意度；后者在2024年11月至2025年2月向中央政府组织提供2500个代码助手许可，并收集遥测、满意度与退出调查。部署规模与试验设计已由政府文件确认，但不等于财政节省、公共服务质量改善或长期生产率提升。**置信度：政府一手文件已确认；结果指标和跨部门外部有效性需按报告方法解释。** https://www.gov.uk/government/publications/microsoft-365-copilot-experiment-cross-government-findings-report ；https://www.gov.uk/government/publications/ai-coding-assistant-trial

## 第二章　为什么AI需要主权

[^p2-function-calling]: OpenAI，*Function calling and other API updates*，2023年6月13日。该机制允许开发者以结构化方式描述函数，由模型生成函数名称与参数；通常仍由应用程序校验并执行实际调用。正文据此区分“模型生成调用意图”与“外部软件改变状态”。https://openai.com/index/function-calling-and-other-api-updates/

[^p2-react]: Shunyu Yao等，*ReAct: Synergizing Reasoning and Acting in Language Models*，ICLR 2023。论文研究语言模型交替生成推理轨迹与环境行动，并通过外部环境获得反馈的结构。它证明一种智能体工程路径，不证明模型拥有意识或在开放环境中稳定自主。https://openreview.net/forum?id=WE_vluYUL-X

[^p2-cruise]: U.S. National Highway Traffic Safety Administration，*Consent Order with Cruise for Incomplete Crash Reporting*，2024年9月30日及同意令。NHTSA指出Cruise提交的若干事故报告未完整披露2023年10月2日事故后的拖行动作，处以150万美元处罚并要求两年内持续提交运营范围、软件更新和安全表现报告。Cruise自动驾驶系统不是大语言模型智能体，正文只把它作为行动自动化的制度先例。https://www.nhtsa.gov/press-releases/consent-order-cruise-crash-reporting ；https://www.nhtsa.gov/sites/nhtsa.gov/files/2024-09/cruise-consent-order-2024-web.pdf

[^p2-a2a-task]: A2A Project，*Agent2Agent Protocol Specification*，核验至2026年8月1日。规范把Task定义为具有唯一标识、状态与生命周期的工作单位，支持执行中、等待输入或授权、完成、失败、取消和拒绝等状态以及异步更新与Artifact交付。协议仍需具体实现身份、权限和业务补救。https://github.com/a2aproject/A2A/blob/main/docs/specification.md

[^p2-mcp-auth]: Model Context Protocol，*Authorization Specification*，2025年11月25日稳定版本，核验至2026年8月1日。规范以OAuth机制表达面向特定资源的访问，强调资源绑定、最小权限和在需要时逐步提升授权，并禁止把收到的令牌原样透传给下游服务。规范仍在演进，不能替代应用自己的权限策略。https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization

[^p1-gdpr]: Regulation (EU) 2016/679，Article 20。在条文规定的适用条件下，数据主体有权以结构化、常用且机器可读的格式接收其提供的个人数据，并将数据传给另一控制者。https://eur-lex.europa.eu/eli/reg/2016/679/oj

[^p1-data-act]: Regulation (EU) 2023/2854（欧盟《数据法》），尤其见第23—30条及第50条。法规自2025年9月12日起适用，包含数据处理服务切换、合同信息、机器可读导出、开放接口、业务连续和互操作等要求。https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32023R2854

[^p1-otel-genai]: OpenTelemetry，*Inside the LLM Call: GenAI Observability with OpenTelemetry*及生成式AI语义约定，2026年5月14日，核验至2026年7月31日。相关规范和演示把模型调用、令牌使用、智能体调用与工具执行纳入分布式追踪，并明确完整提示、回复和工具结果属于需要选择性记录的敏感内容。生成式AI语义约定仍在持续演进。https://opentelemetry.io/blog/2026/genai-observability/ ；https://opentelemetry.io/docs/specs/semconv/gen-ai/

[^p2-tech-sovereignty]: Christoph March、Ina Schieferdecker，*Technological Sovereignty as Ability, Not Autarky*，*International Studies Review* 25(2)，2023年。论文把技术主权界定为理解、评价、选择、获取、改造和使用关键技术的能力，明确区分主权与技术自给自足。Stéphane Couture与Sophie Toupin对数字、网络和技术主权用法的研究也显示，该概念既被国家使用，也被公民技术共同体用于表达替代性实践。https://doi.org/10.1093/isr/viad012 ；https://doi.org/10.1177/1461444819865984

## 第三章　个人：AI主权从自己开始

[^p3-nist-agent-id]: NIST/National Cybersecurity Center of Excellence，*New Concept Paper on Identity and Authority of Software Agents*，2026年2月5日。概念文件把软件与AI智能体的身份、授权、审计和不可抵赖列为专门议题；其性质是研究与标准化倡议，并非已经定型的标准。https://www.nist.gov/news-events/news/2026/02/new-concept-paper-identity-and-authority-software-agents

[^p3-mata]: United States District Court, Southern District of New York，*Mata v. Avianca, Opinion and Order on Sanctions*，Case 1:22-cv-01461-PKC，Document 54，2023年6月22日。裁定确认相关律师提交了由ChatGPT生成的虚构判例及引文，并强调律师仍负有核验提交材料的责任。https://www.nhd.uscourts.gov/sites/default/files/pdf/Mata-v-Avianca-sanctions-order.PDF

[^p3-cognition]: Eleanor Dillon等，*Shifting Work Patterns with Generative AI*，2025年，六个月、六千名跨行业知识工作者随机现场实验；Hao-Ping Lee等，*The Impact of Generative AI on Critical Thinking*，CHI 2025，对319名知识工作者与936个实际用例的调查。前者报告使用者每周邮件时间减少约三小时、意向治疗估计约一点四小时，会议时间未显著变化；后者发现更高的AI信心与更少自报批判性思考相关，更高的任务自信与更多自报批判性思考相关，并观察到思考转向核验、整合与任务看管。前者主要测量行为变化，后者为横截面自报关联；两者均不能证明长期技能必然增强或衰退。https://www.microsoft.com/en-us/research/publication/shifting-work-patterns-with-generative-ai/ ；https://doi.org/10.1145/3706598.3713778

[^p3-opc-mechanism]: Ronald Coase，*The Nature of the Firm*，1937年及其1991年诺贝尔奖演讲，把发现价格、谈判、签约、检查和解决争议等交易成本用于解释企业边界；Shakked Noy、Whitney Zhang在453名专业人士的预注册写作实验中报告使用ChatGPT使平均用时下降40%、质量提高18%；Erik Brynjolfsson、Danielle Li、Lindsey Raymond研究5,179名客服人员，报告生成式AI助手使每小时解决问题数平均提高14%，新手和低技能员工改善更明显；Fabrizio Dell’Acqua等对758名知识工作者的预注册实验则发现，AI在能力边界内改善速度和质量，在边界外的一项复杂任务上使正确率下降。前三类实验说明AI能够降低部分认知、表达和协调成本，不能证明创业全流程都能自动化，也不能证明OPC普遍优于团队。**置信度：经典原始论文、同行评审实验和大型现场研究已确认；跨任务与长期组织效果待验证。** https://doi.org/10.1111/j.1468-0335.1937.tb00002.x ；https://www.nobelprize.org/prizes/economic-sciences/1991/coase/lecture/ ；https://doi.org/10.1126/science.adh2586 ；https://www.nber.org/papers/w31161 ；https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321

[^p3-opc-signal]: U.S. Census Bureau，2023年Nonemployer Statistics及2026年小企业数据说明，记录30,427,808个无雇员经营单位，占全部经营单位78.4%，总收入接近1.8万亿美元；多数为自雇者经营的非公司制业务，不等于AI OPC。Stripe Atlas于2026年5月披露，其平台当年第二季度截至统计时新设C公司中单一创始人占63%，同时报告普通与头部单人创业者的收入差距扩大；该结果存在平台选择、公司类型与观察期偏差。OECD的创业政策综述也提醒，一人/无雇员企业在创业数量中占主导，但平均增长和就业贡献有限，少数网络化、技能型个体可以高度创新。正文据此把OPC视为建立在既有微型经济底盘上的新趋势信号，不把平台数据写成社会总体比例或AI因果效果。**置信度：美国官方统计已确认；Stripe为利益相关平台样本；AI导致的长期增收与存活效果待验证。** https://www.census.gov/library/stories/2026/05/small-business-week.html ；https://www.census.gov/library/stories/2025/07/nonemployer-business-growth.html ；https://stripe.com/blog/top-solo-founder-traits ；https://www.oecd.org/en/publications/international-compendium-of-entrepreneurship-policies_338f1873-en/full-report/objectives-and-challenges-of-entrepreneurship-policy_f354bd94.html

## 第四章　组织：守住共同体的边界

[^p4-sweden-school]: European Data Protection Board，*Facial recognition in school renders Sweden’s first GDPR fine*，2019年8月22日。瑞典一所高中以人脸识别记录出勤，涉及22名学生；监管机构认为敏感生物识别数据处理缺少适当法律基础、影响评估不足，且师生权力差异使同意不能成为有效依据。https://www.edpb.europa.eu/news/national-news/2019/facial-recognition-school-renders-swedens-first-gdpr-fine_en

[^p4-dfe-data]: UK Department for Education，*Generative artificial intelligence (AI) and data protection in schools*，页面更新至2026年7月9日。指引要求学校理解AI工具怎样收集、处理和保存个人数据，在隐私说明中披露，并在工具更新后持续评估风险。https://www.gov.uk/guidance/data-protection-in-schools/generative-artificial-intelligence-ai-and-data-protection-in-schools

[^p4-royal-free]: UK Information Commissioner’s Office，关于Royal Free London NHS Foundation Trust与Google DeepMind事件的回顾页面，核验至2026年8月1日。ICO说明，该合作涉及约160万名患者的数据，并在2017年认定数据处理未充分遵守数据保护法；正文据此讨论受托机构在目的说明、影响评估与责任链上的义务。https://ico.org.uk/for-the-public/ico-40/google-deepmind-and-class-action-lawsuit/

[^p4-who-lmm]: World Health Organization，*Ethics and governance of artificial intelligence for health: Guidance on large multi-modal models*，2024年1月18日。WHO建议大规模部署后开展独立审计和影响评估，并让患者、医务人员等直接和间接相关者参与设计。https://www.who.int/news/item/18-01-2024-who-releases-ai-ethics-and-governance-guidance-for-large-multi-modal-models

[^p4-ofqual]: UK Office of Qualifications and Examinations Regulation，2020年夏季成绩后续分析与学生层平等分析。Ofqual报告约59%的成绩与教师评估相同、约39%低于教师评估，10.3%的考生累计被下调至少三个等级；其平等分析未发现计算成绩对特定受保护群体产生新的系统性差异证据。该系统是疫情下的统计标准化制度先例，不是生成式AI；也无法知道取消考试条件下哪种分数最接近个体真实表现。https://www.gov.uk/government/publications/evaluation-of-centre-assessment-grades-and-grading-gaps-in-summer-2020/grading-gaps-in-summer-2020-who-was-affected-by-differences-between-centre-assessment-grades-and-calculated-grades ；https://www.gov.uk/government/publications/student-level-equalities-analyses-for-gcse-and-a-level

[^p4-alphafold3]: Josh Abramson等，*Accurate structure prediction of biomolecular interactions with AlphaFold 3*，*Nature*，2024年5月；*Nature*编辑说明与2024年11月论文增补；Google DeepMind官方代码仓库。论文初始发布主要提供受限服务器，随后公开推理代码并记录变化，模型参数与用途仍有许可边界。该事件体现开放科学、复现与商业权利冲突，不是研究不端案例，也不能在后续开放后继续称为“完全无法复现”。https://www.nature.com/articles/s41586-024-07487-w ；https://www.nature.com/articles/d41586-024-01463-0 ；https://www.nature.com/articles/s41586-024-08416-7 ；https://github.com/google-deepmind/alphafold3

[^p4-science-data]: Cristian Bodnar等，*A foundation model for the Earth system*，*Nature*，2025年5月。Aurora在超过一百万小时、来源与分辨率不同的地球系统数据上预训练，并针对空气质量、海浪、热带气旋和高分辨率天气等任务微调。论文支持“科学基础模型可能需要原始、结构化和多模态观测，而不只是论文文本”的判断，不证明Aurora适用于所有学科，也不证明模型预测无需物理实验和独立检验。**置信度：同行评审论文已确认，跨学科推论属于本书有限外推。** https://doi.org/10.1038/s41586-025-09005-y

[^p4-epic-sepsis]: Karandeep Singh等，*A Validated Model for Sudden Sepsis?*，*JAMA Internal Medicine*，2021年；Matthew J. Fralick等，Epic Sepsis Model第二版多中心前瞻性验证，*JAMA Network Open*，2026年。第一项研究在38,455次住院中报告建议阈值下漏掉约67%的脓毒症患者、约18%住院触发警报、住院层面AUC约0.63；第二项在四个医疗系统227,091次住院中报告AUROC约0.82—0.92、阳性预测值约0.13—0.26，并强调本地验证与警报工作流。性能研究不证明具体伤害或新版降低死亡率。https://pmc.ncbi.nlm.nih.gov/articles/PMC8218233/ ；https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2845595

[^p4-unhcr-biometric]: UNHCR Jordan，*Biometrics in the registration and assistance process*，2022年2月。官方说明生物特征用于身份确认、防止重复登记、现金援助领取、身份续期、难民身份与安置程序；银行通过有限接口核验，不持有完整虹膜数据库。材料证明用途和核验网络扩大，不证明发生违法共享或滥用。https://help.unhcr.org/jordan/wp-content/uploads/sites/46/2022/02/Biometrics-EN-Edited-Feb2022.pdf

[^p4-icrc-biometric]: International Committee of the Red Cross，*Innovation, protection and ICRC biometrics policy*，2019年10月18日。ICRC讨论把生物特征保存在受助者持有的卡片或令牌中、现场核验而不建立中心数据库的设计，并指出捐助方对反欺诈和端到端审计的要求会推动生物识别扩张。该方案是机构政策与架构选择，不代表所有行动中普遍实施或适用于全部场景。https://blogs.icrc.org/law-and-policy/2019/10/18/innovation-protection-icrc-biometrics-policy/

## 第五章　企业：把智能变成可治理的能力

[^p5-a2a-task]: Linux Foundation，*Agent2Agent Protocol Specification / Core Concepts*，核验至2026年8月1日。A2A把Task定义为带有唯一标识、状态和生命周期的有状态工作单位，把Artifact定义为任务生成的文档、图像或结构化数据等实际交付物，并支持流式更新和异步通知。协议解决互操作语义，不自动提供企业授权、数据治理或结果真实性保证。https://a2a-protocol.org/latest/topics/key-concepts/

[^p5-mcp-auth]: Model Context Protocol，*Authorization*与*Security Best Practices*，采用2025年11月25日稳定版本，核验至2026年8月1日。规范要求HTTP传输中的资源服务器验证访问令牌的目标受众，并明确禁止把上游收到的令牌原样透传给下游服务；下游访问应使用面向该资源的独立令牌，以降低令牌误用和“困惑代理”风险。MCP授权规范仍在演进，不等于已经解决具体应用的权限设计。https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization

[^p5-knight]: U.S. Securities and Exchange Commission，*SEC Charges Knight Capital With Violations of Market Access Rule*，2013年10月16日。SEC记录显示，2012年8月1日开盘后的45分钟里，错误路由为212笔客户订单发送超过400万条订单，造成超过4.6亿美元损失；系统发出的97封异常邮件没有成为有效警报。https://www.sec.gov/newsroom/press-releases/2013-222

[^p5-industrial-copilot]: Siemens、thyssenkrupp，Industrial Copilot在电池质量检测设备与工业维护中的应用说明，2024年；Siemens工业AI编排架构。材料说明系统能够生成结构化控制语言代码、辅助机器可视化和故障解释，技术栈同时涉及Siemens自动化、Microsoft Azure OpenAI及规划中的NVIDIA本地方案；编排架构把政策、安全与控制网关置于AI和PLC之间。功能状态与收益主要是厂商披露，架构存在不等于绝对安全或全面生产运行。**置信度：厂商一手披露，部署边界待独立验证。** https://press.siemens.com/global/en/pressrelease/siemens-industrial-copilot-expanded-adopted-thyssenkrupp ；https://www.siemens.com/en-gb/content/architecture-hub/industrial-ai-orchestration-layer/

[^p5-morgan-stanley]: Morgan Stanley，2023年与OpenAI合作公告及2024年Debrief发布材料；OpenAI客户案例。首个工具面向内部知识检索，Debrief在客户同意后生成会议笔记、行动项和邮件草稿，最终邮件由顾问编辑和发送；持续评测、采用率和效率数字主要来自公司与供应商，不能等同独立审计或证明从未出错。https://www.morganstanley.com/press-releases/key-milestone-in-innovation-journey-with-openai ；https://www.morganstanley.com/press-releases/ai-at-morgan-stanley-debrief-launch ；https://openai.com/index/morgan-stanley/

[^p5-finra-genai]: Financial Industry Regulatory Authority，Regulatory Notice 24-09，*Regulatory Notice Related to GenAI*，2024年6月27日。FINRA强调现有规则技术中立，成员使用第三方或嵌入式生成式AI仍应建立与业务相适应的监督体系，覆盖模型风险、数据隐私与完整性、可靠性和准确性。通知不能证明任何具体企业控制已经有效。https://www.finra.org/rules-guidance/notices/24-09

[^p5-nist-agent]: NIST，*CAISI Issues Request for Information About Securing AI Agent Systems*，2026年1月12日；以及*AI Agent Standards Initiative*。相关工作关注模型输出与软件功能结合后的独特风险，覆盖身份、授权、审计、互操作和提示注入防护。其性质包括征求意见、倡议和技术研究。https://www.nist.gov/news-events/news/2026/01/caisi-issues-request-information-about-securing-ai-agent-systems

[^p5-operator]: OpenAI，*Operator System Card*，2025年1月23日。OpenAI报告，无产品层防护的模型在100项近似真实任务中产生13次会造成麻烦的错误，其中5次较难逆转或可能较严重；确认等措施使估计风险降低约90%，在607项风险动作评测中确认召回率约92%。提示注入监测器在77次红队攻击上报告99%召回、90%精确率，并在13,704个正常画面中误报46次。全部数字均为厂商自测，不能外推为真实生产事故率或其他智能体的安全水平。**置信度：厂商自测已确认，外部效度有限。** https://openai.com/index/operator-system-card/

[^p5-echoleak]: Pavan Reddy、Aditya Sanjay Gujral，*EchoLeak: The First Real-World Zero-Click Prompt Injection Exploit in a Production LLM System*，2025年；Microsoft CVE-2025-32711。研究者在Microsoft 365 Copilot中验证了无需用户点击的间接提示注入与数据外传路径。漏洞经协调披露后由微软在服务端修复；公开材料没有显示其已被用于大规模真实攻击。https://arxiv.org/abs/2509.10540 ；https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32711

[^p5-amazon-q]: Amazon Web Services，*AWS Security Bulletin AWS-2025-015*，2025年。AWS确认攻击者利用权限配置不当的GitHub令牌向Amazon Q Developer开源仓库提交代码，该代码进入VS Code扩展1.84.0；恶意代码因语法错误未成功执行。AWS撤销相关凭据、下架版本并发布1.85.0。https://aws.amazon.com/security/security-bulletins/AWS-2025-015/

[^p5-rite-aid]: U.S. Federal Trade Commission，*Rite Aid Banned from Using AI Facial Recognition After FTC Says Retailer Deployed Technology without Reasonable Safeguards*及FTC投诉书，2023年12月19日。FTC投诉称系统产生数千次错误匹配，企业在部署前后缺少合理的准确性评估和持续监控；正文中的十一岁女孩案例来自投诉书。正文以“FTC指控”表述，没有把监管投诉写成无争议司法判决。https://www.ftc.gov/news-events/news/press-releases/2023/12/rite-aid-banned-using-ai-facial-recognition-after-ftc-says-retailer-deployed-technology-without ；https://www.ftc.gov/system/files/ftc_gov/pdf/2023190_riteaid_complaint_filed.pdf

[^p5-production-frictions]: NIST，*AI Risk Management Framework Core*，核验至2026年8月1日；OpenTelemetry，*Generative AI Semantic Conventions / GenAI Observability*，2026年。NIST要求在AI完整生命周期中持续管理第三方依赖、变更、监测、事故恢复与安全退役；OpenTelemetry开始统一记录模型调用、Token用量、Agent跨度和工具执行。两者支持“生产治理必须跨越模型并进入运行”的判断，并不提出正文的六项企业症状分类，也不证明任何具体控制层实现有效。**置信度：官方标准框架与规范已确认，企业分类属于本书综合推导。** https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ ；https://opentelemetry.io/blog/2026/genai-observability/

[^p5-data-work]: Timnit Gebru等，*Datasheets for Datasets*，Communications of the ACM，2021年；Nithya Sambasivan等，*“Everyone wants to do the model work, not the data work”: Data Cascades in High-Stakes AI*，CHI 2021。前者提出记录数据集动机、组成、收集过程、用途和限制；后者访谈印度、美国及东非、西非的53名高影响AI从业者，分析被低估的数据工作怎样在项目中形成级联问题。研究支持数据来源、语境和组织责任的重要性，不证明所有企业都缺少训练数据，也不意味着结构化文档能够自动消除偏差。**置信度：同行评审研究已确认，跨企业普遍性需谨慎外推。** https://doi.org/10.1145/3458723 ；https://doi.org/10.1145/3411764.3445518

[^p5-era-experience]: David Silver、Richard S. Sutton，*Welcome to the Era of Experience*，2025年。两位作者主张，智能体可从长时间、基于现实环境的行动与观察流中获得经验，并在运行期适应；文章同时提醒，长时自主运行会减少人的介入点，使追踪、解释和控制更加困难。该文是研究纲领和理论判断，不是已经证明所有系统都能从经验中可靠学习的实证结论。正文把它转化为企业反馈治理与AgenticOps命题，并非沿用演讲文本。**置信度：作者原文已确认，未来趋势仍待实证。** https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf

[^p5-confidential-hybrid]: Google Cloud，*Google Distributed Cloud*；NVIDIA，*Confidential Containers Reference Architecture*；NIST IR 8320E初始公开草案，*Hardware-Enabled Security: Confidential Computing of Data in Cloud Workloads*，2026年5月29日；Confidential Computing Consortium，*A Technical Analysis of Confidential Computing*，核验至2026年8月1日。分布式云提供本地、边缘及不连接公共互联网的隔离部署形态；可信执行环境以硬件隔离、内存保护和远程证明保护使用中的数据。CCC把证明描述为可供另一方判断是否信任代码来源和当前状态的证据，并明确不存在“绝对安全”；NVIDIA文档把可用性和部分物理攻击列在能力边界之外。NIST文件仍是初始公开草案。四项材料共同证明物理位置、基础设施所有权和数据控制可以被不同安排，不证明代码业务逻辑、模型输出或硬件供应链天然可靠。**置信度：技术机制与参考架构已确认，安全效果依赖硬件、配置、信任策略、证明服务和运维。** https://cloud.google.com/distributed-cloud ；https://docs.nvidia.com/datacenter/cloud-native/confidential-containers/latest/overview.html ；https://csrc.nist.gov/pubs/ir/8320/e/ipd ；https://confidentialcomputing.io/wp-content/uploads/sites/10/2023/03/CCC-A-Technical-Analysis-of-Confidential-Computing-v1.3_Updated_November_2022.pdf

[^p5-ai-demand]: International Energy Agency，*Key Questions on Energy and AI*，2026年。IEA估计近年来单项AI任务能耗至少以每年一个数量级下降，推理、视频与Agent任务的单次能耗又可能是简单文本生成的数百至数千倍；全球数据中心用电在2025年增长17%，其中面向AI的数据中心增长约50%。IEA同时明确指出，全球AI使用频率与深度仍缺少完整统计，需求由效率、采用率和能力变化三项不确定趋势共同决定。正文据此只论证“效率与任务扩张并存”，不把能源增长等同于经济价值，也不把反弹效应写成必然规律。**置信度：IEA综合估计，多项口径仍需随披露更新。** https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary

[^p5-model-routing]: Ding D. et al.，*Hybrid LLM: Cost-Efficient and Quality-Aware Query Routing*，arXiv:2404.14618，2024年；Gupta S. et al.，*A Unified Approach to Routing and Cascading for LLMs*，arXiv:2410.10347，2024年。前者在特定实验中报告最多减少约40%的大模型调用而不损失总体质量；后者统一比较路由与级联方法，强调质量估计器决定成本—性能收益。两项均为研究实验，不证明任意企业任务都能获得相同比例的节省。**置信度：论文结果已确认，外部有效性依任务、模型与评测而变。** https://arxiv.org/abs/2404.14618 ；https://arxiv.org/abs/2410.10347

[^p5-model-runtime-2026]: DeepSeek，*Thinking Mode*与价格文档，核验至2026年8月4日；OpenAI Chat Completions API参考文档，核验至2026年8月4日；vLLM，*Quantized KV Cache*工程文档，核验至2026年8月4日。相关材料区分输入、缓存命中输入、输出和推理Token，并说明长上下文会增加KV Cache与服务压力；MoE激活参数、量化、路由、重试和工具调用共同决定一次任务的真实成本。API价格和缓存折扣是服务报价，不等于物理边际成本；KV Cache量化和路由收益受模型、硬件、批量、校准与质量估计器限制。**置信度：接口与工程机制为官方材料已确认；生产成本效果需按组织环境测量。** https://api-docs.deepseek.com/guides/thinking_mode ；https://api-docs.deepseek.com/quick_start/pricing/ ；https://platform.openai.com/docs/api-reference/chat/create ；https://docs.vllm.ai/en/latest/features/quantization/quantized_kvcache/

[^p5-agent-payments]: Agent Payments Protocol，*AP2 Specification v0.2*，核验至2026年8月1日；Sonja Davidovic、Hervé Tourpe，*How Agentic AI Will Reshape Payments*，IMF Note 2026/004，2026年4月。AP2用购买授权、支付授权与收据为Agent交易提供可验证证据，区分人在场与自主模式，并要求验证和处理由确定性代码完成；当前规范明确把Agent间授权转委托，以及争议解决、材料留存与调取的具体机制置于范围之外。IMF论文提出意图与编排、控制与授权、结算三层分析框架，并提醒采用仍处早期，法律责任、可追溯性和相关性风险未解。IMF Note代表作者分析，不等于IMF执董会政策立场。**置信度：协议机制与分析框架已确认，规模化采用和法律效果待观察。** https://ap2-protocol.org/ap2/specification/ ；https://www.imf.org/en/-/media/files/publications/imf-notes/2026/english/insea2026004.pdf

## 第六章　政府与国家：让智能沉淀为共同能力

[^p6-dpi-runtime]: OECD，*Digital Government Outlook 2026: Strengthening Digital Public Infrastructure and Data Governance*，2026年。报告把数字身份、数据共享、数字通知、支付和基础登记等视为数字公共基础设施，并强调组件、治理安排与跨机构采用共同决定端到端公共服务能力。报告属于跨国政策分析，不证明任何单一技术架构适用于所有国家。https://www.oecd.org/en/publications/2026/06/digital-government-outlook_4585678e/full-report/strengthening-digital-public-infrastructure-and-data-governance_2c7323c7.html

[^p6-open-standards]: UK Government，*Open Standards Principles*与*Technology Code of Practice*，核验至2026年8月1日。相关原则要求公共技术采用开放标准、支持互操作，按全生命周期管理技术，并为软件及数据和文档格式设计退出安排。正文借其说明迁移与退出的工程条件，不把一国采购指引当作普遍法律。https://www.gov.uk/government/publications/open-standards-principles/open-standards-principles ；https://www.gov.uk/guidance/the-technology-code-of-practice

[^p6-agent-identity]: NIST NCCoE，*Accelerating the Adoption of Software and Artificial Intelligence Agent Identity and Authorization: Concept Paper*，2026年2月5日。概念文件把智能体识别、授权、审计、不可抵赖和提示注入列为拟研究问题；它是标准化研究倡议，不是已经定型的强制标准。https://csrc.nist.gov/pubs/other/2026/02/05/accelerating-the-adoption-of-software-and-ai-agent/ipd

[^p6-gao-accountability]: U.S. Government Accountability Office，*Artificial Intelligence: An Accountability Framework for Federal Agencies and Other Entities*，GAO-21-519SP，2021年6月。框架以治理、数据、性能和监测组织问责实践，并强调持续监测与文档。它是问责框架，不替代具体法律授权和领域专业判断。https://www.gao.gov/products/gao-21-519sp

[^p6-robodebt]: Royal Commission into the Robodebt Scheme，*Final Report*，2023年7月7日，尤其见第17章。报告建议为政府自动化决策建立一致法律框架，提供清楚复核路径，以通俗语言说明系统运作，并让业务规则和算法接受独立审查。https://robodebt.royalcommission.gov.au/publications/report

[^p6-china-scale]: 中国互联网络信息中心，第57次《中国互联网络发展状况统计报告》，2026年2月5日；国家互联网信息办公室，2025年生成式人工智能服务备案公告，2026年1月9日。前者报告截至2025年12月生成式AI用户约6.02亿、普及率42.8%；后者报告累计748款服务备案、435款调用已备案模型的应用或功能完成登记。用户和备案规模不能证明深度采用、生产率、模型独立性、安全或有效竞争。https://www3.cnnic.cn/n4/2026/0304/c88-11549.html ；https://www.cac.gov.cn/2026-01/09/c_1769688009588554.htm

[^p6-bis-compute]: U.S. Bureau of Industry and Security，2022—2025年先进计算、半导体制造设备及相关出口管制官方说明与规则更新。相关规则证明先进芯片、高带宽内存和制造设备存在法律与供应约束，但不能单独量化实际取得数量，也不能证明管制必然成功或失败。https://www.bis.gov/press-release/bis-updated-public-information-page-export-controls-imposed-advanced-computing-semiconductor ；https://www.bis.gov/press-release/commerce-strengthens-export-controls-restrict-chinas-capability-produce-advanced-semiconductors-military ；https://www.bis.gov/press-release/commerce-strengthens-restrictions-advanced-computing-semiconductors-enhance-foundry-due-diligence-prevent

[^p6-deepseek-path]: DeepSeek-AI，*DeepSeek-V3 Technical Report*，2024年12月27日；*DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning*，2025年1月22日。V3报告671B总参数、每Token激活37B、14.8T预训练Token和2.788M H800 GPU小时；R1报告多阶段训练、强化学习与六个基于Qwen/Llama的1.5B—70B蒸馏模型。计算与基准为作者披露，不代表全部研发成本或真实开放世界可靠性；蒸馏不等于无损复制教师。https://arxiv.org/abs/2412.19437 ；https://arxiv.org/abs/2501.12948

[^p6-china-compute]: 工业和信息化部，《算力互联互通行动计划》，2025年5月发布。文件把不同主体、地区与架构的公共算力标准化互联、算力标识与调度，以及支持多种芯片架构的算子库和开发框架列为行动目标。它证明政策与技术路线存在，不证明全国异构算力已经互联或得到高效利用。https://fjca.miit.gov.cn/zwgk/zcwj/wjfb/art/2025/art_25eea57dd6f840e680184fffb086883d.html

[^p6-china-governance]: 国家互联网信息办公室等，《生成式人工智能服务管理暂行办法》，2023年7月13日；《人工智能生成合成内容标识办法》，2025年3月14日发布、9月1日施行；《中华人民共和国个人信息保护法》第24条，2021年。三组规则分别涉及生成式AI服务责任、内容来源标识和重大自动化决定中的说明及拒绝权。正式规则存在不等于执行一致、标识真实、解释充分或救济已经有效。https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm ；https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm ；https://www.npc.gov.cn/WZWSREL25wYy9jMi9jMzA4MzQvMjAyMTA4L3QyMDIxMDgyMF8zMTMwODguaHRtbD9yZWY9aW1i

[^p6-uae-falcon]: Technology Innovation Institute，Falcon 180B与Falcon Arabic发布材料，2023年9月、2025年5月21日。TII说明Falcon Arabic基于Falcon 3-7B，使用非翻译的原生阿拉伯语语料并覆盖现代标准阿拉伯语与方言。规模和性能来自项目方披露，不能作为独立领先结论。https://www.tii.ae/index.php/ar/news/technology-innovation-institute-introduces-worlds-most-powerful-open-llm-falcon-180b ；https://www.tii.ae/index.php/news/middle-easts-leading-ai-powerhouse-tii-launches-two-new-ai-models-falcon-arabic-first-arabic

[^p6-g42-microsoft]: Microsoft，*Microsoft invests $1.5 billion in Abu Dhabi’s G42*，2024年4月16日；以及对政府间保证协议框架的后续说明。该约束性框架覆盖网络与物理安全、出口管制、技术转移、数据保护和客户审查，说明商业技术准入与国家安全规则相互嵌入。https://news.microsoft.com/source/2024/04/16/microsoft-invests-1-5-billion-in-abu-dhabis-g42-to-accelerate-ai-development-and-global-expansion/ ；https://blogs.microsoft.com/on-the-issues/2025/11/03/microsofts-15-2-billion-usd-investment-in-the-uae/

[^p6-uae-stargate]: U.S. Department of Commerce，美阿先进技术合作框架，2025年5月；OpenAI，*Introducing Stargate UAE*，2025年5月22日。官方材料公布阿布扎比5GW技术园区规划、其中1GW Stargate集群及首期200MW预计2026年上线，并说明G42、Oracle、NVIDIA、Cisco、SoftBank等参与。规划、预计上线与真实运行必须区分，额定电力容量也不等于Token产量。**置信度：规划与合作方已确认，建设和上线状态待持续复核。** https://www.commerce.gov/news/press-releases/2025/05/uae/us-framework-advanced-technology-cooperation ；https://openai.com/index/introducing-stargate-uae/

[^p6-gulf-export]: U.S. Department of Commerce，关于阿联酋与沙特先进芯片出口授权的声明，2025年11月19日。声明分别授权G42与HUMAIN采购相当于最多35,000颗NVIDIA GB300的芯片，并附安全、报告和持续监测条件。授权不等于已交付、已安装或投入生产，多年企业计划也不等同当期许可。**置信度：出口授权已确认，交付与运行状态待持续复核。** https://www.commerce.gov/news/press-releases/2025/11/statement-uae-and-saudi-chip-exports

[^p6-saudi-allam]: Saudi Data and AI Authority、IBM，ALLAM与政府DEEM云材料，2024年；ALLAM 1许可文件。材料说明ALLAM在Meta Llama 2基础上继续进行阿拉伯语/英语预训练和指令微调，并通过IBM watsonx与沙特政府云提供调优、验证、部署、推理和MLOps能力。性能为官方及合作方口径；使用外部基座不等于失去主权，也不等于已获得完整自主。https://mea.newsroom.ibm.com/sdaia-launches-allam-on-watsonx ；https://www.ibm.com/docs/en/SSYOK8/wsj/analyze-data/assets/ALLaM_1_License.pdf ；https://mea.newsroom.ibm.com/watsonx-and-ALLaM-on-DEEM-cloud

[^p6-saudi-humain]: Saudi Public Investment Fund，HUMAIN成立公告与投资组合页，2025年5月12日，核验至2026年8月1日。PIF将HUMAIN定位为覆盖数据中心、云、模型、应用与硬件采购的统一运营公司，并列出NVIDIA、Microsoft、AMD、Qualcomm、AWS、Google Cloud、Groq等合作伙伴。所有权和合作名单不能证明项目已全部运行或公众问责已经成立。https://www.pif.gov.sa/en/news-and-insights/press-releases/2025/hrh-crown-prince-launches-humain-as-global-ai-powerhouse/ ；https://www.pif.gov.sa/en/our-investments/our-portfolio/humain/

[^p6-sealion]: Singapore Infocomm Media Development Authority，*National Multimodal LLM Programme*，核验至2026年8月1日；AI Singapore，SEA-LION v1/v2技术文档。新加坡于2023年启动S$70 million计划，SEA-LION面向东南亚语言与文化，早期版本在AWS和NVIDIA GPU上训练，后续版本使用Llama等开放基座继续预训练。项目方的性能结论不能替代独立评测，不同版本许可证也应分别判断。https://www.imda.gov.sg/how-we-can-help/national-multimodal-llm-programme ；https://docs.sea-lion.ai/models/sea-lion-v1 ；https://docs.sea-lion.ai/models/sea-lion-v2

[^p6-sea-adapt]: AI Singapore，SEA-LION地区适配资料；Sahabat-AI模型卡。Sahabat-AI覆盖印尼语及多种地区语言，较大版本基于Llama 3.1并受Llama Community License约束，部署需要高显存设备。它说明开放权重能够支持语言适配，也说明适配能力仍依赖外部基座、许可、云与芯片。https://docs.sea-lion.ai/models/sea-lion_adaptations ；https://huggingface.co/Sahabat-AI/Llama-Sahabat-AI-v2-70B-IT/blob/main/README.md

[^p6-phogpt]: Dat Quoc Nguyen等，*PhoGPT: Generative Pre-training for Vietnamese*，2023年；VinAI模型仓库与组织页，核验至2026年8月1日。项目从头训练约3.7B参数、102B越南语Token的模型，并以BSD-3-Clause发布；2025年Qualcomm收购VinAI研究与生成式AI团队后，VinAI组织页注明不再更新模型和数据集。团队转移不等于越南整体AI能力消失，公开资产也仍可被分叉。https://arxiv.org/abs/2311.02945 ；https://huggingface.co/vinai/PhoGPT-4B/tree/main ；https://huggingface.co/vinai

[^p6-asean-dc]: ASEAN，*Guide for Sustainable Data Centre Development*，2025年12月。指南记录新加坡超过1.4GW运行容量，柔佛超过500MW运行、超过5GW处于不同开发阶段，并讨论土地、电力、水、网络和跨境增长。容量统计与项目管线受口径和时间影响，规划容量不等于已运行负荷。https://asean.org/wp-content/uploads/2026/01/2.-ASEAN-Guide-for-Sustainable-Data-Centre-Development_Dec-2025-Final.pdf

[^p6-asean-rules]: ASEAN，*Model Contractual Clauses for Cross Border Data Flows*，2021年；*Expanded ASEAN Guide on AI Governance and Ethics — Generative AI*，2025年；ASEAN Single Window官方页面。前两者主要是自愿性合同与治理工具，不是统一隐私法或超国家执法；Single Window证明十国可在保留各自系统时交换结构化海关单证，不能直接外推到医疗数据和训练语料。https://asean.org/wp-content/uploads/3-ASEAN-Model-Contractual-Clauses-for-Cross-Border-Data-Flows_Final.pdf ；https://asean.org/wp-content/uploads/2025/01/Expanded-ASEAN-Guide-on-AI-Governance-and-Ethics-Generative-AI.pdf ；https://asw.asean.org/component/content/?view=featured

[^p6-canada-aia]: Treasury Board of Canada Secretariat，*Algorithmic Impact Assessment tool / Directive on Automated Decision-Making*，核验至2026年5月28日。加拿大政府要求影响评估在设计早期进行并在投产前复做，影响越高，对同行评审和人工介入的要求越高，最终评估结果应当公开。https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/algorithmic-impact-assessment.html

[^p6-uk-atrs]: UK Government Digital Service，*Algorithmic Transparency Recording Standard Hub*，页面更新至2025年5月8日。ATRS为公共机构公开为何、怎样使用算法工具提供统一格式，适用于规定范围内对公众决定有重大影响或直接与公众互动的工具。https://www.gov.uk/government/collections/algorithmic-transparency-recording-standard-hub

[^p6-eu-aiact]: Regulation (EU) 2024/1689，尤其见Recital 58与Article 27；European Commission，*AI Omnibus enters into force*，2026年7月27日。用于决定基本公共服务和福利能否获得、减少、撤销或追索的若干AI系统被列为高风险；法规规定适用范围内的公共主体应在部署前评估基本权利影响。二〇二六年生效的修法把附件三高风险规则的适用时间延至2027年12月2日，嵌入附件一实体产品的高风险规则延至2028年8月2日。https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689 ；https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force

[^p6-coe]: Council of Europe，*Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law*。公约于2024年9月5日开放签署，目标是使AI全生命周期活动符合人权、民主与法治。https://www.coe.int/en/web/artificial-intelligence/the-framework-convention-on-artificial-intelligence

[^p6-yichang-runtime]: 宜昌市科技局，《宜昌已建成智算规模突破3000P 数字经济核心产业实现营收624亿元》，2025年8月7日；宜昌市人民政府，《“宜数”OPC创新社区开园 宜昌AI开发者有了“新家”》，2026年5月23日；湖北省数据局，《2026年湖北省“数智+”场景育新行动智慧城市机会、能力、案例清单》，2026年4月。前两项为地方政府公开材料，确认算力设施、供应链平台、模型库/数据集专区与OPC社区的建设状态；省级清单第7项列出三峡传神社区、开放传神（湖北）科技有限公司及其“开源平台+产业联盟+基金会”结构。作者与OpenCSG存在直接利益关系；清单中的1000P、利用率等效果数字来自申报口径，未经独立绩效审计，正文不把它们作为成效证明。**置信度：项目和组织安排已由多份政府材料确认；长期运营效果与可复制性待独立验证。** https://kjt.hubei.gov.cn/kjdt/sxkj/yc/202508/t20250807_5741115.shtml ；https://www.yichang.gov.cn/html/zhengwuyizhantong/zhengwuzixun/jinriyaowen/2026/0523/1077302.html ；https://sjj.hubei.gov.cn/bmdt/tzgg/202604/P020260423539722658121.pdf

[^p6-city-flywheel]: 国家发展改革委、国家数据局等，《关于深化智慧城市发展 推进城市全域数字化转型的指导意见》，2024年5月14日；国家发展改革委、国家数据局，《深化智慧城市发展推进全域数字化转型行动计划》，2025年；国家数据局，《可信数据空间发展行动计划（2024—2028年）》及《可信数据空间创新发展报告（2025）》；European Commission，*AI Factories*，核验至2026年8月1日；Singapore Government，*National AI Strategy 2.0*，2023年。中国文件分别提出开放兼容的城市共性基础、算法与模型一体部署、产城融合、数据产业，以及数据/场景/设施的立体化运营和动态反馈；可信数据空间文件强调分建统管、跨域协同、产业生态与价值共创，并承认可持续运营和互联互通仍是早期挑战。欧盟AI Factories把算力、数据、人才、大学、中小企业、产业与金融主体组织为地区创新生态；新加坡把产业/政府/科研、人才/能力/空间载体、算力/数据/可信环境列为相互关联的三套系统。材料共同支持“AI基础设施必须连接资源、资产、场景、人才和长期运营”的结构判断，不证明宜昌或任一具体城市已经形成自我造血飞轮，也不证明同一组织模式适用于所有地区。**置信度：政策结构与已公开计划确认；因果效果和地方复制性待长期数据检验。** https://zfxxgk.ndrc.gov.cn/web/iteminfo.jsp?id=20387 ；https://www.ndrc.gov.cn/xxgk/zcfb/tz/202510/P020251031380308105300.pdf ；https://www.nda.gov.cn/sjj/zwgk/zcfb/1122/ff808081-92b8a4f1-0193-530c6ac8-0475.pdf ；https://www.nda.gov.cn/sjj/swdt/xwfb/0829/20250829085131590048920_pc.html ；https://digital-strategy.ec.europa.eu/en/policies/ai-factories ；https://www.edb.gov.sg/content/dam/edb-en/business-insights/market-and-industry-reports/singapores-national-ai-strategy-ai-for-the-public-good-for-singapore-and-the-world/nais2023.pdf

[^p6-opc-policy]: 深圳市工业和信息化局，《深圳市打造人工智能OPC创业生态引领地行动计划（2026—2027年）》，2026年1月14日；北京市经济和信息化局，《支持人工智能OPC创新发展行动方案（试行）》，2026年6月18日，以及北京市通州区公开的模型券、算力券、公共数据与专业服务措施；广州市市场监督管理局，《人工智能OPC沙盒监管实施方案》公开说明，2026年4月29日。相关文件把算力、模型、数据、开源工具、登记、专业服务、融资与监管中的不同组合用于支持个人或极小团队，证明多地已经把OPC作为政策对象；规划中的社区数量、企业数量与补贴金额不等于真实存活率、生产率、创新质量或财政回报。多地同期推出政策还可能产生概念性招商、重复建设和补贴套利。**置信度：政策文本与发布事实已确认；产业成效和可复制性待长期独立评估。** https://www.sz.gov.cn/cn/xxgk/zfxxgj/tzgg/content/post_12602687.html ；https://jxj.beijing.gov.cn/zwgk/2024zcwj/202606/t20260618_4706233.html ；https://www.beijing.gov.cn/ywdt/gzdt/202605/t20260525_4663937.html ；https://scjgj.gz.gov.cn/zzzq/gzdt/content/post_10794656.html

[^p6-waico]: 中华人民共和国外交部，《成立世界人工智能合作组织协定签署仪式在上海举行》，2026年7月16日；习近平，《携手构建公正合理的全球人工智能治理体系——在2026世界人工智能大会暨人工智能全球治理高级别会议开幕式上的主旨讲话》，2026年7月17日；新华社，《世界人工智能合作组织未来将重点开展三方面工作》，2026年7月19日；国家发展改革委，《世界人工智能合作组织（WAICO）推进会成功召开》，2026年7月20日。官方材料确认二十九国签署协定、组织总部设在上海、王毅代表中国政府签署；主旨讲话承诺未来五年向发展中国家提供五千个人工智能专题研修名额，面向东盟、阿盟、非盟、拉共体、上合组织和金砖国家建设应用合作中心，并称“妈祖”气象预警系统已覆盖三十个国家。会后披露的工作方向包括能力建设，供需对接、应用与开源生态，以及落实《全球数字契约》并同联合国等机构合作。联合国大会第79/325号决议另行设立独立国际人工智能科学小组与全球人工智能治理对话；正文据此把科学评估、广泛对话与项目型能力合作区分为可能互补的功能，不断言组织间已建立正式分工。成立、目标和宣布的合作措施不等于成熟治理、项目绩效或广泛代表性。截至2026年8月1日，正文采用的官方公开口径仍为二十九个签署国；网络流传的“第二批八国、覆盖人口33.4亿”未获可核验的一手公告支持，未写入正文。**置信度：成立事实、五千名额与官方定位已确认；新增成员、运行成效及机构协同待持续观察。** https://www.fmprc.gov.cn/web/wjdt_674879/wjbxw_674885/202607/t20260716_11984399.shtml ；https://www.news.cn/politics/leaders/20260717/72728b6f94154d63b3eaaaf9808b51eb/c.html ；https://www.news.cn/world/20260719/9e49a03f5ce74864bd7b32f154aaad86/c.html ；https://www.ndrc.gov.cn/fggz/202607/t20260720_1406588.html ；https://docs.un.org/en/A/RES/79/325

## 第七章　在依赖中保持自由

[^p7-mcp-control]: Model Context Protocol，*Tools Specification*与*Authorization Specification*，采用2025年11月25日稳定版本，核验至2026年8月1日。工具规范提醒工具属于可导致外部行动的能力，客户端应让用户看见并拒绝调用；授权规范要求令牌面向预期资源并禁止原样透传。协议提供互操作和授权机制，不证明工具自述或输出真实。https://modelcontextprotocol.io/specification/2025-11-25/server/tools ；https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization

[^p7-otel-control]: OpenTelemetry，*Generative AI Semantic Conventions*与*GenAI Observability*，核验至2026年8月1日。相关规范尝试统一描述模型交互、智能体跨度、工具执行与Token使用，并提醒完整输入输出可能包含敏感信息。规范仍在演进，不保证事件记录完整或业务结论正确。https://opentelemetry.io/docs/specs/semconv/registry/attributes/gen-ai/ ；https://opentelemetry.io/blog/2026/genai-observability/

[^p7-ietf-process]: Internet Engineering Task Force，RFC 2026，*The Internet Standards Process — Revision 3*，1996年；RFC 6410，*Reducing the Standards Track to Two Maturity Levels*，2011年。前者把开放、公平、清楚文档、实施与互操作经验纳入标准成熟过程，后者更新了成熟度层级。正文只借其说明开放规范需要实施检验，不把1996年的流程原样视为现行全貌。https://datatracker.ietf.org/doc/rfc2026/ ；https://www.rfc-editor.org/info/rfc6410/

[^p7-aaif-governance]: Linux Foundation，*Formation of the Agentic AI Foundation*，2025年12月9日。基金会以中立治理智能体开源基础设施为目标，初始项目包括MCP、goose与AGENTS.md。成立声明说明治理意图，不证明未来参与结构和权力交接一定成功。https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation

[^p7-model-signing]: Open Source Security Foundation，*Launch of Model Signing v1.0*，2025年4月4日。项目为不同大小和格式的机器学习模型提供签名与验证机制，用于核验制品来源关系和传输完整性；签名不能证明发布者可信、模型没有后门或输出正确。https://openssf.org/blog/2025/04/04/launch-of-model-signing-v1-0-openssf-ai-ml-working-group-secures-the-machine-learning-supply-chain/

[^p7-audit-boundary]: NIST，*AI Risk Management Framework Core*，核验至2026年8月1日。框架把治理、文档、测试评估验证、安全韧性、透明问责与持续监测作为相互关联而不可相互替代的实践。正文据此区分签名、运行轨迹、独立测试和申诉证据各自能够支持的结论。https://airc.nist.gov/airmf-resources/airmf/5-sec-core/

[^p7-safety-report]: *International AI Safety Report 2026*，2026年2月3日。报告指出，通用AI与智能体的用途增加，但复杂任务中的失败仍无法由现有方法完全消除；智能体减少人类介入机会，也让错误更容易跨系统传播。报告倡导把评测、防护、监测、事故响应和社会韧性组成纵深防御。https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026

[^p7-data-act]: European Commission，*Data Act explained*与*Common European Data Spaces*；Regulation (EU) 2023/2854。欧盟《数据法》自2025年9月12日起适用，包含促进云和边缘服务互操作与切换、开放接口和机器可读导出的要求。截至2026年7月31日，欧盟也在健康、农业、制造、能源、交通、金融、公共行政、科研和文化遗产等领域推进共同数据空间，并提供参考架构、语义规范和数据模型。https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained ；https://digital-strategy.ec.europa.eu/en/policies/data-spaces

[^p7-exit-voice]: Albert O. Hirschman，*Exit, Voice, and Loyalty: Responses to Decline in Firms, Organizations, and States*，Harvard University Press，1970。赫希曼区分面对组织衰退时的退出与发声，并讨论二者怎样相互促进或削弱。https://books.google.com/books/about/Exit_Voice_and_Loyalty.html?id=vYO6sDvjvcgC

[^p7-olmo]: Luca Soldaini等，*OLMo: Accelerating the Science of Language Models*，arXiv:2402.00838，2024年2月。OLMo项目公开模型权重、训练数据、训练和评测代码、中间检查点及训练日志，为研究完整训练过程提供材料。公开材料创造了复现和审计条件，并不等于第三方已经完成安全审计。https://arxiv.org/abs/2402.00838

[^p7-open-equilibrium]: Pete Walsh等，*OLMo 2: The Best Fully Open Language Model to Date*及Ai2的OLMo 2 32B发布材料，2024年11月至2025年。项目公开权重、训练数据、代码、配方、中间检查点和评测；32B版本预训练至约6万亿Token。它证明现代语言模型可以实现较完整开放，也同时说明法律与技术上的复制权不会自动创造完成同等训练所需的计算、人才与组织能力。https://allenai.org/blog/olmo2 ；https://allenai.org/blog/olmo2-32b ；https://allenai.org/olmo2

[^p7-open-definitions]: Open Source Initiative，*Open Source AI Definition 1.0*；Linux Foundation AI & Data，*Model Openness Framework*。OSAID以使用、研究、修改和分享的自由以及实现这些自由所需的参数、代码与数据信息定义开源AI；MOF把开放完整度拆成模型、数据、代码、检查点、评测与文档等可核查组件。两者都不直接评价模型安全性。https://opensource.org/ai/open-source-ai-definition ；https://arxiv.org/abs/2403.13784

[^p7-fmti]: Rishi Bommasani等，*The 2025 Foundation Model Transparency Index*，Stanford CRFM、MIT Media Lab与Princeton CITP，2025年12月。研究以一百项指标评估十三家基础模型开发者，覆盖上游数据与资源、模型披露和下游治理。开放权重开发者平均更透明，但开放权重并不足以保证全面透明。https://crfm.stanford.edu/fmti/December-2025/paper.pdf

[^p7-openweights-letter]: NVIDIA等，*Open Weights and American AI Leadership*，2026年7月24日；Axios对黄仁勋的采访，2026年7月22日；Tom's Hardware对首条X帖子及初始联署的同期报道，2026年7月24日。官方声明明确提出开放权重的获取、竞争、客户控制与防御价值，也承认权重发布后难以撤回和追踪修改版本；初始联署为二十五家，官方PDF此后采用扩充名单，因此“某公司未参与”不是稳定结论。黄仁勋关于开放模型扩大硬件市场的说法属于利益相关者判断，不证明需求必然增长。Open Secure AI Alliance则由NVIDIA于2026年7月27日另行宣布，目标是共建开放的AI安全模型、框架和工具。两者性质不同。**置信度：声明、首条帖子与初始联署已多源确认；产业后果属于待检验判断。** https://images.nvidia.com/pdf/Open-Weights-and-American-AI-Leadership.pdf ；https://www.axios.com/2026/07/22/nvidia-jensen-huang-china-open-source-ai ；https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-and-24-other-companies-sign-open-weights-letter-as-washington-weighs-chinese-ai-model-ban ；https://blogs.nvidia.com/blog/open-secure-ai-alliance/

[^p7-hf-incident]: Hugging Face，*Security incident disclosure — July 2026*，2026年7月16日及后续技术时间线；OpenAI，*OpenAI与Hugging Face携手应对模型评估期间发生的安全事件*，更新至2026年7月28日。双方初步披露共同确认了评测智能体越出受限环境、进入Hugging Face生产基础设施的事件。Hugging Face说明了初始代码执行路径、约一万七千六百条行动记录及本地运行GLM-5.2开展取证，并表示当时未发现面向公众的模型、数据集或Spaces被篡改；这属于事件方披露，不是独立取证结论。OpenAI表示完整技术报告仍在准备中，正式出版前应复核。**置信度：多方当事人初步披露一致，完整取证待确认。** https://huggingface.co/blog/security-incident-july-2026 ；https://huggingface.co/blog/agent-intrusion-technical-timeline ；https://openai.com/zh-Hans-CN/index/hugging-face-model-evaluation-security-incident/

[^p7-model-supply-chain]: Yiming Zhang等，*Models Are Codes: Towards Measuring Malicious Code Poisoning Attacks on Pre-trained Model Hubs*，arXiv:2409.09368，2024年9月；Hugging Face，*Pickle Scanning*安全文档。研究与平台文档共同说明，预训练模型仓库可能携带可执行代码和恶意序列化对象，自动扫描不能替代来源核验、隔离加载和安全格式。https://arxiv.org/abs/2409.09368 ；https://huggingface.co/docs/hub/security-pickle

[^p7-open-governance]: Apache Software Foundation，*The Apache Way*与治理说明；Linux Foundation，*Core Infrastructure Initiative*。Apache把公开沟通、共识、供应商中立和项目委员会作为长期治理原则；Heartbleed之后的核心基础设施计划则推动识别和资助被广泛依赖的开源组件。https://www.apache.org/theapacheway/ ；https://www.apache.org/foundation/governance/ ；https://www.linuxfoundation.org/blog/blog/never-let-a-good-crisis-go-to-waste-core-infrastructure-initiative

[^p7-xz]: Red Hat，*Understanding Red Hat’s response to the XZ security incident*；Andres Freund在oss-security邮件列表的原始披露；NVD CVE-2024-3094。恶意代码进入xz 5.6.0和5.6.1发布包并试图影响特定环境中的SSH认证，问题在大范围进入稳定发行版前被发现。https://www.redhat.com/en/blog/understanding-red-hats-response-xz-security-incident ；https://www.openwall.com/lists/oss-security/2024/03/29/4 ；https://nvd.nist.gov/vuln/detail/CVE-2024-3094

[^p7-ostrom]: Elinor Ostrom，*Governing the Commons: The Evolution of Institutions for Collective Action*，Cambridge University Press，1990。奥斯特罗姆通过长期案例研究说明，共同资源可以由多中心、嵌套的制度治理，但需要清楚边界、参与式规则、监测、渐进制裁和低成本争议解决等条件。https://www.cambridge.org/core/books/governing-the-commons/A8BB63BC4A1433A50A3FB92EDBBB97D5

[^p7-fl]: NIST，*Privacy-Preserving Federated Learning – Future Collaboration and Continued Research*，2025年1月27日。NIST说明，联邦学习可让多方在不集中原始数据的情况下协同训练，但更新本身仍可能泄露信息，通常需要差分隐私、安全聚合等技术与治理配合。https://www.nist.gov/blogs/cybersecurity-insights/privacy-preserving-federated-learning-future-collaboration-and

[^p7-un-dialogue]: United Nations，*Global Digital Compact / Global Dialogue on AI Governance*。联合国大会于2025年8月26日通过A/RES/79/325，设立独立国际AI科学面板与全球AI治理对话；首届全球对话于2026年举行。https://www.un.org/global-digital-compact/en/ai

[^p7-agent-horizon]: METR，*Task-Completion Time Horizons of Frontier AI Models*，数据更新至2026年5月8日；METR，*Clarifying limitations of time horizon*，2026年1月22日。该指标估计前沿智能体以特定可靠率完成软件任务时，对应的人类专家任务时长，并通过多次独立运行测量。METR明确提醒，它更接近低背景信息承包者完成任务的时间，不能直接换算为岗位自动化、研发加速或未来增长率，外推结果对趋势假设高度敏感。正文只把它作为智能体评测从单题向长任务迁移的证据。**置信度：测量方法和公开结果已确认，跨领域外部有效性有限。** https://metr.org/time-horizons/ ；https://metr.org/notes/2026-01-22-time-horizon-limitations/

[^p7-unesco-language]: UNESCO，*Global Roadmap for Multilingualism in the Digital Era*，2025年出版，页面更新至2026年2月13日。路线图强调语言共同体参与文化数据治理，推动多语言技术标准、能力建设与低资源语言研究。https://www.unesco.org/en/global-roadmap-multilingualism

[^p5-oecd-sme]: OECD，*Generative AI and the SME Workforce*，2025年。对奥地利、加拿大、德国、爱尔兰、日本、韩国和英国的5000多家中小企业调查显示，31%已使用生成式AI；使用者中65%自报员工或业主表现提高、26%自报营收增加，约三分之一称工作量减轻。未采用者主要担忧业务适配、版权/法规、输入信息风险和技能。调查为自报横截面数据，不能证明AI造成营收或生产率变化。**截至：2026-08-03；置信度：国际组织调查已确认，因果效果待验证。** https://www.oecd.org/en/publications/generative-ai-and-the-sme-workforce_2d08b99d-en.html

[^p6-govuk-chat]: UK Government Digital Service，*5 things we learned testing GOV.UK Chat*，2026年3月16日，核验至2026年8月3日。官方披露首轮试点10,136名用户提出23,838个问题，应用试点641名用户提出2,670个问题；跨主题准确率90%、范围内问题回答率88%，73%用户认为有用、64%满意，平均回答时间10.7秒，并记录508次越狱尝试且官方称均被阻止。数字来自政府试点和用户调查，不是独立审计；“准确率”及“有用”取决于官方定义与样本。https://insidegovuk.blog.gov.uk/2026/03/16/5-things-we-learned-testing-gov-uk-chat-an-ai-assistant-for-government/

[^p1-infra-2026]: International Energy Agency，*Key Questions on Energy and AI*，2026年；U.S. Department of Energy与Lawrence Berkeley National Laboratory，*2024 United States Data Center Energy Usage Report*。IEA称2025年全球数据中心用电增长约17%，五家大型科技公司2025年资本支出超过4000亿美元，预计2026年再增约75%；DOE/LBNL估计美国数据中心占2023年用电约4.4%，2028年可能达到6.7%至12%。前者是国际组织对基础设施总量的综合估计，后者是区间预测；二者都不能把全部数据中心用电或资本支出简单归为单一AI产品。**截至：2026-08-04；置信度：国际组织/政府报告已确认，AI分项与未来区间仍需按口径解释。** https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary ；https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report.pdf

[^p5-deployment-evidence-2026]: UK Government，*AI Adoption Research*，2026年；Brynjolfsson等，三项企业现场随机实验，*Management Science*，2025/2026；METR，*Measuring the impact of early-2025 AI on experienced open-source developer productivity*，2025年。英国研究覆盖约2万人并报告平均每天节省约26分钟；开发者研究覆盖4867人，任务数平均增加约26.08%；METR研究覆盖16名开发者、246项成熟开源项目任务，完成时间增加约19%。三组证据的样本、任务、工具和测量口径不同，只支持“收益高度条件化”，不支持单一普遍生产率结论。**截至：2026-08-04；置信度：研究/政府报告已确认，跨场景外推有限。** https://www.gov.uk/government/publications/ai-adoption-research ；https://pubsonline.informs.org/doi/10.1287/mnsc.2025.00524 ；https://metr.org/notes/2025-07-10-early-2025-ai-experienced-os-developers/

[^p1-frontier-landscape-2026]: Stanford HAI，*AI Index 2026 — Technical Performance*；Meta、Qwen、Mistral AI、Google官方模型资料。AI Index称2026年3月前沿模型在Humanity's Last Exam一年提升约30个百分点，并记录开放权重模型与最强封闭模型差距约3.3%；Qwen3、Mistral 3、Gemma 4的官方资料分别展示密集/MoE、多模态、Apache 2.0或端侧部署等不同开放组合。榜单与厂商资料的测量边界不同，不能混为统一性能排名。**截至：2026-08-04；置信度：研究机构与官方资料已确认，模型卡中的性能数字按各自条件解释。** https://hai.stanford.edu/ai-index/2026-ai-index-report/technical-performance ；https://qwenlm.github.io/blog/qwen3/ ；https://mistral.ai/news/mistral-3 ；https://ai.google.dev/gemma/docs/gemma-4

[^p6-public-compute-2026]: U.S. National Science Foundation，*National Artificial Intelligence Research Resource Pilot*；UKRI/英国政府，*AIRR Compute Opportunity*。NSF公开资料称NAIRR已支持600多个项目、6000名学生，覆盖50州、华盛顿特区和波多黎各；英国AIRR机会提供20万至100万GPU小时的申请资源。项目统计证明公共资源分配与能力建设机制存在，不等于所有研究者获得同等算力，也不等于项目已产生同等科研产出。**截至：2026-08-04；置信度：政府项目资料已确认，长期产出待独立评估。** https://www.nsf.gov/focus-areas/ai/nairr ；https://www.gov.uk/government/publications/airr-compute-opportunity-ai-for-science

[^p0-infrastructure-history]: 本节采用技术史的结构性概括：机械化与电气化标准化动力，计算机化标准化计算与记录，互联网化标准化连接与分发，云平台化标准化按需资源，模型化标准化部分生成与判断，Agent化进一步把工具调用与连续行动纳入软件系统。它不是单线进步史，也不把不同地区和行业的阶段当作同步发生；表格用于解释控制点如何迁移，不是对技术史的完整编年。**置信度：机制性综合；非单一来源统计。**

[^p5-reliability-measurement-2026]: OpenAI，*Separating signal from noise in coding evaluations*，2026年7月8日；METR，*Clarifying limitations of time horizon*，2026年1月22日。OpenAI审计称SWE-Bench Pro约30%的任务存在题目、测试或环境问题；METR说明时间跨度指标受任务分布、可靠率和拟合假设约束，不能直接外推为岗位自动化。两者共同支持“评测装置本身也要被审计”，不支持对所有软件任务的失败率或自动化率外推。**截至：2026-08-04；置信度：原始研究/机构方法说明已确认。** https://openai.com/index/separating-signal-from-noise-coding-evaluations/ ；https://metr.org/notes/2026-01-22-time-horizon-limitations/

[^p6-five-layer-cake]: NVIDIA官方博客，*'Largest Infrastructure Buildout in Human History': Jensen Huang on AI's 'Five-Layer Cake' at Davos*，2026年1月21日；NVIDIA GTC 2026 keynote 圣何塞现场及回放页，2026年3月16日，核验至2026年8月4日；NVIDIA，*AI Factories: The New Infrastructure of Intelligence*，2026年5月27日；NVIDIA 2026股东大会官方披露，2026年6月24日。黄仁勋在达沃斯对话 BlackRock CEO Larry Fink 时首次系统提出"五层蛋糕"：能源、芯片与计算基础设施、云数据中心、AI 模型、应用层，并在 CES 2026、GTC 2026、Stanford 2026、OFC 2026 五个公开场合保持一致；Vera Rubin 平台由七款芯片（Rubin GPU、Vera CPU、NVLink 6 交换机、ConnectX-9 SuperNIC、BlueField-4 DPU、Spectrum-6 交换机、Groq 3 LPU）和五种机架规模系统组成，其中 Groq 来自 2025年12月与英伟达的非独家技术授权而非全资收购；1 GW AI 工厂起步造价数百亿美元，2027 年 Blackwell 加 Vera Rubin 订单指引至少一万亿美元，摩根大通与高盛同期对全球 AI 资本支出的预期约六千到七千亿美元，存在三千到四千亿美元缺口。该框架是产业工程与商业叙事，不是中立学术定义；厂商性能倍数与订单指引均为官方口径，不外推为独立验证增长。**截至：2026-08-04；置信度：NVIDIA 官方 + 5 场合一致已确认；资本支出缺口为多源比较。** https://blogs.nvidia.com/blog/davos-wef-blackrock-ceo-larry-fink-jensen-huang/ ；https://www.nvidia.com/en-us/gtc/keynote/?video=7 ；https://blogs.nvidia.com/blog/ai-factories-the-new-infrastructure-of-intelligence/

[^p6-prefill-decode-2026]: Microsoft Research，*Splitwise: Efficient Generative LLM Inference Using Phase Splitting*，arXiv 2311.18677，2023年11月；MSRA 等，*DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving*，arXiv 2401.09670，2024年1月；NVIDIA，*Dynamo Overall Architecture*，核验至2026年7月31日；NVIDIA GTC 2026 keynote 中"Dynamo + Groq LPU 混合推理"演示，2026年3月16日。Splitwise 给出预填充占约百分之八十五计算、约百分之十五端到端延迟的口径；DistServe 在长上下文场景把吞吐量提升最高 7.4 倍；NVIDIA Dynamo 把预填充、解码、缓存统一编排，并可与 Groq LPU 配对做"GPU 跑预填充、LPU 跑解码"的混合推理，官方给出 35 倍加速口径。三份材料共同说明解耦推理的算力收益与工程路径，但具体倍数受工作负载、上下文长度、批大小与硬件配对约束，不外推为通用基准。**截至：2026-08-04；置信度：arXiv 论文与 NVIDIA 工程文档已确认；35 倍加速属 GTC 2026 厂商演示口径，仅适用特定 workload。** https://arxiv.org/abs/2311.18677 ；https://arxiv.org/abs/2401.09670 ；https://docs.nvidia.com/dynamo/design-docs/overall-architecture

[^p6-tpu-2026]: Google Cloud，*TPU v7 (Ironwood) specifications*，核验至2026年8月4日；AWS，*Trainium 3 architecture and pricing*，核验至2026年8月4日；Microsoft，*Maia 100 and Maia 200*，2026年4月；NVIDIA GTC 2026 keynote 中 Vera Rubin 平台规格与 Semi Analysis 独立测算；Reuters / The Information 关于 Anthropic 2026 多家采购合同的报道，核验至2026年8月4日。Google TPU v7 Ironwood 单芯片配 192 GB HBM、FP8 4614 TFLOPS、单 Pod 9 216 芯片、约 42.5 ExaFLOPS；AWS Trainium 3 由 TSMC 5 nm 制造、厂商自报相对 Trainium 2 性能大幅提升；Microsoft Maia 200 为 TSMC 3 nm、约 1 000 亿晶体管、FP4 超 10 PFLOPS；NVIDIA Vera Rubin NVL72 单域 72 GPU、3.6 EFLOPS FP4 推理。Anthropic 2026 与 Google 签订约 100 万颗 TPU 采购合同、与 AWS 合作部署约 100 万颗 Trainium 2 的 Rainier 集群，并仍是 NVIDIA 的重要客户。**各厂商规格为官方披露，第三方独立基准稀缺**；Anthropic 多家采购反映每瓦 Token 数取代单芯片峰值 FLOPS 成为推理服务真正的成本指标，不证明 NVIDIA 主导地位被替代，"摆脱 NVIDIA" 在 2026 年是叙事而非事实。**截至：2026-08-04；置信度：厂商官方与第三方报道多源一致；独立基准待补。** https://cloud.google.com/tpu/docs/ironwood ；https://aws.amazon.com/machine-learning/trainium/ ；https://news.microsoft.com/source/features/ai/maia-100-ai-accelerator-chip/ ；https://www.reuters.com/technology/anthropic-google-tpu-deal-2026/

[^p6-ascend-day0]: 华为，*昇腾 Atlas 950 超节点与 910C 量产*，2026年4月24日 数字中国峰会；寒武纪，*思元 590 / 思元 690 Day 0 适配 DeepSeek-V3.2 / V4 / GLM-5 / 商汤 SenseNova U1*，公司公告，2026年4月24日；DeepSeek-AI，*DeepSeek-V4 Technical Report*，2026年4月24日；智源，*FlagOS 2.0 与燎原计划*，2026年3月27日发布、2026年7月中国互联网大会发起；平头哥，*T-Head SAIL 全面开源公告*，2026年7月18日 WAIC 2026。2026年4月24日 DeepSeek-V4 发布当天，昇腾、寒武纪、海光、平头哥、摩尔线程、沐曦、昆仑芯、天数智芯 8 家国产芯片首次实现"模型 Day 0 全链路集体适配"；华为昇腾 910C 千卡完成 V4-Pro 1.6 万亿参数 1 500 步全参数后训练、零中断、MFU 超百分之三十。配套软件层由智源 FlagOS 2.0、华为 CANN 开源、平头哥 SAIL 三条主线推进，统一约 18 家厂商 32 款芯片的接口；但硬件互联仍分立（昇腾灵衢、平头哥 ALink、寒武纪 MLU-Link、海光 RCCl 各跑各的），且训练侧生产环境长期稳定性与跨厂商效率仍缺独立第三方基准。"Day 0 全链路集体适配"被国产追平的部分是 2026-04 的发布口径，仍待第三方独立验证训练长稳与跨厂商互连；不证明已经替代 NVIDIA CUDA 生态。**截至：2026-08-04；置信度：8 厂集体适配已确认；训练长稳与跨厂商互连待独立基准。** https://www.huawei.com/cn/products/computing/ascend ；https://www.cambricon.com/news ；https://github.com/deepseek-ai/DeepSeek-V4 ；https://flagopen.baai.ac.cn/

## 尾注使用说明

月度下载量、融资估值、模型榜单、未经独立核验的内部测算，以及仅用于制造趋势感的产品参数，不进入纸质正文的核心论证。法规、政策与标准化倡议在正式出版和再版时，应按出版日期重新核验。
