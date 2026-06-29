dba-transform-2026/                # 仓库根目录
├── README.md                      # 【门面】个人简介、学习路线图、项目索引（必读）
├── LICENSE                        # MIT/Apache 开源协议
├── .gitignore                     # 忽略敏感文件、临时文件、IDE配置
│
├── 01-python-automation/          # === M1-M3: Python自动化 ===
│   ├── m1-slow-query-catcher/     # M1: 慢查询抓取脚本
│   │   ├── main.py
│   │   ├── config.yaml            # 数据库连接配置(示例)
│   │   └── README.md              # 使用说明+效果截图
│   ├── m2-inspection-collector/   # M2: 巡检数据采集器
│   │   ├── collector.py
│   │   ├── templates/             # Excel/HTML报告模板
│   │   └── README.md
│   ├── m3-dingtalk-alert-bot/     # M3: 钉钉告警机器人
│   │   ├── bot.py
│   │   ├── scheduler.py           # 定时任务
│   │   └── README.md
│   └── notes/                     # Python学习笔记
│       ├── pandas-cheatsheet.md
│       └── pymysql-best-practices.md
│
├── 02-k8s-cloud-native-db/        # === M4-M6: K8s与云原生 ===
│   ├── m4-mysql-on-k8s/           # M4: K8s部署MySQL
│   │   ├── dockerfile
│   │   ├── manifests/             # Deployment/PVC/Service yaml
│   │   └── README.md
│   ├── m5-troubleshooting-sop/    # M5: 故障排查SOP
│   │   ├── oom-analysis.md
│   │   ├── pod-crash-loop.md
│   │   └── scripts/               # 排查辅助脚本
│   ├── m6-prometheus-grafana/     # M6: 监控体系
│   │   ├── docker-compose.yml     # 本地一键部署监控栈
│   │   ├── dashboards/            # Grafana JSON面板
│   │   └── README.md
│   └── notes/
│       ├── k8s-core-concepts.md
│       └── promql-examples.md
│
├── 03-domestic-db-cert/           # === M7-M9: 国产库+认证 ===
│   ├── oceanbase/                 # (或 dameng/)
│   │   ├── architecture-notes.md  # 架构原理笔记
│   │   ├── migration-lab/         # OMS迁移实验记录
│   │   │   ├── steps.md
│   │   │   └── issues-and-fixes.md
│   │   └── cert-prep/             # 备考资料(注意版权)
│   │       ├── oca-mock-questions.md
│   │       └── knowledge-map.md
│   └── certificates/              # 🏆 证书扫描件(PDF/IMG)
│       ├── obca-2026.pdf
│       └── obcp-2026.pdf          # ⚠️ 打码处理个人信息
│
├── 04-job-hunt-assets/            # === M10-M12: 求职资产 ===
│   ├── resume/                    # 简历版本管理
│   │   ├── dba-v1-outsource.md    # 旧版(备份)
│   │   └── dba-v2-xinchuang.md    # 新版信创DBA简历
│   ├── interview-log/             # 面试复盘日志
│   │   ├── 2026-10-xx-company-a.md
│   │   └── template.md            # 复盘模板
│   └── portfolio-showcase.md      # 项目作品集汇总页
│
└── docs/                          # 通用文档/参考资料
    ├── learning-roadmap.md        # 12个月计划原文
    ├── resources.md               # 优质学习链接合集
    └── weekly-review-template.md  # 周复盘模板
